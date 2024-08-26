On [[Linux]], you can find config files for Firefox in `~/.mozilla/firefox/` or for Chrome in `~/.config/google-chrome/`
Therefore, this [[find]] command is useful:
```sh
sudo find /home -type d \( -path "*/.mozilla/firefox" -o -path "*/.config/google-chrome" \) 2>/dev/null
```

You can then use [Dumpzilla](https://www.dumpzilla.org/) to pull information from Firefox config files
```sh
sudo python3 /home/investigator/dumpzilla.py /home/eduardo/.mozilla/firefox/niijyovp.default-release --Summary --Verbosity CRITICAL
```
That is an example of a profile file. If it has just `.default`, you can usually ignore it since it's a template.
`--Help` is really handy for finding your options while running dumpzilla