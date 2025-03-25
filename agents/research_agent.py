import requests
from bs4 import BeautifulSoup

def fetch_trending_hr_topics():
    url = "https://www.forbes.com/workplace/"
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        topics = [a.text.strip() for a in soup.find_all("h2")[:5]]
        return topics
    return ["HR Trends for 2025", "AI in Hiring", "Remote Work Strategies"]

if __name__ == "__main__":
    print(fetch_trending_hr_topics())
