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
    t1.join()   # 使用join
    for i in range(5):
        print(i)

'''       
执行后的结果是：
999 
0 
1 
2 
3 
4
机器上运行时，999之前，有明显的停顿。

解释：线程t1 start后，主线程停在了join()方法处，
等sleep（5）后，线程t1操作结束被join，
接着，主线程继续循环打印。
'''
