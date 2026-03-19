import numpy as np
def array_calculator():
    try:
        r=int(input("enter the size of array: "))
        a=[]
        for i in range(r):
            b=int(input(f"enter number {i+1} : "))
            a.append(b)
        a=np.array(a)
        while True:
            o=input("enter the operation(+,-,*,/ or reset): ")
            if o=="+":
                p=int(input("enter the number to add to the array: "))
                a=a+p
                print(f"result array: {a}")
            elif o=="-":
                p=int(input("enter the number to subtract from the array: "))
                a=a-p
                print(f"result array: {a}")
            elif o=="*":
                p=int(input("enter the number to multiply with the array: "))
                a=a*p
                print(f"result array: {a}")
            elif o=="/":
                p=int(input("enter the number to divide the array: "))
                if p==0:
                    print("division by zero is not allowed.")
                    return
                else:
                    a=a/p
                    print(f"result array: {a}")
            elif o.lower()=="reset":
                return
            else:
                print("invalid operation. Please enter a valid operation.")
    except ValueError:
        print("Invalid input. Please enter valid integers.")
    
while True:
    array_calculator()
    cont=input("do you want to continue? (y/n): ")
    if cont.lower()!="y":
        print("thank you for using the calculator. Goodbye!")
        break





