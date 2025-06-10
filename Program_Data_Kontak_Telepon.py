## Program_Data_Kontak_Telepon.py
# Program yang memiliki fitur CRUD (Create, Read, Update, Delete) untuk memodifikasi data kontak telepon.
# Nama  : Suluh Bagaspati
# Kelas : JCDSOL-021-Online

# Modul untuk membungkus (wrap) teks yang panjangnya melampaui lebar tertentu.
import textwrap

# Dictionary data kontak sebagai data awal. Nomor telepon menggunakan list agar dapat menyimpan lebih dari satu nomor.
kontak = {'Caca': {'Nomor Telepon': ['+6285111222333', '+6285777888999'], 'Perusahaan': 'PT Semen Sejahtera', 'Jabatan': 'CEO',
                   'Email': 'caca@gmail.com', 'Alamat': 'Jl Muara Karang Bl C/10, Dki Jakarta'},
          'Andi' : {'Email': 'andi@gmail.com', 'Nomor Telepon': ['+6289765432100']},
          'Aldi': {'Nomor Telepon': ['+6285444555666'], 'Perusahaan': 'PT Keramik Sentosa', 'Jabatan': 'Supervisor',
                   'Email': 'Aldi@gmail.com', 'Alamat': 'Jl Pelajar Pejuang 45 106, Jawa Barat'}
         }

# Daftar header yang digunakan untuk menampilkan tabel.
headers = ['Nama', 'Nomor Telepon', 'Perusahaan', 'Jabatan', 'Email', 'Alamat']

# Fungsi yang membuat huruf pertama nama kontak menjadi huruf kecil untuk mengurutkan kontak.
def nama_kecil(item):
    return item[0].lower()

