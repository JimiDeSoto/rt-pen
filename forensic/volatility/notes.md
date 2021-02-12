https://code.google.com/archive/p/volatility/wikis/CommandReference.wiki  
psxview procesy i ukryte  
dlllist -p [PID]  - dllki porocesu  
privs -p [PID]  - uprawnienia procesu  
handles -p [PID]   
handles -p [PID] -t key  
envars - srodowisko  
ldrmodules -p 1772  
malfind - szuka malware  
modules  
modscan  
hivelist - rejestr  
printkey “Path\To\Key” - wyswietla klucz  
hashdump  
lsadump  
filescan - poszukiwanie plików  
mutantscan -s - szuka mutexow CID column contains the process ID and thread ID 
thrdscan | findstr "1772"  
netscan - sieciowka dla windows  
userassist - klucze usera  
yarascan -Y "CNC" 
volshell - shell  
procdump -p - zrzut procesu exe  
memdump zrzut pamiecvi  
dumpfiles - zrzuca pliki , bez parametru wszyustkie  
modscan 

dumpfiles -D event/ -r "(txt|log)$"  
cat pslist.txt psscan.txt | awk '{print $2"\t"$3}' | sort | uniq -c | grep -v " 2"  
psscan --output=dot --output-file=graph.dot  
clamscan  
vol3 - yarascan.YaraScan --yara-file ./malware_rules.yar  
