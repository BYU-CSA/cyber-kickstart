## Image Steganography

Steganography is nested under the larger topic of forensics and is the practice of hiding secret data inside of non-secret data. This might be inside an audio file or an image or other text or really anything. The idea in one of these challenges is that you'll get handed a file and you'll have to figure how it's hiding something.

An all around go-to tool for Steganography is [Aperisolve](https://aperisolve.com/) and if you'd like to learn more about the *how* of Steganography, go to Aperisove and work your way through their Cheat Sheet (you can find it on the top bar), which explains everything that their automated tool checks for. If you go to their github, you can even install a CLI version of the web tool to run locally!

### LSB
This is a common steganography tool used to hide data (text, black+white photos, or color photos) in bits of an image. Look at the LSB Steganography.pptx file to learn about *HOW* LSB steg works. Then, look at some of the examples:

* [Before hiding data](Examples/boston-skyline.png)
* [After hiding data](Examples/txt-em-boston.png)

**Tools:**
* Website for text/black&white photo LSB (this is the one used in the examples in the powerpoint)- https://stegonline.georgeom.net/upload
* Website for color photo LSB - https://incoherency.co.uk/image-steganography/
* Python script for text LSB - https://github.com/djrobin17/image-stego-tool
* Stegseek - https://github.com/RickdeJager/stegseek
  * Detects whether or not steghide is used and is wicked fast at brute forcing the steghide password

**Notes:**
* LSB steganography is only used on PNG photos (not JPEGs) because JPEGS are a lossy photo format, meaning that when you compress then uncompress it, you lose data (ie your encoding is gone). Therefore, from a CTF standpoint, LSB steganography is only something to look for in PNG photos, not JPEGs. 

## Challenges
Want to see how well you understand the material? We've provided some photos with hidden messages for you to find! See if you can find them all...

[Challenges](Challenges/)
