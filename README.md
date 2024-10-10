## Flask Selenium Scraper
Este proyecto es una API Flask que utiliza Selenium para extraer productos y sus precios desde una página web específica. La API recibe una URL a través de una solicitud POST, 
navega a la página utilizando un navegador y extrae los nombres de productos, sus precios y, si están disponibles, los precios promocionales de los primeros 15 productos .

Requisitos
Antes de ejecutar el proyecto, asegúrate de tener instalados los siguientes componentes:

- Python 3.6
- Flask
- Selenium
- Google Chrome (o un navegador compatible con Selenium)
- ChromeDriver (o el WebDriver correspondiente al navegador que estés utilizando)
- Docker y Docker Compose

## Instalación
Con Docker y Docker Compose
Opción 1: Usar Docker Compose
Clona este repositorio en tu máquina local:

```bash

git clone https://github.com/usuario/flask-selenium-scraper.git
cd flask-selenium-scraper
```
Asegúrate de tener docker-compose.yml y Dockerfile en el directorio raíz del proyecto.

Construye y levanta los contenedores con Docker Compose:

```bash

docker-compose up --build
```
La API Flask estará disponible en http://localhost:5000 y el servidor de Selenium estará en http://localhost:4444.

## Uso
Realizar una solicitud POST
Con la aplicación Flask en ejecución (ya sea local o en Docker), realiza una solicitud POST al endpoint /extract-products con una URL válida en formato JSON
```
{
    "url": "https://www.tiendasjumbo.co/supermercado/despensa/bebida-achocolatada-en-polvo"
}
```


La API devolverá un JSON con los productos extraídos:
```
{
    "products": [
        {
            "name": "Alimento Milo en polvo bolsa x500g ",
            "price": "$ 23.450",
            "promo_price": "N/A"
        },
        {
            "name": "Alimento Milo en polvo bolsa x250g ",
            "price": "$ 10.890",
            "promo_price": "$ 10.700"
        },
        ....
    
    ],
    "url": "https://www.tiendasjumbo.co/supermercado/despensa/bebida-achocolatada-en-polvo"
}
```
