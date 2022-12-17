import sqlite3

class Urun():
	def __init__(self,UrunAdi,UrunMarkasi,fiyat,skt,cesit,stok):
		self.UrunAdi=UrunAdi
		self.UrunMarkasi=UrunMarkasi
		self.skt=skt 
		self.fiyat=fiyat
		self.cesit=cesit
		self.stok=stok
	def __str__():
		return self.stok

class Market():
	def __init__(self):
		self.SQLbaglanti()

		self.İlkGiris=True   
		self.GunlukMusteri=0  
		self.toplamfiyat=0   
		self.Ciro=0
		self.ToplamIade=0


	def SQLbaglanti(self):
		self.baglanti = sqlite3.connect("veriler.db")
		self.cursor = self.baglanti.cursor()
		sorgu = "CREATE TABLE IF NOT EXISTS veriler(UrunAdi TEXT,UrunMarkasi TEXT,fiyat REAL,skt TEXT,cesit TEXT,stok INT)"
		self.cursor.execute(sorgu)
		self.baglanti.commit()


	def SQLbaglantikes(self):
		self.baglanti.close()


	def urun_ekle(self,urunNesnesi):
		sorgu ="INSERT INTO veriler VALUES(?,?,?,?,?,?)"
		self.cursor.execute(sorgu,(urunNesnesi.UrunAdi,urunNesnesi.UrunMarkasi,urunNesnesi.fiyat,urunNesnesi.skt,urunNesnesi.cesit,urunNesnesi.stok))
		self.baglanti.commit()


	def urun_sil(self,isim):
		sorgu="SELECT * FROM veriler WHERE UrunAdi = ?"
		self.cursor.execute(sorgu,(isim,))
		silinecekUrunler=self.cursor.fetchall()


		if(len(silinecekUrunler)==0):
			print("Böyle bir ürün bulunmuyor.")
		else:
			print("Ürün Silindi.")

		sorgu = "DELETE FROM veriler WHERE UrunAdi = ?"
		self.cursor.execute(sorgu,(isim,))
		self.baglanti.commit()


	def stokUrunAdiSorgula(self,isim):
		sorgu="SELECT * FROM veriler WHERE UrunAdi = ?"
		self.cursor.execute(sorgu,(isim,))
		urunler=self.cursor.fetchall()

		if(len(urunler)==0):
			print("Böyle bir ürün bulunmuyor.")
		else:
			toplamurun=0

			for i in urunler:
				toplamurun+=i[5]

			print(toplamurun)

	def stokUrunMarkasiSorgula(self,marka):
		sorgu="SELECT * FROM veriler WHERE UrunMarkasi = ?"
		self.cursor.execute(sorgu,(marka,))
		markaurunler=self.cursor.fetchall()

		if(len(markaurunler)==0):
			print("Böyle bir ürün bulunmuyor.")
		else:
			toplammarkaurun=0

			for i in markaurunler:
				toplammarkaurun+=i[5]

			print("{} Markasına ait toplamda {} ürün mevcut".format(marka,toplammarkaurun))

	def stokTumMarketSorgula(self):
		sorgu="SELECT * FROM veriler"
		self.cursor.execute(sorgu)
		toplamstok=self.cursor.fetchall()

		if(len(toplamstok)==0):
			print("Stokta ürün bulunmuyor.")
		else:
			toplamurunstok=0
			for i in toplamstok:
				toplamurunstok+=i[5]

				print("Tüm ürünlerin stoğu {} dır.\n".format(toplamurunstok))
	def TarihGecenSil(self,isim):
		sorgu="DELETE FROM veriler WHERE UrunAdi = ?"
		self.cursor.execute(sorgu,(isim,))
		self.baglanti.commit()


	def SonKullanmaTarihiGeceniSil(self,tarih):
		sorgu = "SELECT * FROM veriler"
		self.cursor.execute(sorgu)
		butunurunler=self.cursor.fetchall()

		if(len(butunurunler)==0):
			print("Stokta ürün bulunmuyor.")

		else:
			for i in butunurunler:
				sktlistesi =i[3].split(".")
				tarihlistesi=tarih.split(".")

				if(tarihlistesi[2]>sktlistesi[2]):
					self.TarihGecenSil(i[0])
				elif(tarihlistesi[2]==sktlistesi[2] and tarihlistesi[1]>sktlistesi[1]):
					self.TarihGecenSil(i[0])
				elif(tarihlistesi[2]==sktlistesi[2] and tarihlistesi[1]==sktlistesi[1] and tarihlistesi[0]>sktlistesi[0]):
					self.TarihGecenSil(İ[0])


	def SatisYap(self,isim):
		self.satisisim=isim
		sorgu="SELECT * FROM veriler WHERE UrunAdi = ?"
		self.cursor.execute(sorgu,(isim,))
		urun=self.cursor.fetchall()


		if(len(urun)==0):
			print("Böyle bir ürün bulunmuyor.")
		else:
			if(self.İlkGiris):
				self.urunstok=urun[0][5]
			self.urunstok-=1

			self.toplamfiyat +=urun[0][2]

			print("Ürün Sepetinize Eklendi.")
			self.İlkGiris=False


	def FisKes(self):
		sorgu ="UPDATE veriler SET stok = ? WHERE UrunAdi = ?"
		self.cursor.execute(sorgu,(self.urunstok,self.satisisim))
		self.baglanti.commit()
		print("Toplam tutar: {} Tl".format(self.toplamfiyat))
		self.GunlukMusteri +=1
		self.Ciro+=self.toplamfiyat
		self.İlkGiris=True
		self.toplamfiyat=0

	def GunlukMusteriSayisi(self):
		print("Toplam müşteri sayınız {}".format(self.GunlukMusteri))

	def CiroGunluk(self):
		if(self.Ciro<0):
			print("Zarardasınız...")
		elif(self.Ciro>0):
			print("Kardasınız...")
		print("Günlük Cironuz {} TL".format(self.Ciro))

	def IadeAl(self,isim):
		sorgu="SELECT * FROM veriler WHERE UrunAdi = ?"
		self.cursor.execute(sorgu,(isim,))
		urunler=self.cursor.fetchall()

		stok1 = urunler[0][5]
		stok1 +=1
		self.Ciro-=urunler[0][2]
		sorgu2="UPDATE veriler SET stok = ? WHERE UrunAdi = ?"
		self.cursor.execute(sorgu2,(stok1,isim))
		self.baglanti.commit()

		print("İade alındı!")
	
	def KasayiKapa(self):
		baglanti2=sqlite3.connect("gunlukVeriler.db")
		cursor2=baglanti2.cursor()
		sorgu="CREATE TABLE IF NOT EXISTS gunlukVeriler(GunlukMusteri INT,CiroGunluk INT)"
		cursor2.execute(sorgu)
		baglanti2.commit()
		sorgu2="INSERT INTO gunlukVeriler VALUES(?,?)"
		cursor2.execute(sorgu2,(self.GunlukMusteri,self.Ciro))
		baglanti2.commit()

		
		self.GunlukMusteri=0
		self.CiroGunluk=0