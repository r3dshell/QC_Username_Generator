#!/usr/bin/python3

import argparse
import os

parser = argparse.ArgumentParser(description='A username and wordlist generator for Quebec specific users.')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-u', '--username', action='store_true', help='Generate a user list')
group.add_argument('-w', '--wordlist', action='store_true', help='Generate a password list')
group2 = parser.add_mutually_exclusive_group(required=True)
group2.add_argument('-m', '--male', action='store_true', help='Include only male first names')
group2.add_argument('-f', '--female', action='store_true', help='Include only female first names')
group2.add_argument('-b', '--both', action='store_true', help='Include both male and female first names')
group3 = parser.add_mutually_exclusive_group(required=False)
group3.add_argument('-d', '--domain', action='store_true', help='Generate a username list as emails')
parser.add_argument('-o', '--output', help='Output file name (do not include extensions or path)', required=True)
args = parser.parse_args()
email = ""

if args.male:
    first_male = open("./source/william.txt", "r")
    fname = first_male.read()
if args.female:
    first_female = open("./source/olivia.txt", "r")
    fname = first_female.read()
if args.both:
    first_male = open("./source/william.txt", "r")
    first_female = open("./source/olivia.txt", "r")
    fname = first_male.read() + first_female.read()
if args.wordlist:
    year_doc = open("./source/years.txt", "r")
    years = year_doc.read()

last_name = open("./source/tremblay.txt", "r")
lname = last_name.read()

print("")
a = open("banner.txt","r")
print(a.read())
a.close()
print("Version: 1.0 - June 2, 2021")
print("Author: @r3dshell")
print("")

if args.domain:
    print("")
    email = input("[*] Enter the domain name (example.com)\n")
    print("")

if args.username:
    print("")
    format = input("[*] Select the format for the username generation (first,last,first.last,first_last,flast,lastf,firstl,lfirst,firstlast,lastfirst): \n")
    print("")

    if format == 'first':
        user = '{}'.format(fname)
        file = open("tmp.txt", "w")
        if email:
            for lines in user.splitlines():
                file.write(lines.lower() + "@" + email + '\n')
        else:
            file.write(user.lower())

    if format == 'last':
        user = '{}'.format(lname)
        file = open("tmp.txt", "w")
        if email:
            for lines in user.splitlines():
                file.write(lines.lower() + "@" + email + '\n')
        else:
            file.write(user.lower())

    if format == 'first.last':
        file = open("tmp.txt", "w")
        if email:
            for lines in fname.splitlines():
                for lines2 in lname.splitlines():
                    file.write(lines.lower() + "." + lines2.lower() + "@" + email + '\n')
        else:
            for lines in fname.splitlines():
                for lines2 in lname.splitlines():
                    file.write(lines.lower() + "." + lines2.lower() + '\n')

    if format == 'first_last':
        file = open("tmp.txt", "w")
        if email:
            for lines in fname.splitlines():
                for lines2 in lname.splitlines():
                    file.write(lines.lower() + "_" + lines2.lower() + "@" + email + '\n')
        else:
            for lines in fname.splitlines():
                for lines2 in lname.splitlines():
                    file.write(lines.lower() + "_" + lines2.lower() + '\n')

    if format == 'flast':
        file = open("tmp.txt", "w")
        if email:
            for lines in fname.splitlines():
                for lines2 in lname.splitlines():
                    file.write(lines[0].lower()+lines2.lower()+"@"+email+'\n')
        else:
            for lines in fname.splitlines():
                for lines2 in lname.splitlines():
                    file.write(lines[0].lower()+lines2.lower()+'\n')

    if format == 'lastf':
        file = open("tmp.txt", "w")
        if email:
            for lines in fname.splitlines():
                for lines2 in lname.splitlines():
                    file.write(lines2.lower() + lines[0].lower() + "@" + email + '\n')
        else:
            for lines in fname.splitlines():
                for lines2 in lname.splitlines():
                    file.write(lines2.lower()+lines[0].lower()+'\n')

    if format == 'firstl':
        file = open("tmp.txt", "w")
        if email:
            for lines in fname.splitlines():
                for lines2 in lname.splitlines():
                    file.write(lines.lower()+lines2[0].lower()+'\n')
        else:
            for lines in fname.splitlines():
                for lines2 in lname.splitlines():
                    file.write(lines.lower() + lines2[0].lower() + '\n')

    if format == 'lfirst':
        file = open("tmp.txt", "w")
        if email:
            for lines in fname.splitlines():
                for lines2 in lname.splitlines():
                    file.write(lines2[0].lower()+lines.lower()+'\n')
        else:
            for lines in fname.splitlines():
                for lines2 in lname.splitlines():
                    file.write(lines2[0].lower() + lines.lower() + '\n')

    if format == 'firstlast':
        file = open("tmp.txt", "w")
        if email:
            for lines in fname.splitlines():
                for lines2 in lname.splitlines():
                    file.write(lines.lower() + lines2.lower() + '\n')
        else:
            for lines in fname.splitlines():
                for lines2 in lname.splitlines():
                    file.write(lines.lower() + lines2.lower() + '\n')

    if format == 'lastfirst':
        file = open("tmp.txt", "w")
        if email:
            for lines in fname.splitlines():
                for lines2 in lname.splitlines():
                    file.write(lines2.lower() + lines.lower() + '\n')
        else:
            for lines in fname.splitlines():
                for lines2 in lname.splitlines():
                    file.write(lines2.lower() + lines.lower() + '\n')

if args.wordlist:
    print("")
    format = input("[*] Select the format for the password list generation (first+year, last+year, First+year, Last+year): \n")

    if format == 'first+year':
        file = open("tmp.txt", "w")
        for lines in fname.splitlines():
            for lines2 in years.splitlines():
                file.write(lines.lower() + lines2 + '\n')

    if format == 'last+year':
        file = open("tmp.txt", "w")
        for lines in lname.splitlines():
            for lines2 in years.splitlines():
                file.write(lines.lower() + lines2 + '\n')

    if format == 'First+year':
        file = open("tmp.txt", "w")
        for lines in fname.splitlines():
            for lines2 in years.splitlines():
                file.write(lines.lower().capitalize() + lines2 + '\n')

    if format == 'Last+year':
        file = open("tmp.txt", "w")
        for lines in lname.splitlines():
            for lines2 in years.splitlines():
                file.write(lines.lower().capitalize() + lines2 + '\n')

# Duplicate removal
content = open("tmp.txt",'r').readlines()
content_set = set(content)
cleandata = open('./'+args.output+'.txt','w')
for line in content_set:
        cleandata.write(line)
os.remove("tmp.txt")