# Fungsi untuk menampilkan tabel berdasarkan kriteria tertentu.
def tabel(kriteria, inputFilter):
    global kontak 
    kontak = dict(sorted(kontak.items(), key=nama_kecil)) # Mengurutkan berdasarkan nama kontak

    # Menentukan filter berdasarkan kriteria yang diberikan (nama atau karakter awal)
    if kriteria == 'Individu': # Kondisi ketika kriteria adalah 'Individu'
        while True: # Jika inputFilter False maka fungsi akan meminta input sebagai filter nama
            if inputFilter == False: 
                filterNama = input('\nMasukkan nama kontak: ').lower()
            else: # Menggunakan filter nama yang sudah diberikan inputFilter
                filterNama = inputFilter.lower() 
            if filterNama in (nama.lower() for nama in kontak): 
                filter = [filterNama] # Filter berdasarkan nama yang sesuai
                break
            else: # Jika nama tidak ditemukan, keluar dari fungsi
                print('\nNama kontak tidak ditemukan.')
                return 
    elif kriteria == 'Karakter': # Kondisi ketika kriteria adalah 'Karakter'
        while True:
            karakter = input('\nMasukkan karakter: ')
            if len(karakter) == 1: # Validasi bahwa input hanya satu karakter
                if karakter.lower() in (nama[0].lower() for nama in kontak): # Cek karakter pertama nama kontak
                    filter = [nama.lower() for nama in kontak if nama[0].lower() == karakter.lower()] # Filter berdasarkan karakter
                    break
                else: # Jika tidak ada kontak yang sesuai, keluar dari fungsi
                    print(f'\nTidak ada kontak dengan awalan {karakter}.')
                    return
            else: # Input lebih dari satu karakter tidak valid
                print('\nMasukan lebih dari 1 karakter. Silakan di coba kembali.') 

    ## Menentukan lebar kolom berdasarkan panjang teks terpanjang di setiap kolom
    lebar_max = 20 # Lebar maksimal setiap kolom
    lebarKolom = {} # Dictionary dari lebar setiap kolom
    for header in headers: # Iterasi setiap header kolom
        header_len = len(header) 
        # Panjang kolom ditentukan dari nilai maksimal dari panjang header kolom dan panjang kolom informasi kontak
        if header == 'Nama': # Menentukan panjang kolom nama
            karakter_max = max(header_len, max(len(nama) for nama in kontak)) 
        elif header == 'Nomor Telepon': # Menentukan panjang kolom nomor telepon
            nomor_len_max = (max((len(nomor) for nomor in info.get(header, [])), default=0) for info in kontak.values())
            # Nomor telepon terpanjang ditambah 1 untuk memperhitungkan potensial koma ketika nomor lebih dari satu
            karakter_max = max(header_len, max(nomor_len_max) + 1) 
        else: # Menentukan panjang kolom dari setiap kolom lainnya
            karakter_max = max(header_len, max(len(info.get(header, '')) for info in kontak.values()))
        # Mengatur lebar kolom agar tidak melebihi lebar maksimal. Agar tiap informasi kontak memiliki jarak maka ditambah 2.
        lebarKolom[header] = min(lebar_max, karakter_max + 2) 

    # Menampilkan header tabel
    print()
    print(f'{'DAFTAR KONTAK':^{sum(lebarKolom.values())}}')
    for header in headers: # Memberi garis untuk header bagian atas. Header terputus setiap kolom untuk membedakan antar kolom
        print(f'{'='*(lebarKolom[header]-1)+' ':<{lebarKolom[header]}}', end='')
    print()
    for header in headers:
        print(f'{header:<{lebarKolom[header]}}', end='')
    print()
    for header in headers: # Garis untuk header bagian bawah yang memisahkan header dan kolom
        print(f'{'='*(lebarKolom[header]-1)+' ':<{lebarKolom[header]}}', end='')
    print()

    # Menampilkan data kontak
    for nama, info in kontak.items(): 
        if kriteria != 'Semua': # Jika kriteria dari fungsi bukan 'Semua' maka data akan ditampilkan sesuai filter
            if nama.lower() not in filter:
                continue # Lewati kontak yang tidak sesuai filter
        no_telepon = info.get('Nomor Telepon', [''])
        data_baris = [nama, ', '.join(no_telepon)] + [info.get(header, '') for header in headers[2:]]

        # Membungkus data agar sesuai dengan lebar kolom
        data_wrapped = [] # Menyimpan data yang dibungkus untuk setiap baris
        for i in range(len(data_baris)):
            # Membungkus teks dengan panjang maksimal sesuai lebar kolom dikurangi 2 untuk memberi jarak tiap informasi kontak
            wrapped = textwrap.wrap(data_baris[i], lebarKolom[headers[i]] - 2) 
            if not wrapped:
                wrapped = [''] # Apabila teks tidak dibungkus karena berupa kosong atau whitespace
            data_wrapped.append(wrapped) # Data yang dibungkus ditambahkan ke list data_wrapped

        # Menampilkan data yang sudah dibungkus sesuai lebar kolom
        baris_wrapped = max(len(teks) for teks in data_wrapped) # Menentukan jumlah baris terbanyak dari setiap data yang dibungkus
        for i in range(baris_wrapped): # i menentukan baris
            for j in range(len(data_wrapped)): # j menentukan kolom
                teks = data_wrapped[j] # Menentukan data pada kolom ke-j
                if i < len(teks): # Menentukan data pada baris ke-i berdasarkan list data yang dibungkus
                    teks_wrapped = teks[i] 
                else: # Apabila list data yang dibungkus kurang dari i maka data baris ke-i adalah ''
                    teks_wrapped = ''
                print(f'{teks_wrapped:<{lebarKolom[headers[j]]}}', end='') # Menampilkan data per kolom
            print()
            
        # Menampilkan pembatas antar baris yang terputus setiap kolom untuk membedakan antar kolom
        for header in headers:
                print(f'{'-'*(lebarKolom[header]-1)+' ':<{lebarKolom[header]}}', end='')
        print()

# Fungsi untuk mengecek apakah data kontak kosong
def cekKontak():
    if not kontak:
        print('\nData kontak telepon kosong.')
        return False
    else:
        return True

# Fungsi untuk mengecek nomor telepon yang baru dan sesuai format internasional
def cekNomor():
    while True:
        nomor = input('Masukkan nomor telepon baru: ')
        if nomor[0] != '+' or not nomor[1:].isdigit():
            print('\nNomor telepon harus berupa angka dan mengikuti format internasional.\nContoh: +6281223334444\n')
            continue
        for info in kontak.values():
            if info.get('Nomor Telepon') and nomor in info['Nomor Telepon']:
                print('\nNomor telepon telah terdaftar. Silakan masukkan nomor lain.\n')
                break
        else:
            return nomor

