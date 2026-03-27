import re
from pythainlp.tokenize import word_tokenize
from pythainlp.transliterate import romanize

# ---------------------------
# 1. อ่านไฟล์
# ---------------------------
with open("song.txt", "r", encoding="utf-8") as f:
    s = f.read()  # อ่านข้อความทั้งหมดจากไฟล์

# ---------------------------
# 2. ตัดคำ
# ---------------------------
words = word_tokenize(s)  # แยกข้อความเป็นคำ ๆ

# ---------------------------
# 3. แปลงเป็นโรมัน (วิธีสั้น)
# ---------------------------
result = " ".join([romanize(w) for w in words])
print(result)

# ---------------------------
# 4. แปลงเป็นโรมัน (วิธี loop)
# ---------------------------
result = ""
for w in words:
    result += romanize(w) + " "

# ---------------------------
# 5. เขียนไฟล์ใหม่
# ---------------------------
with open("song1.txt", "w", encoding="utf-8") as f:
    f.write(result)

print("บันทึกไฟล์ song1.txt แล้ว")


# ---------------------------
# 7. แยกประโยคด้วย re.split
# ---------------------------
text = s
x = re.split(r"[.?!]", text)  # แยกเมื่อเจอ . ? !

# ---------------------------
# 8. ลบช่องว่าง/ประโยคว่าง
# ---------------------------
x = [s for s in x if s.strip() != ""]















print(x)
