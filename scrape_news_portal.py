import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# URL dari news portal (misalnya CNN Indonesia)
url = "https://www.cnnindonesia.com/"

# Membuat function untuk scraping data
def scrape_news(url):
    # Mengirim request ke URL
    response = requests.get(url)
    
    # Memastikan respons berhasil
    if response.status_code != 200:
        print("Failed to retrieve page")
        return None
    
    # Parsing HTML dengan BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Menyimpan data dalam list
    news_data = []
    
    # Mengambil konten artikel (misal judul, link, dan ringkasan)
    articles = soup.find_all("article", class_="list-berita")
    for article in articles:
        # Mengambil judul artikel
        title = article.find("h2", class_="title").get_text(strip=True)
        
        # Mengambil link artikel
        link = article.find("a")["href"]
        
        # Mengambil ringkasan artikel
        summary = article.find("p", class_="content").get_text(strip=True)
        
        # Menyimpan hasil scraping ke list
        news_data.append({
            "Title": title,
            "Link": link,
            "Summary": summary
        })
    
    # Mengembalikan hasil scraping sebagai DataFrame
    return pd.DataFrame(news_data)

# Memanggil function dan menyimpan hasil
news_df = scrape_news(url)

# Menampilkan hasil
if news_df is not None:
    print(news_df.head())
    # Simpan hasil dalam CSV jika diinginkan
    news_df.to_csv("news_data.csv", index=False)
    print("Data berhasil disimpan ke 'news_data.csv'")
else:
    print("Tidak ada data yang diambil")
