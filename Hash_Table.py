class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash(self, key):
        return key % self.size  # Division method

    def insert(self, key, value):
        h = self.hash(key)
        for pair in self.table[h]:
            if pair[0] == key:
                pair[1] = value
                print("✅ Updated")
                return
        self.table[h].append([key, value])
        print("✅ Inserted")

    def search(self, key):
        h = self.hash(key)
        for pair in self.table[h]:
            if pair[0] == key:
                print(f"🔍 Found → {pair[1]}")
                return
        print("⚠️ Not found")

    def delete(self, key):
        h = self.hash(key)
        for i, pair in enumerate(self.table[h]):
            if pair[0] == key:
                del self.table[h][i]
                print("🗑️ Deleted")
                return
        print("⚠️ Not found")

    def display(self):
        print("\n📦 Hash Table:")
        for i, bucket in enumerate(self.table):
            print(f"{i} → {bucket}")


# --- Main Menu ---
ht = HashTable()
while True:
    print("\n1.Insert 2.Search 3.Delete 4.Display 5.Exit")
    c = input("Choose: ")
    if c == '1':
        ht.insert(int(input("Key: ")), input("Value: "))
    elif c == '2':
        ht.search(int(input("Key to search: ")))
    elif c == '3':
        ht.delete(int(input("Key to delete: ")))
    elif c == '4':
        ht.display()
    elif c == '5':
        break
    else:
        print("⚠️ Invalid choice")
