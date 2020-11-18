
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


print(plus_(a=3, b=2))


def say_HEllo(name, age):
    return "Hello" + name + "you are" + age+"years old"
    # f"hell {name} you are {age} years old"


hello = say_HEllo(name="kim", age=20)  # 순서 상관X 이름이 중요
print(hello)

# make No.7 function Challenge! + - / * %


def plus(a=0, b=0):
    return float(a) + float(b)


def minus(a=0, b=0):
    ma = float(a)
    mb = float(b)
    print(ma, mb)
    print(type(ma))
    return ma - mb


def times(a=0, b=0):
    return float(a) * float(b)


def division(a=0, b=0):
    return float(a) / float(b)


def reminder(a=0, b=0):
    return float(a) % float(b)


def nigate(a=0):
    return -float(a)


def power(a=0, b=0):
    return float(a) ** float(b)


p_plus = plus("2", 3)
m_minus = minus(2, "3")
t_times = times("2", 3)
d_division = division(2, "3")
r_reminder = reminder("2", 3)
n_nigate = nigate("2")
p_power = power(2, "3")

print(p_plus, m_minus, t_times, d_division, r_reminder, n_nigate, p_power)
