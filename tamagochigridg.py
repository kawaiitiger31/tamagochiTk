from tkinter import *
import shelve
import random
import time
class Watereat:
    def __init__(self,name,energy,power):
        self.name = name
        self.energy = energy
        self.power = power

class Waterlife:
    def __init__(self, name, eattype, energy=100, home='ocean', power=1,razmer=1):
        self.name = name
        self.eattype = eattype
        self.energy = energy
        self.home = home
        self.power = power
        self.razmer = razmer
    def __str__(self):
        return '%s : %s, кушает %s, текущая энергия %d, дом- %s' %(self.__class__.__name__, self.name, self.eattype.name,
                                                                   self.energy, self.home)
        
    def changeHome(self, newnamehome):
        self.home= newnamehome
        
    def giveEnergy(self, num):
        self.energy+=num

class Watersnakes(Waterlife):
    def giveEnergy(self, num):
        self.energy= self.energy+ num/2

krevetka = Waterlife('Креветочка','musor',300,'ocean last floor',4)
akula = Waterlife('Akulius SMF','krevetka',450)
murena= Watersnakes('MurMurena','akula',800,'ocean last floor')






root = Tk()
root.geometry('480x100+100+100')
root.title("WaterZoo Tamagochi ver. 0.01")
#f_top = Frame() #для текста фрейм
#f_bot = Frame() #для кнопок
 

r_var= BooleanVar() #бул знач для радиокнопки
r_var.set(0) # ставим по умолчанию false


def exitz():
    root.destroy()

def save():
    db = shelve.open('waterzoo',flag="n")
    db['krevetka'] = krevetka
    db['akula'] = akula
    db['murena'] = murena
    db.close()
    lfeed['text']="Статус сохранен!"

def load():
    global krevetka
    db = shelve.open('waterzoo')
    krevetka= db['krevetka']
    lfeed['text']="Статус загружен!"
def about():
    a= Toplevel()
    a.geometry('550x150')
    #a['bg'] = 'grey'
    Label(a, text="""Это написано на Python версии 3.6.4 в качестве учебного проекта.
Использован модуль time, shelve, random, функции и классы, встроенный GUI TKinter.
Telegram: @ru_python_beginners
Автор: @kawaii772
Необходимо добавить:
Привязку к SQL
Инвентарь
Логин/пароль""").pack()

lfeed=Label(text='Добро пожаловать! \nВаш питомец - креветка')
lfeed.grid(row=1,column=1,columnspan=4,rowspan=3)
def sleep():
    def sleep1():
        t1=time.time()
        t2=t1-t
        lfeed['text']="Ваша " + krevetka.name + " проснулась. Накоплено энергии: " +str(int(t2/3))
        krevetka.energy+=int(t2/3)
        a.destroy()
    t=time.time()
    a=Toplevel()
    a.title("Сон")
    a.geometry('+210+210')
    la=Label(a,text="Ваша "+krevetka.name+" спит.")
    la.grid(row=0,column=0)
    b81=Button(a,text="Проснуться", command=sleep1)
    b81.grid(row=1,column=0)

def status():
    lfeed['text']="Имя " + krevetka.name +". Ваша энергия: " +str(krevetka.energy) \
                   +"\n"+ "Ваша сила: " + str(krevetka.power)+ " Ваш размер: " + str(krevetka.razmer)+ " см."
def play():
    eventlist=["Купаем зверя",
               "Кидаем подводный мячик",
               "Ищем по морским норам",
               "Чешем за ушком",
               "Ищем хвостик",
               "Рисуем с креветочкой на песке"]
    indrand=random.randint(0,len(eventlist)-1)
    event= eventlist[indrand]

    
    def taim():
        lfeed['text']+='.'
    lfeed['text']=event
    lfeed.after(800,taim)
    lfeed.after(1600,taim)
    lfeed.after(2400,taim)
    
    numkri=random.randint(0,30)
   

    def krichis():
        def numclear(i=[0]):
                num = int(e1.get())
                if num == numkri:
                    lfeed['text']= "Вы угадали! Ваша "+krevetka.name +" получает " + str(numkri/2) \
                                   + " силы и " + str(numkri)+ " энергии."
                    krevetka.power+=int(numkri/2)
                    krevetka.energy+=numkri
                    a.destroy()
                elif i[0] == 4:
                    lfeed['text']="Вы проиграли! " +krevetka.name +" теряет " + str(numkri*2)+ " энергии."
                    krevetka.energy-=numkri*2
                    a.destroy()
                
                elif num>numkri:
                    lfeed['text']="Загаданное число меньше " + str(num)
                    i[0]+=1
                elif num < numkri:
                    lfeed['text']="Загаданное число больше " + str(num)
                    i[0]+=1

        a=Toplevel()
        a.geometry('+210+210')
        lfeed['text']="Ваша " + krevetka.name+" загадала число от 1 до 30. \nПостарайтесь угадать его с 5-и попыток"
        e1 = Entry(a)
        e1.grid(row=5,column=0)
        b80 = Button(a,text="Ok",command=numclear)
        b80.grid(row=6,column=0)
        
    lfeed.after(3000,krichis)

    


