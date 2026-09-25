num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))
op = input('Select operation (+, -, *, /): ')
if op == '+':
    ans = num1 + num2
    print(num1,"+",num2,"=",ans)
elif op == '-':
    ans = num1 - num2
    print(num1,"-",num2,"=",ans)
elif op == '*':
    ans = num1 * num2
    print(num1,"*",num2,"=",ans)
elif op == '/':
    ans = num1 / num2
    print(num1,"/",num2,"=",ans)
else:
    print("Error: Operation")