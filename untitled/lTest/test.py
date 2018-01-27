import threading


# 线程测试
class myThread(threading.Thread):
    def __init__(self, t1):
        threading.Thread.__init__(self)
        self.t1 = t1

    def run(self):
        while True:
            print(self.t1)


if __name__ == '__main__':
    threads = []
    thread1 = myThread('aaa')
    thread2 = myThread('bbb')
    threads.append(thread1)
    threads.append(thread2)
    thread1.start()
    thread2.start()
    for a in threads:
        a.join()
