"""
While Looping
Penunjuk Posisi (Pointer): i digunakan untuk mengakses elemen tertentu di dalam list. Misalnya, Nilai[i] berarti "ambil data di posisi ke-i".
Syarat Berhenti (Loop Control): i bertugas memantau kapan loop harus berhenti. Tanpa membandingkan i < len(Nilai), loop akan berjalan selamanya (infinite loop).
Penggerak (Stepper): Dengan adanya i += 1, variabel ini memastikan loop terus bergerak maju dari elemen pertama (0) ke elemen terakhir.
"""

data = ['andika', 'dimas', 'rio', 'fiandy','cikal']
i=0
sakit = ['dimas','cikal']
hadir= []
while i < len(data):
    if data[i] not in sakit:
        hadir.append(data[i])
    i+=1

print(f'Jumlah siswa Yang Hadir = {len(hadir), hadir}')

#Contoh While Looping
Nilai = [1,2,4,5,6,7]
i = 0
output = 0
while i < len(Nilai):
    output += Nilai[i]
    i+=1
    
print(output)



"""
For Looping
 digunakan untuk mengulang suatu blok kode selama ada item di dalam sebuah urutan (seperti list, tuple, string, atau range). 

"""
#For Looping 
Nama = ['dimas','andika','fiandy','rio','cikal']
Sakit = ['dimas']
siswa_hadir=[]

for i in Nama:
    if i not in Sakit:
        siswa_hadir.append(i)

print('Nama Siswa Yang Hadir Hari ini:')
for i in siswa_hadir:
    print(i)

#Enumerate Looping 
    # i = Berfungsi sebagai index, my = berfungsi menujukkan value yang terdapat pada data list 
    # Outputnya i = index ke-1, my = value index 1
data = ['andika', 'dimas', 'rio', 'fiandy','cikal']

for i, my in enumerate(data,start=2):
    if i == 3:
        continue
    print(i, my)


#For Looping dengan range(len(Nama_variabel))
    #Fungsi range(len(nama)) digunakan untuk menciptakan urutan angka berdasarkan jumlah elemen dalam sebuah list. 
    # Ini adalah cara standar jika Anda butuh mengakses indeks (nomor urut) saat melakukan perulangan (looping). w3schools.com
    #Cara Kerjanya:
    #len(nama): Menghitung total isi list. Misal isi listnya 3, maka hasilnya 3.
    #range(3): Menghasilkan deret angka mulai dari 0, 1, 2.
Nama = ['dimas','andika','fiandy','rio','cikal']

for i in range(len(Nama)):
    print(f'Index ke-{i} {Nama[i]}') #wajib menggunakan Nama[i]
