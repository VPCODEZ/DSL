from collections import deque

events = deque()
next_id = 1

def add_event():
    global next_id
    name = input("Event name: ").strip()
    if name:
        events.append({"id": next_id, "name": name})
        print(f"Added: id={next_id}, name='{name}'")
        next_id += 1
    else:
        print("Empty name — not added.")

def process_next():
    if events:
        e = events.popleft()
        print(f"Processed: id={e['id']}, name='{e['name']}'")
    else:
        print("No events to process.")

def display_pending():
    if not events:
        print("No pending events.")
    else:
        print("Pending events:")
        for e in events:
            print(f"  id={e['id']}, name='{e['name']}'")

def cancel_event():
    try:
        cid = int(input("Enter event id to cancel: "))
    except ValueError:
        print("Invalid id.")
        return
    for e in list(events):           # iterate over snapshot to safely remove
        if e["id"] == cid:
            events.remove(e)
            print(f"Canceled: id={cid}, name='{e['name']}'")
            return
    print("Event id not found or already processed.")

menu = {
    "1": add_event,
    "2": process_next,
    "3": display_pending,
    "4": cancel_event,
    "5": exit
}

while True:
    print("\n1.Add  2.Process Next  3.Display Pending  4.Cancel by ID  5.Exit")
    choice = input("Choose: ").strip()
    action = menu.get(choice)
    if action:
        action()
    else:
        print("Invalid choice.")
