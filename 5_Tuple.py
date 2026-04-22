#Tuples
"""
Tuple adalah struktur data yang digunakan untuk menyimpan sekumpulan data dalam satu variabel tunggal. 
Tuple sangat mirip dengan List, namun memiliki satu perbedaan kunci: Immutable. 
Berikut adalah karakteristik utama Tuple:
Tidak Bisa Diubah (Immutable): Setelah dibuat, elemen di dalam tuple tidak bisa ditambah, dihapus, atau diganti. Ini membuatnya lebih aman untuk data yang sifatnya permanen.
Terurut (Ordered): Setiap elemen memiliki posisi atau indeks tetap, dimulai dari angka 0.
Penulisan: Menggunakan tanda kurung biasa () dan setiap elemen dipisahkan oleh tanda koma.
Isi Beragam: Dapat menampung berbagai tipe data sekaligus, seperti string, integer, hingga boolean dalam satu tuple. 
"""

fruit = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruit)

#1. Mengakses Tuples
print(f'Index Tuple 0 - 3 = {fruit[0:4]}')
print(f'Index Tuple 2 sampai akhir = {fruit[2:]}')
print(f'Index Tuple -1 {fruit[-1]}')
print(f'Index Tuple -4 sampai -1 {fruit[-4:-1]}')

#2. Mengecek value pada Exists
if 'banana' in fruit:
    print('Yes, banana exists in fruits tuple')

#3. Update Tuples
    # 3.1. Menambahkan value pada tuple
buah = ('jeruk','mangga','apel')
    #                                           ==> Ubah ke dalam bentuk list
y = list(buah)
y.append('sirsak')
buah = tuple(y)
print(buah)

    # 3.2. Mengubah value pada tuple
buah1 = ('jeruk','mangga','apel')
x = list(buah1)
    #                                           ==> Ubah ke dalam bentuk list
x[1]='pepaya'
buah1=tuple(x)
print(buah1)

    # 3.3. Menambahkan tuple ke tuple
a = ('jeruk','manggis')
b = ('alpukat',)
a+=b
print(a)

#4.Unpack Tuple
    #Ketika kita membuat tuple, kita biasanya memasukkan value kedalamnya. ini disebut packing tuple
fruit = ('apel','jeruk', 'pisang')  #--> Packing

    #tetapi di python, kita juga dizinkan untuk mengekstrak value tersebut kembali ke variabel
fruit = ('apel','jeruk', 'pisang')
(green, yellow, red) =fruit         #--> Unpacking
print(green)
print(yellow)
print(red)

    # 4.1. Menggunakan asterik
# Jika jumlah variabel lebih kecil dari jumlah value, kita bisa menambahkan * ke dalam varibel dan value akan dimasukkan ke variabel dalam bentuk list
fruit=('tomat','jeruk','manggis','coklat','pepaya')
(red,*green,violet) = fruit

print(red)
print(green)
print(violet)

#5 Looping dengan data List 
print("Daftar Nama Buah = ")
#5.1 For biasa
for i in fruit:
    print(i)


#5.2 For range(len(variabel))
for i in range(len(fruit)):
    print(f'No. {i+1} {fruit[i]}')


#6.Menggabungkan Tuple
q = (1,2,3,4)
p = ('a','b','c')
output=p+q
print(output)

# Di python operator (*) saat digunakn pada tuple, list atau string disebut sebagai sequence repetition opertaor
# ini adalah cara yang efisien untuk membuat tuple baru, yang berisi elemen berulang tanpa harus menulis perulangan (loop) secara manual

mytuple = 2 * q
mytuple1 = 2 * p
print(mytuple)
print(mytuple1)