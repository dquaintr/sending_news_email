import requests
from pprint import pprint

class NewsFeed:
    """Representing multiple news titles and links as a single string"""

    base_url = "https://newsapi.org/v2/everything?"
    api_key ="890603a55bfa47048e4490069ebee18c"

    def __init__(self, interest, from_date, to_date,language):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        url = self._build_url()

        articles = self._get_articles(url)
        # pprint(articles)

        email_body = ""
        for article in articles:
            email_body = email_body + article['title'] + "\n " + article['url'] + "\n\n"

        if email_body == "":
            return("Sadly there is no news for your topic in the selected timeframe and language.")
        else:
            return(email_body)

    def _get_articles(self, url):
        response = requests.get(url)
        content = response.json()
        articles = content['articles']
        return articles

    def _build_url(self):
        url = f"{self.base_url}" \
              f"qInTitle={self.interest}" \
              f"&from={self.from_date}&" \
              f"to={self.to_date}&" \
              f"language={self.language}&" \
              f"apiKey={self.api_key}"
        return url


if __name__ == "__main__":

    news_feed = NewsFeed(interest='philosophy', from_date="2024-3-26", to_date="2024-3-27",language="en")

    print(news_feed.get())
