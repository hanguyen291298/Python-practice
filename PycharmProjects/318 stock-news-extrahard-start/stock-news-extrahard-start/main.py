import requests
from datetime import date, timedelta
from twilio.rest import Client
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

yesterday = (date.today() - timedelta(1)).strftime('%Y-%m-%d')
before_yesterday = (date.today() - timedelta(2)).strftime('%Y-%m-%d')

URl_1 = "https://www.alphavantage.co/query?"
API_KEY_1 = "TMWZMYVDGWUCEVPE"
URl_2 = "https://newsapi.org/v2/everything?"
API_KEY_2 = "ad5ae8ae0dad45008eadbacdbeca6ac3"

PRAMETERS_1 = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": API_KEY_1
}

PRAMETERS_2 = {
    "q": COMPANY_NAME,
    "from": before_yesterday,
    "sortBy": "publishedAt",
    "apiKey": API_KEY_2
}

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

response_1 = requests.get(url=URl_1, params=PRAMETERS_1)
data_1 = response_1.json()

ytd_value = data_1["Time Series (Daily)"][yesterday]["4. close"]
bf_value = data_1["Time Series (Daily)"][before_yesterday]["4. close"]

difference = (float(ytd_value) - float(bf_value)) / float(bf_value) * 100
if difference < 0:
    percentage_change = f"🔽{int(difference)}%"
else:
    percentage_change = f"🔼{int(difference)}%"


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

response_2 = requests.get(url=URl_2, params=PRAMETERS_2)
data_2 = response_2.json()
articles = data_2["articles"][: 3]


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

acount_sid = "ACc3f9aa622bc575ea199d31f842d8aa8f"
auth_token = "a0e2393db4a821a8bbfb54d315dd2516"

client = Client(acount_sid, auth_token)

for article in articles:
    title = article["title"]
    description = article["description"]

    message = client.messages.create(from_="+17073772083", to="+84394836655",\
        body=f"{STOCK}: {percentage_change}\nHeadline: {title}\nBrief: {description}")



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

