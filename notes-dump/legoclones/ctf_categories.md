# CTF Categories
After several months of intense research and consulting other top CTFers, this is a very extensive list of CTF topics, techniques, and categories. The list was originally created to tag CTF writeups to make for easier searching, and thus is designed with that in mind. However you're free to use it for whatever purpose you would like. 

## Categories
* Web Exploitation
  * Client-Side
    * Cache Poisoning/Deception
    * Captcha Bypass
    * Clickjacking
    * Cookie Jar Overflow
    * Cookie Tossing
    * CORS Bypass
    * CSP Bypass
    * CSRF
    * CSS Injection
    * CSTI
    * CSWSH
    * Dangling Markup
    * Open Redirect
    * SS Leaks
    * XS Leaks
    * XSS
      * Abusing Service Workers
      * DOM Clobbering
      * JS Hoisting
      * Shadow DOM Bypass
      * SOME
  * Server-Side
    * Account Takeover
    * Arbitrary File Upload
    * Command Injection
      * Argument Injection
    * Deserialization Vuln
      * ASP.NET Deserialization
      * Java Deserialization
      * PHP Deserialization
      * Pickle Deserialization
      * Yaml Deserialization
    * Flask Debug Mode
    * GraphQL Enumeration
    * Host Header Injection
    * IDOR
    * Insecure Flask Cookie
    * Insecure JWT
    * LaTeX Injection
    * LDAP Injection
    * Local File Inclusion
      * LFI to RCE
    * MFA/OTP Exploitation
    * Nginx Alias Vuln
    * Nginx Restriction Bypasses
    * NoSQL Injection
      * MongoDB Injection
    * OAuth/SAML Exploitation
    * Parameter Pollution
    * Password Reset Exploits
    * Path Traversal
    * PHP Filters
    * Rate Limit Bypass
    * Remote File Inclusion
    * Request Smuggling
    * SQL Injection
      * Boolean-Based SQLi
      * Error-Based SQLi
      * MySQL/MariaDB SQLi
      * Oracle SQLi
      * Postgres SQLi
      * SQLi to RCE
      * SQLite SQLi
      * Time-Based SQLi
      * Union-Based SQLi
      * Enumerating User-Defined Funcs
    * SSRF
    * SSTI
    * Type Juggling/Confusion
    * Websockets
    * XPATH Injection
    * XSLT Injection
    * XXE
    * Zip Slip
    * Redis Exploitation
      * Redis Arbitrary Write
      * Redis Load Module
    * Email Injection
  * CRLF Injection
  * Prototype Pollution
  * Web Race Condition
  * Web Timing Attack
* Reverse Engineering
  * Anti-Debugging
  * APK Reversing
  * Binary Patching
  * Corrupted Executable
  * Dynamic Instrumentation
  * eBPF
  * Executable Packing
  * Game Reversing
    * Console ROM Rev
    * Godot Rev
    * Unity Rev
  * Instruction Counting
  * IPA Reversing
  * Kernel Module Reversing
  * Kernel Reversing
  * Network Traffic Capture - Rev
  * Read from /proc/pid/mem
  * Seeded PRNG - Rev
  * SMT Solver
  * strace/ltrace/ptrace
  * Stripped Executable
  * Symbolic Execution
  * Virtual Machine
