import re

text = input("input text: ")
text = re.split(r"[.!?]+", text)
text = [s.strip() for s in text if s.strip()]

print("จำนวนประโยค:", len(text))

word = [len(s.split()) for s in text]
longest = text[word.index(max(word))]
avg = sum(word) / len(word)

print("ค่าเฉลี่ยคำ:", round(avg, 2))
print("ประโยคที่ยาวที่สุด:", longest)
