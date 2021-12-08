import function
import sqlite3



baglanti = sqlite3.connect("elbiseler.db")
komut="CREATE TABLE IF NOT EXISTS elbiseler(Marka text, Model text, Renk text, Fiyat int)"
function.elbise_listele()
baglanti.commit()



komut2 = "INSERT INTO elbiseler where Marka"
function.elbise_ekle()
baglanti.commit()

komut3= "DELETE from elbiseler where Model"
function.elbise_silme()
baglanti.commit()

komut4 = "UPDATE elbiseler WHERE Renk=?"
function.elbise_guncelle("Mavi")
baglanti.commit()



baglanti.close()
