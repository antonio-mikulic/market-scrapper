from win10toast import ToastNotifier
from conf import INTERVAL_MINUTES, SEND_WIN_NOTIFICATION
from njuskalo_scraper.database import NjuskaloAdDB
from typing import List


def parse_urls_file(path):
    return [url.strip() for url in open(path) if url]


class Notifier:
    def __init__(self):
        self.toast = ToastNotifier()

    def new_items_received(self, items):
        if(not SEND_WIN_NOTIFICATION): 
            return
        
        cheap = min(items, key=lambda x: x.price)
        expensive = max(items, key=lambda x: x.price)
        avgPrice = sum([int(i.price) for i in items]) / len(items)

        self.toast.show_toast(
            f"{len(items)} new items appeared in last {INTERVAL_MINUTES} minutes",
            f"Cheapest: {cheap.price}\nMost expensive: {expensive.price}\nAverage: {avgPrice}",
            duration=30)