def hunt():
    if krevetka.razmer<100:
        zhiv1 = Watereat('"Морской червь"',10,2)
        zhiv2 = Watereat('"Морской огурец"',5,1)
        zhiv3 = Watereat('"Морская звезда"',20,5)
        zhiv4 = Watereat('"Морская черепаха"',80,30)
        zhiv5 = Watereat('"Страшная креветка"', 55, 15)
        zhiv6 = Watereat('"Осьминог"', 300, 45)
        zhiv7 = Watereat('"Морской ёж"', 30, 10) 
        zhiv8 = Watereat('"Морской крабик"', 45, 20)
        zhiv9 = Watereat('"Морская медуза"', 65, 40)
        zhiv10 = Watereat('"Кальмарчик"', 50, 35)
        zhiv11= Watereat('"Маленькая креветка"', 15, 7)


    if krevetka.razmer>100:
        zhiv1 = Watereat('"Морской тюлень"',100,50)
        zhiv2 = Watereat('"Морской скат"',120,60)
        zhiv3 = Watereat('"Морской морж"',140,65)
        zhiv4 = Watereat('"Морской дельфин"',200,80)
        zhiv5 = Watereat('"Морской касатка"',250,85)
        zhiv6 = Watereat('"Морской акула"',250,90)
        zhiv7 = Watereat('"Морской нерпа"',350,70)
        zhiv8 = Watereat('"Морской кашалот"',1000,100)
        zhiv9 = Watereat('"Морской кит"',1500,150)
        zhiv10 = Watereat('"Гигантская креветка"',10000,250)
        zhiv11 = Watereat('"Патрульный Корабль"',20000,350)
    
    eventlist=["Ищем в водорослях",
               "Плаваем среди скал",
               "Роем песочек",
               "Лезем в чужую нору",
               "Сидим в засадной ракушке",
               "Плывем под акулой",
               "Проплываем нефтяное пятно"]
    zhivotnie=[zhiv1, zhiv2, zhiv3, zhiv4, zhiv5, zhiv6, zhiv7, zhiv8, zhiv9, zhiv10, zhiv11]
    def kri():
        ind= random.randint(0,len(zhivotnie)-1)
        if krevetka.power > zhivotnie[ind].power:
            lfeed['text']="Вы поймали " + zhivotnie[ind].name + " !"
            krevetka.energy+=zhivotnie[ind].energy
            krevetka.razmer+=1
        else:
            lfeed['text']=zhivotnie[ind].name+ " сильнее Вас! \nПопробуйте еще раз..."
    
    indrand=random.randint(0,len(eventlist)-1)
    event= eventlist[indrand]

    def taim():
        lfeed['text']+='.'
    lfeed['text']=event
    lfeed.after(800,taim)
    lfeed.after(1600,taim)
    lfeed.after(2400,taim)
    lfeed.after(3000,kri)

b0 = Button(text="Статус",command=status).grid(row=2,column=5,sticky=E+N)   
b1 = Button(text="Охота",command=hunt).grid(row=4,column=2,sticky=W+S)
b2 = Button(text="Поиграть со зверем",command=play).grid(row=4,column=3,sticky=W+S)
b3 = Button(text="Спать",command=sleep).grid(row=5,column=3,sticky=W+S)
b4 = Button(text="Сохранить",command=save).grid(row=5,column=4,sticky=W+S)
b5 = Button(text="Загрузить",command=load).grid(row=4,column=4,sticky=W+S)
b6 = Button(text="Выйти",command=exitz).grid(row=5,column=5,sticky=E+S)
b7 = Button(text="О программе",command=about).grid(row=4,column=5,sticky=E+S)
l1 = Label(text="").grid(row=2,column=0,sticky=W+S)


root.mainloop()
