import unittest
import multiprocessing as mp
from new import ProcessPool
from new import f


class TestProcessPool(unittest.TestCase):

    def test_nain(self, max_mem_usage='0gb'):        #проверка на 0гб памяти

        ooo = int(max_mem_usage[:-2])
        try:
            if ooo == 0:
                raise Warning
        except Warning:
            pass
        else:
            raise Warning


class TestProcessPool(unittest.TestCase):

    def test_max_mem_usage_creation(self):
        pool1 = ProcessPool(max_mem_usage='1Gb')
        pool2 = ProcessPool(max_mem_usage='40MB')
        pool3 = ProcessPool(max_mem_usage='1099kb')
        self.assertEqual([1, 0.04, 0.001], [pool1.max_mem_usage, pool2.max_mem_usage, pool3.max_mem_usage])

    def test_pool_creation(self):
        pool = ProcessPool(min_workers=2, max_workers=10, max_mem_usage='3gb')
        self.assertEqual(2, pool.min_workers)
        self.assertEqual(10, pool.max_workers)
        self.assertEqual(3, pool.max_mem_usage)

    def test_memory_error(self):
        pool = ProcessPool(min_workers=2, max_workers=10, max_mem_usage='1kb')
        q = mp.Queue()
        q.put(1)
        q.put(20)
        try:
            pool.map(f, q)
        except Warning:
            pass
        else:
            raise Warning

    def test_min_workers_error(self):
        pool = ProcessPool(min_workers=100, max_workers=101, max_mem_usage='1gb')
        q = mp.Queue()
        q.put(1)
        q.put(20)
        try:
            pool.map(f, q)
        except Warning:
            pass
        else:
            raise Warning

    def test_max_workers_change(self):
        pool = ProcessPool(min_workers=1, max_workers=1, max_mem_usage='1Gb')
        q = mp.Queue()
        q.put(1)
        q.put(20)
        pool.map(f, q)
        self.assertEqual(pool.workers_num, 1)



if __name__ == '__main__':
    unittest.main()


if __name__ == '__main__':
    unittest.main()