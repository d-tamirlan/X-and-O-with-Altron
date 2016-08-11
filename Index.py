#coding: utf - 8
from Tkinter import *
import tkFont
import tkMessageBox
from PIL import Image, ImageTk
import random


root = Tk()
lab1 = Label(root)# Label для заталкивания в него фотографий
#Создадим список win_steps со всевозможными выйгрышными ходами
win_steps = [[11,12,13],[21,22,23],[31,32,33],[11,21,31],[12,22,32],[13,23,33],[11,22,33],[13,22,31]]
#Список всевозможных ходов
all_steps = [11,12,13,21,22,23,31,32,33]
#Создаем два списка для записывания ходов
steps_user = []
steps_altron = []
# Указывем путь к необходимым фотографиям
iml = Image.open('lose.jpg')
imx = Image.open('X.png')
imo = Image.open('O.png')
im1 = Image.open('easy.jpg')
im2 = Image.open('normal.jpg')
im3 = Image.open('hard.jpg')
#Загружаем фото на форму (как я понял)
imgl = ImageTk.PhotoImage(iml)
imgx = ImageTk.PhotoImage(imx)
imgo = ImageTk.PhotoImage(imo)
img1 = ImageTk.PhotoImage(im1)
img2 = ImageTk.PhotoImage(im2)
img3 = ImageTk.PhotoImage(im3)

def onEasy():
    lab1['image'] = img1 #Заталкиваем фото в Label
    lab1.place(x=890, y=0) #Задаем местоположение

def onNormal():
    lab1['image'] = img2
    lab1.place(x=790, y=0)

def onHard():
    lab1['image'] = img3
    lab1.place(x=680, y=0)

