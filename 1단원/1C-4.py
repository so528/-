# 함수 내부, 외부에서 정의한 변수와 객체의 식별 번호를 출력하기

n = 1
def put_id():
    x = 1
    print(id(x))

print(id(1))
print(id(n))
put_id()
