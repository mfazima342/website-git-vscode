d_nama = []
d_nip = []
d_kelas = []
d_jurusan = []
d_hadir = []
d_tugas = []
d_uts = []
d_uas = []
d_akhir = []

def judul():
    print('=====================================')
    print('|    PROGRAM NILAI DATA SISWA SMK KALIBARU   |')
    print('=====================================')

def menu():
    judul()
    print('|                                   |')
    print('|      1. GURU                      |')
    print('|      2. SISWA                     |')
    print('|      3. KELUAR                    |')
    print('|                                   |')
    print('=====================================')
    print('-------------------------------------')
    menupilih = (input('Pilih Menu Login : '))

    if menupilih == '1':
       guru()
    elif menupilih == '2':
         siswa()
    elif menupilih == '3' :
         exit()
    else:
        menu()

# guru
def guru():
    print('=====================================')
    print('|               Login               |')
    print('=====================================')
    print('Masukkan kode Login')
    print('\n')
    kode = input('Masuk : ')
    if kode == 'admin' or kode == 'ADMIN':
        menu_guru()
    else:
        salah = input('Kode salah')
        guru()

def menu_guru():
    print('=====================================')
    print('Input Data Nilai Mahasiswa')
    print('=====================================')
    print('| 1. Tambah Data                    |')
    print('| 2. Lihat Data Mahasiswa           |')
    print('| 3. Selesai                        |')
    print('=====================================')
    pilih2 = input('Pilih Menu : ')
    if pilih2 == '1':
        tambah()
    elif pilih2 == '2':
        lihat()
    elif pilih2 == '3':
        selesai()
    else:
        tidak = input('Menu Tidak Ada ')
        menu_guru()

def tambah():
    print('Tambah Data')
    print('=====================================')
    jurusan = input ('Prodi [TKJ/AK] : ')
    if jurusan == 'TKJ' or jurusan == 'tkj':
        j = 'Teknik Komputer Jaringan'
        d_jurusan.append(j)
    elif jurusan == 'AK' or jurusan == 'ak':
        j = 'Akutansi'
        d_jurusan.append(j)
    else:
        kembali = input('Pilihan Tidak Ada')
        tambah()
    nama = input('Nama  : ')
    d_nama.append(nama)
    nip = input('Nip   : ')
    d_nip.append(nip)
    kelas = input('Kelas :')
    d_kelas.append(kelas)

    print('Tambah Data')
    print('=====================================')
    hadir = float(input('Jumlah Hadir : '))
    j_hadir = ((hadir/16)*20/100)*100
    d_hadir.append(j_hadir)

    tugas = float(input('Nilai Tugas  :'))
    j_tugas = tugas*(25/100)
    d_tugas.append(j_tugas)

    uts = float(input('Nilai UTS  :'))
    j_uts = uts*(25/100)
    d_uts.append(j_uts)

    uas = float(input('Nilai UAS  : '))
    j_uas = uas*(30/100)
    d_uas.append(j_uas)

    total = j_hadir+j_tugas+j_uts+j_uas
    d_akhir.append(total)
    print ('Data Tersimpan')
    kembali = input('Kembali [enter]')
    menu_guru()

def lihat():
    for i in range (len(d_nip)):

        print('%d. Nama        : %s'%(i+0, d_nama[i]))
        print('    Nim         : %s'%d_nip[i])
        print('    Kelas       : %s'%d_kelas[i])
        print('    Prodi       : %s'%d_jurusan[i])
        print('    Kehadiran   : %.2f'%d_hadir[i])
        print('    Tugas       : %.2f'%d_tugas[i])
        print('    UTS         : %.2f'%d_uts[i])
        print('    UAS         : %.2f'%d_uas[i])
        print('    Nilai Akhir : %.2f'%d_akhir[i])
        print('---------------------------')
    kembali = input('Kembali Tekan [enter]')
    menu_guru()

def selesai():
    menu()

# siswa
def siswa():
    m_nip = input('Masukkan Nim : ')
    for i in range (len(d_nip)):
        if m_nip == d_nip[i]:
            print('--------------------------')
            print('Nama        : ',d_nama[i])
            print('Nim         : ',d_nip[i])
            print('Kelas       :',d_kelas[i])
            print('Prodi       :',d_jurusan[i])
            print('Kehadiran   : ',d_hadir[i])
            print('Tugas       : ',d_tugas[i])
            print('UTS         : ',d_uts[i])
            print('UAS         : ',d_uas[i])
            print('--------------------------')
            print('Nilai Akhir : ',d_akhir[i])
            break
            
    else:
        tidak = input('Data Tidak ada')
        siswa()
        
    kembali = input('Kembali Tekan [Enter]')
    menu()
   
menu()