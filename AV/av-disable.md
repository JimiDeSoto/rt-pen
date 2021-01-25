##Defender
### Disable
``Set-MpPreference -DisableRealtimeMonitoring $true``  
Client - ``New-ItemProperty -Path “HKLM:\SOFTWARE\Policies\Microsoft\Windows Defender” -Name DisableAntiSpyware -Value 1 -PropertyType DWORD -Force``  
### Exclude ext
``Set-MpPreference -ExclusionExtension EXTENSION``
### Exclude folder
``Set-MpPreference -ExclusionPath C:\Users``
### Exclude file
