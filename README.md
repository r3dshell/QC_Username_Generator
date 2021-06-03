# Quebec Username Generator

## What

This script is used to generate a username list using the most common first and last names in Quebec in different formats. It can also generate some passwords using specific patterns such as Tremblay2020.

The following patterns are supported for usernames:
* first
* last
* first.last
* first_last
* flast
* lastf
* firstl
* lfirst
* firstlast
* lastfirst

The following patterns are supported for passwords:

* first+year
* last+year
* First+year (capital first letter)
* Last+year (capital first letter)

---
## How it works

A few examples:

To generate an email username list, using both male and female first names:
```
python3 main.py --username --both --domain --output example
```

To generate a username list, using both male and female first names:
```
python3 main.py --username --both --output example
```

To generate a password list, using male first names:
```
python3 main.py -wmo example
```
---
## Help

```
usage: main.py [-h] (-u | -w) (-m | -f | -b) [-d] -o OUTPUT

A username and wordlist generator for Quebec specific users.

optional arguments:
  -h, --help            show this help message and exit
  -u, --username        Generate a user list
  -w, --wordlist        Generate a password list
  -m, --male            Include only male first names
  -f, --female          Include only female first names
  -b, --both            Include both male and female first names
  -d, --domain          Generate a username list as emails
  -o OUTPUT, --output OUTPUT
                        Output file name (do not include extensions or path)
```

---
## Source

First names are coming from prenomsquebec.ca from the most popular first names from 1980 to 2020.

Last names are from the *most common family names from Québec* [wikipedia article](https://fr.wikipedia.org/wiki/Liste_des_noms_de_famille_les_plus_courants_au_Qu%C3%A9bec)

---
### DISCLAIMER

Usage of the wordlist for attacking targets without prior mutual consent is illegal. It's your responsibility to obey  applicable local, state and federal laws. 

I assume no liability and am not responsible for any misuse or damage caused by using this tool.
