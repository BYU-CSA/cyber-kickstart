In Android studio you can load a compiled apk in:
When given a .apk file, you can reverse it by opening it in Android Studio using the three dots at the right when you open Android Studio and the Profile or Debug APK option

Once you're there, typically files will be stored under Java > com > name_of_producer. So for the vilo application, you can find them in com.viloliving. You can also look at the AndroidManifest.xml file for further hints about how the application works and which files it relies on to run

You turn on debug mode by clicking Settings > System > About > Build 7 times, then you can go into dev settings and enable usb debugging to get cmd to interface it by default