# Dictionary

""" 
Dictionary Python adalah struktur data bawaan yang menyimpan koleksi item berurutan (sejak Python 3.7) dan dapat diubah (mutable), 
yang memetakan kunci unik (key) ke nilai (value) tertentu menggunakan format key:value di dalam kurung kurawal {}. 
Dictionary sangat efisien untuk mencari data berdasarkan kata kunci, layaknya kamus bahasa. 
Berikut adalah poin penting mengenai dictionary Python:
    Struktur Pasangan Key-Value: Terdiri dari kunci (pengidentifikasi unik) dan nilai (data yang terkait dengan kunci).
    Mutable & Unordered: Dapat diubah, ditambah, atau dihapus setelah dibuat.
    Key Unik & Immutable: Kunci tidak boleh duplikat dan harus menggunakan tipe data yang tidak dapat diubah seperti string, angka, atau tuple.
    Sintaksis: {} digunakan untuk mendefinisikan dictionary, contoh: karyawan = {'nama': 'Andi', 'umur': 25}.
    Akses Data: Menggunakan kunci di dalam kurung siku [] atau metode .get() untuk mengakses nilai.
"""

karyawan = {
    'nama' :'agus',
    'umur' : 20,
    'asal' : 'Kota Malang'
}
print(type(karyawan))


#1. Access Items Dictinaries

    #1.1 Menggunakan metode get()

Mobil = {
    'Model' : 'avanza',
    'Model' : 'aza',
    'Tahun' : 2017,
    'asal'  : 'jepang'
}

x = Mobil.get('Model')
print(x)

    #1.2 Menggunakan keys()
barang = {
    'nama': 'meja',
    'usia': 10,
    'lokasi': 'Labuan Bajo'
}

x=barang.keys()
print(f'Menggunaka metode keys : {x}')

#2. Mengubah dan Menambahkan Item Dictionaries
    #2.1 Menggunakan nama['nama_keys']=='nama/value yang mau diubah'
pc = {
    'jenis' : 'xiomei',
    'asal': 'china',
    'tahun pembuatan': 2017,
    'warna' : 'hitam'
}

pc['warna']='merah'                         # mengubah value
pc['stok'] = 10                             # menambahkan value
print(f'Dengan Perintah Standar = {pc}')

    #2.2 Menggungkan update()
motor = {
    'Jenis': 'Ducati',
    'Tahun' : 2020,
    'asal': 'Italia',
    'Lokasi': 'Jakarta'
}



motor.update({'Lokasi' :'Medan'})           # mengubah value 
motor.update({'Warna': 'Hitam', 'kapasitas': '500 cc'})            # menambahkan value
print(f'Dengan update() = {motor}')        


a= {'x':10}
a.update({'y':20})
print(f'Dict a : {a}')
#print(f'Dict b : {b}')

#3. Menghapus item pada data dictionaries
    #3.1 Menggunakan pop
sayur = {
    'jenis' : 'daun',
    'kandungan' : 'zat besi',
    'tempat' : 'pasar lokal',

}

sayur.pop('kandungan', 'tempat')
print(f'Metode pop(): {sayur}')

    #3.2 Menggunakan del
kantor = {
    'pegawai': 3,
    'kehadiran':'tiap hari',
    'minuman': 'kopi',
    'makanan': 'gorengan'
}
del kantor['minuman']
print(f'Menggunakan del = {kantor}')    # jika: del kantor --> ini akan menghapus data dictionari kantor

    #3.3 menggunakan clear()
kantor1 = {
    'pegawai': 3,
    'kehadiran':'tiap hari',
    'minuman': 'kopi',
    'makanan': 'gorengan'
}

kantor1.clear()                         # ini akan mengosongkan value pada data dictionari
print(f'Menggunakan clear {kantor1}')

#4. Looping data dictionaries
a = {
    'kerja': '4 kali',
    'libur': '3 kali',
    'bonus': '2 kali'

}
i = 0
# Menggunakan for biasa
for value in a:
    print(f'Looping biasa : {value}')
    # Outputnya berupa data key : kerja, libur, bonus

# Menggunakan .values()
ruang = {
    'motor': 'scoopy',
    'laptop': 'Thinkpad',
    'handphone': 'poco x7'
}

for x in ruang.values():
    print(f'Menggunakan values : {x}')

# Menggunakan .keys()
for k in ruang.keys():
    print(f'menggunakan keys : {k}')

# Menggunakan for a.items()
for value, k in a.items():
    print(f'Menggunakan items : {value,k}')



b = {
    'siswa':{'nama':'andi', 'usia':20},
    'siswa2':{'nama':'dimas', 'usia': 22}
}


print('++++++++')
for a,i in b.items():
    print(a)
    for x,y in i.items():
        print(x,y)


print('++++++++')

for i,va in b.items():
    print(f'{i}:')
    for a in va.values():
        print(a)




# Looping nested list
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

for ke, va in myfamily.items():
    print(ke)
    for i, y in va.items():
        print(i + ':', y)

x = myfamily.fromkeys('child1')
print(x)





def math(*args, **kwargs):
    if kwargs.get('Operasi') == 'tambah':
        output = 0
        for i in args:
            output += i
        return output
    return 'No Value'

    

x = math(1,2,4,6,9, Operasi = 'tambah')
print(x)

