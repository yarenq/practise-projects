ogrencino=int(input("öğrenci numaranızı giriniz"))
isim=input("adınız soyadınızı giriniz")
lab=int(input("laboratuvar notunuzu giriniz"))
arasınav=int(input("ara sınav notunuzu giriniz"))
final=int(input("final notunuzu giriniz"))
donemsonu=lab*20/100+arasınav*30/100+final*50/100
print ("ad soyad:",isim)
print("öğrenci numarası:",ogrencino)
print ("dönem sonu notu=",donemsonu)