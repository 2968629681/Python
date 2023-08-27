import time
from multiprocessing import Process, Queue


def producer(name, q, count):
    for i in range(count):
        time.sleep(0.5)
        d = f"生产者{name} 第{i}包子"
        print(d)
        q.put(d)


def consumer(name, q):
    while True:
        time.sleep(1)
        if q.empty():   # 判断队列是否为空, 为空结束索取
            break
        print(f"\033[1;32m消费者{name} 吃了{q.get()}\033[0m")


if __name__ == '__main__':
    queue = Queue()
    for i in range(1, 3):
        p = Process(target=producer, args=(i, queue, 10))
        p.start()

    for i in range(1, 6):
        c = Process(target=consumer, args=(i, queue))
        c.start()

    print("主进程")
