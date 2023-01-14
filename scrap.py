import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def extract_emails(url):
  # Fetch the page
  response = requests.get(url)
  html = response.text
  
  # Use BeautifulSoup to parse the HTML
  soup = BeautifulSoup(html, 'html.parser')
  
  # Find all the email addresses on the page
  emails = re.findall(r'(?!mailto:)[\w\.-]+@[\w\.-]+', html)
  
  # Find all the links on the page
  links = []
  for link in soup.find_all('a'):
    links.append(link.get('href'))
  
  # Extract emails from the linked pages using an iterative approach
  queue = links
  visited = set()
  while queue:
    link = queue.pop(0)
    if not link:
        continue
    if not link.startswith(('http://', 'https://')):
        continue
    full_url = urljoin(url, link)
    if full_url not in visited:
      visited.add(full_url)
      response = requests.get(full_url)
      html = response.text
      for email in re.findall(r'[\w\.-]+@[\w\.-]+', html):
        emails.append(email)
      for email in re.findall(r'mailto:[\w\.-]+@[\w\.-]+', html):
        emails.append(email.replace('mailto:', ''))
      soup = BeautifulSoup(html, 'html.parser')
      for link in soup.find_all('a'):
        queue.append(link.get('href'))
  
  return emails

# Example usage
url = 'https://www.enfsolar.com/directory/installer/Germany'
emails = extract_emails(url)

# Save the emails to a file
with open('emails.txt', 'w') as f:
  for email in emails:
    f.write(email + '\n')
