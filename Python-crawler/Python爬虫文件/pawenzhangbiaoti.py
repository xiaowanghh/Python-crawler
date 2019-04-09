import requests
import re
from bs4 import BeautifulSoup
headers={
	'Host': 'zone.secevery.com',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:62.0) Gecko/20100101 Firefox/62.0',
	'Referer':'http://www.baidu.com',
}
#获取所有页码
def get_total_pages():
	url="http://zone.secevery.com/"
	resp=requests.get(url=url,headers=headers)
	soup=BeautifulSoup(resp.content,"html.parser")
	a=soup.find_all('a',href=re.compile('is_recommend-0__page-'))
	a=str(a[-1])
	total_pages=a.split('-')[-1].split('"')[0]
	print(total_pages)
	return total_pages
#过去所有标题
def get_all_titles(pages):
	titles=[]
	total_pages=int(pages)
	for page in range(1,1+1):
		url="http://zone.secevery.com/sort_type-new__day-0__is_recommend-0__page-%d" % page	
		resp=requests.get(url=url,headers=headers)
		soup=BeautifulSoup(resp.content,"html.parser")
		a=soup.find_all('a',href=re.compile(r'com/article'))
		for x in a:
			if x.string != "查看全部":
				titles.append(x.string)
	return titles
#写入文件
def Write2txt(titles):
	with open('title.txt','w+')as f:
		for title in titles:
			f.write(title+'\n')
if __name__ == '__main__':
	print('-'*60)
	print("程序启动中....")
	print('-'*60)
	total_pages=get_total_pages()
	print("页面总数为：%s" % total_pages)
	print('-'*60)
	titles=get_all_titles(total_pages)
	print("文件正在写入。。")
	print('-'*60)
	Write2txt(titles)
	print("well done")