#Алгоритм вычисления побидителя
def Winner():
    brk = False
    winner = False
    level = var.get()
    if len(steps_user) > 2: # Запускаем алгоритм на 3 ходе для быстродействия программы
        for i in range(len(win_steps)):
            for j in range(len(win_steps[0])):
                #Присвоим переменным btn1,btn2,btn3 кнопки всевозможных выйгрышных ходов
                btn1 = all_btn.get(win_steps[i][j])
                btn2 = all_btn.get(win_steps[i][j+1])
                btn3 = all_btn.get(win_steps[i][j+2])

                wbtn1 = win_steps[i][j]
                wbtn2 = win_steps[i][j+1]
                wbtn3 = win_steps[i][j+2]
                #Если победил игрок:
                if (wbtn1 in steps_user) and (wbtn2 in steps_user) and (wbtn3 in steps_user):#Если во всех 3 кнопках "X"
                    if level == 1:
                        btn1['bg'], btn2['bg'], btn3['bg'] = 'red', 'red', 'red'#Выделям выйгрышные ходы красным
                        tkMessageBox.showinfo(parent=root, title=' ',message='Альтрон: Ты выиграл, но это был легкий уровень!')
                    elif level == 2:
                        btn1['bg'], btn2['bg'], btn3['bg'] = 'red', 'red', 'red'#Выделям выйгрышные ходы красным
                        tkMessageBox.showinfo(parent=root, title=' ',message='Альтрон: Неплохо, но я играл не в полную силу!')
                    elif level == 3:
                        winner = True

                    if level != 3:
                        for i in range(len(all_steps)):
                            btn = all_btn.get(all_steps[i])
                            btn['state'] = DISABLED# Блокируем оставшиеся ходы для полной остоновки игры после оперед-я победителя
                    brk = True
                    if level != 3:
                        return brk

                #Если победил Альтрон
                if (wbtn1 in steps_altron) and (wbtn2 in steps_altron) and (wbtn3 in steps_altron):
                    btn1['bg'], btn2['bg'], btn3['bg'] = 'red', 'red', 'red'
                    if level == 1:
                        tkMessageBox.showinfo(parent=root, title=' ',message='Альтрон: Ха-ха-ха! Ничтожество!')
                    elif level == 2:
                        tkMessageBox.showinfo(parent=root, title=' ',message='Альтрон: Ха-ха-ха! Как же ты жалок!')
                    elif level == 3:
                        lab1['image'] = imgl
                        lab1.place(x=890, y=0)
                        tkMessageBox.showinfo(parent=root, title=' ',message='Альрон: Ха-ха-ха! Тебе меня никогда не победить!')

                    for i in range(len(all_steps)):
                        btn = all_btn.get(all_steps[i])
                        btn['state'] = DISABLED# Блокируем оставшиеся ходы для полной остоновки игры после оперед-я победителя

                    brk = True
                    return brk# Вернуть True если найден побидитель

                break #Т.к. мы за один проход цикла "j" присваеваем все элементы по которым он проходит, необходимо
                #Всегда его прерывать дабы командой "j+1" и "j+2" не выйти за массив

            if brk == True:
                break# Если побидитель найден завершить алгоритм

        if winner is True:
            brk = False
            steps_user.reverse()#Чтобы достать последний сделанный ход играка реверсним список и возьмем 0-й элемент
            #Алгоритм перезаписывающий именно победный ход игрока если перезаписав его победа будет Альтрона
            for i in range(len(win_steps)):
                count = 0
                for j in range(len(win_steps[i])):
                    if steps_user[0] in win_steps[i]:
                        if win_steps[i][j] in steps_altron:
                            count += 1
                        if count == 2: # Если в подсписке "j" ести два 0-я, то перезапеши третий и сломай систему )
                            btn = all_btn.get(steps_user[0])
                            btn['image'] = imgo
                            btn['width'],btn['height'] = 130, 155
                            steps_altron.append(steps_user[0])
                            steps_user.pop(0)

                            btn1 = all_btn.get(win_steps[i][0])
                            btn2 = all_btn.get(win_steps[i][1])
                            btn3 = all_btn.get(win_steps[i][2])

                            btn1['bg'], btn2['bg'], btn3['bg'] = 'red', 'red', 'red'#Выделям выйгрышные ходы красным

                            for i in range(len(all_steps)):
                                btn = all_btn.get(all_steps[i])
                                btn['state'] = DISABLED# Блокируем оставшиеся ходы для полной остоновки игры после оперед-я победителя

                            lab1['image'] = imgl
                            lab1.place(x=890, y=0)
                            tkMessageBox.showinfo(parent=root, title=' ',message='Альрон: Ха-ха-ха! Тебе меня никогда не побидить!')
                            brk = True
                            break
                if brk is True:
                    return brk
            # Алгоритм перезаписывающий любой ход если перезаписав его Альтрон выиграет
            for i in range(len(win_steps)):
                count = 0
                for j in range(len(win_steps[i])):
                    if win_steps[i][j] in steps_altron:
                        count += 1
                    if count == 2:# Если имеется два 0-я в подсписке "j"
                        btn1 = all_btn.get(win_steps[i][0])
                        btn2 = all_btn.get(win_steps[i][1])
                        btn3 = all_btn.get(win_steps[i][2])
                        btn = all_btn.get(steps_user[0])

                        btn1['image'], btn2['image'], btn3['image'] = imgo, imgo, imgo
                        btn1['width'], btn1['height'] = 130, 155
                        btn2['width'], btn2['height'] = 130, 155
                        btn3['width'], btn3['height'] = 130, 155
                        btn['image'] = ''
                        btn['width'], btn['height'] = 18, 10
                        all_steps.append(steps_user[0])
                        steps_user.pop(0)

                        if win_steps[i][0] in all_steps:
                            all_steps.remove(win_steps[i][0])
                            steps_altron.append(win_steps[i][0])

                        elif win_steps[i][1] in all_steps:
                            all_steps.remove(win_steps[i][1])
                            steps_altron.append(win_steps[i][1])

                        elif win_steps[i][2] in all_steps:
                            all_steps.remove(win_steps[i][2])
                            steps_altron.append(win_steps[i][2])

                        btn1['bg'], btn2['bg'], btn3['bg'] = 'red', 'red', 'red'#Выделям выйгрышные ходы красным
                        lab1['image'] = imgl
                        lab1.place(x=890, y=0)

                        tkMessageBox.showinfo(parent=root, title=' ',message='Альрон: Ха-ха-ха! Тебе меня никогда не побидить!')

                        for i in range(len(all_steps)):
                            btn = all_btn.get(all_steps[i])
                            btn['state'] = DISABLED# Блокируем оставшиеся ходы для полной остоновки игры после оперед-я победителя

                        brk = True
                        break
                if brk is True:
                    return brk
            #Алгоритм который в любом случае присваивает победу Альтрону
            for i in range(len(win_steps)):
                for j in range(len(win_steps[i])):
                    if win_steps[i][j] in steps_altron: # Если в подсписке "j" имеется хотябы один 0
                        btn1 = all_btn.get(win_steps[i][0])
                        btn2 = all_btn.get(win_steps[i][1])
                        btn3 = all_btn.get(win_steps[i][2])
                        btn = all_btn.get(steps_user[0])

                        btn1['image'], btn2['image'], btn3['image'] = imgo, imgo, imgo
                        btn1['width'], btn1['height'] = 130, 155
                        btn2['width'], btn2['height'] = 130, 155
                        btn3['width'], btn3['height'] = 130, 155
                        btn['image'] = ''
                        btn['width'], btn['height'] = 18, 10
                        all_steps.append(steps_user[0])
                        steps_user.pop(0)

                        if win_steps[i][0] in all_steps:
                            all_steps.remove(win_steps[i][0])
                            steps_altron.append(win_steps[i][0])

                        elif win_steps[i][1] in all_steps:
                            all_steps.remove(win_steps[i][0])
                            steps_altron.append(win_steps[i][1])

                        elif win_steps[i][2] in all_steps:
                            all_steps.remove(win_steps[i][0])
                            steps_altron.append(win_steps[i][2])

                        btn1['bg'], btn2['bg'], btn3['bg'] = 'red', 'red', 'red'#Выделям выйгрышные ходы красным

                        for i in range(len(all_steps)):
                            btn = all_btn.get(all_steps[i])
                            btn['state'] = DISABLED# Блокируем оставшиеся ходы для полной остоновки игры после оперед-я победителя

                        lab1['image'] = imgl
                        lab1.place(x=890, y=0)
                        tkMessageBox.showinfo(parent=root, title=' ',message='Альрон: Ха-ха-ха! Тебе меня никогда не побидить!')
                        brk = True
                        break
                if brk is True:
                    return brk

    #Если произошла ничья
        if len(all_steps) == 0:
            tkMessageBox.showinfo(parent=root, title=' ',message='Ничья!')# Выводим сообщение о ничье

    if brk == False:
        return brk # Вернуть False если побидитель не найден


