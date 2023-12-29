import math
#from sympy import *


def createFunction(g):
    name={
        "cos":math.cos,  
        "sin":math.sin ,
        "e":math.e,
        
    }
    return eval("lambda x: "+g,name)

def main():
    print("enter initial guess")
    x=float(input())

    print("enter the function g(x)")
    g=input()
    g=createFunction(g) #make the function legal python code by adding lambda, making it a lambda function.

    print("enter the number of accuracy you want")
    accuracy = int(input())

    x_next=g(x)#get the xi+1 befor we enter the loop, so we can use it it's condition

 

    iteration=0
    print("enter the maximum number of iterations: ")
    max_iteration=int(input())
    
    while x!=x_next and iteration<max_iteration:   
        x=x_next
        x_next=round(g(x),accuracy) #10 because we want 10 number after the ,
        iteration+=1
        print("x:",x)
        print("x next:",x_next)
        print("number of iterations:",iteration)
        
main()
