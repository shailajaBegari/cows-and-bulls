from random import randint
def list1(a):
    list2=[]
    i=0
    while i<4:
        a=randint(0,9)
        if a not in list2:
            list2.append(a)
            i=i+1
    print(list2)
    list3(list2)
    
def list3(list2):
    list3=[]
    list4=[]
    cow=5
    while cow>0:
        number=int(input("enter a num:"))
        position=int(input('enter a pos:'))
        if number in list2:
            if position==(list2.index(number)):
                print("Bull")
                list3.insert(position,number)
            else:
                print("cows")
                list4.insert(position,number)
        print("************************")
        cow=cow-1
    print(list3)
    while True:
        if list2==list3:
            print("congrats! u are winner")
        else:
            print("oops u are the looser!")
        playagain=input("do u want play again(y or n):")
        if playagain=="y":
            list1(a)
        elif playagain=="n":
            print("thank for playing...!")
            break
a=[0,1,2,3,4,5,6,7,8,9]
list1(a)
