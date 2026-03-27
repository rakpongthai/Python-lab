import re

text = input("พิมพ์ข้อความ: ")
print("ก่อน:", text)

text = text.lower()
text = re.sub(r"[^\w\sก-๙]", "", text)
text = " ".join(text.split())

print("หลัง:", text)
