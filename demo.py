import requests
from bs4 import BeautifulSoup
import json
import re
import csv
import math

d_data = ['Sp', 'Sq', 'Sr', 'St', 'Su', 'Sw', 'Sy', 'Tj', 'Tk', 'Tl', 'Tn', 'To', 'Tp', 'Tq', 'Tr', 'Ts', 'Tu', 'Tv', 'Tw', 'Tx', 'Ty', 'Wi', 'Wj', 'Wk', 'Wl', 'Wm', 'Wn', 'Wo', 'Wp', 'Wr', 'Ws', 'Wt', 'Wu', 'Wx', 'Wy']

# CE CODE, Eng Name, Chinese Name, Address, Active, Phone no., Fax no, Email, R01...R06


def get_list(alphabet):

    print (alphabet)

    url = "https://az-ae-app-fal-prod-webservice.azurewebsites.net/api/lawyer/"

    payload = '{\"lastName\":\"' + str(alphabet) + '\",\"otherName\":\"\",\"suburb\":\"\",\"region\":\"\",\"accreditedSpecialist\":\"\",\"page\":1,\"pageSize\":10}'

    # payload = "{\"lastName\":\"Aa\",\"otherName\":\"\",\"suburb\":\"\",\"region\":\"\",\"accreditedSpecialist\":\"\",\"page\":\"1\",\"pageSize\":10}"

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
        count = json_data['resultCount'] + 100

        # noofpages = math.ceil(json_data['resultCount']/1000)
        # print (noofpages)
        page = 1
        # while page <= noofpages:


        url = "https://az-ae-app-fal-prod-webservice.azurewebsites.net/api/lawyer/"

        # payload = '{\"lastName\":\"' + str(
        #     alphabet) + '\",\"lastNameSearchOption\":\"beginsWith\",\"otherName\":\"\",\"suburb\":\"\",\"region\":\"\",\"accreditedSpecialist\":\"\",\"page\":' + str(page) + ',\"pageSize\":1000}'

        payload = '{\"lastName\":\"' + str(
            alphabet) + '\",\"lastNameSearchOption\":\"beginsWith\",\"otherName\":\"\",\"suburb\":\"\",\"region\":\"\",\"accreditedSpecialist\":\"\",\"page\":1,\"pageSize\":' + str(count)   +'}'


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
                # print (item)
                first_name = ''
                last_name= ''
                middleName = ''
                preferredName = ''
                admissionDate = ''
                certificateType = ''
                pcType = ''
                placeOfPractice = ''
                pClass = ''

                streetAddress =''
                postalAddress = ''
                phoneWithAreaCode = ''
                firmFaxWithAreaCode = ''
                fullDx = ''
                firmEmail = ''
                region = ''
                email =''
                specialistAccreditation = ''
                languages = ''


                if 'id' in item:
                    corp_id = item['id']

                    print ('https://az-ae-app-fal-prod-webservice.azurewebsites.net/api/lawyer/' + str(corp_id))

                    response2 = requests.request("GET", 'https://az-ae-app-fal-prod-webservice.azurewebsites.net/api/lawyer/' + str('93004'))

                    json_data2 = json.loads(response2.text)

                    if 'firstName' in json_data2:
                        first_name = json_data2['firstName']

                    if 'lastName' in json_data2:
                        last_name = json_data2['lastName']

                    if 'middleName' in json_data2:
                        middleName = json_data2['middleName']

                    if 'preferredName' in json_data2:
                        preferredName = json_data2['preferredName']

                    if 'admissionDate' in json_data2:
                        admissionDate = json_data2['admissionDate']

                    if 'certificateType' in json_data2:
                        certificateType = json_data2['certificateType']

                    if 'pcType' in json_data2:
                        pcType = json_data2['pcType']

                    if 'placeOfPractice' in json_data2:
                        placeOfPractice = json_data2['placeOfPractice']

                    if 'placeOfPractice' in json_data2:
                        company = json_data2['placeOfPractice']

                    if 'pClass' in json_data2:
                        pClass = json_data2['pClass']

                    if 'streetAddress' in json_data2:

                        if json_data2['streetAddress']:

                            if 'street' in json_data2['streetAddress']:
                                streetAddress = streetAddress + json_data2['streetAddress']['street'] + ' '

                            if 'suburb' in json_data2['streetAddress']:
                                streetAddress = streetAddress + json_data2['streetAddress']['suburb'] + ' '

                            if 'state' in json_data2['streetAddress']:
                                streetAddress = streetAddress + json_data2['streetAddress']['state'] + ' '


                            if 'postCode' in json_data2['streetAddress']:
                                streetAddress = streetAddress + json_data2['streetAddress']['postCode'] + ' '

                    if 'postalAddress' in json_data2:

                        if json_data2['postalAddress']:

                            if 'street' in json_data2['postalAddress']:
                                postalAddress = postalAddress + json_data2['postalAddress']['street'] + ' '

                            if 'suburb' in json_data2['postalAddress']:
                                postalAddress = postalAddress + json_data2['postalAddress']['suburb'] + ' '

                            if 'state' in json_data2['postalAddress']:
                                postalAddress = postalAddress + json_data2['postalAddress']['state'] + ' '


                            if 'postCode' in json_data2['postalAddress']:
                                postalAddress = postalAddress + json_data2['postalAddress']['postCode'] + ' '


                    if 'phoneWithAreaCode' in json_data2:
                        phoneWithAreaCode = json_data2['phoneWithAreaCode']

                    if 'firmFaxWithAreaCode' in json_data2:
                        firmFaxWithAreaCode = json_data2['firmFaxWithAreaCode']

                    if 'fullDx' in json_data2:
                        fullDx = json_data2['fullDx']

                    if 'firmEmail' in json_data2:
                        firmEmail = json_data2['firmEmail']

                    if 'region' in json_data2:
                        region = json_data2['region']

                    if 'email' in json_data2:
                        email = json_data2['email']

                    if 'specialistAccreditation' in json_data2:
                        accr = json_data2['specialistAccreditation']
                        if accr:
                            for acc in accr:
                                specialistAccreditation = specialistAccreditation + acc + ','

                    if 'languages' in json_data2:
                        lang = json_data2['languages']
                        if lang:
                            for lan in lang:
                                languages = languages + lan + ','

                    arr = []
                    temp = []
                    temp.append(first_name)
                    temp.append(last_name)
                    temp.append(middleName)
                    temp.append(preferredName)
                    temp.append(admissionDate)
                    temp.append(certificateType)
                    temp.append(pcType)
                    temp.append(placeOfPractice)

                    temp.append(pClass)
                    temp.append(streetAddress)
                    temp.append(postalAddress)

                    temp.append(phoneWithAreaCode)
                    temp.append(firmFaxWithAreaCode)
                    temp.append(fullDx)
                    temp.append(firmEmail)
                    temp.append(region)
                    temp.append(email)
                    temp.append(specialistAccreditation)
                    temp.append(languages)

                    arr.append(temp)

                    # print (arr)

                    with open('new123.csv', 'a+') as csvfile:
                        csvwriter = csv.writer(csvfile)
                        csvwriter.writerows(arr)




        # page = page + 1




if __name__ == '__main__':

    file = open('alphabet.txt','r')

    for f in file:
        alpha = f.replace('\n','')
        get_list(alpha)

        done = open('done.txt','a+')
        done.write(alpha + '\n')
        done.close()