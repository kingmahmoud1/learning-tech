while True :
    num1=int(input("entre the first  number :\n"))
    num2=int(input("entre the second number :\n"))
    opearation=input("which opearation do you make choose between add or mins or times or devied")
    opearatio=opearation.lower()
    if opearatio=="add":
        sum=num1+num2
        print(sum)
    elif opearatio=="mins":
        min=num1-num2
        print(min)
    elif opearatio=="times":
        ti=num1*num2
        print(ti)
    elif opearatio=="devied":
        dev=num1/num2
        print(dev)
    finsh=input("To leave , Write leave:\n")
    fin=finsh.lower()
    if fin=="leave":
        print("hi")
