from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
articles= soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
for article_tag in articles:
    article_text = article_tag.text
    article_texts.append(article_text)
    article_link = article_tag.get("href")
    article_links.append(article_link)

# article_votes = []
# article_scores = soup.find_all(name="span", class_="score")
# print(article_scores)
# for article_score in article_scores:
#     article_vote = article_score.text
#     article_votes.append(article_vote)

article_votes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(article_votes)
largest_number = max(article_votes)
print(largest_number)
article_index = article_votes.index(largest_number)
print(article_links[article_index + 1])
print(article_texts[article_index + 1])

