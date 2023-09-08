from threading import enumerate, Condition, Thread, Event

class Master(Thread):
    def __init__(self, max_work, condition):
        Thread.__init__(self, name="Master")
        self.max_work = max_work
        self.condition = condition
    
    def set_worker(self, worker):
        self.worker = worker
    
    def run(self):
        for i in range(self.max_work):
            # generate work
            self.work = i
            with self.condition:
                # notify worker
                self.condition.notify()
                # wait for result
                self.condition.wait()
            if self.get_work() + 1 != self.worker.get_result():
                print("oops")
            print("%d -> %d" % (self.work, self.worker.get_result()))
    
    def get_work(self):
        return self.work

class Worker(Thread):
    def __init__(self, terminate, condition):
        Thread.__init__(self, name="Worker")
        self.terminate = terminate
        self.condition = condition

    def set_master(self, master):
        self.master = master
    
    def run(self):
        while not self.terminate.is_set():
            with self.condition:
                # wait for work
                self.condition.wait()
                if self.terminate.is_set():
                    break
                # generate result
                self.result = self.master.get_work() + 1
                # notify master
                self.condition.notify()
    
    def get_result(self):
        return self.result

if __name__ == "__main__":
    # create shared objects
    terminate = Event()
    condition = Condition()
    
    # start worker and master
    w = Worker(terminate, condition)
    m = Master(10, condition)
    w.set_master(m)
    m.set_worker(w)
    w.start()
    m.start()

    # wait for master
    m.join()

    # wait for worker
    # semnalam ca am terminat
    # notificam workerii sa revina
    terminate.set()
    with condition:
        condition.notify()
    w.join()

    # print running threads for verification
    print(enumerate())
