import random
n=random.randint(1,50)
i=1
l=5
print("you got",l," guesses")
while (i< 5):
    print("number of guesses left==",(5-i))
    print("enter a number you want to check",end="          ANS:-          ")
    c=int(input())
    if c<(n-10) and c>(n-15) :
        if i != 5:
            print("little far away")
            i=i+1
    elif c>(n+10) and c<(n+15) :
        if i != 5:
            print("little far away")
            i=i+1
    elif c<(n) and c>(n-10):
        if i != 5:
            print("add some more")
            i=i+1
    elif c>(n) and c<(n+10):
        if i != 5:
            print("subtract some")
            i=i+1
    elif c<(n-15):
        if i != 5:
            print("too less")
            i=i+1
    elif c>(n+15):
        if i != 5:
            print("too more")
            i=i+1
    elif c==n:
        print("you guessed it right, it was",n)
        print("no of guesses took to finish==",i)
        i=i+1
        break
    elif i==5:
        print("it was ",n)
        print("game over!!! 5 chance finished")