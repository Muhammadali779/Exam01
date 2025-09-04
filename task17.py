score = float(input("Ballingizni kiriting: "))

if 90 <= score <= 100:
    print("A (A'lo)")

elif 80 <= score < 90:
    print("B (Yaxshi)")

elif 70 <= score < 80:
    print("C (Qoniqarli)")

elif 60 <= score < 70:
    print("D (Qoniqarsiz)")

elif 0 <= score < 60:
    print("F (Yomon)")

else:
    print("Ball 0-100 oralig'ida bo'lishi kerak!")

