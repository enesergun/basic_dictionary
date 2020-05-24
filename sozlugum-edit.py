def kelime_ekle():
    with open("sozluk.txt", "a+",encoding="utf-8") as file:
        ingilizce = input("Kelimeyi giriniz:")
        turkce = input("Kelimenin Türkçe karşılığını giriniz:")
        ingilizce=ingilizce.ljust(15, " ")
        file.write(ingilizce+":"+turkce+"\n")
def kelime_goruntule():
    with open("sozluk.txt", encoding="utf-8") as file:
        print("ingilizce      :Türkçe")
        print(file.read())

########

while True:

    ıslem=input("""
1)Kelime ekleyiniz.
2)Tüm kelimeleri görüntüleyiniz.
3)Çıkış
=>""")

    if ıslem == "3":
        print("Çıkılıyor...")
        break
    elif ıslem == "1":
        kelime_ekle()
    elif ıslem =="2":
        kelime_goruntule()


