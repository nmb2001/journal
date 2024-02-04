import time
import gui

def menu():
    print("______________________")
    print("|   r     w     e    |")
    print("|         n          |")
    print("|____________________|")
    print("| r - read w - write |")
    print("| e - exit n - number|")
    print("|____________________|\n")

def menu2():
    print("______________________")
    print("|     r  w  e  n     |")
    print("|____________________|")


def choice():
    kill = 0
    while kill == 0:
        options = input()
        if options == "r":
            f = open("journal.txt", "r")
            print(f.read())
            f.close()
            menu2()
        elif options == "w":
            f = open("journal.txt", "a")
            f.write(timee)
            f.write("\n")
            user = input("Enter prompt: ")
            f.write(user)
            f.write("\n")
            f.close()
            menu2()
        elif options == "n":
            f = open("journal.txt", "r")
            num = len(f.readlines()) / 2
            print("Total Entries: ", num)

        elif options == "e":
            kill += 1



if __name__ == '__main__':
    x = time.time()
    timee = str(x)
    gui.window_func()

    menu()
    choice()
