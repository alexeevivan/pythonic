import os
from colorama import init
from colorama import Fore, Back, Style

# добавляем возможность выбора языка
lang_selection = int(input("Для выбора русского языка введите «1»\nTo choose english language press «2»:"))
while lang_selection!=1 and lang_selection!=2:
    print(Fore.RED)
    print("\nВведён некорректный символ. Попробуйте еще раз.\nAn invalid response was entered. Try again.")
    print(Fore.WHITE)
    lang_selection = int(input("Для выбора русского языка введите «1»\nTo choose english language press «2»:"))

if lang_selection==1:
# задаём значения всем переменным, которые будут встречаться в коде, при этом не требующие ввода данных от игроков
    j = ("\nВас приветствует игра «-Tic-Tac-Toe-» !!! \nКаждая ячейка выделена цифровым индикатором для удобства планирования ходов.")
    b2 = """
        |     |                  |     |   
     ■  |  ■  |  ■            1  |  2  |  3  
        |     |                  |     |    
    — — — — — — — — —         — — — — — — — — —
        |     |                  |     |   
     ■  |  ■  |  ■            4  |  5  |  6  
        |     |                  |     |     
    — — — — — — — — —         — — — — — — — — —
        |     |                  |     |   
     ■  |  ■  |  ■            7  |  8  |  9  
        |     |                  |     |
    — — — — — — — — —         — — — — — — — — — 
    """
    x = ("X")
    o = ("O")
    c = ("Отлично! Игрок")
    d = ("использует символ X. Осталось совсем чуть-чуть.")
    e = ("использует символ O. Пора начинать.")
    pl = ("+")
    pl_1 = ("/'+'/")
    pl_2 = ('/"+"/')
    pl_3 = ("«+»")
    pl_4 = pl or pl_1 or pl_2 or pl_3
    m = ("-")
    m_1 = ("/'-'/")
    m_2 = ('/"-"/')
    m_3 = ("«-»")
    m_4 = m or m_1 or m_2 or m_3

    print(j)
    print(Fore.MAGENTA, b2)
    print(Fore.WHITE)

    player_1 = str.title(input("Введите имя первого игрока:"))
    player_2 = str.title(input("\nВведите имя второго игрока:"))
    p_1, p_2  = player_1, player_2

    print(Fore.LIGHTCYAN_EX)
    print("Приветствую,", player_1, "и", player_2, "!")

    # добавление вопроса о предпочтении использования того или иного сивола, поскольку ввод первого имени не будет являтся причиной получения права первого хода
    print(Fore.WHITE)
    f = int(input("Введите «1», если игрок №1 желает использовать символ Х, или «2» - если будет использовать символ О:"))
    print(Fore.LIGHTCYAN_EX)
    while f!=1 and f>2:
        print("Введён некорректный ответ. Попробуйте ещё раз.")
        f = int(input("Введите «1», если игрок №1 желает использовать символ Х, или «2» - если будет использовать символ О:"))
    if f==1:
        print(c, p_1, d)
    if f==2:
        print(c, p_1, e)

    print(Fore.WHITE)
    g = int(input("Введите «1», если игрок №2 использует символ Х, или «2» - если использует символ О:"))
    while g==f:
        print(Fore.RED)
        print("К сожалению, данный символ зарезервирован за игроком", player_1, ".")
        print(Fore.WHITE)
        g = int(input("Введите «1», если игрок №2 использует символ Х, или «2» - если использует символ О:"))
    while g!=1 and g>2:
        print(Fore.RED)
        print("Введён некорректный ответ. Попробуйте ещё раз.")
        print(Fore.WHITE)
        g = int(input("Введите «1», если игрок №2 использует символ Х, или «2» - если использует символ О:"))
    print(Fore.LIGHTCYAN_EX)
    if g==1:
        print(c, p_2, d)
    if g==2:
        print(c, p_2, e)

    print(Fore.WHITE)

    # создание дополнительной вариативности соврешения ходов
    u = input("Как правило, первый ход совершает игрок, чьим символом является «Х». \nВ зависимости от выбранного Вами ответа («+» или «-») я пойму, желаете ли Вы следовать этому правилу:")

    # отображение результатов в зависимости от внесённых условий от пользователя
    while u!=pl_4 and u!=m_4:
        print("Введён некорректный символ. Попробуйте ещё раз:")
        u = input("Как правило, первый ход совершает игрок, чьим символом является «Х». \nВ зависимости от выбранного Вами ответа («+» или «-») я пойму, желаете ли Вы следовать этому правилу:")
    print(Fore.LIGHTCYAN_EX)
    if (u==pl_4 and f==1) or (u!=pl_4 and g==2) or (u!=m_4 and f==1) or (u==m_4 and g==2):
        print("Отлично. Игрок", p_1, "использует символ", x,"и начнёт игру первым!")
        print("Отлично. Игрок", p_2, "использует символ", o,"и начнёт игру вторым!")
    elif (u!=pl_4 and f==1) or (u==pl_4 and g==2) or (u==m_4 and f==1) or (u!=m_4 and g==2):
        print("Отлично. Игрок", p_2, "использует символ", o,"и начнёт игру первым!")
        print("Отлично. Игрок", p_1, "использует символ", x,"и начнёт игру вторым!")
    elif (u==pl_4 and g==1) or (u!=pl_4 and f==2) or (u!=m_4 and g==1) or (u==m_4 and f==2):
        print("Отлично. Игрок", p_2, "использует символ", x,"и начнёт игру первым!")
        print("Отлично. Игрок", p_1, "использует символ", o,"и начнёт игру вторым!")
    elif (u!=pl_4 and g==1) or (u==pl_4 and f==2) or (u==m_4 and g==1) or (u!=m_4 and f==2):
        print("Отлично. Игрок", p_1, "использует символ", o,"и начнёт игру первым!")
        print("Отлично. Игрок", p_2, "использует символ", x,"и начнёт игру вторым!")

    print(Fore.MAGENTA, b2)
    print(Fore.WHITE)

    # сокращение до переменных выбора игрока
        # player_1 == X, player_2 == 0
    xx_1 = int((u==pl_4 and f==1) or (u!=pl_4 and g==2) or (u!=m_4 and f==1) or (u==m_4 and g==2))
        # player_1==O, player_2==X
    xx_2 = int((u!=pl_4 and g==1) or (u==pl_4 and f==2) or (u==m_4 and g==1) or (u!=m_4 and f==2))
        # player_2==X, player_1==O
    xx_3 = int((u==pl_4 and g==1) or (u!=pl_4 and f==2) or (u!=m_4 and g==1) or (u==m_4 and f==2))
        # player_2==O, player_1==X
    xx_4 = int((u!=pl_4 and f==1) or (u==pl_4 and g==2) or (u==m_4 and f==1) or (u!=m_4 and g==2))

    win_combo = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
    board = list(range(1, 10))


    # функция отображения строки, которая будет использована каждый раз после совершения хода
    def draw_board():
        for i in range(3):
            print("     |     |     ")
            print(" ", board[0 + i * 3], " | ", board[1 + i * 3], " | ", board[2 + i * 3])
            print("     |     |     ")
            print("— — — — — — — — —")


    # функция, отслеживающая ситуацию на игровом поле в зависимости от выбранной ячейки для хода
    def take_input(player_token):
        while True:
            value = input("Введите номер ячейки для совершения хода:")
            if not (value in '123456789'):
                print("Введён некорректный символ. Попробуйте ещё раз:")
                continue
            value = int(value)
            if str(board[value - 1]) in "XO":
                print(Fore.RED)
                print("К сожалению, данная клетка уже занята Вашим оппонентом. Выберите пустую ячейку:")
                print(Fore.WHITE)
                continue
            board[value - 1] = player_token
            break


    # функция проверки условий для победы
    def check_win():
        for each in win_combo:
            if (board[each[0]-1]) == (board[each[1]-1]) == (board[each[2]-1]):
                return board[each[1]-1]
        else:
            return False


    def main():
        # установка счётчика ходов
        counter = 0
        while True:
            # если предыдущие введённые данные пользователем привели к следующему результату:\
            # игрок_1 начнёт игру первым с использованием символа «Х»
            if xx_1==True:
                os.system('cls' if os.name=='nt' else 'clear')
                print(Fore.MAGENTA)
                draw_board()
                print(Fore.WHITE)
                if counter % 2 == 0:
                    take_input(x)
                else:
                    take_input(o)
                if counter > 3:
                    victory = check_win()
                    if victory:
                        print(Fore.GREEN)
                        draw_board()
                        if victory==check_win() and victory==x:
                            print(Fore.BLUE)
                            print(player_1, "победил(-a)!")
                            print(Fore.WHITE)
                            break
                        if victory==check_win() and victory==o:
                            print(Fore.BLUE)
                            print(player_2, "победил(-a)!")
                            print(Fore.WHITE)
                            break
                counter += 1
                if counter > 8:
                    draw_board()
                    print(Fore.YELLOW)
                    print("Ничья!")
                    print(Fore.WHITE)
                    break
            # если предыдущие введённые данные пользователем привели к следующему результату:\
            # игрок_1 начнёт игру первым с использованием символа «О»
            elif xx_2==True:
                os.system('cls' if os.name=='nt' else 'clear')
                print(Fore.MAGENTA)
                draw_board()
                print(Fore.WHITE)
                if counter % 2 == 0:
                    take_input(o)
                else:
                    take_input(x)
                if counter > 3:
                    victory = check_win()
                    if victory:
                        print(Fore.GREEN)
                        draw_board()
                        if victory==check_win() and victory==o:
                            print(Fore.BLUE)
                            print(player_1, "победил(-a)!")
                            print(Fore.WHITE)
                            break
                        if victory==check_win() and victory==x:
                            print(Fore.BLUE)
                            print(player_2, "победил(-a)!")
                            print(Fore.WHITE)
                            break
                counter += 1
                if counter > 8:
                    draw_board()
                    print(Fore.YELLOW)
                    print("Ничья!")
                    print(Fore.WHITE)
                    break
            # если предыдущие введённые данные пользователем привели к следующему результату:\
            # игрок_2 начнёт игру первым с использованием символа «Х»
            elif xx_3==True:
                os.system('cls' if os.name=='nt' else 'clear')
                print(Fore.MAGENTA)
                draw_board()
                print(Fore.WHITE)
                if counter % 2 == 0:
                    take_input(x)
                else:
                    take_input(o)
                if counter > 3:
                    victory = check_win()
                    if victory:
                        print(Fore.GREEN)
                        draw_board()
                        if victory==check_win() and victory==x:
                            print(Fore.BLUE)
                            print(player_2, "победил(-a)!")
                            print(Fore.WHITE)
                            break
                        if victory==check_win() and victory==o:
                            print(Fore.BLUE)
                            print(player_1, "победил(-a)!")
                            print(Fore.WHITE)
                            break
                counter += 1
                if counter > 8:
                    draw_board()
                    print(Fore.YELLOW)
                    print("Ничья!")
                    print(Fore.WHITE)
                    break
            # если предыдущие введённые данные пользователем привели к следующему результату:\
            # игрок_2 начнёт игру первым с использованием символа «О»
            elif xx_4==True:
                os.system('cls' if os.name=='nt' else 'clear')
                print(Fore.MAGENTA)
                draw_board()
                print(Fore.WHITE)
                if counter % 2 == 0:
                    take_input(o)
                else:
                    take_input(x)
                if counter > 3:
                    victory = check_win()
                    if victory:
                        print(Fore.GREEN)
                        draw_board()
                        if victory==check_win() and victory==o:
                            print(Fore.BLUE)
                            print(player_2, "победил(-а)!")
                            print(Fore.WHITE)
                            break
                        if victory==check_win() and victory==x:
                            print(Fore.BLUE)
                            print(player_1, "победил(-а)!")
                            print(Fore.WHITE)
                            break
                counter += 1
                if counter > 8:
                    draw_board()
                    print(Fore.YELLOW)
                    print("Ничья!")
                    print(Fore.WHITE)
                    break
            

    main()

