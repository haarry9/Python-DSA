def chck_palindrome(n):
    x = n
    rev =0
    while(x !=0):
        rev = rev*10+x%10
        x//=10
    bool = False
    if(rev == n):
        bool  =True
    return bool

n = int(input("Enter input: "))
print(chck_palindrome(n))
        
