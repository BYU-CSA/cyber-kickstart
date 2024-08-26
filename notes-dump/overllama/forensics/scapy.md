`scapy` is a [[Python]] library for interfacing with pcap files, which is really useful if you're trying to assemble various pieces of packets. Here is a basic guide for forensics on a pre-existing pcap file.

```python
from scapy.all import *
```

Examine the packets first, and figure out what they look like:
```python
pcap = rdpcap('nameoffile.pcap')

for pkt in pcap:
	print(pkt.show())
```
This will show you a view something like this of each packet:
```
None
###[ cooked linux ]###
  pkttype   = sent-by-us
  lladdrtype= 0x1
  lladdrlen = 6
  src       = b'2QUW\xf57\x04\x06'
  proto     = IPv4
###[ IP ]###
     version   = 4
     ihl       = 5
     tos       = 0x0
     len       = 53
     id        = 58890
     flags     = DF
     frag      = 0
     ttl       = 64
     proto     = tcp
     chksum    = 0x40b4
     src       = 10.0.0.2
     dst       = 10.0.0.3
     \options   \
###[ TCP ]###
        sport     = 31337
        dport     = 35866
        seq       = 509012137
        ack       = 3073917579
        dataofs   = 8
        reserved  = 0
        flags     = PA
        window    = 510
        chksum    = 0x914f
        urgptr    = 0
        options   = [('NOP', None), ('NOP', None), ('Timestamp', (806616584, 205470911))]
###[ Raw ]###
           load      = b'Q'
```

You can then access the various pieces of the packet in your script like so:
```python
for pkt in pcap:
	if pkt['cooked linux'].pkttype == 4:
		if pkt.haslayer('Raw'):
			print(pkt['Raw'].load)
```