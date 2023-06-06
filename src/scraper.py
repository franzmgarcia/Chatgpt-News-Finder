import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    # Enviamos una solicitud HTTP a la URL de la página web que queremos acceder
    response = requests.get(url)

    # Si la solicitud fue exitosa y la página web retornó un status code de 200
    if response.status_code == 200:
        # Obtenemos el contenido de la página web
        page_content = response.content

        # Creamos un objeto BeautifulSoup y especificamos el analizador (parser) a utilizar
        soup = BeautifulSoup(page_content, 'html.parser')

        # Ahora puedes utilizar el objeto soup para encontrar elementos en la página web
        # Por ejemplo, para encontrar todos los titulares en una página que estén marcados con la etiqueta h1, podrías hacer algo como esto:
        
        headlines = []
        
        # Esto retornará una lista de todos los elementos h2 en la página web
        # Puedes iterar sobre esta lista y hacer lo que necesites con cada elemento
        for headline in soup.find_all('body'):
            headlines.append(headline.get_text())  # esto anadirá el texto del titular
        
        return headlines
    else:
        print(f"Error al cargar la página {url}: {response.status_code}")
        return []
