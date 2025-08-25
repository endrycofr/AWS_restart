# === Import library yang dibutuhkan ===
import csv
import copy

# === Template dictionary untuk menyimpan data mobil ===
myVehicle = {
    "vin": "<empty>",
    "make": "<empty>",
    "model": "<empty>",
    "year": 0,
    "range": 0,
    "topSpeed": 0,
    "zeroSixty": 0.0,
    "mileage": 0
}

# Cetak isi template awal
for key, value in myVehicle.items():
    print(f"{key} : {value}")

# List kosong untuk menampung inventory mobil
myInventoryList = []

# === Membaca file CSV dan membuat salinan data ke RAM ===
with open('car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    lineCount = 0

    for row in csvReader:
        if lineCount == 0:
            print(f"Column names are: {', '.join(row)}")
            lineCount += 1
        else:
            print(f"vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}")
            
            # Salin template dictionary ke objek baru
            currentVehicle = copy.deepcopy(myVehicle)
            currentVehicle["vin"] = row[0]
            currentVehicle["make"] = row[1]
            currentVehicle["model"] = row[2]
            currentVehicle["year"] = row[3]
            currentVehicle["range"] = row[4]
            currentVehicle["topSpeed"] = row[5]
            currentVehicle["zeroSixty"] = row[6]
            currentVehicle["mileage"] = row[7]
            
            # Tambahkan data mobil ke list inventory
            myInventoryList.append(currentVehicle)
            lineCount += 1

    print(f"Processed {lineCount} lines.")

# === Cetak inventory mobil dari memory ===
for myCarProperties in myInventoryList:
    for key, value in myCarProperties.items():
        print(f"{key} : {value}")
    print("-----")
