#!/usr/bin/python3

import argparse
import random

parser = argparse.ArgumentParser(description='A username and wordlist generator for Quebec and French Canadian users.')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-u', '--username', action='store_true', help='Generate a user list')
group.add_argument('-w', '--wordlist', action='store_true', help='Generate a password list')
group.add_argument('-p', '--persona', action='store_true', help='Generate a list of persona from random names')
group3 = parser.add_mutually_exclusive_group(required=False)
group3.add_argument('-d', '--domain', action='store_true', help='Generate a username list as emails')
parser.add_argument('-o', '--output', help='Output file name (do not include extensions or path)', action='store')
args = parser.parse_args()

lnames_file = open("source/tremblay.txt", "r")
lnames = lnames_file.read()

male_file = open("source/william.txt", "r")
mnames = male_file.read()

f_file = open("source/olivia.txt", "r")
fnames = f_file.read()

bnames = fnames + mnames

email = ""
begin_year = 1900  ##update if needed
end_year = 2023  ##update if needed

print("")
a = open("banner.txt", "r", encoding="utf-8")
print(a.read())
a.close()
print("Version: 1.1 - June 5, 2021")
print("Author: @r3dshell, @d33ds")
print("")

if args.domain:
    print("")
    email = input("[*] Enter the domain name (example.com)\n")
    print("")


def print_names(format):
    res = []
    if format == 2:  # Last
        for l in lnames.splitlines():
            res.append((l).lower())
    else:
        gen_ans = input("[*] Would you like to only use F or M names? (Y/N) : ")
        if gen_ans.upper() == 'Y':
            gen_q = input("[+] (M)ale or (F)emale? : ")
            if gen_q.upper() == 'M':
                firstN = mnames
            elif gen_q.upper() == 'F':
                firstN = fnames
            else:
                firstN = bnames
        else:
            firstN = bnames
        if format == 1:  # First
            for f in firstN.splitlines():
                res.append((f).lower())
        elif format == 3:  # Firstname.Lastname
            for f in firstN.splitlines():
                for l in lnames.splitlines():
                    res.append((f + '.' + l).lower())
        elif format == 4:  # Firstname_Lastname
            for f in firstN.splitlines():
                for l in lnames.splitlines():
                    res.append((f + '_' + l).lower())
        elif format == 5:  # FLastname
            for f in firstN.splitlines():
                for l in lnames.splitlines():
                    res.append((f[0] + l).lower())
        elif format == 6:  # LastnameF
            for f in firstN.splitlines():
                for l in lnames.splitlines():
                    res.append((l + f[0]).lower())
        elif format == 7:  # FirstnameL
            for f in firstN.splitlines():
                for l in lnames.splitlines():
                    res.append((f + l[0]).lower())
        elif format == 8:  # LFirstname
            for f in firstN.splitlines():
                for l in lnames.splitlines():
                    res.append((l[0] + f).lower())
        elif format == 9:  # FirstnameLastName
            for f in firstN.splitlines():
                for l in lnames.splitlines():
                    res.append((f + l).lower())
        elif format == 10:  # LastnameFirstname
            for f in firstN.splitlines():
                for l in lnames.splitlines():
                    res.append((l + f).lower())
        else:
            print('[X] Error')
    if args.domain:
        d_res = []
        for entry in res:
            d_res.append(entry + '@' + email)
        return d_res
    else:
        return res


def print_wordlist(format):
    res = []
    if format == 2:  # lastYYYY
        for l in lnames.splitlines():
            for y in range(begin_year, end_year):
                res.append((l).lower() + str(y))
    elif format == 4:  # LastYYYY
        for l in lnames.splitlines():
            for y in range(begin_year, end_year):
                res.append((l).lower().capitalize() + str(y))
    else:
        gen_ans = input("Would you like to only use F or M names? (Y/N) : ")
        if gen_ans.upper() == 'Y':
            gen_q = input("[+] (M)ale or (F)emale? : ")
            if gen_q.upper() == 'M':
                firstN = mnames
            elif gen_q.upper() == 'F':
                firstN = fnames
            else:
                firstN = bnames
        else:
            firstN = bnames
        if format == 1:  # firstYYYY
            for f in firstN.splitlines():
                for y in range(begin_year, end_year):
                    res.append((f).lower() + str(y))
        elif format == 3:  # FirstYYYY
            for f in firstN.splitlines():
                for y in range(begin_year, end_year):
                    res.append((f).lower().capitalize() + str(y))
        else:
            print('[X] Error')
    bang = input("Do you want to add a ! at the end? (Y/N) : ")
    if bang.upper() == 'Y':
        new_res = []
        for entry in res:
            new_res.append(entry + '!')
        return new_res
    else:
        return res

def print_persona(format):
    res = []
    gen = input("Would you like to only use F or M names? (Y/N) : ")
    if gen.upper() == 'Y':
        gen_q = input("[+] (M)ale or (F)emale? : ")
        if gen_q.upper() == 'M':
            firstN = mnames
        elif gen_q.upper() == 'F':
            firstN = fnames
        else:
            firstN = bnames
    else:
        firstN = bnames
    for i in range(format):
        res.append(random.choice(firstN.splitlines()).lower().capitalize().title()+" "+random.choice(lnames.splitlines()).lower().capitalize().title())
    return res

if args.persona:
    print("")
    format = int(input("[*] How many persona do you want?: "))
    print("")
    data = print_persona(format)

if args.username:
    print("")
    print("Example: Jean Tremblay")
    print("[1] Firstname : jean")
    print("[2] Lastname : tremblay")
    print("[3] Firstname.Lastname : jean.tremblay")
    print("[4] Firstname_Lastname : jean_tremblay")
    print("[5] FLastname : jtremblay")
    print("[6] LastnameF : tremblayj")
    print("[7] FirstnameL : jeant")
    print("[8] LFirstname : tjean")
    print("[9] FirstnameLastName : jeantremblay")
    print("[10] LastnameFirstname : tremblayjean")
    format = int(input("[*] Select the format for the username generation: "))
    print("")
    data = print_names(format)

if args.wordlist:
    print("")
    print("Example: Jean Tremblay")
    print("[1] firstname+Year : jean1970")
    print("[2] lastname+Year : tremblay1970")
    print("[3] Firstname+Year : Jean1970")
    print("[4] Lastname+Year : Tremblay1970")
    format = int(input("[*] Select the format for the password list generation :"))
    print("")
    data = print_wordlist(format)

data = list(dict.fromkeys(data))

if args.output:
    with open('./' + args.output + '.txt', mode='w', encoding='utf-8') as file:
        file.write('\n'.join(data))
else:
    print("")
    for thing in data:
        print(thing)
    print('\n')
