menu = ['Makanan', 'Minuman', 'snack']
makanan = ['Nasi Goreng', 'Mie goreng', 'Mie Kuah']
minuman = ['Es Teh', 'Soda', 'Es Degan']
snack = ['Kripik', 'Kentang Goreng', 'Roti']
hasil = []

while True:
    print("==============")
    for var in range(0, len(menu)):
        print(f'{var+1}. {menu[var]}')
    menu_pilihan = input("masukan pilihan 1-3 :")
    if menu_pilihan == "1":
        for menu_makanan in range(0, len(menu)):
            print(f'{menu_makanan+1} {makanan[menu_makanan]}')
        ulang = True
        while ulang:
            select_makan = int(input(f'Silahkan Pilih Makanan 1-{len(makanan)} :'))
            if select_makan <= 0 or select_makan > len(makanan):
                print('silahkan masukan menu dengan benar')
                for menu_makanan in range(0, len(makanan)):
                    print(f'{menu_makanan + 1}. {makanan[menu_makanan]} ')
                continue
            else:
                hasil.append(makanan[select_makan - 1])
                print('==== Pesanan ====')
                for list_hasil in range(0, len(hasil)):
                    print(f'{list_hasil +1} . {hasil[list_hasil]}')
                ulang = False
            continue
    elif menu_pilihan == "2":
        for menu_minuman in range (0, len(menu)):
            print(f'{menu_minuman+1} {minuman[menu_minuman]}')
        ulang = True
        while ulang:
            select_minum = int(input(f'silahkan pilih minuman 1-{len(minuman)} :'))
            if select_minum <=0 or select_minum > len(minuman):
                print('silahkan masukan menu dengan benar')
                for menu_minuman in range (0, len(minuman)):
                    print(f'{menu_minuman + 1}. {minuman[menu_minuman]}')
                continue
            else:
                hasil.append(minuman[select_minum - 1])
                print('==== Pesanan ====')
                for list_hasil in range (0, len(hasil)):
                    print(f'{list_hasil +1}. {hasil[list_hasil]}')
                ulang = False
            continue
    elif menu_pilihan == "3":
        for menu_snack in range (0, len(menu)):
            print(f'{menu_snack+1} {snack[menu_snack]}')
        ulang = True
        while ulang:
            select_snack = int(input(f'silahkan pilih snack 1-{len(snack)} :'))
            if select_snack <=0 or select_snack > len(snack):
                print('silahkan masukan menu dengan benar')
                for menu_snack in range (0, len(snack)):
                    print(f'{menu_snack + 1}. {snack[menu_snack]}')
                continue
            else:
                hasil.append(snack[select_snack - 1])
                print('==== Pesanan ====')
                for list_hasil in range (0, len(hasil)):
                    print(f'{list_hasil +1}. {hasil[list_hasil]}')
                ulang = False
            continue
    else:
        print('Menu Tidak Ditemukan')
        continue
    pilih = input('Apakah ada lagi yang ingin dipesan  ?')
    if pilih == 'y' or pilih == 'Y':
        continue
    else:
        print('==== Pesanan ====')
        for list_hasil in range(0, len(hasil)):
            print(f'{list_hasil +1} . {hasil[list_hasil]} 1x')
        break


   