def Restart():
    global all_steps#Сделаем список "all_steps" глобальным, чтобы его изменение фиксирывались и вне функции "Restart"
#Заполним список всевозможных ходов и приведем кнопки в рабочее состояния для начала игры
    level = var.get()
    if level == 3:
        lab1['image'] = img3
        lab1.place(x=680,y=0)

    all_steps = [11,12,13,21,22,23,31,32,33]
    for i in range(len(all_btn)):
        btn = all_btn.get(all_steps[i])
        btn['image'] = ''
        btn['width'], btn['height'] = 18, 10
        btn['state'] = NORMAL
        btn['bg'] = 'white'
    hard['state'], normal['state'], easy['state'] = NORMAL, NORMAL, NORMAL# Приводим Radiobutton'ы в рабочее состояние
    rool['text'] = 'Ты ходишь первым, человек!'
    while steps_user:
        steps_user.pop(0)
    while steps_altron:
        steps_altron.pop(0)

def Altron(m):
    if (m in steps_user) or (m in steps_altron): #Если одна кнопка нажимается дважды
        return 0
    rool['text'] = ' '
    steps_user.append(m)
    level = var.get()# Достаем значение переменной "var" т.е. узнаем какой Radiobutton активен
    btn = all_btn.get(m)# Достаем из словоря all_btn кнопку соответ-ю ходу игрока
    btn['image'] = imgx#Задаем имя "Х"
    btn['width'],btn['height'] = 130, 155
    #btn['state'] = DISABLED# Делаем ее не активной, чтобы хитрюга не нажал ее дважды
    all_steps.remove(m)# Удаляем из списка совершенный ход, дабы не перезаписать ход игрока
    brk = Winner()
    if brk == False:#Если игрок совершил победный ход т.е. функция Winner() вернула True, то не совршать ход Альтрона
        #И полностью завершить игру
        if level == 1:
            hard['state'], normal['state'] = DISABLED, DISABLED# Блокируем выбор сложности при старте игры дабы хакер не схитрил
            if len(all_steps): # Если список all_steps не пустой
                r = random.randint(0, len(all_steps) - 1)# Задаем "r" рандовмный индекс => что all_steps[r] - рандомный ход
                btn = all_btn.get(all_steps[r])# Достаем из словоря кнопку соответ-ю рандомному ходу
                btn['image'] = imgo
                btn['width'],btn['height'] = 130, 155
                steps_altron.append(all_steps[r])
                all_steps.remove(all_steps[r])# Удаляем из списка рандомный ход Альтрона
                Winner()

        #Алгоритм для уровня сложности "Средний"
        if level == 2:
            hard['state'], easy['state'] = DISABLED, DISABLED
            brk = False
            #Выискивание победного хода Альтрона и совершение его
            for i in range(len(win_steps)):
                for j in range(len(win_steps[i])):

                    btn1 = all_btn.get(win_steps[i][j])
                    btn2 = all_btn.get(win_steps[i][j+1])
                    btn3 = all_btn.get(win_steps[i][j+2])

                    wbtn1 = win_steps[i][j]
                    wbtn2 = win_steps[i][j+1]
                    wbtn3 = win_steps[i][j+2]

                    if (wbtn1 in steps_altron) and (wbtn2 in steps_altron):
                        if win_steps[i][j+2] in all_steps:
                            btn3['image'] = imgo
                            btn3['width'], btn3['height'] = 130, 155
                            steps_altron.append(win_steps[i][j+2])
                            all_steps.remove(win_steps[i][j+2])
                            brk = True

                    if (wbtn1 in steps_altron) and (wbtn3 in steps_altron):
                        if win_steps[i][j+1] in all_steps:
                            btn2['image'] = imgo
                            btn2['width'],btn2['height'] = 130, 155
                            steps_altron.append(win_steps[i][j+1])
                            all_steps.remove(win_steps[i][j+1])
                            brk = True

                    if (wbtn2 in steps_altron) and (wbtn3 in steps_altron):
                        if win_steps[i][j] in all_steps:
                            btn1['image'] = imgo
                            btn1['width'],btn1['height'] = 130, 155
                            steps_altron.append(win_steps[i][j])
                            all_steps.remove(win_steps[i][j])
                            brk = True

                    break
                if brk == True:
                    Winner()
                    break


            if brk == False:
                brk = False
                #Выискиваем победный ход игрока и не даем его совершить
                for i in range(len(win_steps)):
                    for j in range(len(win_steps[i])):

                        btn1 = all_btn.get(win_steps[i][j])
                        btn2 = all_btn.get(win_steps[i][j+1])
                        btn3 = all_btn.get(win_steps[i][j+2])

                        wbtn1 = win_steps[i][j]
                        wbtn2 = win_steps[i][j+1]
                        wbtn3 = win_steps[i][j+2]

                        if (wbtn1 in steps_user) and (wbtn2 in steps_user):
                            if win_steps[i][j+2] in all_steps:
                                btn3['image'] = imgo
                                btn3['width'], btn3['height'] = 130, 155
                                steps_altron.append(win_steps[i][j+2])
                                all_steps.remove(win_steps[i][j+2])
                                brk = True

                        if (wbtn1 in steps_user) and (wbtn3 in steps_user):
                            if win_steps[i][j+1] in all_steps:
                                btn2['image'] = imgo
                                btn2['width'], btn2['height'] = 130, 155
                                steps_altron.append(win_steps[i][j+1])
                                all_steps.remove(win_steps[i][j+1])
                                brk = True

                        if (wbtn2 in steps_user) and (wbtn3 in steps_user):
                            if win_steps[i][j] in all_steps:
                                btn1['image'] = imgo
                                btn1['width'],btn1['height'] = 130, 155
                                steps_altron.append(win_steps[i][j])
                                all_steps.remove(win_steps[i][j])
                                brk = True

                        break
                    if brk == True:
                        Winner()
                        break

            # Если не найдены победные ходы игрока и Альтрона делаем рандомный ход
            if brk == False:
                if len(all_steps):
                    r = random.randint(0,len(all_steps) - 1)# Задаем "r" рандовмный индекс => что all_steps[r] - рандомный ход
                    btn = all_btn.get(all_steps[r])
                    btn['image'] = imgo
                    btn['width'],btn['height'] = 130, 155
                    steps_altron.append(all_steps[r])
                    all_steps.remove(all_steps[r])
                    Winner()

        #Алгоритм для уровня сложности "Тяжелый"
        if level == 3:
            normal['state'], easy['state'] = DISABLED, DISABLED
            brk = False
            #Выискивание победного хода Альтрона и совершение его
            for i in range(len(win_steps)):
                for j in range(len(win_steps[i])):

                    btn1 = all_btn.get(win_steps[i][j])
                    btn2 = all_btn.get(win_steps[i][j+1])
                    btn3 = all_btn.get(win_steps[i][j+2])

                    wbtn1 = win_steps[i][j]
                    wbtn2 = win_steps[i][j+1]
                    wbtn3 = win_steps[i][j+2]

                    if (wbtn1 in steps_altron) and (wbtn2 in steps_altron):
                        if win_steps[i][j+2] in all_steps:
                            btn3['image'] = imgo
                            btn3['width'], btn3['height'] = 130, 155
                            steps_altron.append(win_steps[i][j+2])
                            all_steps.remove(win_steps[i][j+2])
                            brk = True

                    if (wbtn1 in steps_altron) and (wbtn3 in steps_altron):
                        if win_steps[i][j+1] in all_steps:
                            btn2['image'] = imgo
                            btn2['width'],btn2['height'] = 130, 155
                            steps_altron.append(win_steps[i][j+1])
                            all_steps.remove(win_steps[i][j+1])
                            brk = True

                    if (wbtn2 in steps_altron) and (wbtn3 in steps_altron):
                        if win_steps[i][j] in all_steps:
                            btn1['image'] = imgo
                            btn1['width'],btn1['height'] = 130, 155
                            steps_altron.append(win_steps[i][j])
                            all_steps.remove(win_steps[i][j])
                            brk = True

                    break
                if brk == True:
                    Winner()
                    break


            if brk == False:
                brk = False
                #Выискиваем победный ход игрока и не даем его совершить
                for i in range(len(win_steps)):
                    for j in range(len(win_steps[i])):

                        btn1 = all_btn.get(win_steps[i][j])
                        btn2 = all_btn.get(win_steps[i][j+1])
                        btn3 = all_btn.get(win_steps[i][j+2])

                        wbtn1 = win_steps[i][j]
                        wbtn2 = win_steps[i][j+1]
                        wbtn3 = win_steps[i][j+2]

                        if (wbtn1 in steps_user) and (wbtn2 in steps_user):
                            if win_steps[i][j+2] in all_steps:
                                btn3['image'] = imgo
                                btn3['width'], btn3['height'] = 130, 155
                                steps_altron.append(win_steps[i][j+2])
                                all_steps.remove(win_steps[i][j+2])
                                brk = True

                        if (wbtn1 in steps_user) and (wbtn3 in steps_user):
                            if win_steps[i][j+1] in all_steps:
                                btn2['image'] = imgo
                                btn2['width'], btn2['height'] = 130, 155
                                steps_altron.append(win_steps[i][j+1])
                                all_steps.remove(win_steps[i][j+1])
                                brk = True

                        if (wbtn2 in steps_user) and (wbtn3 in steps_user):
                            if win_steps[i][j] in all_steps:
                                btn1['image'] = imgo
                                btn1['width'],btn1['height'] = 130, 155
                                steps_altron.append(win_steps[i][j])
                                all_steps.remove(win_steps[i][j])
                                brk = True

                        break
                    if brk == True:
                        Winner()
                        break
