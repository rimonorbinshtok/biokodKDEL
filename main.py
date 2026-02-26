fasta=open('orf_trans_all.fa.txt','r')
count=0
header=""
seq=""
for line in fasta:
    line=line.strip()
    if line.startswith('>'):
        if seq.replace('*', '').strip().endswith("KDEL"):
            print(header)
            count += 1
        header = line
        seq = ""
    else:
        seq+=line.upper()
    
if seq.endswith("KDEL"):
    print(header)
    count += 1
print("Number of proteins containing KDEL Motif:", count)
fasta.close()