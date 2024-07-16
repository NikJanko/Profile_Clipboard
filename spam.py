import keyboard as kb
import time as t
import csv


with open('messages.csv', newline='', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter='|')

    for x in reader:
        print(x[0]) # printing as a list -> save it in file









def txt(s: ""):
    kb.release("CTRL")
    t.sleep(0.1)
    kb.write(text=s, delay=0)
    kb.release("CTRL")
    kb.unhook_all()


def main():
    p1 = []

    while not kb.is_pressed(']'):

        # t.sleep(0.5)
        if kb.is_pressed('CTRL+F1'):
            txt(p1[0])
            pass
        elif kb.is_pressed('CTRL+F2'):
            txt(p1[1])
            pass
        elif kb.is_pressed('CTRL+F3'):
            txt(p1[2])
            pass
        elif kb.is_pressed('CTRL+F4'):
            txt(p1[3])
            pass
        elif kb.is_pressed('CTRL+F5'):
            txt(p1[4])
            pass
        elif kb.is_pressed('CTRL+F6'):
            txt(p1[5])
            pass
        elif kb.is_pressed('CTRL+F7'):
            txt(p1[6])
            pass
        elif kb.is_pressed('CTRL+F8'):
            txt(p1[7])
            pass
        elif kb.is_pressed('CTRL+F9'):
            txt(p1[8])
            pass
        elif kb.is_pressed('CTRL+F10'):
            txt(p1[9])
            pass

    kb.unhook_all()
    return

# if __name__ == '__main__':
#     main()


# while not kb.is_pressed('\\'):
#     key = kb.read_key()
#     print(key)
