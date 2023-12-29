import math
def createFunction(g):
    name={
        "cos":math.cos,  
        "sin":math.sin ,
        "e":math.e,
        "ln":math.log
    }
    return eval("lambda x: "+g,name)
def simpson(f):
    a=input("enter point a")
    while(not a.replace(".","").isnumeric() and not a.replace("-","").isnumeric()): #check if a is a number
        a=input("a should be a number")
    a=float(a)    
    b=input("enter point b")
    while(not b.replace(".","").isnumeric() and not a.replace("-","").isnumeric()): #check if b is a number
        b=input("b should be a number")
    b=float(b)
    n=input("enter the number of panels") #number of paneels
    n=int(n)
    h=(b-a)/n 
    even=0
    odd=0
    for i in range(1,n): #1 to n-1
        if i%2==0:       #even case   
            x=a+i*h
            print("x in even: ",x)
            even=even+f(x)
        else:            #odd case
            x=a+i*h
            print("x is odd: ",x)
            odd=odd+f(x)
    intergal=(h/3)*(f(a)+f(b)+4*odd+2*even)
    print("the integral is: ",round(intergal,4))
def main():
    print("enter the function g(x)")
    f=input()
    f=createFunction(f)
    simpson(f)
main()
