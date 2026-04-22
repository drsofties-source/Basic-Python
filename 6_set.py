# Set
"""
Karakteristik Set
- Unordered: elemen tidak memiliki urutan tetap.
- Unique: otomatis menghapus duplikat.
- Mutable: bisa ditambah atau dihapus setelah dibuat.
- Tidak mendukung indeksasi: tidak bisa diakses dengan set[0]
- set dapat terdiri dari berbagai tipe data
"""
tipe = {True, False, 20, 10, 'a', 'cantik'}    # Berbagai Tipe Data
print(tipe)

fruit = {'pisang', 'jeruk', 'manggis', 'apel'} # Urutan tidak tetap
print(fruit)
print(len(fruit))

angka = {7,10,12,5,9,3}
print(angka)

fruit = {'pisang', 'apel', 'manggis', 'apel'} # tidak boleh duplikat 
print(fruit)
print(len(fruit))

#1 Mengakses Set
fruit={'banana','apel','semangka'}
print(f'mengakses set : {'apel' in fruit}')

#2 Menambahkan set 
thisset = {'apel','jeruk', 'manggis', 'advokat'}
    # 2.1 Menggunakan fungsi add()
thisset.add('pineapple')
print(thisset)

    # 2.2 Menggunakan update
    # objek di dalam fungsi update(), tidak harus dalam bentuk tipe set, dia dapat menggunakan berbagai bentuk tipe data (list,tuples, dict,dan sebagainya)
thisset = {'apel','jeruk', 'manggis', 'advokat'}
set2=['kismis', 'kue']
thisset.update(set2)
print(thisset)

#3 Menggabugkan sets
    # 3.1. Menggunanakan union()
    # digunakan untuk menggabungkan value dari 2 atau lebih data set, dengan menghasilkan data set baru
set1 = {'apple', 'banana', 'orange'}
set2 = {1,3,5,6}
set3 = set1.union(set2)
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)    # pada fungsi union() harus menambahakan variabel baru untuk menggunakan fungsi ini (contoh kasus: myset)
print(myset)                            # union() akan menghasilkan data set baru, (contoh : myset). 
                                        # union() dapat digunakan untuk menggabunggkan data tipe set dengan list,tuple dan outpuntnya akan berupa tipe data set

    #3.2 Menggabungkan tuple dan set
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

    #3.3 menggunakan update()
    # menghasilkan value dari gabungan 2 set atau lebih, dengan mengubah value pada data set originalnya
set1 = {'apple', 'banana', 'orange'}
set2 = {1,3,5,6,'apple'}
set1.update(set2)                       # sedangkan pada fungsi update() kita tidak perlu membuat variabel baru dan tidak bisa digunakan apabila kita menambahkan variabel baru
print(f'Update = {set1}')               # update() akan mengubah data original pada data sebelumnya, tanpa menghasilkan data set baru. dalam hal ini data set1


                                        #NOTE : union() dan update() akan menggabungkan semua value pada data sets, kecuali value yang duplicate

    #3.4 menggunakan intersection()
         #intersection akan menghasilkan value yang sama (duplicates), dan data set baru
a1 = {1,2,3,4,5,'apel'}
a2 = {'pisang', 'apel', 'jeruk', 2}     
a3 = a1.intersection(a2)
print(f'intersection = {a3}')           # intersection() akan menghasilkan value pada data set baru, (contoh: a3)
    
    #3.5 menggunakan intersection_update()
         #intersection_update() akan menghasilkan value baru yang memiliki value yang sama (duplicates), dengan mengubah data set sebelumnya (contoh kasus a1)
a1 = {1,2,4,5,6, False}
b1 = {True,2,90, 0}
a1.intersection_update(b1)
print(f'Intersection_update = {a1}')    # intersection_update() menghasilkan value baru dengan mengubah value pada dataset sebelumnya (contoh: a1)

    #3.6 Menggunakan difference()
    # digunakan untuk menghasilkan data set baru dari value yang tidak sama, pada data set pertama dengan data set selanjutnya. #
    # dalam kasus ini data set a dan b
                                        # a.difference(b), a akan menjadi set pertama, kalo b.difference(a), maka b akan menjadi set pertama
a = {1,2,4,5,6}                         # a--> set pertama
b = {2,5,6,9}                           # b--> set kedua
c = b.difference(a)                     # c--> set baru
print(f'difference = {c}')              # outputnya 1 dan 4

    #3.7 Menggunakan difference_update()
    # digunakan untuk menghasilkan value yang tidak sama pada data set pertama dan mengubah data original (pertama)
                                        # Jika x.difference_update(y) maka data x akan bertindak sebagai data set original.
                                        # begitu juga sebaliknya, jika y.difference_update(x) maka y kan bertindal sebagai data set original
x = {1,3,7,5}                           # set original   
y = {1,5,9,10}                          # set kedua
x.difference_update(y)                  # mengubah value pada data set original
print(f'difference_update = {x}')       # outputnya : 3 dan 7

    #3.8 Menggunakan symmetric_difference()
    # digunakan untuk menggabungkan value dari 2 atau lebih data set yang memilik value yang tidak sama, dan menghasilkan set baru
o = {2,3,4,5,6,7,8}                     
p = {1,2,4,6,8}
q = o.symmetric_difference(p)
print(f'symmetric_difference = {q}')

    #3.9 Menggunakan symmetric_difference_update()
    #digunakan untuk menggabungkan value dari 2 atau lebih data sets yang memiliki value yang berbeda, dengan mengubah set originalnya
o = {1,2,3,4,5,6,7,8}
p = {1,3,5,7,10}
o.symmetric_difference_update(p)
print(f'symmetric_difference_updata = {o}')

#4. Looping Set 
x = {1,4,5,6,7,True,False}
for value in x:
    print(value)

#5.Menghapus data set
    #5.1 Menggunakan remove()
a = {1,2,5,6,9}
a.remove(2)
print(f'remove = {a}')


    #5.2 Menggunakan clear()
a = {1,2,5,6,9}
a.clear()
print(f'clear = {a}')

#6. Menambahkan data set
    #untuk menambahkan data set dapat digunakan dengan menggunakan metode add
a = {1,2,4}
a.add(3)
print(f'Update = {a}')
    
    #Note : untuk menambahkan value dari data set yang berbeda kita juga bisa menggunakan fungsi update()

