# Ziel: Bei einem Tag die Spiele rausfinden, und den Namen, Likes
# Tags etc scrapen
# Steam speichert 
import requests
from beautifulsoup4 import BeautifulSoup


steam_url = f'https://store.steampowered.com/search/?tags=492'

def main():
    start = 0
    # get the get url by scrolling and inspecting network and xhr
    # runs till end of entries (infinity)
    url = f'https://store.steampowered.com/search/results/?query=&start={start}&count=100&d&tags=492&&infinite=1'




if __name__ == '__main__': 
    
    main()