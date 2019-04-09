from time import ctime,sleep
import threading
def do_homework(arg):
	for i in range(2):
		print("I was doing my %s homework! %s"%(arg,ctime()))
		sleep(1)

def watch_tv(arg):
	for x in range(2):
		print("I was watching %s on TV!wen %s"%(arg,ctime()))
		sleep(2)

if __name__ == '__main__':
	threads=[]
	t1=threading.Thread(target=do_homework,args=('English',))
	t2=threading.Thread(target=watch_tv,args=(u'阿凡达',))

	threads.append(t1)
	threads.append(t2)

	for t in threads:
		t.setDaemon(True)
		t.start()
	t.join()
	print("all over %s"% ctime())