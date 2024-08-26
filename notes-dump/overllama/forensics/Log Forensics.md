
- `/var/log/` : `messages`, `syslog`, `dmesg`, `auth.log`, `secure`, `boot.log`
- `grep`/`cat`/`sed`/`awk`/`jq`/`ccze`
- Angle-grinder
- Logfile Navigator

`grep` is a classic, and the syntax is grep {searchparam} {file}

`cut` is also a classic. Cut can be used to read files by slicing them into pieces and only taking what you want.
```
-d : delimiter
-f[num] : which slice
```
So running cut on a file with strings formatted: `[2023/10/25:16:17:14] 10.10.140.96 storage.live.com:443 GET / 400 630 "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"` will let you see just what you want.
`cut -d ' ' -f1 access.log` will output only strings matching `[2023/10/25:15:42:02]` 
whereas `cut -d ' ' -f1,3,6 access.log` will output strings matching `[2023/10/25:15:42:02] sway.com:443 200` since it's taking the first, third, and sixth pieces

`sort` is great cuz it'll sort output piped to it, and `uniq` will filter out any with repeats when handed a sorted list
`uniq -c` will also show you the count for each option and `sort -n` will let you sort by numeric value.
So piping a `cut` to `sort` then `uniq` then `sort` again will give you a really nice list

`wc -l` will count your lines for you
`base64 -d` will command line decode base64 for you

`xxd` has a `-r` option which will go from hex dump to binary data
`gzip -d` will decompress

`awk` is a really valuable command line tool, and I have no idea how to use it. I'll look into it later