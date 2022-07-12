import pytest
from providers.website_scraper import scrap_page

# First test use cases expected, then test Error an catch those error


@pytest.mark.parametrize(
    "site_link",
    [
        "https://www.zonaprop.com.ar/departamentos-alquiler-2-ambientes-menos-70000-pesos.html"
    ],
)
def test_scraping_pages(site_link):
    output_page = scrap_page(site_link)
    assert True == bool(
        "html" in output_page
    )  # buscamos html en el texto y si existe devuelve booleano


def test_scraping_pages(site_link="https://asdddddddddddasdads.ar/"):
    with pytest.raises(Exception): # hay un raise de exception
        output_page = scrap_page(site_link)
