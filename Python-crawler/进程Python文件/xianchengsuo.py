from time import time,sleep
import threading
num=0
lock=threading.Lock()

def test():
 	global num
 	lock.acquire()
 	t=num
 	print("Current Num is %d" % t)
 	sleep(0.1)
 	num=t+1
 	print("alter Num is %d" % num)
 	lock.release()

if __name__ == '__main__':
	start=int(time())

	threads=[]
	for i in range(0,20):
		t=threading.Thread(target=test)
		threads.append(t)
	for t in threads:
		t.setDaemon(True)
		t.start()
	for t in threads:
		t.join()
	print("Used time:%d" % int(time()-start))
