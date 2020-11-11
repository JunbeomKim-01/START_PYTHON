# 튜블고 리스트
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
# 순서가 아니라 Key를 넣는 것이 포인트
# Key 중복X
print(dic.keys())
print(dic.values())
