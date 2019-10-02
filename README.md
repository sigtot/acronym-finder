# Acronym Finder

## Usage
Assuming you have a file named `inputfile.txt` containing a single unique word for each line:

`./acronyms.py inputfile.txt`

All words that have acronyms will be printed to stdout along with their acronyms, e.g.
```
bra, bar
dro, ord, rod
løst, støl
...
```

## Performance analysis
```bash
time for i in {1..10}; do ./acronyms.py /usr/share/dict/words > /dev/null; done

real    0m3.739s
user    0m3.580s
sys     0m0.128s
```
