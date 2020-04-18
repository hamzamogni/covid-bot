import urllib.request as ul
from bs4 import BeautifulSoup
from textblob import TextBlob


class Crawler():
	def __init__(self):
		self.http_headers = {
	        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 '
	                      'Safari/537.11',
	        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
	        'Accept-Encoding': 'none',
	        'ALanguage': 'en-US,en;q=0.8',
	        'Connection': 'keep-alive'
    	}

		self.webpage = None


	def set_webpage(self, url):
		page =  ul.urlopen(ul.Request(url, headers=self.http_headers))
		self.webpage = BeautifulSoup(page.read(), "lxml")

	
	def country_row(self, country):
		if country == "World":
			return self.webpage.find("td", text=country).find_parent("tr")
		
		return self.webpage.find("a", text=country).find_parent("tr")


	def run(self, country):
		try:
			self.set_webpage("https://www.worldometers.info/coronavirus")
		except Exception as e:
			return {
				"error": "Something went wrong getting worldometers page"
			}

		try:
			row = self.country_row(country).find_all("td")
		except Exception as e:
			return {
				"error": "Country not found"
			}
		
		return {
			"target": country,
			"target_arab": str(TextBlob(country).translate(to="ar")),
			"total_cases": row[1].text,
			"new_cases": row[2].text,
			"total_deaths": row[3].text,
			"new_deaths": row[4].text,
			"total_recovered": row[5].text,
			"active_cases": row[6].text,
			"serious_critical": row[7].text,
			"tot_cases_per_million": row[8].text,
			"deaths_per_million": row[9].text,
			"total_tests": row[10].text,
			"tests_per_million": row[11].text,
		}