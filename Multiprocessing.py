from multiprocessing import Process
import os

def square_numbers():
    for i in range(1000):
        result = i * i

        
if __name__ == "__main__":        
    processes = []
    num_processes = os.cpu_count()
    # number of CPUs on the machine. Usually a good choise for the number of processes

    # create processes and asign a function for each process
    for i in range(num_processes):
        process = Process(target=square_numbers)
        processes.append(process)

    # start all processes
    for process in processes:
        process.start()

    # wait for all processes to finish
    # block the main programm until these processes are finished
    for process in processes:
        process.join()

from multiprocessing import Process, Value, Array
import time

def add_100(number):
    for _ in range(100):
        time.sleep(0.01)
        number.value += 1

def add_100_array(numbers):
    for _ in range(100):
        time.sleep(0.01)
        for i in range(len(numbers)):
            numbers[i] += 1


if __name__ == "__main__":

    shared_number = Value('i', 0) 
    print('Value at beginning:', shared_number.value)

    shared_array = Array('d', [0.0, 100.0, 200.0])
    print('Array at beginning:', shared_array[:])

    process1 = Process(target=add_100, args=(shared_number,))
    process2 = Process(target=add_100, args=(shared_number,))

    process3 = Process(target=add_100_array, args=(shared_array,))
    process4 = Process(target=add_100_array, args=(shared_array,))

    process1.start()
    process2.start()
    process3.start()
    process4.start()

    process1.join()
    process2.join()
    process3.join()
    process4.join()

    print('Value at end:', shared_number.value)
    print('Array at end:', shared_array[:])

    print('end main')