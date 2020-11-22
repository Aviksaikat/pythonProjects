import requests
import json

def main():

    content = requests.get("https://cve.circl.lu/api/last")
    jsonData = content.json()

    for item in jsonData:
        print("{} {}".format("Vuln Num:", item['id']))
        print("{} {}\n".format("Description:", item['summary']))

main()