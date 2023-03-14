# ile=0
# for i in range(1,11):
#     if i%2 == 0:
#         ile +=1
#         print (i)
# print(f"ile liczb parzystych {ile}")


def fizz():
    k=""
    for i in range(1,101):
        if i%3 == 0 and i%5 == 0:
            k+="fizzbuzz \n"
        elif i%3 == 0:
            k+="fizz \n"
        elif i%5 == 0:
            k+="buzz \n"
        else:
            k+=str(i)+"\n"
    return k
print(fizz()) 