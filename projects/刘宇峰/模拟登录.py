import requests
import hashlib
import re

def login(username,pwd):
    s=requests.session()
    html = s.get("http://cas.hdu.edu.cn/cas/login?service=http%3A%2F%2Fi.hdu.edu.cn%2Fdcp%2Findex.jsp").text
    data={
        "username":username,
        "password":hashlib.md5(pwd.encode()).hexdigest(),
        "loginErrCnt":0,
        "serviceName":"null",
        "encodedService":"http%3a%2f%2fi.hdu.edu.cn%2fdcp%2findex.jsp",
        "lt":re.findall('name="lt" value="(.*)"',html)[0],
        "service":"http://i.hdu.edu.cn/dcp/index.jsp",
    }
    html = s.post("http://cas.hdu.edu.cn/cas/login",data=data).text
    url=re.findall('a href="(.*)"',html)[0]
    s.get(url)
    #html=s.get("http://i.hdu.edu.cn/dcp/forward.action?path=/portal/portal&p=wkHomePage").text
    html=s.get("http://i.hdu.edu.cn/dcp/portal/gVarInit.jsp?p=wkHomePage&gId=null&user_id=null").text
    print(html)
login("17051627","liuyufeng990412")
