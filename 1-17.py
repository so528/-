# 가로, 세로 길이가 정수이고 넓이가 area인 직사각형에서 변의 길이 나열하기

area = int(input('직사각형의 넓이를 입력하세요.:'))

for x in range (1,area+1,1):
    if x * x > area:
        break
    if area % x:
        continue
    print(x,'X', area // x)
