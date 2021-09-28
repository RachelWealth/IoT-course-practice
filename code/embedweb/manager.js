var datas = [{
                name: '李寻欢',
                subject: 'javascript',
                scores: 100
            }, {
                name: '周杰伦',
                subject: 'javascript',
                scores: 99
            }, {
                name: '陈奕迅',
                subject: 'javascript',
                scores: 98
            }, {
                name: '昼夜',
                subject: 'javascript',
                scores/**/: 97
            }, {
                name: '柯南',
                subject: 'javascript',
                scores: 100
            }]
            // 2、添加行tr，利用for循环（i的数量与数组的长度有关）
            // 获取元素
        var tbody = document.querySelector('tbody');

        for (var i = 0; i < datas.length; i++) {
            //创建行tr
            var tr = document.createElement('tr');
            //将新创建的行tr添加给tbody
            tbody.appendChild(tr);
            // 3、内层for循环，创建每一行中的所有单元格td，单元格td的数量与对象中的属性多少有关，故用for...in...
            for (var k in datas[i]) {
                // 创建td元素
                var td = document.createElement('td');
                // 将每个对象中的属性值传给td
                td.innerHTML = datas[i][k];
                //给tr添加td子元素
                tr.appendChild(td);
            }
            //4、在每一行的最后，添加一个td，内容为a标签‘删除’
            // 创建td新元素
            var td = document.createElement('td');
            //把a标签的‘删除’传给td
            td.innerHTML = "<a href='javascript:;'>删除</ a>";
            // 给tr添加上td
            tr.appendChild(td);
        }

        //以上，整个表格就创建完成了
        // 5、下面给表格添加点击‘删除’，就删除整行的事件
        // 获取元素
        var as = document.querySelectorAll('a');
        // 添加事件
        for (var i = 0; i < as.length; i++) {
            as[i].onclick = function() {
                tbody.removeChild(this.parentNode.parentNode);
            }
        }