# Fungsi untuk memilih opsi ubah atau hapus pada submenu ubah kontak
def opsi_ubah_hapus():
    while True:
        print('[1] Ubah\n[2] Hapus\n[0] Kembali ke submenu ubah kontak')
        pilihan = input('Silakan masukkan pilihan [0-2]: ')
        if pilihan == '1':
            return True
        elif pilihan == '2':
            return False
        elif pilihan == '0':
            return
        else:
            print('\nMasukan tidak ada dalam pilihan. Silakan di coba kembali.\n')

# Fungsi untuk memilih nomor telepon ketika ada lebih dari satu
def pilihNomor(nomorList):
    if len(nomorList) == 1:
        return nomorList[0] # Jika hanya satu nomor, langsung mengembalikan nomor tersebut
    indeks = 1
    for nomor in nomorList:
        print(f'[{indeks}] {nomor}') # Menampilkan pilihan nomor telepon
        indeks += 1
    while True:
        try:
            pilihan = int(input('Pilih nomor telepon (masukkan angka): '))
            if 1 <= pilihan <= len(nomorList):
                return nomorList[pilihan - 1] # Mengembalikan nomor yang dipilih
            else:
                print('\nPilihan di luar jangkauan.\n')
        except ValueError:
            print('\nMasukan harus berupa angka.\n')

# Fungsi untuk menyimpan perubahan pada kontak
def simpan():
    while True:
        pilihan = input('\nApakah kontak akan diubah? (Y/N): ').upper()
        if pilihan == 'N':
            print('\nKontak tidak diubah.')
            return False
        elif pilihan == 'Y':
            print('\nKontak berhasil diubah.')
            return True
        else:
            print("\nMasukan tidak ada dalam pilihan.\nHarap masukkan 'Y' untuk ya atau 'N' untuk tidak.\n")

# Fungsi untuk menghapus informasi tertentu pada kontak
def hapusInfo():
    while True:
        pilihan = input('\nApakah dihapus? (Y/N): ').upper()
        if pilihan == 'N':
            print('\nInformasi kontak tidak dihapus.')
            return False
        elif pilihan == 'Y':
            print('\nInformasi kontak berhasil dihapus.')
            return True
        else:
            print("\nMasukan tidak ada dalam pilihan.\nHarap masukkan 'Y' untuk ya atau 'N' untuk tidak.\n")

# Fungsi untuk menambahkan atau mengubah kontak
def tambah_ubah_kontak(nama, nomor = None, perusahaan = None, jabatan = None, email = None, alamat = None, nomorLama = None, namaBaru = None):
    dataBaru = {} # Dictionary kosong untuk menampung data baru yang akan diubah atau ditambahkan

    # Mengganti nama kontak apabila ada namaBaru
    if namaBaru and nama in kontak:
        kontak[namaBaru] = kontak.pop(nama)
        nama = namaBaru # Agar variabel nama diproses selanjutnya menggunakan namaBaru

    #Jika nomor telepon baru diberikan, tambahkan atau ubah nomor telepon pada kontak yang sesuai
    if nomor:
        if nama in kontak:
            nomor_list = kontak[nama].get('Nomor Telepon', []) # Daftar kontak telepon yang sudah ada
            if nomorLama and nomorLama in nomor_list: # Jika nomorLama ada maka ganti nomor lama dengan nomor baru
                nomor_list[nomor_list.index(nomorLama)] = nomor
            else:
                nomor_list.append(nomor) # Tambahkan nomor baru
            dataBaru['Nomor Telepon'] = nomor_list # Nama ada dikontak sehingga datanya berasal dari list lama
        else:
            dataBaru['Nomor Telepon'] = [nomor] # Jika nama belum ada dikontak, tambahkan nomor baru ke list kosong
            
    # Jika informasi baru diberikan maka tambahkan ke dataBaru
    if perusahaan:
        dataBaru['Perusahaan'] = perusahaan
    if jabatan:
        dataBaru['Jabatan'] = jabatan
    if email:
        dataBaru['Email'] = email
    if alamat:
        dataBaru['Alamat'] = alamat
    
    if nama in kontak:
        kontak[nama].update(dataBaru) # Update kontak jika nama kontak sudah ada
    else:
        kontak[nama] = dataBaru # Buat entri baru jika nama kontak belum ada

