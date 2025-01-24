from customer import Customer
import random
import datetime

atm = Customer(id)

while True:
    id = int(input('Masukkan PIN anda: '))
    trial = 0
    while id != int(atm.checkPin()) and trial < 3:
        id = int(input('PIN anda salah. Silahkan masukkan lagi: '))
        trial += 1
        if trial == 3:
            print('Error. Silahkan ambil kartu dan coba lagi..')
            exit()
    while True:
        print('Selamat Datang di ATM AING!')
        print('\n1. Cek Saldo\n2. Debet\n3. Simpan\n4. Ganti PIN\n5. Keluar')
        selectmenu = int(input('Pilih Menu: '))
        if selectmenu == 1:
            print('\nSaldo anda sekarang: ' + str(atm.checkBalance()) + '\n')
        elif selectmenu == 2:
            nominal = float(input('Masukkan nominal saldo: '))
            verify_withdraw = input(
                'Anda akan melakukan debet dengan nominal berikut ? (y/n) ' + str(nominal) + ' ')
            if verify_withdraw == 'y' or verify_withdraw == 'Y':
                print('Saldo awal anda adalah: Rp. ' + str(atm.checkBalance()) + '')
            else:
                break
            if nominal < atm.checkBalance():
                atm.withdrawBalance(nominal)
                print('Transaksi berhasil!')
                print('Sisa saldo sekarang adalah: Rp. ' + str(atm.checkBalance()) + '')
            else:
                print('Maaf. Saldo sisa sekarang tidak cukup untuk melakukan debet')
                print('Silahkan isi saldo terlebih dahulu')
        elif selectmenu == 3:
            nominal = float(input('Masukkan nominal saldo: '))
            verify_deposit = input(
                'Anda akan melakukan penyimpanan dengan nominal berikut ? (y/n) ' + str(nominal) + ' ')
            if verify_deposit == 'y' or verify_deposit == 'Y':
                atm.depositBalance(nominal)
                print('Saldo anda sekarang adalah: Rp. ' + str(atm.checkBalance()) + '\n')
            else:
                break
        elif selectmenu == 4:
            verify_pin = int(input('Masukkan PIN anda: '))
            while verify_pin != int(atm.checkPin()):
                print('PIN anda salah, silahkan masukkan pin: ')
                verify_pin = int(input('Masukkan PIN anda: '))
                trial += 1
                if trial == 3:
                    print('Error. Silahkan ambil kartu dan coba lagi..')
                    exit()
            updated_pin = int(input('Silahkan masukkan PIN baru: '))
            print('PIN anda berhasil diganti')
            verify_newpin = int(input('Coba masukkan PIN baru '))
            if verify_newpin == updated_pin:
                print('PIN baru anda sukses')
            else:
                print('Maaf, PIN anda salah')
        elif selectmenu == 5:
            print('Resi tercetak otomatis saat anda keluar. harap simpan tanda terima ini sebagai bukti transaksi anda.')
            print('No. Rekord: ', random.randint(100000, 1000000))
            print('Tanggal: ', datetime.datetime.now())
            print('Saldo akhir: ', atm.checkBalance())
            print('Terima kasih telah menggunakan ATM AING! ')
            exit()
        else:
            print('Error. maaf menu tidak tersedia')