dictionary = {'KEY':'VALUE'
,"Kenobi": "Capricorn",
"Hermas": "Leo",
"Amalya": "Pisces"}

def showfull():   
    print ('_________________________')
    for x, y in dictionary.items():
        print(x+'\t','|'+y)
        print('_________________________')

def add():
    check = False
    while check==False:
        times = input('Tambah berapa biodata? ')
        if times.isdigit()==True:
            inttimes = int(times)
            for a in range(inttimes):
                x = input(str('Masukkan nama->'))
                y = input(str('Masukan zodiak->'))
                xx = str(x)
                yy = str(y)
                dictionary[xx] =yy
                showfull()
            check = True
        else:
            print('Masukan karakter angka')
            check = False

def search():
    searchword = input('Search->')
    i=0
    for item in dictionary:
        if str.lower(searchword) in str.lower(item):
            print('Karakter '+ str(searchword)+ ' ditemukan di -> ' +'{}- {}'.format(item,dictionary[item]))
    if str.lower(searchword) not in str.lower(item):
        print('None found')

def keluar():
    print('Bonne Nuit')

check = False
while check==False:
    print ("MAIN MENU")
    print ("1. Lihat kamus bio zodiak")
    print ('2. Isi biodata baru')
    print ('3. Cari biodata')
    print ('4. Keluar')
    pilihutama = input('Pilih sesuai nomor-->')
    index = int(pilihutama)-1
    menu=[showfull,add,search,keluar]
    menu[index]()
    again = input('Ulang lagi?Y/N')
    if again=='Y' or again=='y':
        check = False
    if again=='N' or again=='n':
        keluar()
        check = True
    else:
        print('Tidak bisa memasukkan angka atau karakter lain, hanya Y atau N, akan mengulang ke awal')
        check = False

