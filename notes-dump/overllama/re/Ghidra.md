Apparently Ghidra is way cooler than I thought it was, and I thought it was freaking awesome.

Export patched binary in Ghidra: file > export program > format:original file > rename (to like patched or something)
### Scripting
Java skeleton:
```java
// TODO: write a description for this script
//@author
//@category Stack
//@keybinding
//@menupath 
	// lets you choose where in the menu it goes
	// ex. @menupath Tools.Packt.Learn Ghidra Script
	// that will put it in the Ghidra main menu under Tools
	// just make sure you check the "In Tool" box
//@toolbar

// imports. Check Ghidra's Javadocs for specifics
import ghidra.app.script.GhidraScript;

public class NewScript extends GhidraScript {
	public void run() throws Exception {
		// TODO : add code here
	}
}
```

Python skeleton:
```python
# TODO: write a description for this script
#@author
#@category Stack
#@keybinding ctrl alt shift n
	# keybinding lets you choose a keybinding to be associated with this script
#@menupath
#@toolbar
```
Window > Python will pull open Ghidra's Python interpreter
`help()` is a useful command because it will spit out documentation for whatever you put inside it. Try starting with `help(currentProgram)`

Actually, it's best to use the Eclipse IDE to make new scripts and edit old ones, since you can run them in there using Ghidra and debug them. 
Go to Ghidra > New > Ghidra Script and it'll let you create a new one