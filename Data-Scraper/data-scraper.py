from turtle import title
from urllib import response
import requests
from bs4 import BeautifulSoup
import csv

def scrape_website(url, output_file):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all the relevant data you want to scrape (e.g., articles, titles, etc.)
        # Extracting all article titles from <h2> tags with a specific class
        # articles = soup.find_all('h2', class_='entry-title')
        job_listing = soup.find_all('li', class_= 'job-list-li') # Find all job listings
        jobs = []
        
        for job in job_listing:
            # Extract job title 
            title_tag = job.find('h2')
            title = title_tag.get_text(strip=True) if title_tag else 'No Title Found'
        
            # Extract job description
            desc_tag = job.find('li', class_='job-desc')
            description = desc_tag.get_text(strip=True) if desc_tag else 'No Description Found'
        
            # Extract job link
            link_tag = title_tag.find('a') if title_tag else None
            link = f"https://www.myjobmag.com{link_tag['href']}" if link_tag and 'href' in link_tag.attrs else 'No Link Found'
        
            # Append the job data to the list
            jobs.append([title, description, link])
            
        # Save the scraped data into a CSV file
        with open(output_file, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['Title', 'Description', 'Link'])      # Write the header row
            writer.writerows(jobs) # Write all job data 
            
                
        print(f"Scraped data saved to {output_file} successfully.")
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
        
# Test the function
if __name__ == "__main__":
    print("Welcome to the Web Scraper!")
    website_url = input("Enter the URL of the website to scrape: ")
    output_file = 'scraped_data.csv'
    scrape_website(website_url, output_file)
        
