#List
"""
List adalah tipe data di Python yang digunakan untuk menyimpan kumpulan item dalam satu variabel tunggal. Bayangkan list seperti sebuah kotak kontainer yang bisa menampung banyak barang sekaligus dengan urutan tertentu. 
Dalam Python, list ditandai dengan penggunaan kurung siku [ ]. 
Karakteristik Utama List
    Ordered (Terurut): Setiap elemen memiliki posisi tetap yang disebut index (dimulai dari 0).
    Changeable (Mutable): Anda bisa menambah, menghapus, atau mengubah isi list setelah dibuat.
    Allow Duplicates: Boleh ada nilai yang sama di dalam satu list (seperti contoh Anda: [79, 90, 80, 90]).
    Mixed Data Types: Bisa berisi campuran angka, teks (string), bahkan list lain. 
"""
# Contoh List:
        #nama = ['fandi','dimas','andika']

#1. Mengakses List
penghuni_kost = ['dimas','fandi','fiandy', 'cikal', 'rio', 'andika']
print(penghuni_kost[0])     # menampilkan value pada index ke 0 ==> 'dimas'
print(penghuni_kost[0:4])   # menampilkan value pada index ke 0 - ke 3
print(penghuni_kost[0:])    # menampilkan value pada index ke 0 - value terakhir
print(penghuni_kost[:5])    # menampilkan value pada index ke 0 - ke 
print(penghuni_kost[-1])    # menampilkan value terakhir yang terdapat pada data list


#2. Menambahkan value Pada data list
    #2.1 Menggunankan insert
buah = ['jeruk','manggis','kelapa']
buah.insert(1,'pepaya')            # menambahkan value 'pepaya' pada index ke-1
buah.insert(0,'mangga')            # menambahkan value 'mangga' pada index ke-0
print(buah)

    #2.2 Menggunakan append
buah = ['jeruk','manggis','kelapa']
buah.append('tomat')
buah.append('apel')                # menambahkan value pada data list dan akan berada pada index serta value terakhir   
print(buah)

#3. Mengubah value pada data list
motor = ['scoopy', 'vario', 'mio','vixion','megapro']
motor[1]='beat'                    # Jika value yang ingin diganti hanya 1, tidak perlu menggunakan kurung siku []
motor[2:4]=['cb', 'ADV']
print(motor)

#4. Mengurutkan value pada list
motor = ['scoopy', 'vario', 'mio','vixion','megapro']
motor.sort()                        # Mengurutkan value pada list berdasarkan abjad dari A ke Z
print(motor)            
motor.sort(reverse=True)            # Mengurutkan value pada list berdasarkan abjad dari Z ke A
print(motor)

#5 Menghapus value pada list
    # 5.1. Menggunakan remove()
buah = ['apel','cherrry', 'mangga', 'pisang', 'manggis']
buah.remove('apel')                 # menghapus list berdasarkan valuenya                 
print(f'menggunakan remove() : {buah} ')
fruit = ['banana','chese','milk','cofee','Tea','sugar','Tea']
fruit.remove('Tea')
#apabila terdapat lebih dari satu data yang memiliki value yang sama, contoh dalam kasus ini "Tea",maka data dengan value pertama yang akan terhapus"
print(fruit)

    # 5.2. menggunakan pop()
buah = ['apel','cherrry', 'mangga', 'pisang', 'manggis']
buah.pop(1)                         # menghapus list berdasarkan indexnya
buah.pop(0)                         # jika kita tidak memasukan nilai indexnya, index terakhir yang akan dihapus
print(f'menggunaka pop() : {buah}')


    # 5.3. menggunakan del
buah = ['apel','cherrry', 'mangga', 'pisang', 'manggis']
del buah[0:2]                       # menghapus list berdasarkan indexnya
print(f'Menggunakan del : {buah}')  #
#del buah                             menghapus list buah
#print(buah)                          akan eror jika karena data listnya sdah dihapus
                 
    # 5.4. menggunakan clear()
buah = ['apel','cherrry', 'mangga', 'pisang', 'manggis']
buah.clear()                        # menghapus value pada list
print(f'Menggunaka clear() : {buah}')

#6. Menggabungkan data list
    #6.1 menggunakan operator +
n = [75,80,90,55,88,68,78,90]
buah = ['apel','cherrry', 'mangga', 'pisang', 'manggis']
print(f'Dengan operator + = {n + buah}')
    #6.2 menggunakan extend()
n = [75,80,90,55,88,68,78,90]
buah = ['apel','cherrry', 'mangga', 'pisang', 'manggis']
n.extend(buah)
print(f'menggunakan extend() = {n}')
    #6.3 menggunakan for dan append
n = [75,80,90,55,88,68,78,90]
buah = ['apel','cherrry', 'mangga', 'pisang', 'manggis']

for i in buah:
    n.append(i)
print(f'menggunakan for dan append = {n}')



#list comprehansion
"""
adalah cara singkat dan elegan untuk membuat list baru dari list yang sudah ada hanya dalam satu baris kode.
struktur dasar list comprehension : [ekspresi for item in list_lama if kondisi]
"""

n = [75,80,90,55,88,68,78,90]
lulus = [x for x in n if x  >= 75]
print(lulus)


penghuni_kost = ['dimas','fandi','fiandy', 'cikal', 'rio', 'andika']
keluar= ['fiandy','cikal']
penghuni = [x for x in penghuni_kost if x not in keluar]
print(f'Daftar penghuni kost {penghuni}')


y = [x+5 for x in lulus]
print(y)



""" Jika Anda ingin menggunakan if-else di dalam List Comprehension, urutan penulisannya sedikit berubah. Kondisinya dipindahkan ke depan sebelum perintah for.
Strukturnya menjadi:
[hasil_if if kondisi else hasil_else for item in list]
"""
nilai = [75,80,90,55,88,68,78,90]
akhir = ['lulus'if x > 74  else 'Tidak lulus' for x in nilai]
print(akhir)


"""
saat menggunakan nested if-else (lebih dari satu kondisi) di dalam list comprehension, Anda tetap harus menyertakan kata kunci else untuk setiap if.
Strukturnya adalah:
[hasil1 if kondisi1 else hasil2 if kondisi2 else hasil_akhir for x in list]
"""
nilai = [70,75,80,90,55,88,68,78,90]
akhir = ['lulus'if x > 74 else 'standart' if x> 66 else 'Tidak Lulus' for x in nilai]
print(akhir)


