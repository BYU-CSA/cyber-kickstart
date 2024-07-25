Transport Layer Security (TLS), successor to Secure Sockets Layer (SSL). Changed name because it was no longer associated with Netscape.
Most recent version TLS 1.3 published in 2018.
HTTPS is an implementation of TLS + HTTP.
- Encryption
- Authentication
- Integrity
TLS Cert lives on a web server. TLS Cert is issued by a CA to an owner of a domain.

TLS Certificates Fields:
- Issued To
	- Common Name (CN):
	- Organization (O):
	- Organizational Unit (OU):
- Issued By
	- Common Name (CN)
	- Organization (O):
	- Organizational Unit (OU):
- Validity Period:
	- Issued On:
	- Expires On:
- SHA-256 Fingerprints
	- Certificate:
	- Public Key
![[Screenshot 2024-07-08 at 10.41.51 AM.png]]

Downloaded `medium.com`'s certificate, inspected it with `openssl x509 -in ./_.medium.com.pem -text`. Here's the fields

Certificate:
- Data
	- Version: 3
	- Serial Number: `03:44:6f:87:c0:e4:44:f2:ad:f4:2a:26:38:8a:e8:1c`
	- Signature Algorithm: sha256WithRSAEncryption
	- Issuer: C=US, ST=CA, L=San Francisco, O=Affirm, OU=4041384f6cf271449fd95a453221f0d9, CN=ca.affirm.goskope.com, emailAddress=certadmin@netskope.com
	- Validity:
		- Not Before: May 22 2024
		- Not After: Jun 21 2025
	- Subject: CN=\*.medium.com
	- Subject Public Key Info:
		- Public-Key: (2048 bit)
		- Modulus:                     `00:d4:c4:e6:77:92:5a:22:0f:fd:f7:4a:13:54:52:7b:56:5e:d0:8a:e5:cb:bf:0d:dc:c2:8b:a5:09:c8:3c:6e:fb:b9:75:eb:d9:ab:d9:ef:71:0a:7f:2d:50:63:d9:8f:1f:06:dc:5f:42:b1:27:dc:b8:56:ba:ce:0b:25:d3:be:21:2d:a1:e7:f0:d5:dc:3f:4a:c9:a2:b2:0f:8c:9a:fc:75:60:a6:11:84:2e:ac:f2:38:6c:43:37:c0:67:9d:c5:fa:23:8c:5d:33:f1:2a:fc:20:5c:85:49:a9:b5:8b:15:ba:45:53:e5:d0:57:7a:6a:ab:96:33:d6:72:45:e3:a1:2a:5f:b4:9b:44:cc:7f:ba:1d:53:37:3f:50:b4:43:a2:29:3f:79:db:ad:dd:a9:12:67:50:0f:97:81:d5:02:a8:5f:a7:35:bb:92:50:7e:10:d9:88:44:7e:0c:06:10:f3:86:58:08:9b:11:5a:89:e0:aa:2c:b2:2a:eb:15:89:8e:c8:7d:26:aa:81:38:58:3d:25:ec:d7:ac:fa:e2:69:17:ab:d7:a4:3f:be:1b:47:0f:3c:ff:57:48:f4:9d:9e:7a:86:c6:a8:60:7f:39:7e:b1:93:7e:34:1f:47:d4:6c:5f:a9:7f:12:5d:3f:1a:19:91:c3:e3:41:af:e1:a7:c4:36:8f`
		- Exponent: 65537
	- X509v3 extensions:
		- X509v3 Basic Constraints:
			- CA: False
		- X509v3 Subject Key Identifier:
			- `E7:85:BE:8C:8A:F5:1E:A6:77:F4:97:F2:36:A9:F1:2A:34:BE:9C:92`
		- X509v3 Subject Alternative Name:
			- DNS:`*.medium.com`, DNS:`medium.com`
		- X509v3 Key Usage: critical
			- Digital Signature, Key Encipherment
		- X509v3 Extended Key Usage:
			- TLS Web Server Authentication, TLS Web Client Authentication
