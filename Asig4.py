n = int(input("Enter number of elements: "))
elements = [int(input(f"Element {i+1}: ")) for i in range(n)]
x = int(input("Enter number to search: "))
print("Frequency:", elements.count(x))
