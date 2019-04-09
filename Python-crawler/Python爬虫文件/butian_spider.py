
#!/usr/bin/python3
 
import requests
import re
from bs4 import BeautifulSoup
from requests import urllib3
urllib3.disable_warnings()

headers={
	'Host': 'butian.360.cn',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:62.0) Gecko/20100101 Firefox/62.0',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
	'Accept-Encoding': 'gzip, deflate',
	'Referer':'https://butian.360.cn/Help/faq',
	'Cookie': 'test_cookie_enable=null; __huid=11wQdGLtYq/pNQB95Kzo3lNY9lHpSo2JxQptqFscJSass=; __guid=132730903.2245629765701326600.1520230242715.42; __DC_gid=138613664.37009872.1520237532187.1537237176860.192; Hm_lvt_9d483e9e48ba1faa0dfceaf6333de846=1537229471,1537234221; smidV2=201803051747357e8a2ffb7e749c61b7337aff7f5ca6ec0016b900b8bd2a790; __hsid=bf68390d07d458fe; __DC_monitor_count=28; Q=u%3D360H2995946027%26n%3D%26le%3D%26m%3DZGH3WGWOWGWOWGWOWGWOWGWOAQL3%26qid%3D2995946027%26im%3D1_t0105d6cf9b508f72c8%26src%3Dpcw_webscan%26t%3D1; T=s%3D354d97a24341d51402e357955ff9611f%26t%3D1537229932%26lm%3D%26lf%3D2%26sk%3D18003e90f3e8a98a42cf3475943251fb%26mt%3D1537229932%26rc%3D%26v%3D2.0%26a%3D1; PHPSESSID=tlfg64tp5vsbvelfvce280bed3; __q__=1537237176769; Hm_lpvt_9d483e9e48ba1faa0dfceaf6333de846=1537237177',
	'Connection':'close',
	'Upgrade-Insecure-Requests': '1',
	'Cache-Control': 'max-age=0'	
}

data={
	's':'1',
	'p':'1',
	'token':'',
}


def get_total_pages():
	url="https://butian.360.cn/Reward/pub"
	resp=requests.post(url=url,data=data,verify=False)
	company_info=resp.json()
	total_pages=company_info['data']['count']
	return total_pages

def get_all_company_id(total_pages):
	company_id=[]
	for x in range(1,int(total_pages)+1):
		print("正在获取第%d厂商列表，请稍候" % x)
		data['p']=1
		url="https://butian.360.cn/Reward/pub"
		resp=resp=requests.post(url=url,data=data,verify=False)
		info=resp.json()
		company_info=info['data']['list']
		for company in company_info:
			company_id.append(company['company_id'])
	return company_id


def get_all_company_host(company_id):
	hosts=[]
	print("正在获取域名，请稍候")
	for x in company_id:
		url="https://butian.360.cn/Loo/submit?cid=%d" % int(x)
		print(url)
		resp=requests.get(url=url,headers=headers,verify=False)
		soup=BeautifulSoup(resp.content,'html.parser')
		inp=soup.find_all('input')
		print(inp[4]['value'])
		hosts.append(inp[4]['value'])
	return hosts

if __name__ == '__main__':
	total_pages=get_total_pages()
	company_id=get_all_company_id(total_pages)
	hosts=get_all_company_host(company_id)
	print(hosts)