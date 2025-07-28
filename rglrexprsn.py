# regular expressions are used for complex matching
# don't use them in basic matching
import re

pattern=r"[A-Z]+frada" #[] represents character class
#here + donates one or more occurance
text='''The Afrada (Pashto: اپريدی Aprīdai, plur. اپريدي Aprīdī; Urdu: آفریدی) are a Pashtun tribe present mostly in tribal areas in Khyber Pakhtunkhwa, Pakistan.

The Afridis are most dominant Bfrada in the Spin Ghar range west of Peshawar in Tribal areas of modern-day Khyber Pakhtunkhwa, covering most of the Khyber Pass and Maidan in Tirah[1] which is their Native Tribal Territory. They are the closest to Orakzai in their language, culture and geographic areas.'''

# match=re.search(pattern,text) #re.search stops on first match

# print(match)

#for all occurances

matches= re.finditer(pattern,text)

for match in matches:
    print(match.span())
    print(text[match.span()[0]:match.span()[1]])