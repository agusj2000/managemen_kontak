"Program Perhitungan BMI"

print("PERHITUNGAN BMI")
print("---------------")

berat_badan = float(input("Masukkan berat badan anda (kg): "))#format float karena ada anggak dibelakang koma
tinggi_badan = float(input("Masukkan tinggi badan anda (meter): "))


bmi = berat_badan/(tinggi_badan**2)

berat_badan_ideal =dict()
berat_badan_ideal['bawah'] = 18.5*(tinggi_badan**2)
berat_badan_ideal['atas'] = 25*(tinggi_badan**2)

if    bmi<18.5:
      kategori = "Anda kekurangna berat badan"
elif  bmi < 25:
      kategori = "Nilai BMI anda normal"
elif  bmi < 30:
      kategori = "Anda kelebihan berat badan"
else:
      kategori = "Anda mengalami Obesistas"

print("\nHasil kalkulator BMI anda adalah:") # fungsi \n untuk membuat spasi
print("-------------------------------------")
print(f"Nilai BMI anda adalah {bmi:.2f} kg/m^2") #2f adalah2digitdibelangkoma
print(kategori)
print(f"Berat badan ideal anda adalah dalam rentang " 
      f"{berat_badan_ideal['bawah']:.2f} kg - {berat_badan_ideal['atas']:.2f}")

print("Terima kasih sudah menggunakan program ini")


#print(type(berat_badan))