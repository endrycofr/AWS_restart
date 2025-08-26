import json

def readJsonFile(fileName):
    try:
        with open(fileName, encoding='utf-8') as json_file:
            data = json.load(json_file)
        return data
    except FileNotFoundError:
        print(f"Error: File '{fileName}' tidak ditemukan.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: File '{fileName}' bukan JSON yang valid.")
        return {}

# Panggil fungsi
insulinJson = readJsonFile("insulin.json")
print(insulinJson)
