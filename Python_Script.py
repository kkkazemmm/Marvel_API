##########################Libraries############################

import json
import urllib3
http = urllib3.PoolManager() #handles details of connection pooling and thread safety

#######################Authentication##########################

public_key = input("Enter your public key: ") #asking for public key
md5_hash = input("Enter your generated md5 hash(timestamp + private key + public key): ") #generated md5 key
print()

request = http.request("GET","http://gateway.marvel.com/v1/public/characters?ts=1&apikey="+public_key+"&hash="+md5_hash) #request to the link
print()


while request.status != 200:
    public_key = input("Connection failed, please try again.\nEnter your public key: ")
    md5_hash = input("Enter your generated md5 hash(timestamp + private key + public key): ")

    request = http.request("GET",
                           "http://gateway.marvel.com/v1/public/characters?ts=1&apikey=" + public_key + "&hash=" + md5_hash)


else:
    print('Connected succesfully to Marvel API!','\n')
    data_decoded = json.loads(request.data.decode('utf-8'))  # decoding data to UTF-8 format
###########################Searching in API#################################

    name = input("Which Marvel comic character do you want to know about?")

    if name in data_decoded['data']['results'][10]['name']:
        print('\n',len(data_decoded['data']['results'][10]['description']) * '•')
        print('\n',name, data_decoded['data']['results'][10]['description'], sep='     ')
        print('\n',len(data_decoded['data']['results'][10]['description']) * '•')
    else:
        print("Not found, try another one please!")

print('\n')
thanks = input("Thank you!")