elif lang_selection==2:
    # задаём значения всем переменным, которые будут встречаться в коде, при этом не требующие ввода данных от игроков
    j = ("\nWelcome to the «Tic-Tac-Toe» game!!! \nEach cell is highlighted with a digital indicator for easy planning of moves.")
    b2 = """
        |     |                  |     |   
     ■  |  ■  |  ■            1  |  2  |  3
        |     |                  |     |    
    — — — — — — — — —         — — — — — — — — —
        |     |                  |     |   
     ■  |  ■  |  ■            4  |  5  |  6  
        |     |                  |     |     
    — — — — — — — — —         — — — — — — — — —
        |     |                  |     |   
     ■  |  ■  |  ■            7  |  8  |  9  
        |     |                  |     |
    — — — — — — — — —         — — — — — — — — — 
    """
    x = ("X")
    o = ("O")
    c = ("Greeat! The player")
    d = ("uses X symbol. Wait for a moment.")
    e = ("uses O symbol. Let's start.")
    pl = ("+")
    pl_1 = ("/'+'/")
    pl_2 = ('/"+"/')
    pl_3 = ("«+»")
    pl_4 = pl or pl_1 or pl_2 or pl_3
    m = ("-")
    m_1 = ("/'-'/")
    m_2 = ('/"-"/')
    m_3 = ("«-»")
    m_4 = m or m_1 or m_2 or m_3

    print(j)
    print(Fore.MAGENTA, b2)
    print(Fore.WHITE)

    player_1 = str.title(input("Enter the name of the first player:"))
    player_2 = str.title(input("\nEnter the name of the second player:"))
    p_1, p_2  = player_1, player_2

    print(Fore.LIGHTCYAN_EX)
    print("Welcome,", player_1, "and", player_2, "!")

    # добавление вопроса о предпочтении использования того или иного сивола, поскольку ввод первого имени не будет являтся причиной получения права первого хода
    print(Fore.WHITE)
    f = int(input("Enter «1» if player # 1 wants to use the X symbol, or «2» - if wants to use the O symbol:"))
    print(Fore.LIGHTCYAN_EX)
    while f!=1 and f>2:
        print("An invalid response was entered. Try again:")
        f = int(input("Enter «1» if player # 1 wants to use the X symbol, or «2» - if wants to use the O symbol:"))
    if f==1:
        print(c, p_1, d)
    if f==2:
        print(c, p_1, e)

    print(Fore.WHITE)
    g = int(input("Enter «1» if player # 1 wants to use the X symbol, or «2» - if he/she want to use the O symbol:"))
    while g==f:
        print(Fore.RED)
        print("Unfortunately, this symbol is reserved for the player", player_1, ".")
        print(Fore.WHITE)
        g = int(input("Enter «1» if player # 1 wants to use the X symbol, or «2» - if he/she want to use the O symbol:"))
    while g!=1 and g>2:
        print(Fore.RED)
        print("An invalid response was entered. Try again:.")
        print(Fore.WHITE)
        g = int(input("Enter «1» if player # 2 uses the X symbol, or «2» - if he/she uses the O symbol:"))
    print(Fore.LIGHTCYAN_EX)
    if g==1:
        print(c, p_2, d)
    if g==2:
        print(c, p_2, e)

    print(Fore.WHITE)

    # создание дополнительной вариативности соврешения ходов
    u = input("As a rule, the first move is made by the player whose symbol is «X». \ n depending on the answer you choose («+» or «-»), I will understand if You want to follow this rule:")

    # отображение результатов в зависимости от внесённых условий от пользователя
    while u!=pl_4 and u!=m_4:
        print("An invalid response was entered. Try again:")
        u = input("As a rule, the first move is made by the player whose symbol is «X». \ n depending on the answer you choose («+» or «-»), I will understand if You want to follow this rule:")
    print(Fore.LIGHTCYAN_EX)
    if (u==pl_4 and f==1) or (u!=pl_4 and g==2) or (u!=m_4 and f==1) or (u==m_4 and g==2):
        print("Great. The player", p_1, "uses sybmol", x,"and will start the game first!")
        print("Great. The player", p_2, "uses sybmol", o,"and will start the game first!")
    elif (u!=pl_4 and f==1) or (u==pl_4 and g==2) or (u==m_4 and f==1) or (u!=m_4 and g==2):
        print("Great. The player", p_2, "uses sybmol", o,"and will start the game first!")
        print("Great. The player", p_1, "uses sybmol", x,"and will start the game first!")
    elif (u==pl_4 and g==1) or (u!=pl_4 and f==2) or (u!=m_4 and g==1) or (u==m_4 and f==2):
        print("Great. The player", p_2, "uses sybmol", x,"and will start the game first!")
        print("Great. The player", p_1, "uses sybmol", o,"and will start the game first!")
    elif (u!=pl_4 and g==1) or (u==pl_4 and f==2) or (u==m_4 and g==1) or (u!=m_4 and f==2):
        print("Great. The player", p_1, "uses sybmol", o,"and will start the game first!")
        print("Great. The player", p_2, "uses sybmol", x,"and will start the game first!")

    print(Fore.MAGENTA, b2)
    print(Fore.WHITE)

    # сокращение до переменных выбора игрока
        # player_1 == X, player_2 == 0
    xx_1 = int((u==pl_4 and f==1) or (u!=pl_4 and g==2) or (u!=m_4 and f==1) or (u==m_4 and g==2))
        # player_1==O, player_2==X
    xx_2 = int((u!=pl_4 and g==1) or (u==pl_4 and f==2) or (u==m_4 and g==1) or (u!=m_4 and f==2))
        # player_2==X, player_1==O
    xx_3 = int((u==pl_4 and g==1) or (u!=pl_4 and f==2) or (u!=m_4 and g==1) or (u==m_4 and f==2))
        # player_2==O, player_1==X
    xx_4 = int((u!=pl_4 and f==1) or (u==pl_4 and g==2) or (u==m_4 and f==1) or (u!=m_4 and g==2))

    win_combo = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
    board = list(range(1, 10))


    # функция отображения строки, которая будет использована каждый раз после совершения хода
    def draw_board():
        for i in range(3):
            print("     |     |     ")
            print(" ", board[0 + i * 3], " | ", board[1 + i * 3], " | ", board[2 + i * 3])
            print("     |     |     ")
            print("— — — — — — — — —")


    # функция, отслеживающая ситуацию на игровом поле в зависимости от выбранной ячейки для хода
    def take_input(player_token):
        while True:
            value = input("Pleaese enter the cell number to make the move:")
            if not (value in '123456789'):
                print("An invalid response was entered. Try again:")
                continue
            value = int(value)
            if str(board[value - 1]) in "XO":
                print(Fore.RED)
                print("Unfortunately, this cell is already occupied by your opponent. Select an empty cell:")
                print(Fore.WHITE)
                continue
            board[value - 1] = player_token
            break


    # функция проверки условий для победы
    def check_win():
        for each in win_combo:
            if (board[each[0]-1]) == (board[each[1]-1]) == (board[each[2]-1]):
                return board[each[1]-1]
        else:
            return False


    def main():
        # установка счётчика ходов
        counter = 0
        while True:
            # если предыдущие введённые данные пользователем привели к следующему результату:\
            # игрок_1 начнёт игру первым с использованием символа «Х»
            if xx_1==True:
                os.system('cls' if os.name=='nt' else 'clear')
                print(Fore.MAGENTA)
                draw_board()
                print(Fore.WHITE)
                if counter % 2 == 0:
                    take_input(x)
                else:
                    take_input(o)
                if counter > 3:
                    victory = check_win()
                    if victory:
                        print(Fore.GREEN)
                        draw_board()
                        if victory==check_win() and victory==x:
                            print(Fore.BLUE)
                            print(player_1, "won!")
                            print(Fore.WHITE)
                            break
                        if victory==check_win() and victory==o:
                            print(Fore.BLUE)
                            print(player_2, "won!")
                            print(Fore.WHITE)
                            break
                counter += 1
                if counter > 8:
                    draw_board()
                    print(Fore.YELLOW)
                    print("Draw!")
                    print(Fore.WHITE)
                    break
            # если предыдущие введённые данные пользователем привели к следующему результату:\
            # игрок_1 начнёт игру первым с использованием символа «О»
            elif xx_2==True:
                os.system('cls' if os.name=='nt' else 'clear')
                print(Fore.MAGENTA)
                draw_board()
                print(Fore.WHITE)
                if counter % 2 == 0:
                    take_input(o)
                else:
                    take_input(x)
                if counter > 3:
                    victory = check_win()
                    if victory:
                        print(Fore.GREEN)
                        draw_board()
                        if victory==check_win() and victory==o:
                            print(Fore.BLUE)
                            print(player_1, "won!")
                            print(Fore.WHITE)
                            break
                        if victory==check_win() and victory==x:
                            print(Fore.BLUE)
                            print(player_2, "won!")
                            print(Fore.WHITE)
                            break
                counter += 1
                if counter > 8:
                    draw_board()
                    print(Fore.YELLOW)
                    print("Draw!")
                    print(Fore.WHITE)
                    break
            # если предыдущие введённые данные пользователем привели к следующему результату:\
            # игрок_2 начнёт игру первым с использованием символа «Х»
            elif xx_3==True:
                os.system('cls' if os.name=='nt' else 'clear')
                print(Fore.MAGENTA)
                draw_board()
                print(Fore.WHITE)
                if counter % 2 == 0:
                    take_input(x)
                else:
                    take_input(o)
                if counter > 3:
                    victory = check_win()
                    if victory:
                        print(Fore.GREEN)
                        draw_board()
                        if victory==check_win() and victory==x:
                            print(Fore.BLUE)
                            print(player_2, "won!")
                            print(Fore.WHITE)
                            break
                        if victory==check_win() and victory==o:
                            print(Fore.BLUE)
                            print(player_1, "won!")
                            print(Fore.WHITE)
                            break
                counter += 1
                if counter > 8:
                    draw_board()
                    print(Fore.YELLOW)
                    print("Draw!")
                    print(Fore.WHITE)
                    break
            # если предыдущие введённые данные пользователем привели к следующему результату:\
            # игрок_2 начнёт игру первым с использованием символа «О»
            elif xx_4==True:
                os.system('cls' if os.name=='nt' else 'clear')
                print(Fore.MAGENTA)
                draw_board()
                print(Fore.WHITE)
                if counter % 2 == 0:
                    take_input(o)
                else:
                    take_input(x)
                if counter > 3:
                    victory = check_win()
                    if victory:
                        print(Fore.GREEN)
                        draw_board()
                        if victory==check_win() and victory==o:
                            print(Fore.BLUE)
                            print(player_2, "won!")
                            print(Fore.WHITE)
                            break
                        if victory==check_win() and victory==x:
                            print(Fore.BLUE)
                            print(player_1, "won!")
                            print(Fore.WHITE)
                            break
                counter += 1
                if counter > 8:
                    draw_board()
                    print(Fore.YELLOW)
                    print("Draw!")
                    print(Fore.WHITE)
                    break
            

    main()