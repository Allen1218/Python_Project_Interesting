import flask, json
from flask import request
from flask_cors import CORS
import pyttsx3

'''
flask： web框架，通过flask提供的装饰器@server.route()将普通函数转换为服务
登录接口，需要传url、username、passwd

http://127.0.0.1:8888/login?name=xiaoming&pwd=111
'''
# 创建一个服务，把当前这个python文件当做一个服务
server = flask.Flask(__name__)
# CORS(server, resources=r'/*')
# app = Flask(__name__)

server.debug = True

CORS(server, supports_credentials=True)#设置参数

# server.config['JSON_AS_ASCII'] = False
# @server.route()可以将普通函数转变为服务 登录接口的路径、请求方式  , ('Access-Control-Allow-Origin')
@server.route('/login', methods=['get', 'post'] )
def login():
    # 获取通过url请求传参的数据
    print(request.values)
    username = request.values.get('name')
    # 获取url请求传的密码，明文
    pwd = request.values.get('pwd')
    # 判断用户名、密码都不为空，如果不传用户名、密码则username和pwd为None
    if username and pwd:
        if username == 'xiaoming' and pwd == '111':
            resu = {'code': 200, 'message': '登录成功'}
            msg = "Welcome user " + username + " login. "
            msg += "Please enjoy this system. hahaha..."
            test(msg)
            return json.dumps(resu, ensure_ascii=False)  # 将字典转换为json串, json是字符串
        else:
            resu = {'code': -1, 'message': '账号密码错误'}
            return json.dumps(resu, ensure_ascii=False)
    else:
        resu = {'code': 10001, 'message': '参数不能为空！'}
        return json.dumps(resu, ensure_ascii=False)

def test(msg):
    # msg = '''Its better to be alone, than to be with someone, you're not happy to be with...'''

    # teacher = pyttsx3.init()
    # rate = teacher.getProperty('rate')
    # teacher.setProperty('rate', rate - 80)
    # teacher.say(msg)
    # teacher.runAndWait()

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 80)
    # 0：汉语女声；1：英语男声；2：英语女声；3：日语女声；4：韩语女声；5：英语女声；6：粤语女声；7：台语女声
    voices = engine.setProperty('voice', voices[1].id)

    engine.say(msg)

    engine.runAndWait()



if __name__ == '__main__':
    server.run(debug=True, port=8888, host='0.0.0.0')  # 指定端口、host,0.0.0.0代表不管几个网卡，任何ip都可以访问