import random
list1=[0,1,2,3,4,5,6,7,8,9]
list2=[]
def makenumber():
    for i in range (4):
        x=random.choice(list1)
        list2.append(x)
makenumber()

d=set(list2)
c=list(d)
print(c)
def playgame():
    i=0
    list3=[]
    list4=[] 
    cows=0
    bulls=0 
    while i<4:
        number=int(input('enter the number: '))
        position=int(input('enter the position: '))
        if (number in  c) and (position==c.index(number)):
            list3.insert(position,number)
            bulls+=1
        elif (number in  c) and (position!=c.index(number)):
            print('the number is in,but the position is wrong')
            print('these are the correct no.s you can use it by its position',c)
            position=int(input('enter the position by seing above options: '))
            list4.insert(position,number)
            cows+=1
        else:
            print('like this number is not there')
        i=i+1
    print("bulls: ",bulls)
    print('cows: ',cows)
    print(list3)
    if list3==c:
        print('****congratulations!!! you won the game******')
        again=input('you want to play again(y/n): ')
        if again=='yes':
            playgame()
        else:
            print('*THANK YOU FOR PLAYING GAME*')
playgame()