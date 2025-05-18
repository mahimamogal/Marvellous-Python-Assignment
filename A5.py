n = int(input("Enter number: "))
if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print("Not a Prime Number")
            break
    else:
        print("It is Prime Number")
else:
    print("Not a Prime Number")
