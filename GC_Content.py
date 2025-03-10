def gc_content(dna):
    gc_count = dna.count('C') + dna.count('G')
    return (gc_count / len(dna)) * 100

def parse_fasta(file_path):
    sequences = {}
    current_id = None
    
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                current_id = line[1:]  
                sequences[current_id] = ""  
            else:
                sequences[current_id] += line  

    return sequences

def find_highest_gc(file_path):
    sequences = parse_fasta(file_path)
    max_id = max(sequences, key=lambda seq: gc_content(sequences[seq]))
    return max_id, gc_content(sequences[max_id])

file_path = ""  

best_id, best_gc = find_highest_gc(file_path)
print(best_id)
print(f"{best_gc:.6f}")  