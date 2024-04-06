def arithmetic_ops(op):
    num1 = int(input("input 1st number:"))
    num2 = int(input("input 2nd number:"))
    return num1,num2,op(num1,num2)

# +와 -는 함수로 정의한다
def add(x,y):return x+y
def sub(x,y):return x-y

while True:
    op = input("input operation:")
    if op == "end":
       break   # "반복을 종료"
    elif op == "+":
       num1,num2,ret = arithmetic_ops(add)
    elif op=="-":
        num1,num2,ret=arithmetic_ops(sub) # 정의된 함수 사용
    elif op == "*":
       num1,num2,ret = arithmetic_ops(lambda x,y:x*y) # 익명함수(lambda) 사용
    elif op=="/":
        num1,num2,ret=arithmetic_ops(lambda x,y:x/y)
    elif op=="%":
        num1,num2,ret=arithmetic_ops(lambda x,y:x%y)
    else:
        print("Invalid operation")
        continue # Invalid operation이므로 연산결과를 출력하지 않고 "넘어간다".
    print(f"{num1}{op}{num2} = {ret}")  # 연산 결과를 출력

print("Exit program")
