# using the requests library to access internet data

#import the requests library
import requests

def main():
    # Use requests to issue a standard HTTP GET request
    url = "https://waterservices.usgs.gov/nwis/site/?format=rdb&stateCd=ri"
    result = requests.get(url)
    printResults(result)

def printResults(resData):
    print("Result code: {0}".format(resData.status_code))
    print("\n")

    print("Headers: ----------------------")
    print(resData.headers)
    print("\n")

    print("Returned data: ----------------------")
    #print(resData.text)
    lines = resData.text.splitlines()
    for l in lines:
        if not l.startswith('#'):
            print(l.split('\t'))

if __name__ == "__main__":
    main()
