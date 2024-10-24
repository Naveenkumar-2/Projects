from bs4 import BeautifulSoup
import requests,os


try:
    # Make the request to the IMDb page
    response = requests.get("https://owasp.org/www-project-top-ten/")
    soup = BeautifulSoup(response.text, 'html.parser')
    attcs =soup.find('section',class_="page-body").find_all('li')
    i =1
    with open("D:\Cybersecurity projects\data.txt",'w')as file:
      for attc in attcs:      
          attc_name=attc.find('a').strong.text
          disc=attc.text
          file.write(f"{i} {attc_name}\n")
          
          file.write("\n")
          file.write(f"{disc}\n")
        
          
          i=i+1
          
        
      
 

    

except Exception as e:
    print(e)
