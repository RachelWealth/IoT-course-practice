/*
改程序为口令模式，先说 xiao jie ，然后说具体关键词 如广州，、
可通过串口来查看识别结果
接线定义:
3.3V GND 选一组接就行
  3V3--3.3V
  GND--GND
  SCK--A5
  MI--A4
  MO--A3
  CS--A2
  RST--D5
  IRQ--D3
  WR--GND
*/
#include "LD3320.h"

LD3320 WE;

u8 nAsrStatus=0;
u8 nAsrRes=0;
extern u8  ucRegVal;
u8 flag=0;


void setup() {
  Serial.begin(9600);
  WE.LD3320_IO_Init();
  WE.LD_Reset();
  attachInterrupt(1, ProcessInt, FALLING);
  nAsrStatus = LD_ASR_NONE;    //初始状态：没有在作ASR
  SCS_0;
  Serial.println("Start\r\n");  
}

void loop() {
  switch(nAsrStatus)
    {
      case LD_ASR_RUNING:
      case LD_ASR_ERROR:  
           break;
      case LD_ASR_NONE:
      {
        nAsrStatus=LD_ASR_RUNING;
        if (WE.RunASR()==0)  /*  启动一次ASR识别流程：ASR初始化，ASR添加关键词语，启动ASR运算*/
        {
          nAsrStatus = LD_ASR_ERROR;
        }
        break;
      }

      case LD_ASR_FOUNDOK: /* 一次ASR识别流程结束，去取ASR识别结果*/
      {
        nAsrRes = WE.LD_GetResult();   /*获取结果*/                        
        User_Modification(nAsrRes);
        nAsrStatus = LD_ASR_NONE;
        break;
      }
      case LD_ASR_FOUNDZERO:
      default:
      {
        nAsrStatus = LD_ASR_NONE;
        break;
      }
    } 

}

void User_Modification(u8 dat)
{
  if(dat ==0)
  {
    flag=1;
    Serial.println("Received\r\n");
  }
  else if(flag)
  {
    flag=0;
    switch(nAsrRes)      /*对结果执行相关操作,客户修改*/
    {
      case CODE_DMCS:     /*命令“代码测试”*/
          Serial.println("dai ma ce shi\r\n"); /*text.....*/
                        break;
      case CODE_CSWB:     /*命令“测试完毕”*/
          Serial.println("ce shi wan bi\r\n"); /*text.....*/
                        break;
      
      case CODE_1KL1:  /*命令“衣服”*/
          Serial.println("yi fu\r\n"); /*text.....*/
                        break;
      case CODE_1KL2:   /*命令“图书”*/
    
          Serial.println("tu shu\r\n"); /*text.....*/
                        break;
      case CODE_1KL3:  /*命令“调料”*/
          Serial.println("tiao liao\r\n"); /*text.....*/
		  
		  
	  // case CODE_1KL1:  /*命令“北京”*/
          // Serial.println("bei jing\r\n"); /*text.....*/
                        // break;
      // case CODE_1KL2:   /*命令“上海”*/
    
          // Serial.println("shang hai\r\n"); /*text.....*/
                        // break;
      // case CODE_1KL3:  /*命令“开灯”*/
          // Serial.println("kai deng\r\n"); /*text.....*/
                        // break;
      // case CODE_1KL4:   /*命令“关灯”*/        
          // Serial.println("guan deng\r\n"); /*text.....*/
                        // break;
      
      // case CODE_2KL1:  /*命令“....”*/
          // Serial.println("guang zhou\r\n"); /*text.....*/
                        // break;
      // case CODE_2KL2:  /*命令“....”*/
          // Serial.println("shen zhen\r\n"); /*text.....*/
                        // break;
      // case CODE_2KL3:  /*命令“....”*/
          // Serial.println("xiang zuo zhuan\r\n"); /*text.....*/
                        // break;
      // case CODE_2KL4:  /*命令“....”*/
          // Serial.println("xiang you zhuan\r\n"); /*text.....*/
                              // break;
            
      // case CODE_3KL1:  /*命令“....”*/
          // Serial.println("da kai kong tiao\r\n"); /*text.....*/
                        // break;
      // case CODE_3KL2:  /*命令“....”*/
          // Serial.println("guan bi kong tiao\r\n"); /*text.....*/
                        // break;
      // case CODE_5KL1:  /*命令“....”*/
          // Serial.println("hou tui"); /*text.....*/
                        // break;
						
  //    case CODE_3KL4:  /*命令“....”*/
  //        Serial.println("\"代码测试\"识别成功"); /*text.....*/
  //                      break;
  //          
  //          case CODE_4KL1:  /*命令“....”*/
  //              Serial.println("O"); /*text.....*/
  //                            break;
  //          case CODE_4KL2:  /*命令“....”*/
  //              Serial.println("P"); /*text.....*/
  //                            break;
  //          case CODE_4KL3:  /*命令“....”*/
  //              Serial.println("Q"); /*text.....*/
  //                            break;
  //          case CODE_4KL4:  /*命令“....”*/
  //              Serial.println("R"); /*text.....*/
  //                            break;
      
      default:break;
    }
  }
  else  
  {
    Serial.println("Error\r\n"); /*text.....*/  
  }
  
}

void ProcessInt(void)
{
  u8 nAsrResCount=0;
  ucRegVal = WE.LD_ReadReg(0x2B);
  WE.LD_WriteReg(0x29,0) ;
  WE.LD_WriteReg(0x02,0) ;
  if((ucRegVal & 0x10)&&WE.LD_ReadReg(0xb2)==0x21&&WE.LD_ReadReg(0xbf)==0x35)     /*识别成功*/
  { 
    nAsrResCount = WE.LD_ReadReg(0xba);
    if(nAsrResCount>0 && nAsrResCount<=4) 
    {
      nAsrStatus=LD_ASR_FOUNDOK;
    }
    else
    {
      nAsrStatus=LD_ASR_FOUNDZERO;
    } 
  }                              /*没有识别结果*/
  else
  {  
    nAsrStatus=LD_ASR_FOUNDZERO;
  }
    
  WE.LD_WriteReg(0x2b, 0);
  WE.LD_WriteReg(0x1C,0);/*写0:ADC不可用*/
  WE.LD_WriteReg(0x29,0);
  WE.LD_WriteReg(0x02,0);
  WE.LD_WriteReg(0x2B,0);
  WE.LD_WriteReg(0xBA,0);  
  WE.LD_WriteReg(0xBC,0);  
  WE.LD_WriteReg(0x08,1);   /*清除FIFO_DATA*/
  WE.LD_WriteReg(0x08,0);  /*清除FIFO_DATA后 再次写0*/
}