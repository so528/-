# 브루트 포스법으로 문자열 검색하기

def bf_match(txt: str, pat:str) -> int:
    pt = 0
    pp = 0

    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        else:
            pt = pt - pp +1
            pp = 0

        return pt - pp if pp == len(pat) else -1

if __name__=='__main__':
    s1=int(input('텍스트를 입력하세요.:'))
    s2=int(input('패턴을 입력하세요.:'))

    idx = bf_match(s1,s2)

    if idx == -1:
        print('일치하는 패턴이 없습니다.')

    else:
        print(f'{idx+1}번째 문자가 일치합니다.')