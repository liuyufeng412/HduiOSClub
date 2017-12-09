import requests
datas={'name':'LYF','pwd':'shezhangzhenshuai'}
html = requests.post("http://holen1210.xyz/login.php",data=datas)
print(html.text)