* Binary Exploitation
  * Stack Pwn
    * Bypass Canary
    * Bypass NX
    * Format String Vuln
    * JOP
    * Partial Overwrite
    * ret2libc
      * __malloc_hook
      * GOT Overwrite
      * one_gadget
      * ret2dlresolve
      * Unknown libc
    * ret2win
    * ROP
      * Multi-exploitation
      * ret2csu
      * ret2plt
      * ret2syscall
      * ret2system
      * SROP
      * Stack Pivoting
    * Seccomp
    * Shellcode
      * Polymorphic Shellcode
      * ret2reg
    * Stack Buffer Overflow
    * Stack Use After Return
    * Off by One
  * Heap Pwn
    * Double Free
    * Fastbin Attack
    * Heap Buffer Overflow
    * Heap Grooming
    * House of Einherjar
    * House of Force
    * House of Lore
    * House of Orange
    * House of Rabbit
    * House of Roman
    * House of Spirit
    * Largebin Attack
    * Tcache Attack
    * Unlink Exploit
    * Unsortedbin Attack
    * Use-After-Free
    * Alloc-Dealloc Mismatch
    * Container Overflow
    * House of Apple
    * House of Botcake
    * House of Cat
    * House of Corrosion
    * House of Crust
    * House of Fun
    * House of Gods
    * House of Husk
    * House of IO
    * House of Kauri
    * House of Kiwi
    * House of Mind
    * House of Muney
    * House of Pig
    * House of Prime
    * House of Rust
    * House of Storm
    * House of Tangerine
    * House of Water
  * Kernel Pwn
    * Change cr3
    * Change cr4
    * KPTI Signal Handler
    * KPTI Trampoline
    * ksymtab FG-KASLR Bypass
    * Qemu Pwn
    * ret2usr
    * ret2dir
    * Slub Freelist Overwrite
  * Browser Pwn
    * v8 Pwn
    * Wasm Pwn
  * FSOP
  * OOB
  * Info Leak
    * Null-termination Info Leak
  * Integer Overflow
  * Other Buffer Overflow
  * Pwn Race Condition
  * Pwn with Sockets
  * C++ Stack Unwinding
* Web3/Blockchain
  * Platform
    * Algorand
    * Bitcoin
    * Diem/Libra
    * Ethereum
      * delegatecall Context Mismatch
      * delegatecall Overwrite
      * ERC-20
      * Ether Transfer Vuln
      * tx.origin Misuse
    * Solana
    * StarkNet
  * Back-Running
  * Blockchain Integer Overflow
  * Chain-Reliant Random Number
  * Flash Loan Attack
  * Integer Division Rounding Attack
  * Reentrancy
  * Reversing Contract State
  * Same-Nonce Key Recovery
  * Sandwich Attack
  * Uninitialized Storage
