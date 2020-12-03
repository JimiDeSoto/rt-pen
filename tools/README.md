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
      - https://www.ssllabs.com/ssltest/analyze.html - SSL Certificate Testing
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
# 3. Post-exploitation
## 3.1. Tools
      - CrackMapExec - utomate assessing the security of large Active Directory networks https://github.com/byt3bl33d3r/CrackMapExec https://mpgn.gitbook.io/crackmapexec/
# X. Addons
## X.1 Dictionary
      - SecLists - multiple types of lists https://github.com/danielmiessler/SecLists
## x.2 Raporty
      - writehat - generator raportów pentest https://github.com/blacklanternsecurity/writehat
