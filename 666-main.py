import pandas as pd
import matplotlib.pyplot as plt
import requests
import time

api_key_no1_navasan = "freekj9W6HqoQWqoWChjRVxuIQiL9QH9"
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
            }

def get_dollar_price_in_iran():
    for _ in range(3): # Retry up to 3 times
        try:
            url = f"http://api.navasan.tech/latest/?api_key={api_key_no1_navasan}"
            response = requests.get(url, headers=headers, timeout=100)
            data = response.json()
            iran_rate = data['rates']['IRR'] # Assuming 'IRR' is the currency code for Iranian Toman
            return iran_rate
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}. Retrying...")
            time.sleep(5) # Wait for 5 seconds before retrying
    

def analyze_and_visualize(price):
    # For simplicity, we'll use the current date and time for the plot
    from datetime import datetime
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



# This code does the following:

#     Fetches the current dollar price in Iran using the get_dollar_price_in_iran function.
#     Prints the fetched price.
#     Calls the analyze_and_visualize function to plot the price over time. For simplicity, it uses the current date and time as the date for the plot.

# Please note, the API URL used in the get_dollar_price_in_iran function is just an example. You might need to find a reliable source for real-time dollar prices in Iran, as the availability and accuracy of such data can vary.

# This integration should replace the placeholder "Hello, world!" message with real functionality, fetching and displaying real-time dollar prices in Iran along with a simple plot.