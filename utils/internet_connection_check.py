import requests

apiurl = 'https://homeautomationlp.cyclic.app'
timeoutCheck = 1

def internetConnectionCheck():

    try:
        request = requests.get(apiurl, timeout=timeoutCheck)
        print("connected to the internet")
        internetConnectionExists = True



    except (requests.ConnectionError, requests.Timeout) as exception:
        print("no internet connection")
        internetConnectionExists = False

    return internetConnectionExists

internetConnectionCheck()