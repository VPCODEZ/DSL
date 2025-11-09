undo, redo, doc = [], [], ""

while True:
    c = input("\n1.Add 2.Undo 3.Redo 4.Show 5.Exit: ")
    if c == '1':
        t = input("Text: ")
        undo.append(doc); doc += t; redo.clear()
    elif c == '2':
        if undo: redo.append(doc); doc = undo.pop()
        else: print("Nothing to undo")
    elif c == '3':
        if redo: undo.append(doc); doc = redo.pop()
        else: print("Nothing to redo")
    elif c == '4': print("Doc:", doc or "[Empty]")
    elif c == '5': break
