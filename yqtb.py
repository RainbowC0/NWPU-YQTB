import re, requests, sys

cout=eval(sys.argv[1])
s=requests.Session()
s.headers.update({
"User-Agent":"Mozilla/5.0 (Linux; Android 12; V2157A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.14 Mobile Safari/57.36"
})
url="https://uis.nwpu.edu.cn/cas/login"
yq_url="https://yqtb.nwpu.edu.cn/wx/ry/"

def signin(info):
    login=s.get(url).text
    execution=re.search(r"name=\"execution\" value=\"(.+?)\"",login).group(1)
    form={
    "username":info[0],
    "password":info[1],
    "rememberMe":True,
    "currentMenu":1,
    "execution":execution,
    "_eventId":"submit",
    "geolocation":"",
    "submit":"稍等片刻……"
    }
    s.post(url,data=form)
    out=s.post(yq_url+"jrsb_xs.jsp",data=form).text
    sign=re.search(r"url:\'(ry_util\.jsp\?sign=.+?)\'",out).group(1)
    yq_form={
    "hsjc":1,
    "xasymt":1,
    "actionType":"addRbxx",
    "userLoginId":info[0],
    "szcsbm":1,
    "bdzt":1,
    "szcsmc":"在学校",
    "szcsmc1":"在学校",
    "sfyzz":0,
    "sfqz":0,
    "tbly":"mbrowser",
    "qtqksm":'',
    "ycqksm":'',
    "sfxn":0,
    "sfdw":0,
    "longlat":'',
    "userType":2,
    "userName":info[2]
    }
    s.headers.update({
    "Referer":yq_url+"jrsb_xs.jsp"
    })
    fo=s.post(yq_url+sign, data=yq_form).text
    print(fo)

for item in cout:
    signin(item)
