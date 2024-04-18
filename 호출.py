def twofold1(a):
    a = 2 * a

def twofold2(a):
    a = 2 * a
    return a

x = 5
twofold1(x) # 참조호출 방식에서는 x값이 10이 되지만 복사호출 방식에는 x값이 변하지 않음
print(x)

x = 5
x = twofold2(x) # 호출방식과 무관하게 x는 10이 됨
print(x)

def sample(a:int, b):
    a = 2 * a
    b.append('test')
    
x = 5         # 정수(불변타입) -> 복사호출     
y = [1,2]     # 리스트(가변타입) -> 참조호출
sample(x,y)   # x 값은 불변, y 값은 변화
print(x)
print(y)