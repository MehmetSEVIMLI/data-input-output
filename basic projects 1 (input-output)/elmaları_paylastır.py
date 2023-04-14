# "n" çocuk "k" elmayı eşit şekilde paylaşıyor, kalanlar sepete kalıyor.

#program "n" ve "k" sayılarını alıyor ve cevap oalrak 2 sayıyı veriyor.

# bunu çözen bir program yazpınız.

n=int(input("Kaç çocuk var: "))
k=int(input("kaç elma var: "))

dagitilan_elma=k//n
kalan_elma=k%n

print("Her bir çocuğa düşen elma sayısı: ", dagitilan_elma)
print("Sepette kalan elma sayısı: ",kalan_elma)