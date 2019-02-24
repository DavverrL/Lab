from bs4 import BeautifulSoup
import requests



def extract_news(parser):
    """ Extract news from a given web page """
    news_list = []
    i = 0

    table_parser = parser.find_all('table')[2]
    title_urls = table_parser.findAll('td', class_='subtext')

    for title_url in title_urls:
        posts = {}
        name = parser.findAll('a', class_='hnuser')
        points = parser.findAll('span', class_='score')
        comments = title_url.findAll('a')[-1].text[0]
        title = parser.findAll('a', class_="storylink")
        if comments == 'd':
            comments = '0'
        posts['author'] = name[i].text + '\n'
        posts['points'] = int(points[i].text[0])
        posts['comments'] = int(comments)
        posts['title'] = title[i].text
        posts['url'] = title[i].get('href')

        i += 1

        news_list.append(posts)

    return news_list


def extract_next_page(parser):
    """ Extract next page URL """
    next_page = parser.find('a', class_='morelink').get('href')

    return next_page


def get_news(url, n_pages=1):
    """ Collect news from a given web page """
    news = []
    while n_pages:
        print("Collecting data from page: {}".format(url))
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        news_list = extract_news(soup)
        next_page = extract_next_page(soup)
        url = "https://news.ycombinator.com/" + next_page
        news.extend(news_list)
        n_pages -= 1
    return news