class Node:
    def __init__(self, roll, name, marks):
        self.roll, self.name, self.marks, self.next = roll, name, marks, None

class StudentList:
    def __init__(self): self.head = None

    def add(self, r, n, m):
        new = Node(r, n, m)
        if not self.head: self.head = new
        else:
            t = self.head
            while t.next: t = t.next
            t.next = new
        print("✅ Added")

    def delete(self, r):
        t, p = self.head, None
        while t:
            if t.roll == r:
                if p: p.next = t.next
                else: self.head = t.next
                print("🗑️ Deleted"); return
            p, t = t, t.next
        print("⚠️ Not found")

    def update(self, r, n, m):
        t = self.head
        while t:
            if t.roll == r:
                t.name, t.marks = n, m
                print("✅ Updated"); return
            t = t.next
        print("⚠️ Not found")

    def search(self, r):
        t = self.head
        while t:
            if t.roll == r:
                print(f"🎓 Found → Roll:{t.roll}, Name:{t.name}, Marks:{t.marks}")
                return
            t = t.next
        print("⚠️ Not found")

    def sort(self, key="marks", desc=False):
        if not self.head: return
        s = True
        while s:
            s = False; t = self.head
            while t.next:
                a, b = (t.marks, t.next.marks) if key=="marks" else (t.roll, t.next.roll)
                if (not desc and a > b) or (desc and a < b):
                    t.roll, t.next.roll = t.next.roll, t.roll
                    t.name, t.next.name = t.next.name, t.name
                    t.marks, t.next.marks = t.next.marks, t.marks
                    s = True
                t = t.next
        print(f"✅ Sorted by {key} ({'desc' if desc else 'asc'})")

    def show(self):
        if not self.head: print("⚠️ No records"); return
        t = self.head
        print("\n📋 Records:")
        while t:
            print(f"Roll:{t.roll}, Name:{t.name}, Marks:{t.marks}")
            t = t.next


# --- Main Menu ---
s = StudentList()
while True:
    print("\n1.Add 2.Delete 3.Update 4.Search 5.Sort 6.Display 7.Exit")
    c = input("Choose: ")
    if c == '1':
        s.add(int(input("Roll: ")), input("Name: "), float(input("Marks: ")))
    elif c == '2':
        s.delete(int(input("Roll to delete: ")))
    elif c == '3':
        s.update(int(input("Roll to update: ")), input("New Name: "), float(input("New Marks: ")))
    elif c == '4':
        s.search(int(input("Roll to search: ")))
    elif c == '5':
        k = input("Sort by (roll/marks): ")
        o = input("Order (asc/desc): ")
        s.sort(k, o == "desc")
    elif c == '6':
        s.show()
    elif c == '7':
        break
    else:
        print("⚠️ Invalid choice")
