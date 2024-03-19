### 자료형 데이터
> 여러개의 데이터를 하나의 변수에 저장시키는 데이터의 타입
-tuple 
    -자료형 데이터 중 가장 기본적인 형태
    -() 소괄호 안에 데이터들을 적어서 저장
    -한번 생성이 되면 안에 원소들을 수정, 추가, 삭제 불가능
-list
    -[]안에 데이터들을 적어서 저장
    -tuple과는 다르게 안에 원소들을 수정하거나 추가, 삭제 가능
    가능
    -내부의 함수들을 이용하여 데이터를 수정
    -리스트의 원소의 개수는 0개부터 생성 가능
-dict
    -{}안에 데이터들을 key:value의 형태로 적어서 저장
    -list는 위치를 기준으로 데이터가 생성이 된다면 dict는
    key값을 기준으로 데이터가 생성
    -딕셔너리의 원소의 개수는 0개부터 생성 가능

# tuple 데이터를 생성
tuple_a=(10,'test')
tuple_b=(3,3.14)
print(tuple_a)
print(tuple_b)
print(type(tuple_a))
print(type(tuple_b))
