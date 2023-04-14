#3 günün başından beri kaç dakika geçtiği programa "n" olarak giriliyor.
# program kaç saat ve dakika geçtiğini gösteriyor.
# saat 0 ile 23 arası. dakika 0 ile 59 arası.
# programa girilen n sayısı bir gündek 24 saatten fazla olabilir.

print(2%24)
n=int(input("toplam dakika sayısını giriniz: "))

gunVEYAsaat=( ( n // 60 ) % 24 ) ## n sayısını öncelikle saate çeviriyoruz ve ardından saati güne bölerek gün sayısını çıkarıyoruz.
dakika=(n%60)
print(gunVEYAsaat)
print(dakika)
