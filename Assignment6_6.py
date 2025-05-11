def For(number):
    if(number > 0):
     print("number is positive")

    elif(number == 0):
     print("number is zero")

    else:
     print("number is negative")



def main():
    print("enter number:")
    num = int(input())
    
    result = For(num)

if __name__ == "__main__":
    main()