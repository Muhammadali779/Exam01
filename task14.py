file = input("Fayl nomini kiriting: ")
pdf = ".pdf"
docx = ".docx"
txt = ".txt"

if file.endswith(pdf):
    print("Fayl turi: pdf")

elif file.endswith(docx):
        print("Fayl turi: docx")

elif file.endswith(txt):
        print("Fayl turi: txt")
else:
       print("Dokument turi hato")
