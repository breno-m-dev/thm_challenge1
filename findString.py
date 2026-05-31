input_file = "output.txt"
output_file = "filtered.txt"

with open(input_file, "r", encoding="utf-8", errors="ignore") as f:
    lines = f.readlines()

filtered = []

for line in lines:
# i knew these 3 following characters had to be in the same line to find the info we needed
    if "{" in line and "}" in line and "_" in line: 
        filtered.append(line)

with open(output_file, "w", encoding="utf-8") as f:
    f.writelines(filtered)

print(f"Done! {len(filtered)} lines saved to {output_file}")