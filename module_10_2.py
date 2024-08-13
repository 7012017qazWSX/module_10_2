import time
from threading import Thread


class Knight(Thread):
    def __init__(self, name, power, enemies = 100):
        self.Name = name
        self.Power = power
        self.Enemy = enemies
        super().__init__()

    def run(self):
        print(f'{self.Name} на нас напали!')
        data_count = 0
        while self.Enemy != 0:
            self.Enemy = self.Enemy - self.Power
            data_count = data_count + 1
            print(f'{self.Name} сражается {data_count} дней(дня). Воинов осталось : {self.Enemy} ')
            time.sleep(1)
        print(f'{self.Name} одержал победу спустя {data_count} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)


first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')
