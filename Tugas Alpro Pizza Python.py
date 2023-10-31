print("Selamat Datang di Pizza Python")

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
    HargaCrust=11818
    HargaTotal=HargaTopping+HargaCrust
    print("Harga pizza anda Rp.", HargaTotal)
elif Crust=="StuffedCrust Sausage":
    HargaCrust=9091
    HargaTotal=HargaTopping+HargaCrust
    print("Harga pizza anda Rp. ", HargaTotal)
elif Crust=="Cheesy Bites":
    HargaCrust=13636
    HargaTotal=HargaTopping+HargaCrust
    print("harga pizza anda Rp. ", HargaTotal)
elif Crust=="Crown Cust":
    HargaCrust=11818
    HargaTotal=HargaTopping+HargaCrust
    print("harga pizzamu Rp. ", HargaTotal)
elif Crust=="Pan":
    HargaTotal=HargaTopping
    print("Harga pizzamu Rp. ", HargaTotal)
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
XtraCheese = input("Apakah anda ingin Extra Cheese? (Ya/Tidak): ")
if XtraCheese == "Ya":
    HargaXtraCheese = 13636
    HargaTotalAkhir = HargaTotalUkuran + HargaXtraCheese
    print("Total harga pizza anda: Rp. ", HargaTotalAkhir)
else:
    HargaTotalAkhir = HargaTotalUkuran+0
    print("Baik, total harga pizza anda: Rp. ", HargaTotalAkhir)
















