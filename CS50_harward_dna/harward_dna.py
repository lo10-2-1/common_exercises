import csv

database_small = r"C:\\Users\\Lydia\\Projects\\Other\\harward_dna\\dna\\databases\\small.csv"
database_large = r"C:\\Users\\Lydia\\Projects\\Other\\harward_dna\\dna\\databases\\large.csv"

dna_sequence = open(r"C:\\Users\\Lydia\\Projects\\Other\\harward_dna\\dna\\sequences\\" + input() + ".txt", "r")
dna_sequence = dna_sequence.read()

dna = {'AGATC': 0, 'TTTTTTCT': 0, 'AATG': 0, 'TCTAG': 0, 
        'GATA': 0, 'TATC': 0, 'GAAA': 0, 'TCTG': 0
        }

for title, count in dna.items():
    i = dna_sequence.find(title)
    temp = 1
    for j in range(i, len(dna_sequence), len(title)):
        if title*temp in dna_sequence[i:]:
            dna[title] += 1
            temp += 1
    dna[title] = str(dna[title])

print(dna)

with open(database_small, "r", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        quan = 3
        for title, count in dna.items():
            if title in row:
                if count == row[title]:
                    quan -= 1
                    if quan == 0:
                        print(row['name'])
            else:
                continue

with open(database_large, "r", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        quan = 8
        for title, count in dna.items():
            if title in row:
                if count == row[title]:
                    quan -= 1
                    if quan == 0:
                        print(row['name'])
            else:
                continue
    
if quan != 0:
    print('No match')