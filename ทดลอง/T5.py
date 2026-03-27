files = ["f1.txt", "f2.txt", "f3.txt"]

q = input("ค้นหา: ")

for file in files:
    f = open(file, "r", encoding="utf-8")
    text = f.read()
    f.close()
    
    count = text.count(q)
    
    if count > 0:
        print(file, count)
