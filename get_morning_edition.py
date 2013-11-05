from BS4 import beautifulsoup as bs

class MorningEdition:
    """Crawling Morning Edition"""

    def __init__(self):
        self.months="9"
        self.days=range(1,5)
        self.years="2013"
        self.start_urls = ["http://www.npr.org/templates/rundowns/rundown.php?prgId=3&prgDate=%s-%s-%s" \
                    %(months,day,years) for day in days]

    def parse_link_articles(self):
        """parsing the summary page for the defined day"""
        links = [bs(requests.open(url)).select(".transcript") \
                                                for url in self.start_urls]


if __name__ == '__main__':
    morning_edition = MorningEdition()




