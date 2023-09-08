"""
    Basic thread handling exercise:

    Use the Thread class to create and run more than 10 threads which print their name and a random
    number they receive as argument. The number of threads must be received from the command line.

    e.g. Hello, I'm Thread-96 and I received the number 42

"""
import threading
import random
import sys

class NumberThread(threading.Thread):
    def __init__(self, number):
        super().__init__()
        self.name = name
        self.number = number

    def run(self):
        print(f"Hello, I'm {self.name} and I received the number {self.number}")

if __name__ == "__main__":
    num_threads = int(sys.argv[1])
    threads = []
    for i in range(num_threads):
        name = f"Thread-{i}"
        number = random.randint(1, 100)
        thread = NumberThread(number)
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()