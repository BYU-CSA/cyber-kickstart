look up `dd`
Mounting a disk image:
```sh
sudo losetup -fP disk.flag.img # finds / creates the device for the disk image
sudo losetup -a # lists it
sudo mkdir /mnt/disk_image
lsblk # lists all loop devices, which will show you all partitions of that disk that now is linked to devices
sudo mount /dev/loop0p3 /mnt/disk_image
```
With any given file, you can run `file` on it. Make sure you run `-a` with `ls` so you don't miss files in a disk image

### Registry and Hives
Find your hives in C:\\Windows\\System32\\config

Interesting and useful ones: 

C:\\Users\\Macen\\AppData

With the SAM hive loaded, go to the ROOT\\SAM\\Domains\\Account\\Users folder

In the SYSTEM hive, document the following values of interest:
- SYSTEM\\\[CurrentControlSetFolder]\\Control\\ComputerName\\ComputerName\\Data
- SYSTEM\\\[CurrentControlSetFolder]\\Control\\TimeZoneInformation\\TimeZoneKeyName
- SYSTEM\\\[CurrentControlSetFolder]\\Control\\Windows\\ShutdownTime
- SYSTEM\\\[CurrentControlSetFolder]\\Services\\Tcpip\\Parameters\\InTerfaces\\DHCPDomain
- SYSTEM\\\[CurrentControlSet]\\Services\\Tcpip\\Parameters\\Interfaces

Document the following SOFTWARE hive values:
- SOFTWARE\\Microsoft\\Windows NT\\Current Version\\ProductName
- SOFTWARE\\Microsoft\\Windows NT\\Current Version\\ReleaseID
- SOFTWARE\\Microsoft\\Windows NT\\Current Version\\CurrentBuild
- SOFTWARE\\Microsoft\\Windows NT\\Current Version\\InstallDate (interpret it)
- SOFTWARE\\Microsoft\\Windows NT\\Current Version\\RegisteredOwner
- SOFTWARE\\Microsoft\\Windows NT\\Current Version\\NetworkList (make sure you’re looking at the “Known networks” tab)…document the Network Name, Name Type, First Connect LOCAL and Last Connected LOCAL times

Document the following NTUSER.DAT hive values:
- NTUSER.DAT\\Software\\Microsoft\\Windows\\Currentversion\\Explorer\\UserAssist\
	- Shows recently launched applications
- NTUSER.DAT\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\WordWheelQuery
	- This is a record of any search terms that have been typed in the desktop “Search” field. If there is not a folder, it is likely the desktop Search hasn’t been used.
- NTUSER.DAT\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\TypedPaths
	- This shows any queries typed into Windows Explorer’s built-in “Search” field
- NTUSER.DAT\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\RecentDocs
	- This shows all the recent documents, and the order in which they were opened (via the MRU key).  Which document was most recently opened?
- Validate the info above by looking at the
NTUSER.DAT\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\ComDlg32\\OpenSavePidlMRU values.  What information is available here that wasn’t available in the RecentDocs values?