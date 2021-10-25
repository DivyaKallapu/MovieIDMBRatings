from bs4 import BeautifulSoup
import requests


class GetRating():
    def __init__(self, title):
        """
        Constructor of the class
        :type title: str
        :param title: Movie name
        """
        self.title = title

    def get_rating(self):
        # Setting up session
        s = requests.session()
        for i in range(1):
            url = "https://www.imdb.com/search/title/?title=" + self.title
            print(url)
            try:
                response = s.get(url)
                # parse the content using beautifulsoup
                soup = BeautifulSoup(response.content, features="html.parser")
                # searching all films containers found
                containers = soup.find_all("div", class_="lister-item-content")
                # only checking the top search
                rating = containers[0].find("div", class_="inline-block ratings-imdb-rating")["data-value"]
                return rating

            except Exception:
                print("Try again with valid combination of tile and release year")