#Необходимо при любом конце игры иметь хотябы одну пару "О"! Зачем? Ибо я так задумал программу!
            #Ход 22 в этом отлично помогает
            if brk == False:
                if 22 in all_steps:
                    btn = all_btn.get(22)
                    btn['image'] = imgo
                    btn['width'],btn['height'] = 130, 155
                    steps_altron.append(22)
                    all_steps.remove(22)
                    brk = True
                    Winner()

            #Если ход 22 занять то делать угловые ходы! Зачем? Затем, что я так хочу!
            if brk == False:
                angles = [11,13,31,33]
                for i in range(len(angles)):
                    if angles[i] not in all_steps:
                        angles[i] = 0
                while 0 in angles:
                    angles.remove(0)# Если элементы списка удалять сразу, то список смещается и цикл проходит не по всем элементам! Поэтому я их сначала обнуляю и затем удаляю
                if angles:
                    r = random.randint(0,len(angles) - 1)
                    btn = all_btn.get(angles[r])
                    btn['image'] = imgo
                    btn['width'], btn['height'] = 130, 155
                    steps_altron.append(angles[r])
                    all_steps.remove(angles[r])
                    brk = True
                    Winner()



            if brk == False:
                if len(all_steps):
                    r = random.randint(0,len(all_steps) - 1)# Задаем "r" рандовмный индекс => что all_steps[r] - рандомный ход
                    btn = all_btn.get(all_steps[r])
                    btn['image'] = imgo
                    btn['width'], btn['height'] = 130, 155
                    steps_altron.append(all_steps[r])
                    all_steps.remove(all_steps[r])
                    Winner()