* Cryptography
  * Encryption
    * Asymmetric Encryption
      * RSA
        * Boneh Durfee
        * Wieners Attack
        * Multiprime RSA
        * Coppersmith
        * Totient
          * Eulers Totient
          * Carmichaels Totient
      * ElGamal
      * Paillier Cryptosystem
      * Hybrid Cryptography
      * Public Key Infrastructure - PKI
    * Symmetric Encryption
      * Stream Cipher
        * One Time Pad
          * XOR
        * ChaCha20-Poly1305
        * Salsa20
      * Block Cipher
        * CBC Mode
        * CTR Mode
        * GCM Mode
        * ECB Mode
      * Feistel Network
        * Blowfish
        * Twofish
        * GOST
        * DES
          * Triple DES - 3DES
        * FEAL Cipher
      * Substitution Permutation Network
        * AES
        * S-Box
        * P-Box
      * Meet in the Middle Attack
      * RC2 Cipher
      * NSA Speck Cipher
      * Round Keys
      * Classical Cryptography
        * Caesar Shift Cipher
        * Vigenere
        * Substitution Cipher
          * Polyalphabetic Substitution Cipher
        * Enigma
    * Chosen Plaintext Attack
    * Chosen Prefix Attack
    * Known Plaintext Attack
  * Key Encapsulation Method
    * Diffie Hellman Key Exchange
      * Elliptic Curve Diffie Hellman - ECDH
  * Digital Signature
    * Asymmetric Signature
      * EDDSA
      * Elliptic Curve Digital Signature Algorithm - ECDSA
    * Symmetric Signature - MAC
      * CMAC
        * CBC-MAC
      * HMAC
      * Poly1305
      * One Time Signature Scheme
        * WOTS
  * Hash Function
    * Hash Cracking
    * Length Extension Attack
    * Hash Collision
      * Collision Resistance
      * Birthday Attack
    * Preimage Resistance
      * Second Preimage Resistance
    * SHA-256 - Crypto
      * SHA-512 - Crypto
    * SHA1 - Crypto
    * SHA3 - Keccak
    * MD5 - Crypto
    * Cyclic Redundancy Check - CRC
      * CRC-32
      * CRC-64
    * Salted Hash
  * Multi Party Computation - MPC
  * Multisig
  * Post Quantum Cryptography
    * BIKE
    * CRYSTALS-KYBER
    * SABER
    * FALCON
    * Learning With Errors - LWE
      * Ring-LWE
    * SIKE
    * SPHINCS+
    * HQC - Hamming Quasi-Cyclic
  * Fully Homomorphic Encryption
    * BFV - Brakerski-Fan-Vercauteren
    * BGV - Brakerski-Gentryu-Vaikuntanathan
    * CKKS - Cheon-Kim-Kim-Song
  * Differential Cryptanalysis
  * Linear Cryptanalysis
  * Integral Cryptanalysis
  * Elliptic Curve Cryptography - ECC
  * CSPRNG
    * Custom PRNG
  * Chinese Remainder Theorem
  * EGCD
  * Polynomial Ring
  * Cyclotomic Polynomials
  * Lagrange Interpolating Polynomial
  * Galois Field
  * Finite Fields
  * Fixed Point
  * Short Cycles
  * Group Theory
    * Symmetric Group
  * Fourier Transform
  * Modular Arithmetic
  * Rings
  * Sylvester Matrix
  * Integer Factorization
  * Discrete Logarithm Problem
  * Lattices
    * LLL
    * Shortest Vector Problem
    * Closest Vector Problem
    * Gram-Schmidt Algorithm
  * Interactive Proof
  * Oblivious Transfer
  * Pairing Based Cryptography
  * Isogeny Based Cryptography
  * Signature Aggregation
  * Padding
  * Oracle
    * Padding Oracle
    * Compression Oracle
  * Secret Sharing Scheme
    * Shamir Secret Sharing
  * Zero Knowledge Proofs
    * Zero Knowledge Machine Learning
    * ZK-SNARKs
    * ZK-STARKs
  * Privacy Preserving Machine Learning
  * SSH - Crypto
  * SSL/TLS
* Forensics
  * Disk Forensics
    * AmCache Analysis
    * Browser History Analysis
      * Chrome Forensics
      * Edge Forensics
      * Firefox Forensics
    * Deleted File Recovery
    * File Carving
    * RAID Recovery
    * Registry/Hive Analysis
    * Shellbag Analysis
    * SQLite Forensics
    * Timestomping
  * File Forensics
    * 3D Object Forensics
    * EML File Forensics
    * Font File Forensics
    * GIF Forensics
    * JPEG Forensics
    * Microsoft Office File Forensics
    * Minecraft File Forensics
    * PDF Forensics
    * PNG Forensics
    * XCF File Forensics
    * ZIP Forensics
  * Log Analysis
    * Protobuf
    * Web Log Analysis
    * Windows Event Log Analysis
  * Memory Forensics
    * Custom Kernel Profile
    * Hibernation File Analysis
    * LSASS Analysis
  * Network Forensics
    * ARP PCAP Analysis
    * DNS PCAP Analysis
      * DNS Tunneling
    * FTP PCAP Analysis
    * HTTP PCAP Analysis
    * ICMP PCAP Analysis
    * Kerberos PCAP Analysis
    * Modbus PCAP Analysis
    * MQTT PCAP Analysis
    * RTSP PCAP Analysis
    * SMB PCAP Analysis
    * VoIP PCAP Analysis
  * QR Code Forensics
  * Steganography
    * Bitplane Steganography
    * DTMF
    * EAS/SAME
    * LSB Steganography
    * Spectrogram Steganography
    * Steghide
    * Unicode Steganography
  * Unredacting
