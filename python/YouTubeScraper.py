# This class handles the scraping for youtube comments.

import Interpreter


class YouTubeScraper:
    def scrape(self, url):
        html_soup = Interpreter.getRequest(url)
        return "Youtube support coming soon."