- Signature Algorithm: sha256WithRSAEncryption
- Signature Value: `29:51:11:db:1a:bc:c6:dd:ae:a8:ed:03:2b:2b:f8:74:cf:01:1d:79:61:1f:9d:58:fc:4e:64:9c:2d:e0:19:2a:54:da:ad:d4:85:63:7f:9a:67:22:38:6f:6d:ea:b1:39:04:17:20:fb:03:56:1e:49:04:fd:cc:ee:c4:20:a0:cf:0a:43:a0:ad:57:f4:44:47:aa:a7:89:57:b6:e1:e6:8b:99:a7:c8:a5:84:2d:e9:7a:6b:76:32:bf:70:6f:ff:0f:b7:34:c7:47:eb:06:17:56:12:9f:35:b8:4f:30:66:b5:42:ab:a6:82:bf:78:35:02:28:41:43:94:e6:18:38:77:8a:0f:46:3d:f9:d4:90:f2:74:89:fa:4d:f7:02:55:9f:e0:1e:80:41:90:bf:28:d8:67:7b:18:2a:4d:bc:29:5c:58:3d:5f:c8:38:80:f3:52:71:d6:73:e5:fb:bf:4e:4a:73:f1:50:b7:38:00:2f:9b:80:cd:96:fa:e1:04:30:5b:93:bb:4b:6d:43:88:f1:63:c4:21:28:5c:81:5a:9a:42:f7:56:99:f5:78:72:c4:26:02:45:52:e1:d7:a6:55:88:e2:a3:50:1e:97:a5:fb:ec:4c:bd:39:40:6d:75:68:d1:d5:97:dd:6f:98:ab:ba:8c:fd:0e:17:01:d3:b2:c4:ef`

Filename extensions:
- `.pem`: Privacy-enhance Electronic Mail: Base64 encoded DER certificate, enclosed between `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----`. May container a certification chain, starting with the leaf / end certificate of the service, followed by the certificate that signed it, usually up to but not including the trusted oot certificate.
```pem
-----BEGIN CERTIFICATE-----
base 64 encoding of the DER encoded certificate.
-----END CERTIFICATE-----
```
- `.cer`, `.crt`, `.der` - usually in binary DER form, but Base64-encoded certs are common/possible.
- `.p8`, `.p8e`, `.pk8` - Exported private key from PKCS#8, in DER or PEM form that starts with `-----BEGIN PRIVATE KEY-----`. Encrypted key starts with `-----BEGIN ENCRYPTED PRIVATE KEY-----`.
- `.crl`- Certification Revocation List.

DER: Distinguished Encoding Rules. Created to meet the requirements of X.509. Can encode any data, also describe encoded [certificate](https://stackoverflow.com/questions/22743415/what-are-the-differences-between-pem-cer-and-der).
PEM: Method of encoding binary data, containing the header and a footer line.

## RSA
Secret vars:
- $p$ and $q$: Distinct prime numbers
- $d$: Private exponent, module multiplicative inverse of $e \mod \phi(n)$.
- $m$: Plaintext message

Public vars:
- $n$: Modulus used in both the public and private keys, calculated as $n = p * q$.
- $\phi(n)$: Euler's totient function of $n$, computed as $phi(n) = (p - 1)(q - 1)$.
- $e$: Public exponent between $1 < e < \phi(n)$ and is coprime with $\phi(n)$, meaning $gcd(e,\phi(n)) = 1$. In practice this is typically `0x10001` or 65,537.
- $c$: Ciphertext message


Vars:
- $p$ and $q$: Distinct prime numbers
- $N$: Modulus, the predict of $p$ and $q$, so $N = pq$.
- $e$: Encryption exponent
- $d$: Decryption exponent, satisfying $e * d = 1 \mod (p - 1)(q - 1)$
Public key is $(N, e)$,
Private key is $d$.

Encrypt a message $M$: $C = M^{e}\mod N$
Decrypt a message $C$: $M = C^{d}\mod N$

This can either ensure confidentiality or non-repudiation, depending on the configuration. There are two separate cases:
*Encrypting with private key:* Can be effectively decrypted by everyone, but everyone knows that someone with the private key encrypted it, providing non-repudiation. No assurances for integrity.

*Encrypting with public key*: Can only be decrypted by the person with the private key. Provides integrity, does not provide non-repudiation.