text = input("Matn kiriting: ")

unli = "aeiouAEIOU"

n = 0

for i in text:
    if i in unli:
        n += 1

print(f"Unlilar soni: {n}")