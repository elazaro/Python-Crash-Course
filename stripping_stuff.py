#!/usr/bin/env python3.9

# This example uses lstrip, rstrip and strip, still I think some questions may
# come up with it. for example, is there a built-in method to stripping multi-
# ple consecutive blank spaces at any possition on the string or we must always
# have to use a combination of methods, regex, maybe? how knows, let's discover
# it.

firstname = " augusta "
middlename = " ada "
lastname = " byron "

fullname = f"{firstname} {middlename} {lastname}"
print(f"'{fullname}'")
print(f"'{fullname.rstrip()}'")
print(f"'{fullname.lstrip()}'")
print(f"'{fullname.strip()}'\n")

# but this is not enough, we still have tripple spaces in between the words.

fullname = f"{firstname.lstrip()} {middlename.lstrip()} {lastname.lstrip()}"
print(f"'{fullname}'")
print(f"'{fullname.rstrip()}'")
print(f"'{fullname.lstrip()}'")
print(f"'{fullname.strip()}'\n")

# but this is not enough, we still have double spaces in between the words.

fullname = f"{firstname.lstrip().rstrip()} {middlename.lstrip().rstrip()} {lastname.lstrip().rstrip()}"
print(f"'{fullname}'")
print(f"'{fullname.rstrip()}'")
print(f"'{fullname.lstrip()}'")
print(f"'{fullname.strip()}'\n")

# much better but.... seriously, lstrip().rstrip()???? WTF!

fullname = f"{firstname.strip()} {middlename.strip()} {lastname.strip()}"
print(f"'{fullname}'")
print(f"'{fullname.rstrip()}'")
print(f"'{fullname.lstrip()}'")
print(f"'{fullname.strip()}'\n")

# now we are talking, but.... what about those rstrip() and ltrip() and strip()
# opperating on the fullname variable? can we get rid of them?

fullname = f"{firstname.strip()} {middlename.strip()} {lastname.strip()}"
print(f"'{fullname}'\n")

# Cool! Now let's use the title method to make Ada Lovelace's name as beauty
# as it is.

fullname = f"{firstname.strip()} {middlename.strip()} {lastname.strip()}"
print(f"'{fullname.title()}'\n")

