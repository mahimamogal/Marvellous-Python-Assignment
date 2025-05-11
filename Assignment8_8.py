def Star(num):
    star = ''
    for i in range (num):
     star += "*"
    return star
        
def main():
    print("Enter how many stars you want ?")
    n = int(input())
    ans = Star(n)
    print(ans)

if __name__ == "__main__":
    main()
