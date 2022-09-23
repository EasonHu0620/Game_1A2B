import random
guess = int(input("要猜幾個數字的密碼:"))
pwd = random.sample(range(0,10),guess)
A = 0
B = 0

while A != guess:
    num = input("請輸入"+str(guess)+"個數字:")
    while len(num) != guess or len(set(num)) != guess:
        num = input("請輸入"+str(guess)+"個數字,且數字不重複:")

    list1 = list(map(int,list(num)))
    A = 0
    B = 0
    for i in list1:
        if i in pwd:
            if list1.index(i) == pwd.index(i):
                A += 1
            else:
                B += 1
    print(num,":",A,"A",B,"B",sep="")

print("你猜對了,密碼為：",num)