import random
a = 100


print("""""
====================================
WELCOME TO YOU WILL ALWAYS LOSE
====================================
WIN BIG OR GO HOME WITH NOTHING.....
====================================
GET 3 OF THE SAME NUMBER TO WIN DUBBLE WHAT YOU PLAYED
====================================
""")
b = input("YOU CURRENTLY HAVE ", print(a"CREDITS,HOW MUCH WOULD YOU LIKE TO PLAY"))



def randomNum():
    for iteration, num in enumerate(range(4)):
        firs = random.randint(1,10)
        secon = random.randint(1,10)
        thir = random.randint(1,10)
        fourt = random.randint(1,10)
    print('Lotto number 1', firs)
    print('Lotto number 2', secon)
    print('Lotto number 3', thir)
    print('Lotto number 4', fourt)
    print('the number of tries', iteration)
print(randomNum())

