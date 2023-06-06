from scraper import scrape_website
from nlp_analyzer import NewsAnalyzer

def main():
    # Define las URL de los sitios web de noticias que quieras revisar
    urls = ['https://www.example.com']

    # Crea una instancia de NewsAnalyzer
    analyzer = NewsAnalyzer()

    # Para cada URL, revisa el sitio web y recoge las noticias
    for url in urls:
        news = scrape_website(url)

        # Aquí puedes hacer lo que quieras con las noticias
        # Por ejemplo, podrías imprimir las noticias a la consola:
        for headline in news:
            print('headline: '+headline)

            # Analiza el titular con NewsAnalyzer
            print('analisis: '+analyzer.summarize_text(headline))

if __name__ == '__main__':
    main()
