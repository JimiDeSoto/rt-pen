### Instalacja
```
apt install cmake make gcc g++ flex bison libpcap-dev libssl-dev python3 python3-dev swig zlib1g-dev
git clone --recursive https://github.com/zeek/zeek
cd zeek/
./configure
make
make install 
make install-aux

export PATH=/usr/local/zeek/bin:$PATH!
```
### Start
```
zeekctl 
deploy
status
```

### Analiza offline
przygotowanie logow: ```zeek -Cr file.pcap```  
lista mac-ow: ```cat dhcp.log | zeek-cut -d ts client_addr mac host_name```  
wyswietlenie konta komputera windows: ```krbtgt cat kerberos.log| zeek-cut id.orig_h client service | awk '$3~"krbtgt"' | grep -vi "_host_"```  
nazwa pliku msword: ```cat files.log | zeek-cut mime_type filename | grep msword```  
kiedy pobrano plik: ```cat http.log | zeek-cut -d ts method host uri resp_mime_types resp_filenames | grep _nazwa_pliku_``` 
dropniety exec: ```cat http.log | zeek-cut -d ts method host uri resp_mime_types resp_filenames | grep dosexec```  





