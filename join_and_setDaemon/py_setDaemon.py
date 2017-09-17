# coding:utf8

'''

setDaemon()方法。
主线程A中，创建了子线程B，
并且在主线程A中调用了B.setDaemon(),
这个的意思是，把主线程A设置为守护线程，
这时候，要是主线程A执行结束了，就不管子线程B是否完成,
一并和主线程A退出.
这就是setDaemon方法的含义，这基本和join是相反的。
此外，还有个要特别注意的：必须在start() 方法调用之前设置，
如果不设置为守护线程，程序会被无限挂起。

例子：就是设置子线程随主线程的结束而结束：
'''
import threading
import time


class MyThread(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id

    def run(self):
        time.sleep(5)
        print("This is " + self.getName())


if __name__ == "__main__":
    t1 = MyThread(999)
    t1.setDaemon(True)
    t1.start()
    # t1.join()
    print("I am the father thread.")

'''
解释：t1.setDaemon(True)的操作，将父线程设置为了守护线程。
根据setDaemon()方法的含义，
父线程打印内容后便结束了，不管子线程是否执行完毕了。
'''