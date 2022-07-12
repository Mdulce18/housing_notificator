import cloudscraper


def scrap_page(site_link):
    try:
        scraper = cloudscraper.create_scraper()
        html_page = scraper.get(site_link).text
    except Exception as e:
        raise e
    return html_page
