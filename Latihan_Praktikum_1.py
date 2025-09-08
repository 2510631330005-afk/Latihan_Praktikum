def hitung_kecepatan(jarak, waktu):
    return jarak / waktu
print("Kasus 1-Kendaraan Darat")
mobil_A = hitung_kecepatan(2000, 90)
motor_B = hitung_kecepatan(1500, 50)
sepeda_C = hitung_kecepatan(800, 40)
print(f"Mobil A {mobil_A:.2f} m/s")
print(f"Motor B {motor_B:.2f} m/s")
print(f"Sepeda C {sepeda_C:.2f} m/s")
if mobil_A > motor_B and mobil_A > sepeda_C:
    print("Mobil A tercepat")
elif motor_B > mobil_A and motor_B > sepeda_C:
    print("Motor B tercepat")
else:
    print("Sepeda C tercepat")

print()

print("Kasus 2-Atlet Lari")
pelari_1= hitung_kecepatan(400, 50)
pelari_2= hitung_kecepatan(800, 120)
pelari_3 = hitung_kecepatan(100, 11)
print(f"Pelari 1 {pelari_1:.2f} m/s")
print(f"Pelari 2 {pelari_2:.2f} m/s")
print(f"Pelari 3 {pelari_3:.2f} m/s")
if pelari_1 > pelari_2 and pelari_1 > pelari_3:
    print("Pelari 1 tercepat")
elif pelari_2 > pelari_1 and pelari_2 > pelari_3:
    print("Pelari 2 tercepat")
else:
    print("Pelari 3 tercepat")

print()

print("Kasus 3-Kendaraan Umum")
kereta_ringan = hitung_kecepatan(5000, 180)
bus_kota = hitung_kecepatan(3000, 120)
truk = hitung_kecepatan(2500, 120)
print(f"Kereta Ringan {kereta_ringan:.2f} m/s")
print(f"Bus Kota {bus_kota:.2f} m/s")
print(f"truk {truk:.2f} m/s")
if kereta_ringan > bus_kota and kereta_ringan > truk:
    print("Kereta Ringan tercepat")
elif bus_kota > kereta_ringan and bus_kota > truk:
    print("Bus Kota tercepat")
else:
    print("Truk tercepat")

print()

print("Kasus 4-Udara, Laut, Darat")
drone = hitung_kecepatan(1200, 60)
kapal_cepat = hitung_kecepatan(5000, 300)
pemain_sepak_bola = hitung_kecepatan(60, 7)
print(f"Drone {drone:.2f} m/s")
print(f"Kapal Cepat {kapal_cepat:.2f} m/s")
print(f"Pemain Sepak Bola {pemain_sepak_bola:.2f} m/s")
if drone > kapal_cepat and drone > pemain_sepak_bola:
    print("Drone tercepat")
elif kapal_cepat > drone and kapal_cepat > pemain_sepak_bola:
    print("Kapal Cepat tercepat")
else:
    print("Pemain Sepak Bola tercepat")
