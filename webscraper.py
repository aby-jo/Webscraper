import selenium,requests,sys,re,os
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
def check_url(url):
    pattern=r"^https?://(?:www\.)?[\w.-]+\.(com|org|edu).*"
    if re.search(pattern,url):
        return True
    else:
        sys.exit("Invalid URL")
def connect(url):
    try:
        options=selenium.webdriver.ChromeOptions()
        options.add_argument("--headless")
        browser=selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
        browser.get(url)
    except selenium.common.exceptions.WebDriverException:
        sys.exit("Unable to find the website")
    except requests.exceptions.ConnectionError: 
        sys.exit("You are offline")
    else:
        text=browser.find_element(By.TAG_NAME,"body").text
        browser.quit()
        return text
def write_to_file(text):
    path="scraper_data.txt"
    if os.path.exists(path):
        ans=input("A file already exists with the name \"scraper_data.txt\"\nDo you want to rewrite?(Y/N): ").strip().lower()
        if ans in {"yes","ye","y"}:
            pass
        else:
            sys.exit("Exited the program")
    with open(path,"w",encoding="utf-8") as file:
        file.write(text)

def main():
    url=input("What is the URL?: ").strip()
    check_url(url)
    text=connect(url)
    write_to_file(text)



if __name__ == "__main__":
    main()