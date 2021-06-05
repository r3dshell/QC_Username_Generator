# Quebec Username Generator

## What

This script is used to generate a username list using the most common first and last names in Quebec in different formats. It can generate some passwords using specific patterns such as Tremblay2020.

It can also generate personas using a defined number of random French Canadian names.

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

To generate an email username list:
```
python3 main.py -u -d -o output_file
```

To generate a username lis:
```
python3 main.py -u -o output_file
```

To generate a password list:
```
python3 main.py -w -o output_file
```

To generate random personas:
```
python3 main.py -p -o output_file
```

---
## Help

```
usage: main.py [-h] (-u | -w | -p) [-d] [-o OUTPUT]

A username and wordlist generator for Quebec and French Canadian users.

optional arguments:
  -h, --help            show this help message and exit
  -u, --username        Generate a user list
  -w, --wordlist        Generate a password list
  -p, --persona         Generate a list of persona from random names
  -d, --domain          Generate a username list as emails
  -o OUTPUT, --output OUTPUT
                        Output file name (do not include extensions or path)
```

---
## Source

First names are coming from prenomsquebec.ca from the most popular first names from 1980 to 2020.

Last names are from the *most common family names from Québec* [wikipedia article](https://fr.wikipedia.org/wiki/Liste_des_noms_de_famille_les_plus_courants_au_Qu%C3%A9bec)


---
## Changelog

June 5, 2021
- Added persona generation
- Bug fixes

June 2, 2021
- Initial release

---
### DISCLAIMER

Usage of the wordlist for attacking targets without prior mutual consent is illegal. It's your responsibility to obey  applicable local, state and federal laws. 

I assume no liability and am not responsible for any misuse or damage caused by using this tool.
