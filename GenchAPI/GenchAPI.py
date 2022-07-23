'''
Author: Vincent Young
Date: 2022-07-24 03:56:22
LastEditors: Vincent Young
LastEditTime: 2022-07-24 04:55:57
FilePath: /GenchAPI/GenchAPI/GenchAPI.py
Telegram: https://t.me/missuo

Copyright © 2022 by Vincent, All Rights Reserved. 
'''

import requests
from bs4 import BeautifulSoup
import json

def sign(userid, password):
    session = requests.session()
    url =  'https://cas.gench.edu.cn/cas/login'
    headers = {
        'Upgrade-Insecure-Requests': '1',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4307.0 Safari/537.36 Edg/88.0.692.0',
        'Content-Type':'application/x-www-form-urlencoded',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Referer':'https://cas.gench.edu.cn/cas/login?service=http%3A%2F%2Fmy.gench.edu.cn%2F_web%2Ffusionportal%2Fwelcome.jsp%3F_p%3DYXM9MSZwPTEmbT1OJg__',
        'Origin': 'https://cas.gench.edu.cn',
        'Accept-Encoding': 'gzip, deflate, br'
    }
    html = session.get(url, headers=headers).text
    bs = BeautifulSoup(html,"lxml")
    ex = bs.find("input",attrs={"name":"execution"}).get("value")
    cookies_dict_unlogin = requests.utils.dict_from_cookiejar(session.cookies)


    headers_login = {
        'Upgrade-Insecure-Requests': '1',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4307.0 Safari/537.36 Edg/88.0.692.0',
        'Content-Type':'application/x-www-form-urlencoded',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Referer':'https://cas.gench.edu.cn/cas/login?service=http%3A%2F%2Fmy.gench.edu.cn%2F_web%2Ffusionportal%2Fwelcome.jsp%3F_p%3DYXM9MSZwPTEmbT1OJg__',
        'Accept-Encoding': 'gzip, deflate, br'
    }
    data = {
        'username':userid,
        'password':password,
        'execution':ex,
        'encrypted':'true',
        '_eventId':'submit',
        'loginType':'1'
    }

    cookie = cookies_dict_unlogin

    response = session.post(url = url,headers = headers_login,data = data)
    cookies_logined = requests.utils.dict_from_cookiejar(session.cookies)


    skipurl = 'http://i1.gench.edu.cn/_web/fusionportal/stu/index.jsp?_p=YXM9MSZwPTEmbT1OJg__'
    headers_skip = {
        'Upgrade-Insecure-Requests': '1',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4307.0 Safari/537.36 Edg/88.0.692.0',
        'Content-Type':'application/x-www-form-urlencoded',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br'
    }

    skipweb = session.get(url=skipurl,headers=headers_skip)
    cookies_skiped = requests.utils.dict_from_cookiejar(session.cookies)
    # print(cookies_skiped)
    if "CASTGC" in cookies_skiped.keys():    
        print("Information portal login successful!")
    else:
        print("Login failed, please check userid and password!")
        return

    ihealth_url = 'http://i1.gench.edu.cn/mobile/openModule.do?_p=YXM9MSZwPTEmbT1OJg__'
    headers_ihealth = {
		'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
		'Content-Type':'application/x-www-form-urlencoded',
		'Accept':'application/json, text/javascript, */*; q=0.01',
		'X-Requested-With': 'XMLHttpRequest',
		'Accept-Encoding': 'gzip, deflate',
		'Referer': 'http://ihealth.hq.gench.edu.cn/pc/login-student'
	}
    ihealth_data = {
		'appName':'pc.sudy.xgfytbxs',
		'screenSize':'1920*1080',
		'clientVersion':'MacIntel-Chrome-5.0'
	}
    ihealth = session.post(url = ihealth_url,headers=headers_ihealth,data=ihealth_data,timeout = 300)
    cookies_ihealth = requests.utils.dict_from_cookiejar(session.cookies)

	
    ihealth_final_middle = 'http://ihealth.hq.gench.edu.cn/api/login/student?timestamp=1622123107678'
    ihealth_final_skip = session.get(ihealth_final_middle)



    headers_ssohq = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
        'Content-Type':'application/x-www-form-urlencoded',
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'http://ihealth.hq.gench.edu.cn/'
    }

    ssohqurl = 'https://ssohq.gench.edu.cn/sso/step?url=http%3A%2F%2Fihealth.hq.gench.edu.cn%2Fmp%2Findex'
    ssohq = session.get(url = ssohqurl,headers = headers_ssohq)
    cookies = requests.utils.dict_from_cookiejar(session.cookies)

    headers_sso = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
        'Content-Type':'application/x-www-form-urlencoded',
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'https://ssohq.gench.edu.cn/sso/step?url=http%3A%2F%2Fihealth.hq.gench.edu.cn%2Fmp%2Findex'
    }
    ssourl = 'https://ssohq.gench.edu.cn/cas/login'
    sso = session.get(url = ssourl, headers = headers_sso)

    ssonexturl = 'https://ssohq.gench.edu.cn/cas/login?ticket=ST-1342754-zNeyhVZffl9oiDLZ2bDD-dd0bd511f33c'
    headers_ssonext = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
        'Content-Type':'application/x-www-form-urlencoded',
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'https://ssohq.gench.edu.cn/'
    }
    session.get(url = ssonexturl, headers = headers_ssonext)

    lasturl = 'http://ihealth.hq.gench.edu.cn/mp/index'
    last = session.get(url = lasturl, headers = headers_ssonext)

    infourl = 'http://ihealth.hq.gench.edu.cn/api/login/clearSession?timestamp=1622123721700'
    infos = session.get(url = infourl)
    infos_dict = json.loads(infos.text)
    if(infos_dict['suc'] == True):
        userinfo = infos_dict['data']['userInfo']
        uuid = userinfo['uuid']
        userid = userinfo['userid']
        username = userinfo['username']
        collegename = userinfo['collegename']
        classname = userinfo['classname']
        phone = userinfo['phone']
        slocation = '上海'
        location = '上海市'
        xlocation = '浦东新区'
        print(username, "ihealth login successful!")
        add_url = 'http://ihealth.hq.gench.edu.cn/api/GDaily/add'
        add_header = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.18(0x17001229) NetType/4G Language/zh_TW',
            'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'
        }
        
        ischool = "0"
        add_data = {
            "type":"学生",
            "uuid":uuid,
            "userid":userid,
            "username":username,
            "collegename":collegename,
            "classname":classname,
            "phone":phone,
            "slocationcode":"310000",
            "slocation":slocation,
            "xlocationcode":310115,
            "xlocation":xlocation,
            "locationcode":"310100",
            "location":location,
            "fever":"0",
            "symptomids":"[]",
            "diagnosis":"0",
            "touchquezhen":"0",
            "inschool": ischool
        }
        add_result = session.post(headers=add_header, url=add_url, data=add_data).text
        if '添加成功' in add_result:
            print(username, "Sign successful!")
        else:
            print(userid, "Sign failed!")
    else:
        print("ihealth error!")
    session.close()
