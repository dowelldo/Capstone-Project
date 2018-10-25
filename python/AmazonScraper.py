# This class handles the scraping for youtube comments.

import Interpreter


class AmazonScraper:
    @staticmethod
    def scrape(url):
        html_soup = Interpreter.getRequest(url)
        comment_containers = html_soup.find_all('div', class_='a-row a-spacing-small review-data')
        return comment_containers
