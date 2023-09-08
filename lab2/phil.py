import threading, time
N = 5
locks = [threading.Lock() for i in range(N)]

class Philosopher(threading.Thread):
    def __init__(self, id):
        super().__init__()
        self.id = id

    def run(self):
        while True:
            if (self.id != N - 1):
                locks[int(self.id)].acquire()
                locks[int(self.id) + 1].acquire()
                print(f"Philosopher {self.id} is eating")
                locks[int(self.id)].release()
                locks[int(self.id) + 1].release()
                print(f"Philosopher {self.id} is thinking")
                time.sleep(5)
            else:
                locks[0].acquire()
                locks[N - 1].acquire()
                print(f"Philosopher {self.id} is eating")
                locks[0].release()
                locks[N - 1].release()
                print(f"Philosopher {self.id} is thinking")
                time.sleep(5)


if __name__ == "__main__":
    philosophers = [Philosopher(i) for i in range(5)]
    # Start the threads
    for philosopher in philosophers:
        philosopher.start()
    for philosopher in philosophers:
        philosopher.join()
