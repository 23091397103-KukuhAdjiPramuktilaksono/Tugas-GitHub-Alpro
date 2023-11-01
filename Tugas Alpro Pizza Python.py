print("Halo selamat datang di Pizza Python! Silahkan pilih Topping Pizza mu")

#pilih topping 
print("===============")
print("Topping Pizza :")
print("===============")
print("Frank Furter")
print("Meat Lovers")
print("Meat Monsta") 
print("Super Supreme")
print("Super Supreme Chicken")
print("===============")
HargaTopping= 43637
ToppingPizza=input("mau topping apa? ")

#pilih crust
print("===============")
print("Varian Crust : ")
print("Pan")
print("StuffedCrust Cheese")
print("StuffedCrust Sausage")
print("Cheesy Bites")
print("Crown Cust")
print("===============")
Crust=input("pilih crust apa? ")
if Crust=="StuffedCrust Cheese":
    HargaCrust=55455
    Personal=0
    Regular=65455
    Large=104545
    print("Total harga pizza anda saat ini: Rp. ", HargaCrust)
elif Crust=="StuffedCrust Sausage":
    HargaCrust=52728
    Personal=0
    Regular=64545
    Large=102727
    print("Total harga pizza anda saat ini: Rp. ", HargaCrust)
elif Crust=="Cheesy Bites":
    HargaCrust=57273
    Personal=0
    Regular=66364
    Large=107273
    Hargatotal=HargaTopping+HargaCrust
    print("Total harga pizza anda saat ini: Rp. ", HargaCrust)
elif Crust=="Crown Cust":
    HargaCrust=55455
    Personal=0
    Regular=65455
    Large=104545
    print("Total harga pizza anda saat ini: Rp. ", HargaCrust)
elif Crust=="Pan":
    HargaCrust=43637
    Personal=0
    Regular=57273
    Large=89091
    print("Total harga pizza anda saat ini: Rp. ", HargaCrust)
else:
    print("mohon maaf jenis crust mu tidak valid")
   
#pilih ukuran pizza
print("===============")
print("Personal")
print("Regular")
print("Large")
print("===============")
Ukuran=input("pilih ukuran pizza anda: ")
if Ukuran=="Personal":
    HargaTotal+=0
    print("Harga pizza anda Rp. ", HargaTotal)
elif Ukuran=="Regular":
    HargaUkuran=55000
    HargaTotalUkuran=HargaTotal+HargaUkuran
    print("Harga pizza anda Rp. ", HargaTotalUkuran)
else: 
    HargaUkuran=89091
    HargaTotalUkuran=HargaTotal+HargaUkuran
    print("harga pizza anda Rp. ", HargaTotalUkuran)

#Tambahan cheese
XtraCheese = input("Apakah anda ingin XtraCheese?  (y/n)")
if XtraCheese == "y":
    Harga_Total_Akhir=Harga_Total_Ukuran+Harga_Xtra_Cheese
    print("Rincian pesanan anda: Pizza ", ToppingPizza, Crust, Ukuran, XtraCheese)
    print("Total harga pizza anda sebesar: Rp. ", Harga_Total_Akhir)
else:
    Harga_Total_Akhir = Harga_Total_Ukuran
    print("Rincian pesanan anda: Pizza ", ToppingPizza, Crust, Ukuran)
    print("Total harga pizza pesanan anda sebesar: Rp. ", Harga_Total_Akhir)
    
#pembayaran
UangDibayar=int(input("Jumlah uang yang anda bayarkan: Rp. "))
Kembalian=UangDibayar-HargaTotalAkhir
print("Jumlah kembalian adnda: Rp. ", Kembalian)
print("Terimakasih telah beli di pizza python")
















