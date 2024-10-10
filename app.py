from flask import Flask, request, jsonify
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pdb
import os
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException

app = Flask(__name__)

def get_products(url):
    selenium_url = "http://localhost:4444/wd/hub"
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Remote(command_executor=selenium_url, options=chrome_options)
    
    driver.get(url)

    
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "gallery-layout-container"))
    )

    products = []
    count = 1
    
    for i in range(15): 
        try:
            
            product_name_element = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, f'//*[@id="gallery-layout-container"]/div[{count}]/section/a/article/div/div[9]/div/h3/span'))
            )

            
            driver.execute_script("arguments[0].scrollIntoView();", product_name_element)
            
            product_name = product_name_element.text
            
            product_price_element = driver.find_element(By.XPATH, f'//*[@id="gallery-layout-container"]/div[{count}]/section/a/article/div/div[6]/div/div/div/div/div[1]/div/div/div/div')
            product_price = product_price_element.text

            
            try: #? xpath promocion 
                promo_price_element = WebDriverWait(driver, 2).until(
                    EC.presence_of_element_located((By.XPATH, f'//*[@id="gallery-layout-container"]/div[{count}]/section/a/article/div/div[7]/div/div/div[2]/div/div/div/div/div'))
                )
                promo_price = promo_price_element.text
            except TimeoutException:
                promo_price = 'N/A'

            product = {
                "name": product_name,
                "price": product_price,
                "promo_price": promo_price
            }
            print(product)
            products.append(product)
            count += 1
        
        except TimeoutException as e:
            print(f"Elemento no encontrado o tiempo de espera agotado en el producto {count}: {e}")
            break 

    driver.quit()
    return products


@app.route('/extract-products', methods=['POST'])
def extract_products():
    data = request.get_json()
    url = data.get('url')

    if not url:
        return jsonify({"error": "URL no proporcionada"}), 400

    try:
        products = get_products(url)
        result = {
            "url": url,
            "products": products
        }
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    #app.run(debug=True)
