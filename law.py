import requests

url = "https://az-ae-app-fal-prod-webservice.azurewebsites.net/api/lawyer/"

payload = "{\"lastName\":\"Aa\",\"otherName\":\"\",\"suburb\":\"\",\"region\":\"\",\"accreditedSpecialist\":\"\",\"page\":\"1\",\"pageSize\":10}"
headers = {
    'sec-ch-ua': "\" Not;A Brand\";v=\"99\", \"Google Chrome\";v=\"91\", \"Chromium\";v=\"91\"",
    'x-requested-with': "XMLHttpRequest",
    'sec-ch-ua-mobile': "?0",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36",
    'content-type': "application/json",
    'accept': "*/*",
    'sec-fetch-site': "cross-site",
    'sec-fetch-mode': "cors",
    'sec-fetch-dest': "empty",
    'cache-control': "no-cache",
    'postman-token': "53c96c98-2e07-6194-7447-6a6c1131181b"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)