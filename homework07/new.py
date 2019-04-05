import time
import threading as th
import multiprocessing as mp
import psutil
import numpy as np

def heavy_computation(data_chunk):
    A1 = np.random.random((data_chunk, data_chunk, data_chunk))
    A2 = np.random.random((data_chunk, data_chunk, data_chunk))
    A = A1*A2
    return A


class ProcessPool:
    """ Реализация пула процессов с учетом памяти, потребляемой одним процессом"""

    def __init__(self, min_workers=1, max_workers=15, max_mem_usage='1gb'):
        self.min_workers = min_workers
        self.max_workers = max_workers
        self.workers_number = 0
        self.mem_usage = 0
        self.mem_usage_list = []
        self.max_mem_comp(max_mem_usage)

    def max_mem_comp(self, max_mem_usage):
        """ Преобразование к единой системы счисления, в данном случае 'gb'. """
        max_mem_usage = max_mem_usage.lower()
        if max_mem_usage.endswith('gb'):
            self.max_mem_usage = int(max_mem_usage[:-2])
        elif max_mem_usage.endswith('mb'):
            self.max_mem_usage = int(max_mem_usage[:-2]) / 1000
        elif max_mem_usage.endswith('kb'):
            self.max_mem_usage = int(max_mem_usage[:-2]) // 1000 / 1000
        elif not max_mem_usage.isdigit():
            self.max_mem_usage = int(max_mem_usage[:-1]) // 1000000 / 1000
        else:
            self.max_mem_usage = int(max_mem_usage)

    def map(self, calculation, big_data):
        """ Фунуция для рассчета количества процессов, а также запуск пула"""
        #  запуск тестового процесса
        p = mp.Process(target=calculation, args=(big_data.get(),))
        p.start()
        p_m = th.Thread(target=self.mem_testing, args=(p.pid,))
        p_m.start()
        p.join()
        p_m.join()
        # вычисление колва процессов
        self.mem_usage = max(self.mem_usage_list)
        self.workers_number = int(self.max_mem_usage // self.mem_usage)
        if self.workers_number > self.max_workers:
            self.workers_number = self.max_workers
        # запуск пула процессов
        process = []
        for i in range(self.workers_number):
            if not big_data.empty(): #проверка на пустоту
                p = mp.Process(target=calculation, args=(big_data.get(),))
                p.start()
                process.append(p)
            else:
                for p2 in process:  # ожидание завершения всех процессов
                    p2.join()
                return self.workers_number, self.mem_usage
        while True:
            for p in process:
                p.join(0.001)
                if not p.is_alive():  # если вдруг процесс еще жив
                    p.terminate()
                    if not big_data.empty():
                        process.remove(p)
                        p2 = mp.Process(target=calculation, args=(big_data.get(),))
                        p2.start()
                        process.append(p2)
                    else:
                        for p2 in process:  # ожидание завершения всех процессов
                            p2.join()
                        return self.workers_number, self.mem_usage

    def mem_testing(self, pid):
        """ Рассчет требуемой памяти"""
        p_psutil = psutil.Process(pid)
        while psutil.pid_exists(pid):                                           #Проверяет, что указанный PID процесса запущен.
            try:
                self.mem_usage_list.append(p_psutil.memory_info().rss // 1000000 / 1000)
            except:
                pass
            time.sleep(0.01)


if __name__ == '__main__':
    queue = mp.Queue()
    for i in range(20):
        queue.put(i)     #Помещает объект i в очередь
    pool = ProcessPool(max_mem_usage='1Gb')
    print(pool.map(heavy_computation, queue))
