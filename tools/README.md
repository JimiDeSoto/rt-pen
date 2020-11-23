# 1. Recon - passive
## 1.1 Web - intel
      - https://apps.db.ripe.net/db-web-ui/fulltextsearch - RIPE Database Text Search, odnajdywanie ip
      - https://searchdns.netcraft.com/ - informacje o domenie i używane technologie
      - https://builtwith.com/ - informacje o domenie i używane technologie, powiązania
      - https://crt.sh/ - Certificate Search, certyfikaty, dodatkowo domeny i subdomeny, autoinfo
      - https://www.entrust.com/resources/certificate-solutions/tools/certificate-transparency-search
      - https://www.virustotal.com/ - +subdomeny
      - https://www.shodan.io/
      - https://www.zoomeye.org/
      - https://censys.io/
      - https://securitytrails.com/dns-trails - historyczne dane DNS
      - https://www.rapid7.com/research/project-sonar/
      - https://openlinkprofiler.org/ - analizowanie powiązań ze stroną web, subdomains
      - https://www.exploit-db.com/google-hacking-database/ - googlehacks

## 1.2 Tools - intel
      - theharvester - The tool gathers emails, names, subdomains, IPs and URLs
        ```bash
           docker pull whiteoaksecurity/docker-theharvester 
           sudo docker run -ti whiteoaksecurity/docker-theharvester
        ```

