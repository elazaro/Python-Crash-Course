#!/usr/bin/env python3.9

# One very very very very common use case is to take several variables an make
# them a single one representing a real life object, like a person full name.
# how would Ada Lovelace sign her letters? 


# something interesting is that different to other scriptiong languages, varia-
# bles are not preceded by weird characters like $ or % or &.

firstname = "AuGusTa";
middlename = "aDa";
lastname = "byroN";

fullname = f"{firstname} {middlename} {lastname}";

print(fullname);

print(f"Hello, {fullname}.");
print(f"Hello, {fullname}.\n");
print(f"Hello, {fullname.title()}.\n");

# What's interesting here is how the "f" f-string feature of Python, this oper-
# ator, allows us to format a string, I still have question about this 
# for example: 
# - How simylar it this to printf C/C++ function.
# - Do a f-string allows control sequences like padding or number formating?



