# cmd 安装 pip install requests

import requests


# 发送http请求
def baidu_get():
    base_url = 'https://www.baidu.com'
    base_header = {'User-Agent':
                       'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}

    response = requests.get(url=base_url, headers=base_header)
    html = response.text  # 响应报文 的响应体(默认编码)
    html2 = response.content.decode('utf8')  # utf8 编码

    print(html2)


'''
    1.页面乱码   2.返回的页面内容不正确（反爬虫） 加headers
    2.get/post 参数都需要时 json格式
'''

def baidu_get2():
    base_url = 'https://www.baidu.com/s'
    base_headers = {'User-Agent':
                           'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}

    base_param = {'wd':'柠檬班'}
    resule = requests.get(url=base_url,params=base_param,headers=base_headers)
    lemon = resule.text
    print(lemon)


# post  http://test.lemonban.com/futureloan/mvc/api/member/login
#post
def lemon_post():
    post_url = 'http://test.lemonban.com/futureloan/mvc/api/member/register'
    post_param={'mobilephone':'13413766443','pwd':'213465'}
    html = requests.post(url=post_url,data=post_param)
    response = html.text        #返回的是str 字符串
    # print(type(response))

    # 1.eval   可把 字符串 转为 字典
    # ’{"status":0,"code":"20110","data":null,"msg":"手机号码已被注册"}‘
    # 2.返回的JSON里面有null，python不认识，要replace替换（所有）
    response = response.replace('null','None')

    #3. 转为dict
    response = eval(response)
    msg = response['msg']

    #  另一种方法    .json()
    html1 = html.json()
    print(type(html1))

    print(response)
    print(msg)

def lemon_login():
    base_url = 'http://test.lemonban.com/futureloan/mvc/api/member/login'
    base_data = {'mobilephone':'13413766443','pwd':'213465'}

    html = requests.post(url=base_url,data=base_data)
    res = html.text
    print(res)

lemon_login()