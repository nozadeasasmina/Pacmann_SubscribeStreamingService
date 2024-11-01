#membuat modul
#modul konversi_jam.py

#fungsi konversi jam ke hari
def hari(jam):
    print(f"Konversi {jam} jam ke hari: {jam/24} hari")

#fungsi konversi jam ke menit
def menit(jam):
    print(f"Konversi {jam} jam ke menit: {jam*60} menit")

#fungsi konversi jam ke detik
def detik(jam):
    print(f"Konversi {jam} jam ke detik: {jam*3600} detik")

#coba function yang sudah dibuat di Notebook
hari(25)
menit(2000)
detik(3000)

print('hello')