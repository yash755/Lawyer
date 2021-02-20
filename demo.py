import requests
from bs4 import BeautifulSoup
import json
import re
import csv
import math

d_data = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z']

# CE CODE, Eng Name, Chinese Name, Address, Active, Phone no., Fax no, Email, R01...R06


def get_list(alphabet):

    url = "https://az-ae-app-fal-prod-webservice.azurewebsites.net/api/lawyer/"

    # payload = '{\"lastName\":\"' + str(alphabet) + '\",\"lastNameSearchOption\":\"beginsWith\",\"otherName\":\"\",\"suburb\":\"\",\"region\":\"\",\"accreditedSpecialist\":\"\",\"page\":1,\"pageSize\":1000}'

    payload = '{\"lastName\":\"' + str(alphabet)  +'\",\"otherName\":\"\",\"suburb\":\"\",\"region\":\"\",\"accreditedSpecialist\":\"\",\"page\":1,\"pageSize\":500}'

    print (payload)

    headers = {
        'sec-ch-ua': "\"Chromium\";v=\"88\", \"Google Chrome\";v=\"88\", \";Not A Brand\";v=\"99\"",
        'x-requested-with': "XMLHttpRequest",
        'sec-ch-ua-mobile': "?0",
        'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36",
        'content-type': "application/json",
        'accept': "*/*",
        'sec-fetch-site': "cross-site",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'cache-control': "no-cache",
        'postman-token': "f3bdf117-99b6-ba90-e75c-56ca8dc85be5"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    json_data = json.loads(response.text)

    if 'resultCount' in json_data:
        print ("Total Count" + str(json_data['resultCount']))
        count = json_data['resultCount'] + 1000

        # noofpages = math.ceil(json_data['resultCount']/1000)
        # print (noofpages)
        page = 1
        # while page <= noofpages:


        url = "https://az-ae-app-fal-prod-webservice.azurewebsites.net/api/lawyer/"

        # payload = '{\"lastName\":\"' + str(
        #     alphabet) + '\",\"lastNameSearchOption\":\"beginsWith\",\"otherName\":\"\",\"suburb\":\"\",\"region\":\"\",\"accreditedSpecialist\":\"\",\"page\":' + str(page) + ',\"pageSize\":1000}'

        payload = '{\"lastName\":\"' + str(
            alphabet) + '\",\"otherName\":\"\",\"suburb\":\"\",\"region\":\"\",\"accreditedSpecialist\":\"\",\"page\":1,\"pageSize\":' + str(count)   +'}'
        print (payload)

        headers = {
            'sec-ch-ua': "\"Chromium\";v=\"88\", \"Google Chrome\";v=\"88\", \";Not A Brand\";v=\"99\"",
            'x-requested-with': "XMLHttpRequest",
            'sec-ch-ua-mobile': "?0",
            'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36",
            'content-type': "application/json",
            'accept': "*/*",
            'sec-fetch-site': "cross-site",
            'sec-fetch-mode': "cors",
            'sec-fetch-dest': "empty",
            'cache-control': "no-cache",
            'postman-token': "f3bdf117-99b6-ba90-e75c-56ca8dc85be5"
        }

        response1 = requests.request("POST", url, data=payload, headers=headers)

        json_data1 = json.loads(response1.text)

        if 'results' in json_data1:
            items = json_data1['results']
            print (len(items))

            for item in items:
                print (item)
                first_name = ''
                last_name= ''
                date_admitted = ''
                company = ''
                email = ''
                class_type = ''
                address = ''
                phone =''


                if 'id' in item:
                    corp_id = item['id']

                    # print ('https://az-ae-app-fal-prod-webservice.azurewebsites.net/api/lawyer/' + str(corp_id))

                    response2 = requests.request("GET", 'https://az-ae-app-fal-prod-webservice.azurewebsites.net/api/lawyer/' + str(corp_id))

                    json_data2 = json.loads(response2.text)

                    if 'firstName' in json_data2:
                        first_name = json_data2['firstName']


                    if 'lastName' in json_data2:
                        last_name = json_data2['lastName']


                    if 'admissionDate' in json_data2:
                        date_admitted = json_data2['admissionDate']

                    if 'placeOfPractice' in json_data2:
                        company = json_data2['placeOfPractice']

                    if 'email' in json_data2:
                        email = json_data2['email']


                    if 'class' in json_data2:
                        class_type = json_data2['class']


                    if 'phoneWithAreaCode' in json_data2:
                        phone = json_data2['phoneWithAreaCode']


                    if 'streetAddress' in json_data2:

                        if json_data2['streetAddress']:

                            if 'street' in json_data2['streetAddress']:
                                address = address + json_data2['streetAddress']['street'] + ' '

                            if 'suburb' in json_data2['streetAddress']:
                                address = address + json_data2['streetAddress']['suburb'] + ' '

                            if 'state' in json_data2['streetAddress']:
                                address = address + json_data2['streetAddress']['state'] + ' '


                            if 'postCode' in json_data2['streetAddress']:
                                address = address + json_data2['streetAddress']['postCode'] + ' '

                    arr = []
                    temp = []
                    temp.append(first_name)
                    temp.append(last_name)
                    temp.append(date_admitted)
                    temp.append(company)
                    temp.append(email)
                    temp.append(class_type)
                    temp.append(address)
                    temp.append(phone)

                    arr.append(temp)

                    # print (arr)

                    with open('merged12356.csv', 'a+') as csvfile:
                        csvwriter = csv.writer(csvfile)
                        csvwriter.writerows(arr)




        # page = page + 1




if __name__ == '__main__':
    d_len = len(d_data)
    i = 0
    while i < d_len:
        get_list(d_data[i])
        i = i + 1