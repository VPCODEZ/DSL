from statistics import mode

# --- Input for Members ---
n = int(input("Enter number of members: "))
members = {}
for i in range(n):
    name = input(f"Member {i+1} name: ")
    count = int(input(f"Books borrowed by {name}: "))
    members[name] = count

# --- Input for Books ---
m = int(input("\nEnter number of books: "))
books = {}
for i in range(m):
    bname = input(f"Book {i+1} name: ")
    borrow = int(input(f"Borrow count of {bname}: "))
    books[bname] = borrow

# --- 1. Average books borrowed by members ---
avg_borrow = sum(members.values()) / len(members)
print("\nAverage borrowed per member:", avg_borrow)

# --- 2. Book with highest & lowest borrowings ---
max_book = max(books, key=books.get)
min_book = min(books, key=books.get)
print("Highest borrowed book:", max_book, "=>", books[max_book])
print("Lowest borrowed book:", min_book, "=>", books[min_book])

# --- 3. Members who borrowed 0 books ---
no_borrow = sum(1 for x in members.values() if x == 0)
print("Members with 0 borrowings:", no_borrow)

# --- 4. Most frequent borrow count (mode) ---
mode_borrow = mode(books.values())
print("Most frequent borrow count:", mode_borrow)