# Fungsi untuk menu tambahkan kontak
def createMenu():
    # Menampilkan menu dan menangani pilihan pengguna
    while True:
        print('\n'+'== Menu Tambahkan Kontak ==')
        print('[1] Menambahkan kontak baru\n[0] Kembali ke menu utama')
        pilihan = input('Silakan masukkan pilihan (0/1): ')

        if pilihan == '1': # Jika pengguna memilih untuk menambahkan kontak baru
            namaBaru = input('\nMasukkan nama kontak: ')
            if namaBaru.lower() in (nama.lower() for nama in kontak):
                print('\nNama kontak telah digunakan.')
                continue
            nomorBaru = cekNomor() # Meminta nomor telepon baru 
                    
            while True:
                # Menanyakan apakah pengguna ingin menambahkan informasi kontak lainnya
                pilihan = input('\nApakah ingin menambahkan informasi kontak lainnya? (Y/N): ').upper()
                if pilihan == 'Y':
                    perusahaanBaru = input('\nMasukkan asal perusahaan: ')
                    jabatanBaru = input('Masukkan jabatan: ')
                    emailBaru = input('Masukkan email: ')
                    alamatBaru = input('Masukkan alamat: ')
                    break
                elif pilihan == 'N':
                    break
                else:
                    print("\nMasukan tidak ada dalam pilihan.\nHarap masukkan 'Y' untuk ya atau 'N' untuk tidak.")
                    
            while True:
                # Menanyakan apakah pengguna ingin menyimpan kontak
                simpan = input('\nApakah kontak akan disimpan? (Y/N): ').upper()
                if simpan == 'N':
                    print('\nKontak tidak disimpan.')
                    break
                elif pilihan == 'Y' and simpan == 'Y':
                    # Jika ingin menyimpan dan menambahkan informasi lainnya
                    tambah_ubah_kontak(namaBaru, nomorBaru, perusahaanBaru, jabatanBaru, emailBaru, alamatBaru)
                    print('\nKontak tersimpan.')
                    break
                elif pilihan == 'N' and simpan == 'Y':
                    # Jika hanya ingin menambah kontak dan nomor
                    tambah_ubah_kontak(namaBaru, nomorBaru)
                    print('\nKontak tersimpan.')
                    break
                else:
                    print("\nMasukan tidak ada dalam pilihan.\nHarap masukkan 'Y' untuk ya atau 'N' untuk tidak.")
                    
        elif pilihan == '0': # Jika pengguna memilih untuk kembali ke menu utama
            return
        else:
            # Menangani input yang tidak valid di menu utama
            print('\nMasukan tidak ada dalam pilihan. Silakan di coba kembali.')

# Fungsi untuk menu tampilkan kontak
def readMenu():
    # Menampilkan menu dan menangani pilihan pengguna
    while True:
        print('\n'+'='*13+' Menu Tampilkan Kontak '+'='*13)
        print('[1] Tampilkan semua kontak\n[2] Tampilkan kontak individu\n[3] Tampilkan kontak berdasarkan awalan karakter\n[0] Kembali ke menu utama')
        pilihan = input('Silakan masukkan pilihan [0-3]: ')

        # Jika pilihan adalah 1, 2, atau 3, lanjutkan dengan memeriksa dan menampilkan kontak
        if pilihan in ['1', '2', '3']:
            if not cekKontak(): # Mengecek apakah ada kontak yang tersedia dengan memanggil fungsi cekKontak()
                continue # Jika tidak ada kontak, kembali ke awal dan menunggu input lagi
            if pilihan == '1': # Menampilkan semua kontak jika pilihan adalah 1
                tabel('Semua', False)
            elif pilihan == '2': # Menampilkan kontak individu jika pilihan adalah 2
                tabel('Individu', False)
            else: # Menampilkan kontak berdasarkan awalan karakter jika pilihan adalah 3
                tabel('Karakter', False)
        elif pilihan == '0': # Jika pilihan adalah 0, keluar dan kembali ke menu utama
            return
        else: # Menangani input yang tidak valid
            print('\nMasukan tidak ada dalam pilihan. Silakan di coba kembali.')

