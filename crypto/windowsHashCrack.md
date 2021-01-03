## Hashe

### LM:
LM przestarzałe, łatwe do połamania.  
john --format=lm hash.txt 
hashcat -m 3000 -a 3 hash.txt  
    
### NTHash:
MD4 trochę bezpieczniejsze, używane w domyślnie w Windows  
john --format=nt hash.txt  
hashcat -m 1000 -a 3 hash.txt  

### Net-NTLM v1  
john --format=netntlm hash.txt  
hashcat -m 5500 -a 3 hash.txt  

### Net-NTLM v2  
john --format=netntlmv2 hash.txt  
hashcat -m 5600 -a 3 hash.txt  
