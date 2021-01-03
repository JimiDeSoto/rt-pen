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

### Hashcat windows passwords
Mode	Hash	Description   
1000	NTLM	Extremely common, used for general domain authentication  
1100	MsCache	Domain cached credentials, old version  
2100	MsCache v2	Domain cached credentials, new version  
3000	LM	Old, rarely used anymore (still a part of NTLM)  
5500	NetNTLMv1 / NetNTLMv1+ESS	NTLM for authentication over the network  
5600	NetNTLMv2	NTLM for authentication over the network  
7500	Kerberos 5 AS-REQ Pre-Auth etype 23	AS_REQ is the initial user authentication request of Kerberoas  
13100	Kerberos 5 TGS-REP etype 23	TGS_REP is the reply of the Ticket Granting Server to the previous request
