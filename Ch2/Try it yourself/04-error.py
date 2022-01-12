#!/usr/bin/env python3.9

# This wrong error shows up something interesting, it is not throwing an error,
# but printing the hex nature of the invoked method and the memory address of
# the object, this might be useful at some point.

personName = "edgar ricardo gonzález lázaro"
print(f"Hello, {personName.upper}, how are you?")
print(f"Hello, {personName.lower}, how are you?")
print(f"Hello, {personName.title}, how are you?")
