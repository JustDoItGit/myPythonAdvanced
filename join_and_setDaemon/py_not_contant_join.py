# coding:utf8

'''
1、join ()方法：主线程A中，创建了子线程B，
并且在主线程A中调用了B.join()，
那么，主线程A会在调用的地方等待，直到子线程B完成操作后，才可以接着往下执行，
那么在调用这个线程时可以使用被调用线程的join方法。

原型：join([timeout])

里面的参数时可选的，代表线程运行的最大时间，
即如果超过这个时间，
不管这个此线程有没有执行完毕都会被回收，
然后主线程或函数都会接着执行的。
'''
import threading
import time


class MyThread(threading.Thread):
    def __init__(self, id):
        '''初始化父类'''
        # threading.Thread.__init__(self)
        super().__init__()  # python3两种写法,这种事python3 独有
        self.id = id

    def run(self):
        x = 0
        time.sleep(5)
        print(self.id)


if __name__ == "__main__":
    t1 = MyThread(999)
    t1.start()
    for i in range(5):
        print(i)

'''
结果:
0
1
2
3
4
999

机器上运行时，4和999之间，有明显的停顿。

解释：线程t1 start后，主线程并没有等线程t1运行结束后再执行，
而是先把5次循环打印执行完毕（打印到4），
然后sleep（10）后，
线程t1把传进去的999才打印出来。
'''
