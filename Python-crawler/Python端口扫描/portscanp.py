import requests
import socket
from bs4 import BeautifulSoup
class PortScanner(object):
	"""docstring for PortScanner"""
	def __init__(self, target,):
		self.target=target
#检查目标是否存在cdn
	def cheak_cdn(self,port):
		pass
#扫描端口
	def scan_port(self,port):
		try:
			s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			s.settimeout(0.5)
			return True if s.connect_ex((self.target,port))==0 else False
		except Exception as e:
			print(e)
		finally:
			s.close()
#获取端口指纹
	def get_port_banner(self,port):
		try:
			s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			s.settimeout(0.5)
			s.connect((self.target,port))
			s.send("HELLO\r\n".encode("utf-8"))
			return s.recv(1024).decode("utf-8")
		except Exception as e:
			print(e)
		finally:
			s.close()
		
#获取web指纹
	def get_http_banner(self,url):
		try:
			resp=requests.get(url=url,verify=False,timeout=5,allow_redirects=True)
			soup=BeautifulSoup(resp.content,"html.parser")
			return soup.title.text.strip()
		except Exception as e:
			pass


if __name__ == '__main__':
	Myscan=PortScanner('106.75.15.117')
	print(Myscan.scan_port(80))
	print(Myscan.get_port_banner(40022))
	print(Myscan.get_http_banner("http://106.75.15.117:80"))