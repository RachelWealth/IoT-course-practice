var datas = [{'id': 1, 'type': 'cloth', 'gender': '女', 'color': '红', 'season': '秋', 'brand': 'Veromoda', 'create_time': '2021-09-28 17:28:58', 'updata_time': '2021-09-28 17:28:58', 'deleted': 0}, 
{'id': 2, 'type': 'cloth', 'gender': '女', 'color': '绿', 'season': '秋', 'brand': 'Veromoda', 'create_time': '2021-09-28 17:28:58', 'updata_time': '2021-09-28 17:28:58', 'deleted': 0}, 
{'id': 3, 'type': 'cloth', 'gender': '女', 'color': '黄', 'season': '秋', 'brand': 'Veromoda', 'create_time': '2021-09-28 17:28:58', 'updata_time': '2021-09-28 17:28:58', 'deleted': 0}, 
{'id': 4, 'type': 'cloth', 'gender': '女', 'color': '蓝', 'season': '夏', 'brand': 'Veromoda', 'create_time': '2021-09-28 17:28:58', 'updata_time': '2021-09-28 17:28:58', 'deleted': 0}, 
{'id': 5, 'type': 'cloth', 'gender': '女', 'color': '粉', 'season': '春', 'brand': 'LEDIN', 'create_time': '2021-09-28 17:28:58', 'updata_time': '2021-09-28 17:28:58', 'deleted': 0},
{'id': 6, 'type': 'cloth', 'gender': '女', 'color': '粉', 'season': '夏', 'brand': 'LEDIN', 'create_time': '2021-09-28 17:28:58', 'updata_time': '2021-09-28 17:28:58', 'deleted': 0}, 
{'id': 7, 'type': 'cloth', 'gender': '女', 'color': '橙', 'season': '冬', 'brand': 'OLNY', 'create_time': '2021-09-28 17:28:58', 'updata_time': '2021-09-28 17:28:58', 'deleted': 0}, 
{'id': 8, 'type': 'cloth', 'gender': '女', 'color': '白', 'season': '春', 'brand': 'OLNY', 'create_time': '2021-09-28 17:28:58', 'updata_time': '2021-09-28 17:28:58', 'deleted': 0},
{'id': 9, 'type': 'cloth', 'gender': '女', 'color': '黑', 'season': '夏', 'brand': 'LEDIN', 'create_time': '2021-09-28 17:28:58', 'updata_time': '2021-09-28 17:28:58', 'deleted': 0},
{'id': 10, 'type': 'cloth', 'gender': '女', 'color': '灰', 'season': '冬', 'brand': 'OLNY', 'create_time': '2021-09-28 17:28:58', 'updata_time': '2021-09-28 17:28:58', 'deleted': 0}, 
{'id': 11, 'type': 'cloth', 'gender': '女', 'color': '红', 'season': '冬', 'brand': 'OLNY', 'create_time': '2021-09-28 17:28:58', 'updata_time': '2021-09-28 17:28:58', 'deleted': 0}]
            // 获取元素
            var data=0;
            var vtbody = document.querySelector('tbody');
            var num = datas.length;
            var numEveryRow = 4;
            for (var i = 0; i < (datas.length/4)+1; i++) {
        	//i 是行， j是列
            //创建行tr
            var vtr = document.createElement('tr');
            vtr.className='tr-'+i;
            //将新创建的行tr添加给tbody
            vtbody.appendChild(vtr);
            // 3、内层for循环，创建每一行中的所有单元格td，单元格td的数量与对象中的属性多少有关，故用for...in...
            for (var j = 0; j < numEveryRow; j++){
//每行四个大格子，每个格子中有一个表格，展示每个返回结果及其具体信息
//先创建四个格子，避免各自个数不同导致的格子大小的不一样和不整齐
var subTd = document.createElement('td');
subTd.classList.add('td-'+j,'subTable');
vtr.appendChild(subTd);
}
            	//通过找到
            	// 开始填充这一行的内容
                // 创建td元素
                var tdEveryTr = document.getElementsByClassName('tr-'+i)[0].getElementsByTagName('td');
                for(var ii = 0; ii < numEveryRow && (data<num); ii++){
                	var subTable = document.createElement('table');
                	document.getElementsByClassName('tr-'+i)[0].getElementsByClassName('td-'+ii)[0].appendChild(subTable);
                	var row = 4;
                	for(var jj = 0; jj < row; jj++){
            	//创建好每个格子中的4*1的表格
            	var subtr = document.createElement('tr');
            	subTable.appendChild(subtr);
            	var subTd = document.createElement('td');
            	subtr.appendChild(subTd);
            	if( jj == 0){
            			//第一行创建图片
            			var picDiv = document.createElement('img');
            			var imgUrl = 'E:\\workplace\\pycharmWork\\IoTPractice\\IoTPractice\\img\\book\\' + datas[data]['id'] + '.jpg';
            			picDiv.src=imgUrl;
            			subTd.appendChild(picDiv);
            		}
            		else if(jj == 1){
            			var myP = document.createElement('p');
            			myP.innerHTML=datas[data]["brand"];
            			subTd.appendChild(myP);
            		}
            		else if(jj == 2){
            			var myP = document.createElement('p');
            			myP.innerHTML=datas[data]["color"] + '   ' + datas[data]["season"];
            			subTd.appendChild(myP);
            		}
            		else if(jj == 3){
            			var myP = document.createElement('p');
            			myP.innerHTML=datas[data]["create_time"];
            			subTd.appendChild(myP);
            		}	
            	}
            	data++;
            }  
        }