ogrenciler=[]
def addStudent(name,surname):
  ogrenciler.append(name+surname)
def deleteStudent(name,surname):
  name=input("Ad:")
  surname=input("Soyad:")
  for student in ogrenciler:
    if student==name+surname:
      ogrenciler.remove(student)
    else:
     print("ogrenci yok")
      
def listOfStudents():
  for student in range(len(ogrenciler)):
    print(ogrenciler[student])
    
def listByNumber(name,surname):
  name= input("Ogrenci  Adi ve Soyadi: ")
  for student in ogrenciler:
    if student==name:
     print(f"Ogrenci No: {ogrenciler.index(student)+1}")
    else:
      print("Oyle bir ogrenci yok")
  
print("Ogrenci Kayit Sistemi")
while True:
  print("1- Ogrenci Ekle") 
  print("2- Ogrenci Sil")
  print("3- Ogrencileri Listele")
  print("4- Birden Fazla Ogrenci Ekle")
  print("5-Ogrenci Numarasını Goster")
  print("6- Birden Fazla Ogrenci Sil")
  print("7-Cikis")
  sec=input("Seciminiz: ") 
  if sec=="1":
    name=input("Ad ")
    surname=input("Soyad:")
    addStudent(name,surname)
    print("---Kayit Yapildi--")
  elif sec=="2":
     deleteStudent(name,surname)
  elif sec=="3":
     listOfStudents()
  elif sec=="4":
    ekle=int(input("Eklenecek ogrenci sayısını gir :"))
    for i in range(ekle):
      name=input("Ad:")
      surname=input("Soyad:")
    addStudent(name,surname)
    print("--Kayıt basarılı--")
  elif sec=="5":
    listByNumber(name,surname)
  elif sec=="6":
    sil=int(input("Silinecek ogrenci sayisi:"))
    for i in range(sil):
      deleteStudent(name,surname)
  else :
    break
  
  