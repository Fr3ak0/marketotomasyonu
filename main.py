from market import *
import time
urunNesne = Market()

print("""************************
Market Uygulamasına Hoşgeldiniz!
1. ÜRÜN EKLE
2. ÜRÜN SİL
3. STOK SORGULA (Ürün Adına Göre) :
4. STOK SORGULA (Marka Adına Göre) :
5. SUPERMARKET TOPLAM ÜRÜN STOĞU SORGULA
----------------------------------------
6. SON KULLANMA TARİHİ GEÇENLERİ KALDIR
----------------------------------------
7. SATIŞ YAP
8. İADE AL
----------------------------------------
9. GÜNLÜK TOPLAM MÜŞTERİ SAYISI
10.GÜNLÜK CİRO HESAPLA
----------------------------------------
11.KASAYI KAPAT
 ************************""")
while True:
	a=input("Seçim Yapınız : ")
	if(a=="11"):
		print("**********\n")
		print("Kasa Kapatıldı!\n")
		urunNesne.GunlukMusteriSayisi()
		urunNesne.CiroGunluk()
		print("Program Sonlanıyor...")
		time.sleep(2)
		urunNesne.KasayiKapa()
		urunNesne.SQLbaglantikes()
		print("Program Sonlandı.")
		break
	elif(a=="1"):
		UrunAdi=input("Ürün Adı : ")
		UrunMarkasi=input("Ürün Markası : ")
		fiyat=float(input("Ürün Fiyatı : "))
		skt=input("Son Kullanma Tarihi(Gün/Ay/Yıl) : ")
		cesit=input("Ürün Çeşiti : ")
		stok=int(input("Stok : "))
		print("Ürün Ekleniyor...")
		time.sleep(3)
		urun=Urun(UrunAdi,UrunMarkasi,fiyat,skt,cesit,stok)
		urunNesne.urun_ekle(urun)
		print("Ürün Eklendi!")
	elif(a=="2"):
		UrunAdi=input("Silmek istediğiniz ürünün adını giriniz : ")
		urunNesne.urun_sil(UrunAdi)
	elif(a=="3"):
		UrunAdi=input("Sorgulamak istediğiniz ürünün adını giriniz : ")
		urunNesne.stokUrunAdiSorgula(UrunAdi)

	elif(a=="4"):
		UrunMarkasi=input("Sorgulamak istediğiniz ürünün markasını giriniz : ")
		urunNesne.stokUrunMarkasiSorgula(UrunMarkasi)
	elif(a=="5"):
		urunNesne.stokTumMarketSorgula()
	elif(a=="6"):
		girdi = input("Hangi Tarihten Öncesini Silmek İstiyorsunuz (Örnek: 25.05.2003) : ")
		urunNesne.SonKullanmaTarihiGeceniSil(girdi)
	elif(a=="7"):
		while True:
			girdi=input("Ürün Adı Gir (iptal : i | fiş : f): ")
			if (girdi=="i"):
				urunNesne.ilkGiris=True     
				break
			elif (girdi=="f"):
				print("Fiş Kesiliyor. Ödeme için teşekkürler!")
				urunNesne.FisKes()
				break
			else:
				urunNesne.SatisYap(girdi)
	elif(a=="8"):
		girdi = input("İade almak istediğiniz ürünün adı : ")
		urunNesne.IadeAl(girdi)
	elif(a=="9"):
		urunNesne.GunlukMusteriSayisi()
	elif(a=="10"):
		urunNesne.CiroGunluk()
