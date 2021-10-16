# IoTPractice
 本项目基于flask框架和OpenCV模块实现。采用LBPH算法实现人脸识别功能，利用web前端实现物品的展示，并用flask实现前后端交互。

# 项目结构
### flask框架

    E:.
    ├─config
    ├─model
    ├─static
    │  ├─css
    │  ├─img
    │  │  ├─book
    │  │  ├─cloth
    │  │  └─flavoring
    │  └─js
    ├─templates
    ├─views
    └─__pycache__

### 程序结构

        E:.
        ├─faceData
        │  └─mem_1
        ├─haarcascades
        ├─LD3320_new
        │  └─LD3320
        ├─modules
        ├─recognizer
        ├─ui
        │  └─__pycache__
        ├─web
        │  ├─config
        │  ├─model
        │  ├─static
        │  │  ├─css
        │  │  ├─img
        │  │  │  ├─book
        │  │  │  ├─cloth
        │  │  │  └─flavoring
        │  │  └─js
        │  ├─templates
        │  ├─views
        │  └─__pycache__
        └─__pycache__

#  开发平台:
 win10×64 + pycharm + Anaconda3
# 依赖配置

 > pip install -r requirements.txt
 
# 运行
 > 注意：两个程序运行注意前后顺序不可改变
 
    
 > cd code\web
 > 
 > python HTMLrender.py
 

 > cd ..
 > 
 > python main.py
 
 