root.title('X and O with Altron')
root.state('zoomed')# Разворачиваем программу на весь экран
s = tkFont.Font(family='Arial',size=10,)

b11 = Button(root, bg='white', width=18,height=10, command=lambda m=11: Altron(m))#Передаем параметру 'm' позицию кнопки
b11.grid(row = 1, column = 1 )

b12 = Button(root, bg='white', width=18,height=10, command=lambda m=12: Altron(m))
b12.grid(row = 1, column = 2)

b13 = Button(root, bg='white', width=18,height=10, command=lambda m=13: Altron(m))
b13.grid(row = 1, column = 3)
#--------------------------------
b21 = Button(root, bg='white', width=18,height=10, command=lambda m=21: Altron(m))
b21.grid(row = 2, column = 1)

b22 = Button(root, bg='white', width=18,height=10, command=lambda m=22: Altron(m))
b22.grid(row = 2, column = 2)

b23 = Button(root, bg='white', width=18,height=10, command=lambda m=23: Altron(m))
b23.grid(row = 2, column = 3)
#--------------------------------
b31 = Button(root, bg='white', width=18,height=10, command=lambda m=31: Altron(m))
b31.grid(row = 3, column = 1)

b32 = Button(root, bg='white', width=18,height=10, command=lambda m=32: Altron(m))
b32.grid(row = 3, column = 2)

