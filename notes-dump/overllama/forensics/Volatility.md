[Cheat Sheet](https://blog.onfvp.com/post/volatility-cheatsheet/)
[Fun Labs](https://github.com/stuxnet999/MemLabs/tree/master)

Volatility Plugins: Triagecheck, FindAES, MemProcFS
Useful commands: pslist/pstree, procdump, filedump
Often load up both 2 and 3 and see what works.
# Volatility2
Fire
### Installation
```sh
git clone https://github.com/volatilityfoundation/volatility.git
cd volatility
sudo python2 setup.py install
```
### Basic use
```sh
python2 vol.py -f "path/to/file" imageinfo
```
When you run this command in vol2, it will return you suggested profiles, from which you can take one and try it out. Usually try for the smiplest one offered to you? So like if it has `Win7SP1x86_23418, Win7SP0x86, Win7SP1x86_24000, Win7SP1x86`, you can take `Win7SP1x86` and use it for future analysis commands:
```sh
python2 vol.py -f “/path/to/file” ‑‑profile <profile> pslist
	# you can also use psscan, pstree, and psxview
python2 vol.py -f “/path/to/file” ‑‑profile <profile> cmdscan
	# checks all commands run with cmd.exe
python2 vol.py -f “/path/to/file” ‑‑profile <profile> consoles
	# displays commands run and attached stdout output
python2 vol.py -f “/path/to/file” ‑‑profile <profile> envars
	# this is a plugin that returns environmental variables
python2 vol.py -f “/path/to/file” ‑‑profile <profile> hashdump
```
#### Errors Running
If you get an error involving `Crypto.Hash`, run these commands:
```sh
sudo apt-get install yara -y  
wget https://ftp.dlitz.net/pub/dlitz/crypto/pycrypto/pycrypto-2.6.1.tar.gz  
tar -xvzf pycrypto-2.6.1.tar.gz  
cd pycrypto-2.6.1  
sudo apt-get install python2-dev
python setup.py build  
sudo python setup.py build install
```
# Volatility3
Notes: basically Volatility3 seems to have less functionality in the favor of ease of use
### Installation
`git clone https://github.com/volatilityfoundation/volatility3.git`
`pip3 install -r requirements.txt` (you will have to either run as administrator or run with `--user` to let it install everything)
### Basics
Run with
```sh
py vol.py -h # get help
py vol.py -f "path/to/file" windows.info # general information
py vol.py -f "path/to/file" windows.pslist # process information
py vol.py -f "path/to/file" windows.cmdline # information if you see cmd.exe
```
