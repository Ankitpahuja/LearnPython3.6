import re
def find(pattern, text):
  match = re.search(pattern,text)
  if match: print(match.group())
  else: print("Not found!")

# Main Program Executes
find("iig", "pig with 3 i's is called piiig")
find("..gs","called piiig")
find("x..g","called piiig much better: xyzgs")
find("..gs","called piiig much better: xyzgs")
find(r"c\.l","c.lled piiig much better: xyzgs")
find(r":\w\w\w","blah :cat blah blah blah")
find(r"\d\d\d","blah: 123xxx")
find(r"\d\s\d\s\d","blah: 1 2 3")
find(r"\d\s+\d\s+\d","blah: 1       2                   3")
find(r":\w+","blah blah :kitten blah blah") #Note: Space isn't a word character.
find(r":.+","blah blah :kitten123&abc blah blah")
find(r":\S+","blah blah :kitten123&abc&yata blah blah")
find(r"[\w.]@[\w.]", "blah nick.p@gmail.com blah blah")

find(r"([\w.])@([\w.])", "blah nick.p@gmail.com blah blah")
