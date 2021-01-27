def factorial(n): 
     
        fact = 1
        while(n > 1): 
            fact *= n 
            n = n-1
        return fact
n=int(input())
answer=factorial(n)
print(answer)

            
