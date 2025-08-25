import re
import os

# Pastikan folder output ada
output_dir = "file_insulin"
os.makedirs(output_dir, exist_ok=True)

# File input
input_file = "insulin_sequence.txt"

# Baca dan bersihkan sequence
with open(input_file, "r") as f:
    seq = f.read()
clean_seq = re.sub(r'[^a-zA-Z]', '', seq).lower()

# Ambil subsequence
file_mapping = {
    "lsinsulin-seq-clean.txt": clean_seq[0:24],     # Signal peptide
    "binsulin-seq-clean.txt": clean_seq[24:54],     # B-chain
    "cinsulin-seq-clean.txt": clean_seq[54:89],     # C-peptide
    "ainsulin-seq-clean.txt": clean_seq[89:110]     # A-chain
}

# Simpan semua subsequence ke folder
for filename, content in file_mapping.items():
    file_path = os.path.join(output_dir, filename)
    with open(file_path, "w") as f:
        f.write(content)

# Cetak informasi
print(f"Files created in '{output_dir}':")
print(f"preproinsulin-seq-clean.txt: {len(clean_seq)} aa")
for filename, content in file_mapping.items():
    print(f"{filename}: {len(content)} aa")