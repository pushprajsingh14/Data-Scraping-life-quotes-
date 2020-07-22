import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://www.goodreads.com/quotes/tag/{}?page={}"
# url of the website to get data from there

# this function get the data and makes it clear
def get_quotes(url):
    res = requests.get(url)

    soup = BeautifulSoup(res.text, features="html.parser")

    quote_divs = soup.find_all("div", attrs={"class": "quote"})

    quotes = []

    for quote_div in quote_divs:
        quoteText_div = quote_div.find_next("div", attrs={"class": "quoteText"})

        striped = quoteText_div.text.strip()

        striped_li = striped.split("\n")

        quote = striped_li[0][1:-1]
        author = striped_li[-1].strip()

        quote_item = {
            "text": quote,
            "author": author
        }

        quotes.append(quote_item)

    return quotes


total = []
for i in range(1, 10):
    total.extend(get_quotes(url.format("life", i)))

# converting into data frame
df = pd.DataFrame(total)

# converting data into csv file and storing as quotes_data.cs
df.to_csv("quotes_data.csv", index=None)