* AI/ML
  * ML Categories
    * Computer Vision
    * Natural Language Processing
    * Tabular
  * ML Algorithms
    * Clustering
    * Dimensionality Reduction
    * Neural Network
    * Trees
  * Adversarial Attack - Image
    * FGSM
    * PGD
  * Adversarial Attack - NLP
    * Prompt Injection
      * LLM Extraction
      * LLM Hijacking
  * Data Poisoning
  * Model Extraction
  * Model Inversion Attack
* Password Cracking
  * Cracking Tools
    * Cewl
    * CUPP
    * Custom cracking script
    * Hashcat
    * Hydra
    * John the Ripper
    * Medusa
  * Hash Type
    * KeePass
    * MD5
    * MD5crypt
    * NTLM
    * SHA1
    * SHA256
    * Zip File Cracking
  * Rules/Wordlist
    * Custom Cracking Rules
    * Custom Cracking Wordlist
    * Leetspeak Rules
    * Rockyou.txt
* Cloud
  * Cloud Service
    * AWS
    * Azure
    * Firebase
    * GCP
  * Cloud API Key Abuse
  * Cloud Enumeration
  * Cloud Service Account Abuse
  * Dangling AWS DNS Delegation Records
  * Discord Bot Abuse
  * Insecure Firebase Instance
  * Insecure Kubernetes Instance
    * Arbitrary Pod Creation
    * Kubernetes Enumeration
  * Insecure Lambda Function
  * Insecure Public Storage Bucket
  * SSRF Metadata Retrieval
* CI/CD
  * Dependency Confusion
  * DevOps API Key Abuse
  * DevOps Code Compromise
  * DevOps Command Injection
  * Environmental Variable Exposure
  * Exposed .git folder
  * Git
  * GitHub Actions Abuse
  * Hard-Coded Secrets
  * Jenkins Exploitation
* Hardware/IoT
  * BLE
  * Exposed Debug Interface
    * JTAG
    * SWD
    * UART
  * External Flash Memory
  * Fault Injection
  * Firmware Analysis and Extraction
  * Hardware Protocol Analysis
    * I2C Analysis
    * JTAG Analysis
    * MQTT Analysis
    * SDA Analysis
    * SPI Analysis
    * UART Analysis
  * NFC
  * PCB Reversing
  * RFID
  * Secure Boot Bypass
  * Sidechanneling
    * Sidechanneling by Power
    * Sidechanneling by Time
  * Vehicle Hacking
    * CAN Bus
    * LIN Bus
  * Verilog
  * VHDL
* Jail
  * Bash Jail
    * BashFuck
  * EVM Jail
  * NodeJS Jail
    * JSFuck
    * JsJail - vm/vm2
  * PHP Jail
    * PHPFuck
  * Python Jail
    * Pickle Jail
    * Pyjail - AST
    * Pyjail - Audit Hooks
    * Pyjail - Code Objects
    * Pyjail - No Builtins
  * Vim Jail
  * Blacklist Restriction
  * Character Restriction
  * Length Restriction
  * Unicode Jail Bypass
  * Whitelist Restriction
* Networking/RF
  * ARP Spoofing
  * DHCP Poisoning
  * DNS Packet Manipulation
  * GNURadio
  * LoRa
  * TCP Packet Manipulation
  * Wireless/WiFi
  * Zigbee
