import random
import time
import webbrowser

TermToSearch="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
BaseSearchURL="https://www.bing.com/search?q="

while TermToSearch:
    TermToSearch = TermToSearch[:-1]
    #print(TermToSearch)
    Wait=random.randint(6,8)
    time.sleep(Wait) 
    webbrowser.open(BaseSearchURL+TermToSearch)

