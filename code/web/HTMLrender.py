import json
from flask import Flask, render_template
from IoTPractice.code.sendDataHelper import sendDataHelper

datas1 = [{"id": 1, "type": "cloth", "gender": "\u5973", "color": "\u7ea2", "season": "\u79cb", "brand": "Veromoda",
          "create_time": "2021-09-28 17:28:58", "updata_time": "2021-09-28 17:28:58", "deleted": 0},
         {"id": 11, "type": "cloth", "gender": "\u5973", "color": "\u7ea2", "season": "\u51ac", "brand": "OLNY",
          "create_time": "2021-09-28 17:28:58", "updata_time": "2021-09-28 17:28:58", "deleted": 0},
         {"id": 19, "type": "cloth", "gender": "\u7537", "color": "\u7ea2", "season": "\u79cb", "brand": "SEMIR",
          "create_time": "2021-09-28 17:28:58", "updata_time": "2021-09-28 17:28:58", "deleted": 0},
         {"id": 28, "type": "cloth", "gender": "\u7537", "color": "\u7ea2", "season": "\u6625", "brand": "\u7279\u6b65",
          "create_time": "2021-09-28 17:28:58", "updata_time": "2021-09-28 17:28:58", "deleted": 0}]

app = Flask(__name__)
fileHelper = sendDataHelper()


@app.route('/welcom')
def loadWelcomWeb():
    return render_template('welcom.html')


@app.route('/index')
def loadWeb():

    datas = fileHelper.readFromFile()
    # objSet_json = json.dumps(datas)
    # print(objSet_json)
    return render_template('index.html', datas=datas)


@app.route('/')
def loadDefaultWeb():
    return render_template('empty.html')


if __name__ == '__main__':
    app.run(debug=True)
