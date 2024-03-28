## 인자의 개수가 가변인 함수를 생성
## 모든 인자 값들을 누적합을 하여 되돌려주는 함수
def func_6(*args):
    print(args)
    print(type(args))
    # 합계 초기 값을 지정
    result=0
    #args가 튜플 형태의 데이터임으로
    #각원소의 값들을 하나씩 출력하여 result 더해준다.
    for i in args:
        #i는 어떤 데이터?: i안에 있는 정수-- 인자값 
        #print(i)
        result+=i 
    return result
