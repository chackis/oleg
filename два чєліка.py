import random
import time


class Student:
    def __init__(self, name):
        self.name = name
        self.happines = 50
        self.progress = 0
        self.alive = True
        self.money = 100
        self.found_work = False
    def to_study(self):
        print("Тужимося..")
        self.progress += 0.12
        self.happines -= 3
    def sleep(self):
        print("дрихну))")
        self.happines += 3
    def find_work(self):
        if self.found_work == False:
            print("Ти шукаєш роботу..")
            time.sleep(0.10)
            print("Пошук роботи: 0%")
            print("Перша робота: Прибиральник")
            time.sleep(1)
            print("Думаю, можна знайти ліпше.")
            time.sleep(0.10)
            print("Пошук роботи: 10%")
            time.sleep(0.30)
            print("Пошук роботи: 25%")
            time.sleep(1)
            print("Друга робота: Адвокат.")
            time.sleep(0.30)
            print("Непогано, але ще можна пошукати.")
            time.sleep(0.20)
            print("Пошук роботи: 40%")
            time.sleep(0.10)
            print("Пошук роботи: 65%")
            time.sleep(0.10)
            print("Пошук роботи: 75%")
            time.sleep(1)
            print("Третя робота: Завод")
            time.sleep(0.20)
            print(". . .")
            time.sleep(2)
            print("Адвокат теж непогано.")
            time.sleep(0.10)
            print("Пошук роботи: 100% (закінчено через скасування)")
            self.found_work = True
        else:
            print("Ти вже маєш роботу!")
    def work(self):
        print("Ти вирішив почати працювати..")
        time.sleep(0.50)
        print("Ти зайшов на робочий сайт, почав шукати замовлення.")
        time.sleep(0.10)
        print("Пошук справи: 0%")
        time.sleep(0.10)
        print("Пошук справи: 10%")
        time.sleep(0.10)
        print("Пошук справи: 15%")
        time.sleep(0.10)
        print("Пошук справи: 25%")
        time.sleep(0.10)
        print("Пошук справи: 40%")
        time.sleep(0.10)
        print("Пошук справи: 50%")
        time.sleep(0.10)
        print("Пошук справи: 65%")
        time.sleep(0.30)
        rand1 = random.randint(1, 3)
        if rand1 == 1:
            print("Справа: Бандера бомбив бомбас")
            print("Загроза: Розстріл")
            time.sleep(0.15)
            print("Ваша задача: не дати Бандері вмерти!!")
            time.sleep(1)
            print("Ти пробуєш сказати шо Бандера не обязан")
            rand2 = random.randint(1, 2)
            if rand2 == 1:
                print("Перший етап пройшов успішно, продовжуємо далі.")
                time.sleep(1)
                print("Ше трохи, ти пробуєш доказати судді що відео це фотошоп")
                time.sleep(2)
                print("ВІТАЮ!!! БАНДЕРА СВОБІДНИЙ!!")
                self.money += 25
            elif rand2 == 2:
                print("Перший етап пройшов як по паштету.., пробуємо дати ")
                time.sleep(2)
                print("ВЗЯТКУ.")
                time.sleep(3)
                rand3 = random.randint(1, 2)
                if rand3 == 1:
                    print("В тебе получилось підкупити суддю! Ти втратив 25 грн, але виграв 15. Ти в боргу на 10 грн.")
                    self.money -= 25
                    self.money += 15
                elif rand3 == 2:
                    print("Суддя відмовився, і тебе затримали.")
                    time.sleep(2)
                    print("Ти не витримав булінгу і вийшов з світу (осуждаю!)")
                    self.is_alive == False
        elif rand1 == 2:
            print("Справа: Стерненко кікнув з світу нападника")
            print("Загроза: 7 років")
            time.sleep(0.15)
            print("Ваша задача: Не дати імператору правого сектору сісти!!!")
            time.sleep(1)
            print("Ця справа легко дається..")
            time.sleep(1)
            print("Вітаю! Ти лакі. (виграв справу)")
            time.sleep(1)
            print("Ти заробив 50 грн.")
            self.money += 50
        elif rand1 == 3:
            print("Справа: Мужик вкрав снікерс з заправки")
            print("Ваша задача: Не.. Я навіть не знаю чого тут треба добитись..")
            time.sleep(3)
            print(". . .")
            time.sleep(0.50)
            print("ВЯЖІТЬ ЙОГО!!!")
            time.sleep(0.50)
            print("ТОБІ ДАЛИ БЕЗРОБІТНЄ ЖИТТЯ!")
            time.sleep(0.10)
            print("ТИ ЗАРОБИВ 100000 ГРН!!!")
            self.money += 100000



    def to_chill(self):
        print("На раслаблонє")
        self.happines += 5
        self.progress -= 0.5
    def is_alive(self):
        if self.progress < -0.5:
            print("БАН")
            self.alive = False
        elif self.happines <= 0:
            print("ol mai frends ar toksik")
            self.alive = False
        if self.progress > 5:
            print("год мод???")
            self.happines = 1000000
            time.sleep(1)
            print(".. але ти здох..")
            self.alive = False
    def stats(self):
        print("Статистика студента:")
        print("Рівень щастя: " + self.happines)
        print("Рівень успішності: " + round(self.progress, 2))
    def live(self, day):
        print("День: " + day + " Ім'я студента: " + self.name)
        rand = random.randint(1, 3)
        if rand == 1:
            self.to_study()
        elif rand == 2:
            self.sleep()
        elif rand == 3:
            self.to_chill()
        self.stats()
        self.is_alive()

        if self.money <= 0:
            print("Йди працюй, бомжара!")
            time.sleep(0.50)
            print("1. Ну ладно( ")
            print("2. Ні! Я живу в свобідній країні!")
            e = input("Ваша відповідь(1/2): ")
            if e == 1:
                Student.work(self)
            elif e == 2:
                print("НУ ТОДІ ПРИЙМИ СМЕРТЬ ГІДНО!")
                self.is_alive == False



