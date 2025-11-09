n = int(input("Enter number of customer IDs: "))
ids = [int(input(f"ID {i+1}: ")) for i in range(n)]
x = int(input("Enter ID to search: "))

# Linear Search
print("Linear:", "Found" if x in ids else "Not Found")

# Binary Search
ids.sort()
l, h, f = 0, n-1, False
while l <= h:
    m = (l + h)//2
    if ids[m] == x: f = True; break
    l, h = (m+1, h) if ids[m] < x else (l, m-1)
print("Binary:", "Found" if f else "Not Found")
