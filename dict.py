import sys
import re
from DictionaryServices import DCSCopyTextDefinition

# ASNI code
PURPLE = "\033[95m"
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
ENDC = "\033[0m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"


exit = False


def main():
    searchword = input(BOLD + "Enter word: ")
    getWord(searchword)
    print("\n\n")


def getWord(searchword: str):
    if searchword == "_exit":
        sys.exit()
    wordrange = (0, len(searchword))
    result = DCSCopyTextDefinition(None, searchword, wordrange)
    if not result:
        print("{} not found in Dictionary.".format(searchword))
    else:
        # result = re.sub(r"\|(.+?)\|", PURPLE + r"/\1/" + ENDC, result)
        result = re.sub(r"(?<!\d)(\d)(?!\d)\s", "\n " + BOLD + r"\1: " + ENDC, result)
        result = re.sub(r"▶", "\n\n " + RED + "▶ " + ENDC, result)
        result = re.sub(r"• ", "\n   " + GREEN + "• " + ENDC, result)
        result = re.sub(r"(‘|“)(.+?)(’|”)", YELLOW + r"“\2”" + ENDC, result)
        # result = re.sub(r"PHRASES", "\n\n" + YELLOW + "PHRASES" + ENDC, result)
        # result = re.sub(r"DERIVATIVES", "\n\n" + YELLOW + "DERIVATIVES" + ENDC, result)
        # result = re.sub(r"ORIGIN", "\n\n" + YELLOW + "ORIGIN" + ENDC, result)
        print(result)


def greeting():
    print("ehllo")
    print("hi")


if __name__ == "__main__":
    while not exit:
        main()
