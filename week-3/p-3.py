
#function ,print(),type(), int()
age = "18"
print(type(age))  # str
n_age = int(age)
print(n_age)
print(type(n_age))  # int

# Creating My Function
# def , 함수를 define 한다


def say_hello(name="Kim"):
    print("hello"+name)


say_hello()
# python은 {}가 함수의 끝을 판단하는 것이 아니라 indent가 함수를 판단.

# Function Argyments


def say_hello2(who):
    print("hello"+" " + who)


say_hello2("junbeom")


def plus(a, b):
    print(a+b)


def minus(a, b):
    print(a-b)


plus(10, 3)  # 10+3
minus(3, 2)  # 3-2

# returns


def plus_(a, b):
    return a+b


print(plus_(3, 2))