# Fungsi untuk menu ubah kontak
def updateMenu():
    # Menampilkan menu ubah kontak dan menangani pilihan pengguna
    while True:
        print('\n'+'='*4+' Menu Ubah Kontak '+'='*4)
        print('[1] Ubah kontak\n[0] Kembali ke menu utama')
        pilihan = input('Silakan masukkan pilihan (0/1): ')

        if pilihan == '1':
            if not cekKontak(): # Mengecek apakah ada kontak yang tersedia dengan memanggil fungsi cekKontak()
                continue # Jika tidak ada kontak, kembali ke awal dan menunggu input lagi
            
            # Meminta input nama kontak yang ingin diubah
            nama_input = input('\nMasukkan nama kontak: ')
            if nama_input.lower() not in (nama.lower() for nama in kontak):
                print('\nKontak tidak ditemukan.')
                continue

            # Menyimpan nama kontak yang ditemukan, terlepas dari kapitalisasi
            namaKontak = None
            for nama in kontak:
                if nama.lower() == nama_input.lower():
                    namaKontak = nama
                    break
                
            tabel('Individu', namaKontak) # Menampilkan detail kontak yang ingin diubah
            # Menanyakan apakah pengguna ingin melanjutkan untuk mengubah kontak
            while True:
                pilihan = input('\nApakah Anda ingin melanjutkan untuk mengubah kontak? (Y/N): ').upper()
                if pilihan == 'Y':
                    break
                if pilihan == 'N':
                    print('\nKontak tidak diubah')
                    break
                else:
                    print("\nMasukan tidak ada dalam pilihan.\nHarap masukkan 'Y' untuk ya atau 'N' untuk tidak.")
            if pilihan == 'N':
                continue # Jika tidak ingin mengubah, kembali ke menu ubah nama

            # Menampilkan submenu untuk memilih informasi yang ingin diubah
            while True:
                tabel('Individu', namaKontak) # Menampilkan tabel dengan data kontak individu
                print('\n'+'='*5+' Submenu Ubah Kontak '+'='*5)
                print('[1] Nama\n[2] Nomor telepon\n[3] Perusahaan\n[4] Jabatan\n[5] Email\n[6] Alamat\n[0] Kembali ke menu ubah kontak')
                pilihan = input('Pilih informasi kontak yang ingin diubah: [0-6]: ')

                if pilihan == '1': # Jika pilihan adalah untuk mengubah nama kontak
                    while True:
                        namaBaru_input = input('\nMasukkan nama baru kontak: ')
                        if namaBaru_input.lower() in (nama.lower() for nama in kontak):
                            print('\nNama kontak telah digunakan.')
                            continue
                        else: 
                            print('\nAnda akan mengubah nama kontak.')
                            break
                    if simpan(): # Menyimpan perubahan nama jika pengguna setuju
                        tambah_ubah_kontak(namaKontak, namaBaru = namaBaru_input)
                        namaKontak = namaBaru_input
                        
                elif pilihan == '2': # Mengubah nomor telepon
                    print('\nAnda akan mengubah nomor telepon.')
                    opsi = opsi_ubah_hapus() # Menanyakan apakah ingin mengubah atau menghapus nomor telepon
                    nomor_list = kontak[namaKontak].get('Nomor Telepon',[])
                    if opsi is True: 
                        nomorBaru = cekNomor()
                        while True:
                            print(f'\nOpsi penyimpanan nomor {nomorBaru}:')
                            print('[1] Tambahkan nomor telepon baru\n[2] Ubah nomor telepon lama\n[0] Kembali ke submenu ubah kontak')
                            pilihan = input('Silakan masukkan pilihan [0-2]: ')
                            if pilihan == '1': # Menambahkan nomor telepon baru
                                print('\nAnda akan menambahkan nomor telepon baru.')
                                if simpan(): # Menyimpan perubahan nama jika pengguna setuju
                                    tambah_ubah_kontak(namaKontak, nomorBaru)
                                    break
                            elif pilihan == '2': # Mengubah nomor telepon lama
                                if not nomor_list: # Menginformasikan kontak kosong
                                    print('\nNomor telepon kosong.')
                                else:
                                    print('\nAnda akan mengubah nomor telepon lama.')
                                    nomor = pilihNomor(nomor_list) # Memilih nomor yang akan diubah
                                    print(f'\nNomor telepon {nomor} akan diganti oleh nomor {nomorBaru}')
                                    if simpan(): # Menyimpan perubahan nama jika setuju
                                        tambah_ubah_kontak(namaKontak, nomorBaru, nomorLama = nomor)
                                        break
                            elif pilihan == '0':
                                break
                            else:
                                print('\nMasukan tidak ada dalam pilihan. Silakan di coba kembali.')
                            
                    elif opsi is False:
                        if not nomor_list: # Menginformasikan kontak kosong
                            print('\nNomor telepon kosong.')
                        else:
                            print('\nAnda akan menghapus nomor telepon.')
                            if len(nomor_list) < 2:
                                if hapusInfo(): # Menghapus jika setuju
                                    kontak[namaKontak].pop('Nomor Telepon') # Ketika nomor kurang dari 2 gunakan fungsi pop()
                            else:
                                nomor = pilihNomor(nomor_list) # Memilih nomor yang akan dihapus
                                print(f'\nNomor telepon {nomor} akan dihapus')
                                if hapusInfo(): # Menghapus jika setuju
                                    nomor_list.pop(nomor_list.index(nomor)) # Menghapus sesuai dengan pilihan nomor
                                    kontak[namaKontak]['Nomor Telepon'] = nomor_list
                        
                elif pilihan == '3': # Mengubah perusahaan
                    print('\nAnda akan mengubah perusahaan.')
                    opsi = opsi_ubah_hapus()
                    if opsi is True: 
                        perusahaanBaru = input('\nMasukkan perusahaan baru: ')
                        if simpan():
                            tambah_ubah_kontak(namaKontak, perusahaan = perusahaanBaru) 
                            
                    elif opsi is False: # Mengubah perusahaan
                        if not kontak[namaKontak].get('Perusahaan',None):
                            print('\nInformasi perusahaan kosong.')
                        else:
                            print('\nAnda akan menghapus perusahaan.')
                            if hapusInfo():
                                kontak[namaKontak].pop('Perusahaan')
                        
                elif pilihan == '4': # Mengubah jabatan
                    print('\nAnda akan mengubah jabatan.')
                    opsi = opsi_ubah_hapus()
                    if opsi is True:
                        jabatanBaru = input('\nMasukkan jabatan baru: ')
                        if simpan():
                            tambah_ubah_kontak(namaKontak, jabatan = jabatanBaru)
                    
                    elif opsi is False:
                        if not kontak[namaKontak].get('Jabatan',None):
                            print('\nInformasi jabatan kosong.')
                        else:
                            print('\nAnda akan menghapus jabatan.')
                            if hapusInfo():
                                kontak[namaKontak].pop('Jabatan')
                            
                elif pilihan == '5': # Mengubah email
                    print('\nAnda akan mengubah email.')
                    opsi = opsi_ubah_hapus()
                    if opsi is True:
                        emailBaru = input('\nMasukkan email baru: ')
                        if simpan():
                            tambah_ubah_kontak(namaKontak, email = emailBaru)
                    
                    elif opsi is False:
                        if not kontak[namaKontak].get('Email',None):
                            print('\nInformasi email kosong.')
                        else:
                            print('\nAnda akan menghapus email.')
                            if hapusInfo():
                                kontak[namaKontak].pop('Email')
                            
                elif pilihan == '6': # Mengubah alamat
                    print('\nAnda akan mengubah alamat.')
                    opsi = opsi_ubah_hapus()
                    if opsi is True:
                        alamatBaru = input('\nMasukkan alamat baru: ')
                        if simpan():
                            tambah_ubah_kontak(namaKontak, alamat = alamatBaru)
                    elif opsi is False:
                        if not kontak[namaKontak].get('Alamat',None):
                            print('\nInformasi alamat kosong.')
                        else:
                            print('\nAnda akan menghapus alamat.')
                            if hapusInfo():
                                kontak[namaKontak].pop('Alamat')
                            
                elif pilihan == '0': # Kembali ke menu ubah kontak
                    break
                else: # Menangani input tidak valid
                    print('\nMasukan tidak ada dalam pilihan. Silakan di coba kembali.')
            
        elif pilihan == '0': # Kembali ke menu utama
            return
        else: # Menangani input tidak valid
            print('\nMasukan tidak ada dalam pilihan. Silakan di coba kembali.')

