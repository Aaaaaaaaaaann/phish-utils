# Phish utils (test)
A small CLI set.

## Ports scanner
Сhecks if ports in the specified domains are open. For ports 80 and 443 shows server name if possible.

### Usage
`python main.py ports scan 130.193.38.46 21 25 80 28445`


## Domains match
Generates similar domains for a keyword and shows registered ones with IPs.

### Usage
`python main.py domains match stackoverflow`


## Google Play app search
Shows apps data by a keyword.

### Usage
`python main.py gp search water`
