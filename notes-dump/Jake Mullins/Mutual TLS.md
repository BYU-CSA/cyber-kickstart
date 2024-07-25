Public Key Cryptography: I swear I knew this like the back of my hand way back, but no más.
Public key: Everyone has access.
Private key: Only the correct parties have access.

Anything encrypted with the public can *only* be decrypted by the private key. 

[Cloudflare blog post](https://www.cloudflare.com/learning/access-management/what-is-mutual-tls/)

Mutual

Typical TLS negotiation:
![[images/Screenshot 2024-07-03 at 8.41.06 AM.png]]
1. Client connects to server
2. Server presents X.509 Cert
3. Client verifies server X.509 Cert
4. Connection is established.

Mutual TLS (mTLS) negotiation
![[images/Screenshot 2024-07-03 at 8.42.44 AM.png]]

1. Client connects to server
2. Server presents server X.509 cert
3. Client verifies server's cert
4. Client presents client X.509 cert
5. Server verifies client's cert
6. Connection is established

This prevents:
- On-path attacks. (Why? I guess I gotta learn about how on-path works)
- Spoofing

This kind of process is really useful in Zero-Trust architectures.
