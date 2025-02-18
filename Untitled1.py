#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
url = "http://quotes.toscrape.com/"
# Send a GET request
response = requests.get(url)


# In[ ]:


get_ipython().system('pip install ')


# In[4]:


# Chck if the request was successful
if response.status_code == 200:
    # Parse the HTML
    soup = BeautifulSoup(response.text, 'html.parser')
 # Find all quote containers
    quotes = soup.find_all("div", class_="quote")
    # Loop through each quote and extract data
    for i, quote in enumerate(quotes[:5]):  # Get first 5 quotes
        text = quote.find("span", class_="text").text  # Quote text
        author = quote.find("small", class_="author").text  # Author name
        tags = [tag.text for tag in quote.find_all("a", class_="tag")]  # List of tags
        print(f"{i+1}. \"{text}\" - {author}")
        print(f"   Tags: {', '.join(tags)}\n")
else:
    print(f"Failed to retrieve the webpage. Status Code: {response.status_code}")


# In[6]:


import requests
from bs4 import BeautifulSoup
# Define the city (e.g., New York)
city = "india/hyderabad" 
# Weather URL
url = f"https://www.timeanddate.com/weather/{city}"
# Send GET request
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
# Extract temperature and description
temp = soup.find("div", class_="h2").text.strip() if soup.find("div", class_="h2") else "N/A"
desc = soup.find("p").text.strip() if soup.find("p") else "N/A"
print(f"Current Weather in New York: {temp} | {desc}")


# In[27]:


import requests
from bs4 import BeautifulSoup
# Product search URL (Example: iPhone)
search_url = "https://www.amazon.in/Ambrane-Wireless-10000mAh-Charging-Magnetic&th=1"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.6943.98 Safari/537.36"
}
# Send GET request
response = requests.get(search_url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
# Extract first product name & price

product = soup.select_one("span .a-size-large")
price = soup.select_one("span.a-price-whole")
# Display product details
if product and price:
    print(f"Product: {product.text.strip()}")
    print(f"Price: Rs.{price.text.strip()}")
else:
    print("Could not find product details.")


# In[16]:


import requests
from bs4 import BeautifulSoup
# Wikipedia page URL
url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
# Send GET request
response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
# Find the table
table = soup.find("table", class_="wikitable")
# Extract the first 5 countries and their population
for row in table.find_all("tr")[1:6]:  # Skip the header row
    columns = row.find_all("td")
    country = columns[1].text.strip()
    population = columns[2].text.strip()
    print(f"{country}: {population}")


# In[22]:


import requests
from bs4 import BeautifulSoup
# Define the city (e.g., New York
city = "india/hyderabad"
# Weather URL
url = f"https://www.timeanddate.com/weather/{city}"
# Send GET request
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
# Extract temperature and description
temp = soup.find("div", class_="h2").text.strip() if soup.find("div", class_="h2") else "N/A"
desc = soup.find("p").text.strip() if soup.find("p") else "N/A"
print(f"Current Weather in Hyderabad: {temp} | {desc}")


# In[23]:


import requests
from bs4 import BeautifulSoup
# Product search URL (Example: iPhone)
search_url = "https://www.amazon.in/s?k=iphone&crid=PQVCJSNISAH4&sprefix=iphone%2Caps%2C233&ref=nb_sb_noss_2"
# Headers (Mimic a browser)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}


# In[24]:


# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    # Find all quote container
    quotes = soup.find_all("div", class_="quote")
    # Loop through each quote and extract dat
    for i, quote in enumerate(quotes[:5]):  # Get first 5 quotes
        text = quote.find("span", class_="text").text  # Quote text
        author = quote.find("small", class_="author").text  # Author nam
        tags = [tag.text for tag in quote.find_all("a", class_="tag")]  # List of tags
        
        print(f"{i+1}. \"{text}\" - {author}")
        print(f"   Tags: {', '.join(tags)}\n")
else:
    print(f"Failed to retrieve the webpage. Status Code: {response.status_code}")


# In[25]:


import requests
from bs4 import BeautifulSoup
# Define the city (e.g., New York)
city = "india/hyderabad"
# Weather URL
url = f"https://www.timeanddate.com/weather/{city}"
# Send GET request
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract temperature and description
temp = soup.find("div", class_="h2").text.strip() if soup.find("div", class_="h2") else "N/A"
desc = soup.find("p").text.strip() if soup.find("p") else "N/A" 
print(f"Current Weather in Hyderabad: {temp} | {desc}")


# In[26]:


from IPython.display import display, HTML
display(HTML("""<table>
  <tr>
    <th>Company</th>
    <th>Contact</th>
    <th>Country</th>
  </tr>
  <tr>
    <td>Alfreds Futterkiste</td>
    <td>Maria Anders</td>
    <td>Germany</td>
  </tr>
  <tr>
    <td>Centro comercial Moctezuma</td>
    <td>Francisco Chang</td>
    <td>Mexico</td>
  </tr>
</table>
"""))


# In[ ]:




