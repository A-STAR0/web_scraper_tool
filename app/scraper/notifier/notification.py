
class Notifier:
    def __init__(self):
        pass

    @staticmethod
    def notify_scraping_summary(num_scraped, num_updated):
        print(f"Scraped {num_scraped} products and updated {num_updated}in DB.")
