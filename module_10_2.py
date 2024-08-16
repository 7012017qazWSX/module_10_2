import time
from threading import Thread


class Knight(Thread):

    def __init__(self, name, skill):

        Thread.__init__(self)
        self.enemies_count = 100
        self.name = name
        self.skill = skill
        self.days_to_protect = self.enemies_count // skill

    def run(self):
        print(f' {self.name} на нас напали!!!')
        for day in range(self.days_to_protect):
            time.sleep(1)
            enemies_rest = self.enemies_count - self.skill * (day+1)
            print(f'{self.name} защищает королевство в течение {day + 1} дня... осталось {enemies_rest} врагов.')
            if enemies_rest == 0:
                print(f'{self.name} одержал победу за {day + 1} день(дней).')



first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)


first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')
