import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

BASIC_URL = "https://books.toscrape.com/"

rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

books_data = []

for page in range(1, 6):

    if page == 1:
        url = BASIC_URL
    else:
        url = f"{BASIC_URL}catalogue/page-{page}.html"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    books = soup.select("article.product_pod h3 a")

    for book in books:

        href = book["href"]
        link = urljoin(url, str(href))

        book_response = requests.get(link)
        book_soup = BeautifulSoup(
            book_response.content,
            "html.parser"
        )

        title = book_soup.find("h1").text.strip()

        rating_text = (
            book_soup.find(
                "p",
                class_="star-rating"
            )["class"][1]
        )

        rating = rating_map[rating_text]

        breadcrumb = book_soup.select(
            "ul.breadcrumb li a"
        )

        genre = breadcrumb[2].text.strip()

        table = book_soup.find(
            "table",
            class_="table table-striped"
        )

        product_info = {}

        for row in table.find_all("tr"):
            key = row.find("th").text.strip()
            value = row.find("td").text.strip()

            product_info[key] = value

        upc = product_info["UPC"]

        price = float(
            product_info["Price (excl. tax)"]
            .replace("£", "")
            .replace("Â", "")
        )

        availability = product_info["Availability"]
        match = re.search(r"\d+", availability)

        availability = int(match.group())

        books_data.append({
            "title": title,
            "genre": genre,
            "rating": rating,
            "upc": upc,
            "price": price,
            "availability": availability
        })

df = pd.DataFrame(books_data)

df.to_csv("books.csv", index=False)

print(df.head())
print(f"\nTotal books scraped: {len(df)}")