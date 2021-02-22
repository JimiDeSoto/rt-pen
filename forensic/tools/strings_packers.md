## Export strings from file
rabin2 -z your_binary - radar2  
strings - sysinternalls  
floss  
https://github.com/Th4nat0s/Chall_Tools.git - rozne detekcja entropii, pakerów


## Identify the packer  
Known tools/packers are easy to identify  
● Unix command file works «only» for Upx  
● Some packers (Upx, Vmprotect) cannot pack .NET PE  
● Yara rules or the old PEid  
○ https://github.com/Yara-Rules/rules/blob/master/Packers/packer.yar  
○ https://www.aldeid.com/wiki/PEiD  
● RDG packer detector  
○ http://www.rdgsoft.net (Mute the browser !!!)  
● DIE (DetectItEasy)   
○ https://github.com/horsicq/Detect-It-Easy | http://ntinfo.biz/  
● Exeinfo  
○ http://exeinfo.atwebpages.com/  
