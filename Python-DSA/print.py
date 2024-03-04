
def loop_fun(n):
    for i in range(1, n+1):
        print(i, end='')

def list_compherension(n):
    print(*[i for i in range(1,n+1)],sep="")

def map_fun(n):
    print("".join(map(str, range(1,n+1))))

# def while_loop(n):
#     i =1
#     while(1 <=n):
#         print(1,end='')
#         i+=1


n = int(input("Enter n: "))
loop_fun(n)
list_compherension(n)
map_fun(n)
# while_loop(n)



'''
Print the list of integers from  through  as a string, without spaces and without using any string functions
'''