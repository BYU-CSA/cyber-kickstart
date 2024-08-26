[[Forensics]] of [[memory]]

Memory tracks all kinds of things:
- Network
- Serial connections
- Windows detections and stuff
- Modification times
- Running processes
You can mess with memory accidentally by:
- Forgetting to have no-write blockers when cloning a machine
- Forgetting no-write blockers on USB drives to dump the RAM
- Changing the network

You need to know the OS version of the machine in question so you can use tools that will appropriately capture the memory
RAM will contain encryption keys of Windows BitLocker!!

How to capture RAM:
- If it's a VM, there are special ways
- BelkaSoft RAM Capturer
- DumpIt
- FTKImager

Volatility is the tool to use