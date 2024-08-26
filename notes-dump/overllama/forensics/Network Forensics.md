Challenge types:
- Statistical
- Text carving
- File carving (network miner)
- OS / protocol fingerprinting
- Obscure protocol values
- Encrypted traffic
- Packet / protocol timing
- malware identification
Tools:
- Wireshark - best for statistics / tshark (apply as filter is goated, `frame contains "x"`)
- TCPdump
- Network miner - parses out by machine, and automatically carves out files. Images automatically displayed to screen if clicked on, credentials automatically grabbed, too
- snort / surikata - just run a pcap through the ruleset and automatically see what's in it. Yara may be good in this, too
- Zeek/Bro - 
- Netflow / Sflow - how many packets went to this address or what type of file went to this address, etc
Approaches / Thought Process:
1. How big is the PCAP file?
	- Easy? You can go for more stuff
	- Large: cut it up and stuff with [PCAPHelper](https://github.com/dlm225/PCAPHelper) maybe
2. Strings, network miner, wireshark filters and stats
3. Sometimes just stray to the side of the faster tool
Sometimes, you just need the RFC

Okay, so for using TLS keys to decrypt Wireshark traffic, you'll need a key. Once you have that key, you can import it in Edit > Preferences > Protocols > TLS by adding a key to the "RSA keys list", you can decrypt traffic. You'll need a port (of the local computer I think?), protocol will be http, port will likely be 443, but you can check the packets, and select your key file.
When I did it in the USCG Open, it didn't directly decrypt these packets in Wireshark for some reason, but by setting a TLS debug file in that same location, I was able to find the flag in the decrypted packets in the log information.

Any time you see DNS or ICMP and you think there's a timing attack, go to chat GPT, get a script that will allow you to see the difference in timing between the attacks. "I have ICMP packets, a request and a reply, and I think there's a timing attack. Write me a script that times them and gives me a binary value (a 1 or a 0) based on that time" so it'll give you a script that returns a string of 0s and 1s, where 0 is around average and 1 is greater than the average time. His example script read each request packet, appends it to a list, changes those to intervals list, calculates the average interval, and then forms a binary string based on the list and how those compare to the average.
You can isolate a protocol: file > export > specified packets > csv. Then that's really easy to parse