# cookie
import requests
#1.登录
login = requests.post(url='http://test.lemonban.com/futureloan/mvc/api/member/login',data={'mobilephone':'13413766443','pwd':'213465'})
res = login.content.decode('utf8')

#充值  登录之后，自动携带cookie去请求接口
from requests.sessions import session

recharge = session().post('http://test.lemonban.com/futureloan/mvc/api/member/recharge',{'mobilephone':'13413766443','amount':'100'})
print(recharge.json())

print(res)