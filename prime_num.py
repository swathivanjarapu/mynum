n=int(input("enter number "))
if n<1:
    print("not prinme")
elif n>2:
    for i in range(n):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i,"is prime")
else:
    print("not prime number")