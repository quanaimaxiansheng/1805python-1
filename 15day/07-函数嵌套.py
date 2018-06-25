import time
#当多个函数里面有相同的功能的时候，就需要把相同的部分挪出来，封装成一个独立的模块，在进行调用
def play_game():
    for i in range(1000):
        time.sleep(1)
        print("刺激呀 战场呀")
        if i == 10:
            father_fight()
def play_game1():
    for i in range(1000):
        time.sleep(1)
        print("刺激呀 撸啊撸")
        if i == 15:
            father_fight()
            print("哈哈哈")

def father_fight():
    print("你爸爸来了，？？？？")
    print("回家被揍了 楱死了")
    
#play_game()
play_game1()
