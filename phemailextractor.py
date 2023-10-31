import re
import requests
from bs4 import BeautifulSoup



#res=requests.get('https://pwstechnext.in/')
res=requests.get('https://talentstack.in/ContactUs.php')

if res.status_code == requests.codes.ok :
    soup = BeautifulSoup(res.text, 'html.parser')


#email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
email_pattern = r'\b[\w\.-]+@[\w\.-]+\b' ## simpler pattern

mobile_pattern = r'(\+\d{1,3}\s?)?(\d{10})'

# Find and extract email addresses and mobile numbers using regex
email_addresses = re.findall(email_pattern, soup.get_text())
mobile_numbers = re.findall(mobile_pattern, soup.get_text())

# Print the extracted email addresses and mobile numbers
print("Email Addresses:")
for email in email_addresses:
      print(email)

print("\nMobile Numbers:")
for mobile in mobile_numbers:
  mobile_number = mobile[0] + mobile[1] if mobile[0] else mobile[1]
  print(mobile_number)
    


