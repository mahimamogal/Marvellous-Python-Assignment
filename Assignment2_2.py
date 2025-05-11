def ChkNum(number):
    if(number%2== 0):
        print("even number")
    else :
        print("Odd number")
def main():
    print("enter number")
    num = int(input())
    ans = ChkNum(num)


if __name__ == "__main__":
    main()

