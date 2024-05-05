from searcher import *
from cloudleaker import *


def main():
    searcher = Searcher()
    base = CloudLeaker()
    searcher.search("night drive",1)

if __name__ == "__main__":
    main()
