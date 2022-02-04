# Ghidra
Ghidra (*pronounced gee-drah*) is a reverse engineering tool that was developed by NSA and released a few years back. It's GUI isn't very pretty, but it's effective at what it does and helps provide a nice overview of what the program does, what functions exist, and how they interact with each other.

## Installing Ghidra
Ghidra is hosted on GitHub, and the latest version can be downloaded [from there](https://github.com/NationalSecurityAgency/ghidra/releases). The ZIP file should then be uncompressed and placed into whatever directory desired. Ghidra is not a program that needs to be installed on a computer, all the files it needs are contained in the downloaded folder, and to start it, all you have to do is run the script for your operating system. Ghidra works on Linux and Windows. 

Before running Ghidra, Java must be installed on the operating system. The [official installation guide](https://ghidra-sre.org/InstallationGuide.html) recommends Java 11, which can be downloaded and installed from [Amazon Corretto](https://docs.aws.amazon.com/corretto/latest/corretto-11-ug/downloads-list.html). However, newer versions may also work. See the official installation guide linked above if any other issues arise. 

*Note - I use Ghidra on Windows. To make things easy, I move the uncompressed Ghidra folder into my Documents folder, and then make a shortcut for `ghidraRun.bat` on my Desktop. Whenever I want to use it, I just double click on the Desktop shortcut.*

## Importing Executables
<img src="openingScreen.png" width="600px">

Each time Ghidra is opened, the screen above is presented. Each file that is analyzed must be located in a project. Think of projects as folders - you can put as many files/executables in a folder/project as you want. Create a new project if you need. Once a project is created, you can import an executable by clicking "File" --> "Import file" in the top menu. Browse to the location of a file and select it. 

<img src="type_detection.png" width="500px">

Once an executable is uploaded, you'll see this screen. Ghidra is smart and will normally detect and tell you the executable type and architecture right here. If you see blanks in these locations instead, your life just got harder and you'll have to manually insert the type of executable. 

*Note - Ghidra is really smart, so if it can't detect what type of executable it is, chances are you did something wrong. It may not be an executable, or it may be corrupted.*

Accept it, press "Okay", and now the executable is all loaded and ready to go. 

## Analyzing Executables
To analyze a file, you'll want to open it up in the Code Browser. Double click on the file or select the file and click the dragon symbol above it. 

<img src="notAnalyzed.png" width="400px">

First thing you'll see is a prompt asking if you want it to analyze the executable. **Answer yes - it's literally asking to do a lot of the hard work**. It will present you with a bunch of decompiling options - select all of them except the ones in red (that say Prototype) and click "Analyze". Ghidra will now pull out a bunch of important information in a format that is more readily available than before.

<img src="codeBrowser.png" width="1000px">

The Code Browser has three main sections - the left pane (Program Trees, Symbol Trees, and Data Type Manager), the middle pane (the assembly of the program), and the right pane (decompiled code and defined strings). There are dozens of features and capabilities that Ghidra has to offer, but I'll only highlight a few of the main ones I've used. 

The Symbol Trees section of the leftmost pane, including imports and functions. Imports are libraries provided by the Operating System that provide functionality - seeing what functions and libraries the program requires can give insight into what it's supposed to do. Also, the functions list is really important! Most functions have a `main` function that starts out, so double clicking on that function will allow you to see it. The middle pane will show the assembly (in Intel syntax, thank goodness) for the `main` function, and the right pane will show you Ghidra's best attempt at turning the assembly into C code. Some other functions listed will be ones that start with underscores (`_`) - these functions are often built-in or from imports/libraries, and perform basic functionality like printing to the screen and so. In addition, functions that start with `FUN` and a bunch of numbers like `FUN00010203` is typically a user-defined function with no name - it's important to inspect these functions and see what's inside. 

The code in the right pane will be of most interest to you - while not easy to read, it greatly decreases the work required to understand what the code does. You'll find `if` statements, `do-while` loops, and more. Note that more complex structures like `for` loops are not there - you'll often find it decomposed into code like `int i = 0; do { /*do something*/; i++; } while (true);`. Variables like `&DAT_00102050` are simply referring to an array or string stored in memory. To see what the array or string is, double click on it and it'll pull it up in the middle pane as both hex and ASCII. The forward and back arrows on the top left and really nice to go back to previous functions you were looking at after double clicking and going inside of them.

Since function names are lost in compilation, Ghidra gives them generic names like `uVar1` and so. These variables can be renamed by right-clicking and selecting "Rename Variable"; this will rename it everywhere in Ghidra, including other functions and the middle pane. Many variables are initialized of type `undefined4` or `undefined8`. This just means it's of a type of that many bytes. Oftentimes, `undefined8` refers to an `int`. 

The code on the right can be exported to a C file by clicking the icon featuring a paper and pencil on the far right. You can even try to fix up the C code to compile and run it yourself if you want!! (although it will take some work...) Many variables, especially strings, are stored as plain ASCII characters and not assembly, and the program can pick those out easily. View all the easily-readable strings by clicking on the "Defined strings" tab on the bottom right, or Window --> Defined Strings on the top menu. Sometimes, this can even give away secret information like hardcoded passwords or flags. 

## Beyond
Ghidra has much more to offer, but these basic functions allow anyone to import an executable, browse functions and see basic functionality, view defined strings, and more!

## Challenge
Want to try Ghidra on an executable yourself? There is an executable called `rev` in this folder that you can use. Can you find the flag??

*Note - if you need help, go to [this page](https://guyinatuxedo.github.io/03-beginner_re/helithumper_re/index.html) for a walkthrough. This is also a **great** resource for learning about reverse engineering!*