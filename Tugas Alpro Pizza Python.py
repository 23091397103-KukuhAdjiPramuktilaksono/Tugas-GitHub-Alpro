print("Halo selamat datang di Pizza Python!")

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
print("Varian Crust")
print("Pan")
print("StuffedCrust Cheese")
print("StuffedCrust Sausage")
print("Cheesy Bites")
print("Crown Cust")
print("===============")
Crust=input("pilih crust apa? ")
if Crust=="StuffedCrust Cheese":
    HargaCrust=11818
    Hargatotal=HargaTopping+HargaCrust
    print("Harga pizza anda Rp.", Hargatotal)
elif Crust=="StuffedCrust Sausage":
    HargaCrust=9091
    Hargatotal=HargaTopping+HargaCrust
    print("Harga pizza anda Rp. ", Hargatotal)
elif Crust=="Cheesy Bites":
    HargaCrust=13636
    Hargatotal=HargaTopping+HargaCrust
    print("harga pizza anda Rp. ", Hargatotal)
elif Crust=="Crown Cust":
    HargaCrust=11818
    Hargatotal=HargaTopping+HargaCrust
    print("harga pizzamu Rp. ", Hargatotal)
elif Crust=="Pan":
    Hargatotal=HargaTopping
    print("Harga pizzamu Rp. ", Hargatotal)
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
    Hargatotal+=0
    print("Harga pizza anda Rp. ", Hargatotal)
elif Ukuran=="Regular":
    HargaUkuran=55000
    print("Harga pizza anda Rp. ", HargatotalUkuran)
else: 
    HargaUkuran=89091
    Hargatotalukuran=Hargatotal+HargaUkuran
    Print("harga pizza anda Rp. ", Hargatotalukuran)

#Tambahan cheese
ExtraCheese = input("Apakah anda ingin Extra Cheese? (Ya/Tidak): ")
if ExtraCheese

















