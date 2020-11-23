# 1. Recon - passive
## 1.1 Web - intel
      - https://apps.db.ripe.net/db-web-ui/fulltextsearch - RIPE Database Text Search, odnajdywanie ip
      - https://hackertarget.com/as-ip-lookup/ - Autonomous System Lookup (AS / ASN / IP)
      - https://searchdns.netcraft.com/ - informacje o domenie i używane technologie
      - https://builtwith.com/ - informacje o domenie i używane technologie, powiązania
      - https://crt.sh/ - Certificate Search, certyfikaty, dodatkowo domeny i subdomeny, autoinfo
```bash
      # SQL Access
      psql -t -h crt.sh -p 5432 -U guest certwatch
```
      - https://www.entrust.com/resources/certificate-solutions/tools/certificate-transparency-search
      - https://www.virustotal.com/ - +subdomeny
      - https://www.shodan.io/
      - https://www.zoomeye.org/
      - https://censys.io/
      - https://securitytrails.com/dns-trails - historyczne dane DNS
      - https://www.rapid7.com/research/project-sonar/
      - https://openlinkprofiler.org/ - analizowanie powiązań ze stroną web, subdomains
      - https://www.exploit-db.com/google-hacking-database/ - googlehacks
      - http://archive.vn/ - archiwalne strony internetowe

## 1.2 Tools - intel/enum
      - host
      - whois
      - amass - In-depth Attack Surface Mapping and Asset Discovery, https://github.com/OWASP/Amass
```bash
      # Search for AS
      amass intel -org "$ORG"
      # Locate main domains
      amass intel -asn $ASN -active
      # Search for domains
      amass intel -d $DOMAIN -whois
      amass enum -d $DOMAIN
      
      
```
      -
      
      
      
      
      - theharvester - The tool gathers emails, names, subdomains, IPs and URLs

# X. Addons
## X.1 Dictionary
      - SecLists - multiple types of lists https://github.com/danielmiessler/SecLists