# Fungsi untuk menu hapus kontak
def deleteMenu():
     # Menampilkan menu untuk menghapus kontak
    while True:
        print('\n'+'='*3+' Menu Hapus Kontak '+'='*3)
        print('[1] Hapus kontak\n[2] Hapus semua kontak\n[0] Kembali ke menu utama')
        pilihan = input('Silakan masukkan pilihan [0-3]: ')
        if pilihan in ['1','2']: # Pilihan untuk menghapus kontak
            if not cekKontak(): # Memeriksa apakah ada kontak yang terdaftar
                continue # Jika tidak ada akan kembali ke menu hapus kontak
            if pilihan == '1': # Pilihan untuk menghapus satu kontak
                # Meminta input nama kontak yang ingin dihapus
                nama_input = input('\nMasukkan nama kontak yang akan dihapus: ')
                if nama_input.lower() not in (nama.lower() for nama in kontak):
                    print('\nKontak tidak ditemukan.')
                    continue
                # Menyimpan nama kontak yang ditemukan, terlepas dari kapitalisasi
                namaKontak = None
                for nama in kontak:
                    if nama.lower() == nama_input.lower():
                        namaKontak = nama
                        break
                # Menanyakan konfirmasi sebelum menghapus
                while True:
                    pilihan = input(f'\nApakah anda akan menghapus kontak {namaKontak}? (Y/N): ').upper()
                    if pilihan == 'N':
                        print('\nKontak tidak dihapus.')
                        break
                    elif pilihan == 'Y':
                        kontak.pop(namaKontak) # Menghapus kontak dengan nama yang telah dinput
                        print('\nKontak berhasil dihapus.')
                        break
                    else:
                        print("\nMasukan tidak ada dalam pilihan.\nHarap masukkan 'Y' untuk ya atau 'N' untuk tidak.\n")
            else: # Pilihan untuk menghapus seluruh kontak
                while True:
                    pilihan = input('\nApakah anda akan menghapus seluruh kontak? (Y/N): ').upper()
                    if pilihan == 'N':
                        print('\nSeluruh kontak tidak dihapus.')
                        break
                    elif pilihan == 'Y':
                        kontak.clear() # Menghapus seluruh data kontak
                        print('\nSeluruh kontak berhasil dihapus.')
                        break
                    else:
                        print("\nMasukan tidak ada dalam pilihan.\nHarap masukkan 'Y' untuk ya atau 'N' untuk tidak.\n")

        elif pilihan == '0': # Pilihan untuk kembali ke menu utama
            return
        else:
            print('\nMasukan tidak ada dalam pilihan. Silakan di coba kembali.') # Menangani input tidak valid