* Miscellaneous
* Pentesting/Fullpwn
  * Network Services
    * Java RMI Functions
    * Pentesting SMTP
      * SMTP Command Execution
      * SMTP Smuggling
    * Pentesting DNS
      * DNS Cache Poisoning
      * DNS Spoofing
      * DNS Zone Transfer
    * Pentesting MSRPC
      * MSRPC Credential Retrieval
      * MSRPC Known Named Pipes
    * Pentesting SMB
      * SMB Anonymous Auth
      * SMB Credential Retrieval
    * Pentesting SNMP
      * Insecure Public Community String
    * Pentesting LDAP
    * RExec
    * Rsh IP Spoofing
    * Pentesting NFS
    * Pentesting Docker
      * Container Escape
      * Docker Registry Enumeration
    * Pentesting RDP
      * RDP Session Stealing
      * RDP Saved Sessions
    * Pentesting X11
      * X11 Keylogging
      * X11 Key Injection
      * X11 Screenshots
    * Splunkd
      * Splunkd LPE
      * Splunkd RCE
    * Pentesting Memcached
  * Privilege Escalation
    * Insecure Account LPE
    * Scheduled Tasks/Cronjob
    * Readable SSH keys
    * Vulnerable Drivers
    * Weak Service Permissions
    * Weak File Permissions
    * Writeable Service Binaries
  * Linux LPE
    * Insecure SUID/SGID Permissions
    * Writable Service/Timer LPE
    * Writeable Socket LPE
    * Weak Sudo Permissions
      * GTFOBins
  * Windows LPE
    * DLL hijack
    * DPAPI Abuse
    * LAPS Abuse
    * LPE Potatoes
    * Registry Manipulation
    * UAC Bypass
    * Unquoted Service Path
    * Weak GPO
    * Winlogon Cred LPS
    * WMI LPE
* OSINT
  * Cryptocurrency OSINT
  * Darknet OSINT
  * Domain Records
  * Ecommerce OSINT
    * Craigslist OSINT
    * eBay OSINT
    * Facebook Marketplace OSINT
    * Venmo OSINT
  * Genealogical OSINT
  * Geosint
  * Google Dorking
  * Official Public Records
    * Business Records
    * County/State/Federal Records
    * Court Records
    * Property Records
    * Tax Records
    * Transportation Records
  * OSINT by Email
    * Google Account OSINT
  * OSINT by Phone Number
  * OSINT by Username
  * Public Scanning
    * censys.io
    * crt.sh
    * Shodan
  * Reverse Image Search
  * Social Media OSINT
    * Blogger OSINT
    * Dating App OSINT
    * Discord OSINT
    * Facebook OSINT
    * Flickr OSINT
    * GitHub OSINT
    * Instagram OSINT
    * LinkedIn OSINT
    * Mastodon OSINT
    * Medium OSINT
    * Pinterest OSINT
    * Reddit OSINT
    * Snapchat OSINT
    * Telegram OSINT
    * TikTok OSINT
    * Tumblr OSINT
    * Twitch OSINT
    * Twitter OSINT
    * Youtube OSINT
  * Wayback Machine
* CVE exploiting
* Scripting/Programming
Language/Architecture
* Operating System
  * Android
  * DOS
  * BSD
  * iOS
  * Linux
  * Mac
  * TempleOS
  * Windows
* Compiled Language
  * C
  * C++
  * Cobol
  * Crystal
  * Fortran
  * Go
  * Haskell
  * Nim
  * OCaml
  * Pascal
  * Rust
  * Swift
* Interpreted Language
  * Awk
  * Bash
  * Batch scripting
  * C-Sharp
  * Dart
  * Erlang/Elixir
  * Java
  * JavaScript
    * Hermes Bytecode
    * Typescript
    * v8 Bytecode
  * Julia
  * Kotlin
  * Lisp
  * Lua
  * Perl
  * PHP
  * PowerShell
  * Python
    * Pickle
    * Python Bytecode
  * REXX
  * Ruby
    * Ruby Bytecode
  * Scala
  * VBScript
* Architecture
  * 64-bit
  * 32-bit
  * 16-bit
  * Alpha
  * ARM
  * Hexagon DSP
  * MIPS
  * PowerPC
  * RISC-V
  * SPARC
  * wasm
  * x86
  * Xtensa
* Esolang
  * Befunge
  * Brainfuck
  * Malbolge
  * Rockstar
* Blockchain Languages
  * Bamboo
  * Cairo
  * EVM Bytecode
  * Liquidity
  * Move
  * Solidity
  * Vyper
  * Yul