import feedparser
import webbrowser
#? run with python 3.6 interpreter

def main():
    print("--Security News Website List--")
    print("[0]: TheHackerNews")
    print("[1]: ThreatPost")
    print("[2]: NakedSecurity")
    print("[3]: Scmagazine")
    print("[4]: Threatpost")
    

    website_list = ("https://feeds.feedburner.com/TheHackersNews", "https://threatpost.com/feed", "https://nakedsecurity.sophos.com/feed", "https://www.scmagazine.com/home/feed", "https://threatpost.com/feed")

    website_input = int(input("Enter website by number (0-3): "))

    n = int(input("Enter how many article you want to see: "))
    NewsFeed = feedparser.parse(website_list[website_input])
    article_list = []
    article_link = []
    for i in range(n):
        article = NewsFeed.entries[i]
        titles = article.title
        link = article.link
        article_link.append(link)
        article_list.append(titles)

    article_num = 1
    for article in article_list:
        print('[{}] {}'.format(str(article_num), article))
        article_num += 1

    article_link_click = False
    while not article_link_click:
        user_choice = int(input(f"Choose the link you want to open (1-{n}): "))
        webbrowser.open(article_link[user_choice-1])
        article_link_click = True

main()
