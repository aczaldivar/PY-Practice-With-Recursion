# Write code for algorithm 3 below
def fibonacci (n):
    if n<=0:
        print("incorrect input")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)    
print ("2nd fibonacci number:")
print (fibonacci(2))
print("4th fib. number")
print(fibonacci(4))
print("8th fib. number:")
print(fibonacci(8))