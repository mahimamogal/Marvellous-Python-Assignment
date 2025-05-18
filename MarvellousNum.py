def ChkPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
    
import MarvellousNum


def ListPrime():
    n = int(input("Enter number of elements: "))
    elements = [int(input(f"Element {i+1}: ")) for i in range(n)]
    
    prime_sum = 0
    for num in elements:
        if MarvellousNum.ChkPrime(num):
            prime_sum += num

    print("Sum of prime numbers:", prime_sum)

if __name__ == "__main__":
    ListPrime()
