import urllib.request as ul
from bs4 import BeautifulSoup
from textblob import TextBlob
import difflib


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
		# soup = BeautifulSoup.BeautifulSoup(content.decode('utf-8','ignore'))
		page =  ul.urlopen(ul.Request(url, headers=self.http_headers))
		self.webpage = BeautifulSoup(page.read(), "lxml")

	
	def country_row(self, country):
		if country == "World":
			return self.webpage.find("td", text=country).find_parent("tr")
		
		return self.webpage.find("a", text=country).find_parent("tr")

	def moroccan_regions(self):
		try:
			self.set_webpage("https://ar.wikipedia.org/wiki/%D8%AC%D8%A7%D8%A6%D8%AD%D8%A9_%D9%81%D9%8A%D8%B1%D9%88%D8%B3_%D9%83%D9%88%D8%B1%D9%88%D9%86%D8%A7_%D9%81%D9%8A_%D8%A7%D9%84%D9%85%D8%BA%D8%B1%D8%A8_2020")
		except Exception as e:
			return {
				"error": "Something went wrong getting Moroccan HM page"
			}

		table = self.webpage.find("span", {"id": "مواقع_الحالات"}).parent.find_next("table").find("tbody").find_all("tr")[3:-1]

		ret = {}

		for row in table:
			title = row.find("a")
			if title is not None:
				title = title.text
			else:
				continue
			ret[title] = row.find("td").text
		return ret


	def get_countries(self):
		try:
			self.set_webpage("https://www.worldometers.info/coronavirus")
		except Exception as e:
			return {
				"error": "Something went wrong getting worldometers page"
			}

		data = self.webpage.find("tbody").find_all("a")
		ret = ["World"]
		for a in data:
			ret.append(a.text)
		return str(ret)


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
			countries = ['World', 'USA', 'Spain', 'Italy', 'France', 'Germany', 'UK', 'Turkey', 'Iran', 'Russia', 'Belgium', 'Brazil', 'Canada', 'Netherlands', 'Switzerland', 'Portugal', 'India', 'Ireland', 'Austria', 'Peru', 'Sweden', 'Israel', 'S. Korea', 'Japan', 'Chile', 'Saudi Arabia', 'Poland', 'Ecuador', 'Romania', 'Pakistan', 'Mexico', 'Denmark', 'Norway', 'UAE', 'Czechia', 'Australia', 'Singapore', 'Indonesia', 'Serbia', 'Philippines', 'Ukraine', 'Qatar', 'Malaysia', 'Belarus', 'Dominican Republic', 'Panama', 'Finland', 'Colombia', 'Luxembourg', 'South Africa', 'Egypt', 'Argentina', 'Morocco', 'Thailand', 'Algeria', 'Bangladesh', 'Moldova', 'Greece', 'Hungary', 'Kuwait', 'Bahrain', 'Croatia', 'Iceland', 'Kazakhstan', 'Uzbekistan', 'Estonia', 'Iraq', 'New Zealand', 'Azerbaijan', 'Slovenia', 'Lithuania', 'Armenia', 'Bosnia and Herzegovina', 'Oman', 'North Macedonia', 'Slovakia', 'Hong Kong', 'Cameroon', 'Afghanistan', 'Cuba', 'Bulgaria', 'Tunisia', 'Ghana', 'Ivory Coast', 'Cyprus', 'Djibouti', 'Latvia', 'Andorra', 'Lebanon', 'Costa Rica', 'Niger', 'Burkina Faso', 'Albania', 'Kyrgyzstan', 'Nigeria', 'Bolivia', 'Guinea', 'Uruguay', 'Channel Islands', 'Honduras', 'San Marino', 'Palestine', 'Malta', 'Taiwan', 'Jordan', 'R\u00e9union', 'Georgia', 'Senegal', 'DRC', 'Mauritius', 'Montenegro', 'Isle of Man', 'Kenya', 'Sri Lanka', 'Vietnam', 'Guatemala', 'Mayotte', 'Venezuela', 'Mali', 'Paraguay', 'El Salvador', 'Faeroe Islands', 'Jamaica', 'Martinique', 'Guadeloupe', 'Tanzania', 'Rwanda', 'Congo', 'Brunei ', 'Somalia', 'Gibraltar', 'Cambodia', 'Madagascar', 'Trinidad and Tobago', 'Ethiopia', 'Gabon', 'Myanmar', 'Aruba', 'French Guiana', 'Monaco', 'Bermuda', 'Togo', 'Liechtenstein', 'Equatorial Guinea', 'Liberia', 'Barbados', 'Sudan', 'Sint Maarten', 'Guyana', 'Zambia', 'Cabo Verde', 'Cayman Islands', 'Bahamas', 'French Polynesia', 'Uganda', 'Maldives', 'Libya', 'Guinea-Bissau', 'Macao', 'Haiti', 'Eritrea', 'Mozambique', 'Syria', 'Saint Martin', 'Benin', 'Chad', 'Mongolia', 'Nepal', 'Sierra Leone', 'Zimbabwe', 'Angola', 'Antigua and Barbuda', 'Eswatini', 'Botswana', 'Laos', 'Timor-Leste', 'Belize', 'New Caledonia', 'Malawi', 'Fiji', 'Dominica', 'Namibia', 'Saint Lucia', 'Cura\u00e7ao', 'Grenada', 'Saint Kitts and Nevis', 'CAR', 'St. Vincent Grenadines', 'Turks and Caicos', 'Falkland Islands', 'Greenland', 'Montserrat', 'Seychelles', 'Suriname', 'Nicaragua', 'Gambia', 'Vatican City', 'Mauritania', 'Papua New Guinea', 'St. Barth', 'Western Sahara', 'Burundi', 'Bhutan', 'Caribbean Netherlands', 'British Virgin Islands', 'Sao Tome and Principe', 'South Sudan', 'Anguilla', 'Saint Pierre Miquelon', 'Yemen', 'China']
			suggestions = difflib.get_close_matches(country, countries)
			return {
				"error": "Country not found",
				"suggestions": suggestions
			}
		
		data = {
			"target": country,
			"target_arab": str(TextBlob(country).translate(to="ar")),
			"total_cases": row[1].text,
			"new_cases": "+0" if row[2].text == "" else row[2].text,
			"total_deaths": row[3].text,
			"new_deaths": "+0" if row[4].text == "" else row[4].text,
			"total_recovered": row[5].text,
			"active_cases": row[6].text,
			"serious_critical": row[7].text,
			"tot_cases_per_million": row[8].text,
			"deaths_per_million": row[9].text,
			"total_tests": row[10].text,
			"tests_per_million": row[11].text,
		}

		if data["target"] == "Morocco":
			data["regions"] = self.moroccan_regions()

		
		return data

