# PROGRAM KASIR RESTORAN
import prettytable as pt
import menu
# menu
ayamBakar = menu.Menu("Ayam Bakar", 25000)
ayamKecap = menu.Menu("Ayam Kecap", 15000)
mieAyam = menu.Menu("Mie Ayam", 10000)
sateAyam = menu.Menu("Sate Ayam", 25000)
sateKambing = menu.Menu("Sate Kambing", 30000)


menu_table = pt.PrettyTable()


menu_table.field_names = ["Menu", "Harga"]
menu_table.add_row([ayamBakar.nama,ayamBakar.harga])
menu_table.add_row([ayamKecap.nama,ayamKecap.harga])
menu_table.add_row([mieAyam.nama,mieAyam.harga])
menu_table.add_row([sateAyam.nama,sateAyam.harga])
menu_table.add_row([sateKambing.nama,sateKambing.harga])

# list input
list_menu = []
list_jumlah = []
totalbeli = 0
# Menampilkan menu ke layar
print("="*20," Restoran Python", "="*20)
print("Silahkan Pilih Menu di Bawah: ")
print(menu_table)
print("="*60)
# input menu pelanggan
inptJumlahMenu = int(input("Masukan Jumlah Menu yang ingin di pesan: "))
for i in range(inptJumlahMenu):
    list_menu.append(menu.Menu(input("Masukan menu\t: "), harga = 0))   
    list_jumlah.append(int(input("Masukan Jumlah\t: ")))

# MENAMPILKAN TOTAL HARGA KEPADA PELANGGAN 

price_table = pt.PrettyTable()
print("="*40," Restoran Python", "="*40)
price_table.field_names = ["Menu", "Harga", "qty", "Total"]
total = pt.PrettyTable()

for i in range(inptJumlahMenu):
    total_harga = list_menu[i].harga * list_jumlah[i]
    totalbeli += total_harga
    price_table.add_row([list_menu[i].nama, list_menu[i].harga, list_jumlah[i], total_harga])
    total.field_names = ["Total", f"Rp.{totalbeli}"]
   

total.padding_width = 5
print(price_table)
print(total)
print('='*100)
# INPUT UANG PELANGGAN
print('Silahkan masukan uang anda: ')
uang = int(input("Masukan Uang: "))
# JIKA UANG LEBIH MAKA TAMPILKAN KEMBALIAN
if uang > totalbeli:
    kembalian = uang - totalbeli
# JIKA UANG PAS MAKA PROGRAM SELESAI
elif uang == totalbeli:
    kembalian = 0
# TAMPILKAN STRUK PEMBAYARAN
print("="*20," RESTORAN PYTHON ", "="*20)
total.add_row(["Uang", f"Rp.{uang}"])
total.add_row(["Kembalian", f"Rp.{kembalian}"])
print(price_table)
print(total)
print("="*60)

# TRANSAKSI SELESAI
print("Terima kasih atas kunjungannya \U0001F60A")
# ============= PROGRAM SELESAI ======================================

