import random
num=[]
attempts=0
def makenumber():
    for i in range(4):
        x=random.randint(0,10)
        num.append(x)  
    if len(num)>len(set(num)):
        num.clear()
        makenumber()
def playgame():
    global attempts
    attempts+=1
    cows=0
    bulls=0
    print(num)
    choices=input('please enter the 4 digit number: ')
    guess=[]
    for i in range(4):
        guess.append(int(choices[i]))
    for i in range(4):
        for j in range(4):
            if (guess[i]==num[j]):
                cows+=1
    for x in range(4):
        if (guess[x]==num[x]):
            bulls+=1
    print('bulls:',bulls)
    print('cows:',cows)
    if (bulls==4):
        print('you won the game!!!')
    if (bulls!=4):
        playgame()

makenumber()
playgame()