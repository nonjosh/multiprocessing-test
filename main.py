"""example program for testing multi-processing service which is always alive"""

from time import sleep
import multiprocessing
from multiprocessing import Pool
import random

def task():
    """task function for testing"""
    print("Executing our Task on Process {}".format(multiprocessing.current_process()))    
    # randomly raise an exception
    if random.randint(0, 1) == 1:
        print("Exception Raised in Task {}".format(multiprocessing.current_process()))
        raise Exception("Random Exception")
    sleep(1)
    print("Task Executed {}".format(multiprocessing.current_process()))

if __name__ == "__main__":
    number_of_processes = 3

    # Create a pool of specific number of CPUs
    p = Pool(number_of_processes)

    # Keep passing tasks (without augment) to pool when a worker is free
    # Restart the worker after 5 seconds in case of any exception
    while True:
        # Check any worker is free or dead
        # If yes, add new tasks to pool
        if p._taskqueue.qsize() < number_of_processes:
            for r in range(number_of_processes - p._taskqueue.qsize()):
                p.apply_async(task)
        else:
            print("All processes are busy")
        sleep(5)
