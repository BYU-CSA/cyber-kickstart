# Static Code Reverse Engineering

Many malicious actors obfuscate their code so that their techniques and identity can evade detection even if their malicious code is caught and analyzed. Or, some benign coders obfuscate their code in order to protect their proprietary coding algorithms. It's hard to look at obfuscated code and know what it does, so as security enthusiasts, we can learn the skills necessary to be successful in decoding code!

**NEVER** run ANY code (doesn't matter the coding language) in a production desktop or server unless you know what the code does. Now, of course there are exceptions-- we don't really know what Microsoft Office, Adobe Photoshop or Sophos runs in their code on their software. However, since they are a **reputable company** it's usually safe to trust and run their code. 

If you find suspicious code and you don't know what it does, either run the code in a Sandbox environment or statically examine the code. *This lesson covers statically examining code.* 

## Tips for Success

1. Understand the syntax of the coding language
2. Check what the program accepts as input arguments
3. Check what the program delivers as output
4. Understand what each standard library function does
5. Check strings in the program
6. Check conditionals (if statements)


## JavaScript Reverse Engineering

Since JavaScript is so often obfuscated for both benign and malicious purpose, there are some online tools to help in the reverse engineering process:




