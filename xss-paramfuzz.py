from validator import ValidateURL
from fuzzer import Fuzz
import pyfiglet
from colorama import *
init(autoreset=True)

# COLOR VARIABLES:
reset = Fore.RESET
red = Fore.RED
yellow = Fore.YELLOW
green = Fore.GREEN
magenta = Fore.MAGENTA


def banner():
    ascii_banner = pyfiglet.figlet_format("XSS-ParamFUZZ")
    print(red + ascii_banner)


def instructions():
    print("-" * 70)
    print(yellow + "[+] Fuzz Usage:")
    print('\t[-] Replace the value in the URL for the parameter you wish to \n\t\t'
          'fuzz with the keyword, "FUZZ".')
    print("\n\t\tEx: https://xss-game.appspot.com/level1/frame?query=FUZZ")
    print("\t\tEx: http://sudo.co.il/xss/level1.php?email=FUZZ#")


class Preparation:
    def __init__(self, cookie=None):
        self.url = input("\nEnter a URL to FUZZ: ")
        self.cookie = cookie
        self.payloads = []

    def validate(self):
        ValidateURL(self.url)

    def add_cookie(self):
        print(yellow + "\n[+] You may add a cookie, if necessary:")
        print(green + '\tEx: cookiename:cookievalue:cookiepath')
        self.cookie = input("Enter a cookie string or press ENTER to skip: ")
        if len(self.cookie) == 0:
            pass
        else:
            try:
                parse_cookie = self.cookie.split(':')
                self.cookie = {
                    'name': parse_cookie[0],
                    'value': parse_cookie[1],
                    'path': parse_cookie[2]
                }
            except:
                print(red + "invalid cookie entered")
                self.cookie = None
                self.add_cookie()

    def add_payload(self):
        self.payloads = input(yellow + "\n[+] Enter a path to a custom wordlist or press ENTER to skip: ")

    def fuzz(self):
        Fuzz(self.url, self.cookie, self.payloads)


banner()
instructions()

Prep = Preparation()
Prep.validate()
Prep.add_cookie()
Prep.add_payload()
Prep.fuzz()
