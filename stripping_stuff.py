#!/usr/bin/env python3.9

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

