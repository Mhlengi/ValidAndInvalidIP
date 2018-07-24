# Back-end Interview Challenge

Feel free to approach and present the solution to the challenge below in any way you like.

Please do not hesitate to let us know if anything is unclear.

#### Valid/invalid IP filtering
Given the following input file (ips.txt):
```
1.1.1.1
255.255.255.255
192.168.1.1
10.10.1.1
132.254.111.10
26.10.2.10
127.0.0.1
10.10.10
10.10
10
a.a.a.a
10.0.0.a
10.10.10.256
222.222.2.999
999.10.10.20
222.999.22.22
22.888.22.2
```
Write a script that differentiates between valid and invalid IPs and output the results in 2 separate files (invalidIPs.txt, validIPs.txt), when the following script is run:
```
python challenge.py ips.txt
```
 
