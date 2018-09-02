import unittest
from .models import news
News = news.News

class MovieTest(unittest.Testcase):
	def setup(self):
		self.new_news = News("abc-news","ABC News","Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.",
			 "http://abcnews.go.com","general","en","au")

	def test_instance(self):
		self.assertTRue(isinstance(self.new_news,News))

if __name__ == '__main__':
	unittest.main()