n = int(input("Enter number of elements: "))
elements = [int(input(f"Element {i+1}: ")) for i in range(n)]
print("Maximum element:", max(elements))
