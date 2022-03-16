#!/usr/bin/python3
from customer import Customer
import random, datetime

atm = Customer(id)

while True:
    pin = int(input("Masukkan Pin Anda  : "))
    trial = 0

    while pin != int(atm.checkPin()) and trial < 3:
        print("Pin Salah! Silahkan Coba Lagi.")
        pin = int(input("Masukkan Pin Anda  : "))
        trial += 1
        if trial == 3:
            print("ERROR!! Silahkan Ambil Kartu, dan Coba Lagi.")
            exit()

    while True:
        print("""
            +++[ WELCOME TO PROGATE ATM ]+++
            1 - Cek Saldo
            2 - Tarik Tunai
            3 - Setor Tunai
            4 - Ganti Pin
            5 - Keluar

            """)
        pilih = int(input("\nSilahkan pilih menu  : "))

        if pilih == 1:
            print("\nSaldo anda sekarang: Rp. " + str(atm.checkBalance()) + "\n" )

        elif pilih == 2:
            nominal = float(input("Masukkan nominal saldo   : "))
            verify_withdraw = input("Konfirmasi: Anda akan melakukan Tarik Tunai dengan nominal berikut, " + str(nominal) + " ? (y/n) ")

            if verify_withdraw == "y":
                print("Saldo awal anda adalah: Rp. " + str(atm.checkBalance()) + "")
            
            else:
                break

            if nominal < atm.checkBalance():
                atm.TarikTunai(nominal)
                print("Transaksi Tarik Tunai berhasil!")
                print("Saldo sisa sekarang: Rp. " + str(atm.checkBalance()) + "")
            
            else:
                print("Maaf. Saldo anda tidak cukup untuk melakukan Tarik Tunai!")
                print("Silakan lakukan penambahan nominal saldo")

        elif pilih == 3:
            nominal = float(input("Masukkan nominal saldo   : "))
            verify_deposit = input("Konfirmasi: Anda akan melakukan penyimpanan dengan nominal berikut, " + str(nominal) + " ? (y/n) ")

            if verify_deposit == "y":
                atm.SetorTunai(nominal)
                print("Saldo anda sekarang adalah: Rp." + str(atm.checkBalance()) + "\n" )

            else:
                break

        elif pilih == 4:
            verify_pin = int(input("Masukkan Pin Anda  : "))

            while verify_pin != int(atm.checkPin()):
                print("Pin Salah! Silahkan Coba Lagi.")
                verify_pin = int(input("Masukkan Pin Anda  : "))

            updated_pin = int(input("Silakan Masukkan Pin baru  : "))
            print("Pin anda berhasil diganti!")

            verify_newpin = int(input("Masukkan Pin Baru Anda  : "))
            
            if verify_newpin == updated_pin:
                print("Pin baru anda sukses!")

            else:
                print("Maaf, Pin anda salah!")
            
        elif pilih == 5:
            print("\nResi tercetak otomatis saat anda keluar. \n\n    Harap simpan tanda terima ini \n   sebagai bukti transaksi anda.\n")
            print("No. Record   : ", random.randint(100000, 1000000))
            print("Tanggal      : ", datetime.datetime.now())
            print("Saldo akhir  : ", atm.checkBalance())
            print("\n Terima kasih telah menggunakan ATM Progate!\n")
            exit()
        else:
            print("Error. Maaf, menu tidak tersedia")