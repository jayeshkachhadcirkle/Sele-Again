import requests
import firebase_admin
from firebase_admin import credentials, messaging
# Path to your service account key file
SERVICE_ACCOUNT_PATH = 'order-management-system-fa92d-firebase-adminsdk-fbsvc-5092b9a078.json'

bearer_token = '412|tqkBiue5C0X5yFxhDIOIgR2pqJqoiqrl0KSNljsAbdc3a123'

headers = {
    "Authorization": f"Bearer {bearer_token}"
}


offlineTokens = ["cT1vK1mTRxu5IPcrSXuP-s:APA91bGx5vVitlDKCPJO5dfq1Eao1Tf-PS_WHEu2tzkjRYZ3q4gdBCYsmTPrsoYILeGu7-S0xl3sbPsAS1FqTSwQQNb4l-RP8HbXqzndyYHTyHHPWBdvMyw",
                 "dmcvCGt9R7W8lS4aF7Ce9O:APA91bFQqo1PfKLtx_VpCfaFoxd93hogMzf-wXG96nppRQMPtBglgpBHsC6YVd8nLJKfjb9m98Wv0yYi0wGJndw1TIO_5-qGI9uRnBPycRPuaV0q3kT8ArY",
                 "fhNr4L50S9SRSSFQJ0srD3:APA91bGmZ010oacXRjtbn7REXQ6rbnSUOsoy-pMLPMFA-iZ6pgkgwHGxuY9XihpRi6XFxKgW3K3qMwgMwf6YABMXE3-5YAq78Sc2I1xPGuouYMy9AZ1PPAQ",
                 "eb7_Z1hwTQ-Iyqc0clYj19:APA91bEIQwCsDR4OneLAukOxD3q-CD9pa0BSyyXt51nc_yrclEacoJDMLwzsw3a8SYzYs5HpDq94q7ZZZXDoUXu6rCakemXaePisJ5FxCkG_-kbdfN1P1ss",
                 "fUsXP9wlQrGE_a-WpXdjT4:APA91bEENTn0dw5zAXFNEO7et32ixZ3tBb-mixLBvLW-BCWQdWvIezd2ftRTT4rsoPZoKs5ivtv1EtqPaOL47rosmw_rh6MkLUk5pjwmU_E0G5ZCLZwKzJU",
                 "fJbZT5RGS2eDSK9fudn8pH:APA91bH7HajiHIjdkXG6aqNAclMJToCThWSgT3wfWWZvzMocd-e1Xv5WV1udbBmXLJX_3H6jAHS7L6t-mpDX9MxnADQ4aDn82Z_eDT1l90GAeON6f0OKnko",
                 "eLaOaqrtTX-jhMD6XN7SIC:APA91bEVMRsy65sX8RLMbwrCdfRIinSpQqBbPf4IBzhRWseVi-zKQUg6m3qKJOEG6Lm9Bo511HaNFL9-qeoH2yQD3--m6u_HG8onllp-SbhIqQ22vF77LyE"
                 ]

def get_api_data(url):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"An unexpected error occurred during the request: {req_err}")
    return None


example_api_url = 'https://mark5.wilerhub.com/pro/public/api/sendall'

api_data = get_api_data(example_api_url)
if api_data:
    print("\nSuccessfully retrieved API Data:")
    print(api_data)
else:
    print("\nFailed to retrieve API data. Please check the URL and your network connection.")

example_list_api_url = 'https://mark5.wilerhub.com/pro/public/api/sendall'
list_data = get_api_data(example_list_api_url)

if list_data:
    print("\nSuccessfully retrieved a list of API Data:")
    for item in list_data:
        print(f"  - ID: {item.get('id')}, Title: {item.get('title')}...") # Print first 30 chars of title
else:
    print("\nFailed to retrieve the list of API data.")


unique_tokens = set()

for record in api_data:
    unique_tokens.add(record["token"])

list_of_unique_tokens = list(unique_tokens)

print(list_of_unique_tokens)

# Initialize Firebase Admin SDK
cred = credentials.Certificate(SERVICE_ACCOUNT_PATH)
firebase_admin.initialize_app(cred)

# Your target device token
# device_token = 'dUTqBcrWSP6Wd4XqZsCGDq:APA91bFWZrSTGIahn7gpt_1vCjor2w0Bv8AlGG72LVJ_Wc9CEemZQ-B9fD6c3yq0CM2oH2WXlFDz-YctVbxNejR7T2LigXEpQI45b_1hZ64z9gl7FaqUWe4'
# Build the message

# last = len(list_of_unique_tokens)
# print("last: ", last)

for i in offlineTokens:
    # print(i)
    message = messaging.Message(
        notification=messaging.Notification(
            title='Test Notification',
            body='Open The App...',
        ),
        token=i,
    )

    response = messaging.send(message)
    print('Successfully sent message:', response)
