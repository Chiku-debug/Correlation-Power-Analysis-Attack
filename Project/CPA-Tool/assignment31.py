import csv
import json

with open('assignment31.json') as json_file:
    data = json.load(json_file)
    with open('assignment31.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        keylist = []
        for key in data["assignment"]["1"]:
            keylist.append(list(key.keys())[0])
        keylist.insert(0, "Key Part/Possible Key")
        csvwriter.writerow(keylist)

        # print(keylist)
        for keypart in data["assignment"].keys():
            rowContent = []
            for possiblekey in data["assignment"][keypart]:
                key = list(possiblekey.keys())[0]
                rowContent.append(possiblekey[key])
            rowContent.insert(0, keypart)
            csvwriter.writerow(rowContent)
                
            # csvwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
            # csvwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
    # for datapoint in data['assignment']:
    #     print('Name: ' + p['name'])
    #     print('Website: ' + p['website'])
    #     print('From: ' + p['from'])
    #     print('')