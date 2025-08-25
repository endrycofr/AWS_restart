# === Exercise: Creating a mixed-type list ===
myMixedTypeList = [
    45,                     # integer
    290578,                 # integer
    1.02,                   # float
    True,                   # boolean
    "My dog is on the bed.",# string
    "45"                    # string yang kebetulan angkanya sama seperti int pertama
]

# Loop untuk menampilkan setiap item dan tipe datanya
for item in myMixedTypeList:
    print("{} is of the data type {}".format(item, type(item)))