# Fungsi untuk menu utama
def mainMenu():
    # Menampilkan menu utama dan menangani pilihan pengguna
    print()
    print('='*5+' Menu Utama '+'='*5)
    print('[1] Menambahkan kontak\n[2] Menampilkan kontak\n[3] Mengubah kontak\n[4] Menghapus kontak\n[0] Keluar Program')

    # Menerima input pilihan menu dari pengguna
    pilihan = input('Silakan pilih menu [0-4]: ')
    if pilihan == '0': # Jika pilihan adalah '0', keluar dari program
        return print('\nTerima Kasih\n')
    else: # Menjalankan fungsi sesuai dengan pilihan
        if pilihan == '1':
            createMenu()
        elif pilihan == '2':
            readMenu()
        elif pilihan == '3':
            updateMenu()
        elif pilihan == '4':
            deleteMenu()
        else:
            print('\nMasukan tidak ada dalam pilihan. Silakan di coba kembali.') # Menangani input yang tidak valid
        return mainMenu() # Setelah menjalankan pilihan, kembali ke menu utama

# Fungsi untuk menjalankan program
def main():
    print('\n'+'='*22)
    print(f'{'Program Data':^22}')
    print(f'{'Kontak Telepon':^22}')
    print('='*22)
    mainMenu() # Memanggil fungsi mainMenu untuk menampilkan menu utama

# Mencegah jalannya main() ketika file di-import sebagai modul
if __name__ == "__main__":
    main() # Memulai program