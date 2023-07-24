from bs4 import BeautifulSoup


def main():
    soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
    print(soup.prettify())


main()
