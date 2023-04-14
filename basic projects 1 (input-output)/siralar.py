# okulda 3 yeni sınıf açılıyor. Her sırada 2 çğrenciden fazlası oturamaz.
# Her sınıftaki öğrenci sayısı bellidir. Kaç tane sıra alınması gerekir?
# programa her sınıftaki öğrenci sayısı ayrı satırlarda giriliyor.

a_sinifi=int(input("Kaç öğrenci var: "))
b_sinifi=int(input("Kaç öğrenci var: "))
c_sinifi=int(input("Kaç öğrenci var: "))

toplam_ogrenci=a_sinifi+b_sinifi+c_sinifi
sira_sayisi=((toplam_ogrenci)//2)+(toplam_ogrenci%2)

print("gerekli sıra sayısı : ", sira_sayisi)