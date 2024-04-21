from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def get_dollar_price_in_iran():
    # Setup WebDriver
    webdriver_service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=webdriver_service)

    # Navigate to the website
    url = "https://irarz.com/"
    driver.get(url)

    # Assuming the prices are in elements with specific IDs or classes
    # You'll need to inspect the website to find the correct selectors
    dollar_price_element = driver.find_element(By.ID, "usdmax")
    
    if dollar_price_element:
        # Extract the prices
        dollar_price = dollar_price_element.text
        driver.quit() # Close the browser
        return dollar_price
    else:
        print("Failed to find price elements.")
        driver.quit() # Close the browser
        return None

def analyze_and_visualize(price):
    # For simplicity, we'll use the current date and time for the plot
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Convert data to a pandas DataFrame
    df = pd.DataFrame([{'Date': current_date, 'Price': price}])
    
    # Basic visualization
    plt.plot(df['Date'], df['Price'])
    plt.title('Dollar Price in Iran Over Time')
    plt.xlabel('Date')
    plt.ylabel('Price (IRR)')
    plt.show()

def hello_world():
    dollar_price_in_iran = get_dollar_price_in_iran()
    print(f"The current dollar price in Iran is: {dollar_price_in_iran} IRR")
    analyze_and_visualize(dollar_price_in_iran)

hello_world()
    