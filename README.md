
# ValidAndInvalidIP


## Requirements
- Python 3.6

## Installation
- Clone the git repo - `git clone https://github.com/Mhlengi/ValidAndInvalidIP.git`
- Go inside the project `ValidAndInvalidIP`
- Create virtual environment: `virtualenv -p python3 venv`
- Activate your virtual environment: `. venv/bin/activate`
- Install all the python dependencies `pip install -r requirements.txt`

## Usage
- Run program by execute command `python challenge.py ips.txt` where `ips.txt` is your input file.
- Example: suppose one is given an input file as follows.
```ips.txt```
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
2001:0db8:85a3:0000:0000:8a2e:0370:7334
2001:db8:1234:0000:0000:0000:0000:0000
2001:db8:0:1:1:1:1:1
```
- If everything is running as excepted, your program should be able to generate 2 file.
- One with Valid IP addresses and other one with Invalid IP addresses.
- Valid output IPs file, the results should be as follows,
```validIPs.txt```
```
1.1.1.1 :-> IPv4
255.255.255.255 :-> IPv4
192.168.1.1 :-> IPv4
10.10.1.1 :-> IPv4
132.254.111.10 :-> IPv4
26.10.2.10 :-> IPv4
127.0.0.1 :-> IPv4
2001:0db8:85a3:0000:0000:8a2e:0370:7334 :-> IPv6
2001:db8:1234:0000:0000:0000:0000:0000 :-> IPv6
2001:db8:0:1:1:1:1:1 :-> IPv6
```

- Invalid output IPs file, the results should be as follows,
```invalidIPs.txt```
```
10.10.10 :-> '10.10.10' does not appear to be an IPv4 or IPv6 address
10.10 :-> '10.10' does not appear to be an IPv4 or IPv6 address
10 :-> '10' does not appear to be an IPv4 or IPv6 address
a.a.a.a :-> 'a.a.a.a' does not appear to be an IPv4 or IPv6 address
10.0.0.a :-> '10.0.0.a' does not appear to be an IPv4 or IPv6 address
10.10.10.256 :-> '10.10.10.256' does not appear to be an IPv4 or IPv6 address
222.222.2.999 :-> '222.222.2.999' does not appear to be an IPv4 or IPv6 address
999.10.10.20 :-> '999.10.10.20' does not appear to be an IPv4 or IPv6 address
222.999.22.22 :-> '222.999.22.22' does not appear to be an IPv4 or IPv6 address
22.888.22.2 :-> '22.888.22.2' does not appear to be an IPv4 or IPv6 address

```

## Run Tests
- Run tests by execute command `py.test --cov=. tests.py;`
