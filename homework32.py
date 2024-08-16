import logging
import unittest
import ranner1
from homework29 import Runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            run1 = Runner("Ivan", speed=-3)
            logging.info(f'"test_walk" выполнен успешно')
        except Exception:
            logging.warning("Неверная скорость для Runner")
    def test_run(self):
        try:
            run2 = Runner(3, 3)
            logging.info(f'"test_run" выполнен успешно')
        except Exception:
            logging.warning("Неверный тип данных для объекта Runner")

# first = Runner('Вося', 10)
# second = Runner('Илья', 5)
# # third = Runner('Арсен', 10)
#
# t = Tournament(101, first, second)
# print(t.start())
if __name__ == "__main__":
    unittest.main()