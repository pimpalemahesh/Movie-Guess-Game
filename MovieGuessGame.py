import random
class MovieGame:

    __movieList = ["janavar", "endgame", "tadap", "nowayhome", "sairat", "junglebook", "titanic", "threeidiots", "baahubali", "baahubalitwo", "dhamaka",
             "herapheri", "jollyllb2", "omg", "pushpa", "terminator", "totaldhamal", "sooryavanshi", "kaabil", "aquiteplace", "infinitywar", "squadgame", "bangbang", 
             "ironman", "singham", "tanaji", "uri", "Indian", "ghayal", "ghatak", "maatuzesalam", "Thor"]

    __ans = []
    __moviename = ""
    __size = 0
    __win = False

    def __init__(self):
        pass

    def __generate_moviename(self):
        self.__moviename = random.choice(self.__movieList).upper()
        self.__size = len(self.__moviename)

    def __chance(self):
        return self.__size + 5

    def __remove_ans(self):
        self.__ans.clear()

    def __display_qst(self):
        i = 0
        while i < self.__size:
            if(len(self.__ans) == 0 or len(self.__ans) < self.__size):
                self.__ans.append("_")
            print(self.__ans[i], end=" ")
            i+=1
        print()

    def __search_char(self, c):
        for i in range(self.__size):
            if(c == self.__moviename[i]):
                self.__ans[i] = c
            else:
                continue

    def __check_win(self):
        flag = 0
        for i in range(self.__size):
            if(self.__ans[i] == self.__moviename[i]):
                flag = 1
            else:
                flag = 0
                break
        return flag

    def play_game(self):
        self.__generate_moviename()
        chance_remain = self.__chance()
        while(chance_remain and not self.__win):
            
            self.__display_qst()
            ch = input("Enter guessed character :")
            self.__search_char(ch[0].upper())
            self.__display_qst()
            print("Chance Remained = ", chance_remain - 1)
            print()
            if(self.__check_win()):
                print("\nYour guess is right.\nMovie name is \"", self.__moviename, "\"")
                print("You win")
                self.__win = True
                break
            chance_remain -= 1

        if(self.__win == False):
            print("\nOut of chance.\nYou Lose!")
            print("Movie name was ", self.__moviename)

    def play_multiple_time(self):
        play_again = 'Y'
        while(play_again == 'Y'):
            self.__remove_ans()
            self.play_game()
            if(self.__win):
                self.__win = False
            
            play_again = input("Do you want to play again?")[0].upper()
