def add(value1,value2):
    output = (value1+value2)
    return output

def main():
    print("Enter value 1:")
    val1 = int(input())
    print("Enter value 2:")
    val2 = int(input())

    ans = add(val1,val2)
    print("Addition of two numbers :",ans)

if __name__ == "__main__":
    main()