## LSB
This is a common steganography tool used to hide data (text, black+white photos, or color photos) in bits of an image. Look at the LSB Steganography.pptx file to learn about *HOW* LSB steg works. Then, look at some of the examples:

* [Before hiding data](https://raw.githubusercontent.com/JustinApplegate/ctf-training/main/Lesson%201%20-%20Introduction%20to%20CTFs/boston-skyline.png)
* [After hiding data](https://raw.githubusercontent.com/JustinApplegate/ctf-training/main/Lesson%201%20-%20Introduction%20to%20CTFs/txt-em-boston.png)

**Tools:**
* Website for text/black&white photo LSB - https://stegonline.georgeom.net/upload
* Website for color photo LSB - https://incoherency.co.uk/image-steganography/
* Python script for text LSB - https://github.com/djrobin17/image-stego-tool

**Notes:**
* LSB steganography is only used on PNG photos (not JPEGs) because JPEGS are a lossy photo format, meaning that when you compress then uncompress it, you lose data (ie your encoding is gone). Therefore, from a CTF standpoint, LSB steganography is only something to look for in PNG photos, not JPEGs. 

## Challenges
Want to see how well you understand the material? We've provided 3 photos with hidden messages for you to find! See if you can find them all...
