#Vowel or constant
#author name:Al- Ekram Hossain ABir
import string
vowel='aeiouAEIOU'
char='A'
if char not in string.ascii_letters:
    print("NOT VAlid")
elif char in vowel:
    print("Vowel")
else:
    print("Consonent")
