price = 100_000

age = int(input("Yoshingizni kiriting: "))

if 0 <= age < 7 :
    result = price - price / 100 * 50
    print(f"Yakuniy narx: {result} so'm (50% chegirma qo'llanildi)")

elif 7 <= age <= 17 :
    result = price - price / 100 * 20
    print(f"Yakuniy narx: {result} so'm (20% chegirma qo'llanildi)")

elif 60 <= age :
    result = price - price / 100 * 30
    print(f"Yakuniy narx: {result} so'm (30% chegirma qo'llanildi)")

else:
    print(f"Yakuniy narx: {price} so'm (chegirma qo'llanilmaydi! )")