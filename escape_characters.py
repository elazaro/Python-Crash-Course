#!/usr/bin/env python3.9

# this is obviously not the best way to handle a list, but the purpose is 
# showing how standard escape characters \n \t can be used to format a string
# that at first glance looks like a long non sense sequence of crap.
# don't readme wrong these people is the best of the best and it is only my 
# favourite people.

people = "\talan turing\n\tada lovelace\n\tmargaret hamilton\n\tdonald knuth\n\tdenis ritchie\n\tstephen wolfram\n\tFrances Northcutt"

print(f"Computing people:\n {people.title()}")

