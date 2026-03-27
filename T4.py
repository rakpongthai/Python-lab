x = input("input: ")
score = 0

spam = ["ฟรี", "ด่วน", "คลิก", "โปรโมชั่น", "เงินคืน", "รับทันที"]

for word in spam:
    if word in x:
        score += 2

if "http" in x or "https" in x:
    score += 3

for c in x:
    if c*4 in x:
        score += 2
        break


if score >= 10:
    level = "สแปม"
elif score >= 5:
    level = "น่าสงสัย"
else:
    level = "ปกติ"

print("คะแนน:", score)
print("ระดับ:", level)
