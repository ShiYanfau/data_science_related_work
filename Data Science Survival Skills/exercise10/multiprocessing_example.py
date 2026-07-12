from multiprocessing import Process, cpu_count, Queue
import os
import numpy as np
import time

class Worker(object):
    def __init__(self, worker_id, g_queue):
        self.g_queue = g_queue
        self.worker_id = worker_id
        self.queue = Queue() # local worker queue
        self.work_process = Process(target=self.work, args=())
        self.work_process.start()
        info(worker_id, self.work_process, "Worker")

    def work(self):

        info(self.worker_id, self.work_process, "work")

        while True:
            data = np.random.randint(1,4)
            self.queue.put(data)

            # process data in queue
            if self.queue.qsize() > 5:
                data = self.queue.get()
                result = data + 0.1
                self.g_queue.put(result) # send result to global queue

            time.sleep(1) # work every x sec interval

        return self.w_id 


class Chief(object):
    def __init__(self, num_workers):
        self.g_queue = Queue() # global queue    
        self.num_workers = num_workers

    def dispatch_workers(self):   
        worker_processes = [Process(target=Worker(w_id, self.g_queue), args=()) for w_id in range(num_workers)]
        return worker_processes

    def result(self):
        if self.g_queue.qsize() > 3:
            result = self.g_queue.get()
            print("result", result)


def info(worker_id, process, function_name):
    print("worker_id=", worker_id,
          'module name:', __name__,
          'function name:', function_name,
          'parent process:', os.getppid(),
          'current process id:', os.getpid(),
          'spawn process id:', process.pid)


if __name__ == '__main__':  
    print('main parent process id:', os.getppid())
    print('main process id:', os.getpid())

    num_workers = 2
    chief = Chief(num_workers)
    workers_processes = chief.dispatch_workers()

    i = 0
    while True:    
        time.sleep(2) # check g_queue every x sec interval to get result
        chief.result()
        print("i =", i)

        if i > 5:
            break
        i+=1  
    

### 
# Source: https://chuacheowhuan.github.io/py_mpp/