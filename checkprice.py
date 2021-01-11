import requests
from bs4 import BeautifulSoup

#URL = 'https://www.ldlc.com/recherche/3060%20TI/'
URL = 'https://www.topachat.com/pages/produits_cat_est_micro_puis_rubrique_est_wgfx_pcie.html'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

#results = soup.find(id="product")   #LDLC
results = soup.find(id="content")   #TOPACHAT
#gpu_elems = results.find_all('section', class_='listing-product')   #LDLC
gpu_elems = results.find_all('section', class_='produits list')   #TOPACHAT

for gpu_elem in gpu_elems:
    title_elem = gpu_elem.find('div', class_="libelle")
    price_elem = gpu_elem.find('div', class_='prod_px_euro v16')
    #availability = gpu_elems.find('class', class_='grille-produit NOR')
    print(title_elem.text.strip())
    print(price_elem.text.strip())
    #print(availability)
