# 튜블고 리스트
from copy import copy  # 값을 복사
t1 = (1, 2, 3, 4, 5, 'a', 'b')
# del t1[0]  # 리스트경우 0번째 삭제 ,오류
# tl[0] = 'a'  # ,오류
t2 = (3, 4)
print(t1+t2)  # 튜블 더하기
print(t1*3)  # t1 튜블을 3번 출력


# 딕셔너리
dic = {'name': 'Kim', 'age': 16}
print(dic)
dic["kind"] = "hi"
print(dic)

# 순서가 아니라 Key를 넣는 것이 포인트,Key 중복X
print(dic.keys())
print(dic.values())

# 집합,중복 x, 순서가 없다. 중복되는 데이터를 다룰 때 사용된다.
sl = set([1, 2, 3])
# sl = {1, 2, 3}
print(sl)
l = [1, 2, 2, 3, 4, 5, 3, 4, 5]
newList = list(set(l))  # set()집합 메서드
print(newList)  # 중복이 제거된 LIst 출력

# 교집합
p1 = set([1, 2, 3, 4, 5, 6])
p2 = set([3, 4, 5, 6, 7])
print(p1.intersection(p2))  # 교집합 출력

# 차집합
p1 = set([1, 2, 3, 4, 5, 6])
p2 = set([3, 4, 5, 6, 7])
print(p1.difference(p2))


#--------------참과 거짓---------------------#

# qw = True
qw = [1, 2, 3, 4]
if True:
    print(qw)
print(type(qw))  # bool 불 == 불리언 w
# 자료형의 거짓은 빈 공간 ,none ,0
# 반복
while True:
    print(qw)
# 받기
a = [1, 2, 3]
b = copy(a)
a[1] = 4
print(a)
print(b)
