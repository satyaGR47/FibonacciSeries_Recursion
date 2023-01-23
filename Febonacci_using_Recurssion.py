def febonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    
    ans = febonacci(n-1)+febonacci(n-2)
    return ans

if __name__=="__main__":
    num = int(input("Enter nth term of Febonacci sereis to get the element : "))
    print(febonacci(num))