class other_guy:
    def __init__(self, name1    ):
        self.name1 = name1
        self.happines1 = 50
        self.alive1 = True
        self.money1 = 250
        self.found_work1 = False
        self.phone = False
    def findwork(self):
        print("Ти прийшов до рішення знайти роботу..")
        time.sleep(2)
        print("Що ж..")
        time.sleep(1)
        print("лес го")
        time.sleep(1)
        print("Ти зайшов на сайт пошуку робіт..")
        time.sleep(0.50)
        print("По тобі видно, ти не хочеш напрягатись.")
        time.sleep(1)
        print("Впринципі, можеш попробувати фріланс, ти заходиш на інший сайт")
        time.sleep(2)
        print("Перше, ти маєш зареєструватись.")
        time.sleep(2)
        print("Заповни ці рядки: ")
        time.sleep(0.50)
        namereg = input("Ваше ім'я: ")
        agereg = int(input("Ваш вік: "))
        emailreg = input("Ваша електронна адреса: ")
        print("Реєстрація..")
        time.sleep(5)
        print("Вітаю, " + namereg + "!")
        time.sleep(0.50)
        rand2 = random.randint(1, 2)
        if rand2 == 1:
            print("Ваше перше замовлення: Зробити логотип для компанії блекбурі.")
            print("Ти заходиш в фотошоп")
            time.sleep(3)
            print("Спочатку, ти зробиш чорний фон, бо компанія блекбурі")
            time.sleep(1)
            print("Чи буде текст на логотипі?(y/n)")
            text = input()
            if text == "y":
                print("Ти пишеш назву компанії")
                time.sleep(1)
                print("На логотипі пише блекбурі")
                time.sleep(1)
                print("Ти намалював рамку навколо тексту")
                time.sleep(1)
                print("Ти домальовуєш ще якійсь класні дизайнерські штуки")
                time.sleep(2)
                rand3 = random.randint(1, 2)
                if rand3 == 1:
                    print("В тебе получилось! Ти відправляєш фото чєлу який замовив..")
                    time.sleep(3)
                    print("Йому сподобалось! Ти отримав +50 баксів.")
                    self.money1 =+ 50
                else:
                    print("Ну, трішки не так як хотілось.. Ти відправляєш фото чєлу який замовив")
                    time.sleep(3)
                    print("Ну, йому більш менш сподобалось. Можна було й ліпше. Ти отримав +30 баксів.")
                    self.money1 =+ 30
            else:
                print("Ну ок, і без нього впринципі могло б бути.")
                time.sleep(0.50)
                print("Ти домальовуєш свої дизайнерські штучкі")
                time.sleep(1)
                print("Всьо, ти скидаєш фото чєлу який замовляв..")
                time.sleep(2)
                print("Він зробив зауваження щодо тексту.. Треба було все ж таки написати.. Але ти отримав 25 доллярів")
                self.money1 =+ 25
        if rand2 == 2:
            print("Ваше замовлення: зробити мотиваційний баннер шоб люди займались спортом")
            time.sleep(1)
            print("Заходиш в фотошоп")
            time.sleep(1)
            print("Додаєш гантелі, бутилку води, додаєш краплі")
            time.sleep(1)
            rand4 = random.randint(1, 2)
            if rand4 == 1:
                print("В тебе більш-менш получилось.. Скидаєш фотку чєлу")
                time.sleep(3)
                print("Йому сподобалось! Ти отримав 30 долларів.")
                self.money1 =+ 30
            if rand4 == 2:
                print("В тебе не получилось взагалі! Але в тебе закінчується час..")
                time.sleep(2)
                print("Крізь сльози на клавішах скидаєш фотку чєлу..")
                time.sleep(2)
                print("ЙОМУ ВЗАГАЛІ НЕ СПОДОБАЛОСЬ! ВІН СКАЗАВ ЧЕКАТИ ЙОГО..")
                time.sleep(1)
                print("Ти зі страху йдеш закривати вікна, двері")
                time.sleep(0.50)
                print("Одне вікно закрите!")
                time.sleep(0.50)
                print("Двері закриті!")
                time.sleep(0.50)
                print("Друге вікно закрите!")
                time.sleep(2)
                print("Ти заховався в шафі.")
                time.sleep(0.50)
                print("Ти зі страху не можеш рухатись..")
                time.sleep(5)
                print("ХТОСЬ ВИЛАМАВ ДВЕРІ")
                time.sleep(1)
                print("Ти почав плакати, сльози впали на гачок вішалки")
                time.sleep(0.50)
                print("ВІШАЛКА ВПАЛА")
                time.sleep(1)
                print("Мужик відкрив шафу..")
                time.sleep(2)
                print("І дав тобі 10 долларів.")
                self.money1 =+ 10
                print("Він пішов..")
                time.sleep(1)
                print("ВІТАЮ!!! ТИ ЗАРОБИВ 10 ДОЛЛЯРІВ!!!!")
    def buyiphone(self):
        if self.money1 < 300:
            print("Тобі не стає грошей! Наразі в тебе " + self.money1 + " грн")
            time.sleep(1)
            print("Йди працюй, лох")
            time.sleep(1)
            if self.found_work1 == False:
                print("Бажаєш знайти роботу? (y/n)")
                goworkbomzh = input()
                if goworkbomzh == "y":
                    time.sleep(0.10)

                else:
                    print("Ну й сиди без грошей далі")
            if self.found_work1 == True:
                print("Бажаєш почати працювати (y/n)?")
                gowork = input()
                if gowork == "y":
                    print("Починаєш працювати..")

                else:
                    print("Ну й сиди без грошей далі")
        if self.money1 > 300:
            print("Ти рілі хочеш айфон купити? Якшо ти купиш айфон за 300 баксів, в тебе буде " +  self.money1 - 300 + " грн")
            time.sleep(1)
            print("Впевнений? (y/n)")
            vpevn = input()
            if vpevn == "y":
                print("Лан, ти купив айфон 12 ес плюс макро максі супер ікс про")
                self.money1 =- 300
            else:
                print("Молодець! Ти звісно зберіг гроші, але ти всеодно без телефону..")
                time.sleep(1)
                print("+rep")