b33 = Button(root, bg='white', width=18,height=10, command=lambda m=33: Altron(m))
b33.grid(row = 3, column = 3)
#================================
# Создадим "словарь" всех кнопок
all_btn = {11:b11,12:b12,13:b13,21:b21,22:b22,23:b23,31:b31,32:b32,33:b33}

Brestart = Button(root,text='Начать заново!',width='15',height='5',command=Restart)
Brestart.place(x=500,y=200)

rool = Label(root,text='Ты ходишь первым, человек!',fg='red',font='Arial 15')
rool.place(x=60,y=500)


# Создадим специальные переменные для работы с Radiobutton
var = IntVar()
var.set(1)

hard = Radiobutton(root,text='Тяжелый',font='Arial 13',fg='red',variable=var,value='3',command=onHard)
hard.place(x=500,y=50)

normal = Radiobutton(root,text='Средний',font='Arial 13',fg='blue',variable=var,value='2',command=onNormal)
normal.place(x=500,y=90)

easy = Radiobutton(root,text='Легкий',font='Arial 13',fg='green',variable=var,value='1',command=onEasy)
easy.place(x=500,y=130)
# Какое значение у переменной "var", тот Radiobutton и активен
# Если "3", то активен "hard", если "1", то активен "easy"

onEasy()# По умолчанию задаем уровень сложности "Легкий"

root.mainloop()