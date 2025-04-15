#   Expects the user to specify as a command-line argument the number of Bitcoins,
#   , that they would like to buy. If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.

#   Queries the API for the CoinCap Bitcoin Price Index at rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey. You should replace YourApiKey with the actual API key you obtained from your CoinCap account dashboard, which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float. Be sure to catch any exceptions, as with code like:


#   import requests

#   try:
#       ...
#   except requests.RequestException:
#       ...

#   Outputs the current cost of Bitcoins in USD to four decimal places, using , as a thousands separator.

import requests
import sys
import json


def main():

    if len(sys.argv) != 2:
        sys.exit("needs two arguments")
    while sys.argv[1].isdigit():
        break
    else:
        sys.exit("the second argument must be a positive number")

    try:
        response = requests.get(
            "https://rest.coincap.io/v3/assets?search=BTC&limit=1&apiKey="
        )
    except requests.RequestException:
        sys.exit("something went wrong")

    object = response.json()

    for result in object["data"]:
        price = result["priceUsd"]

    output = float(price) * float(sys.argv[1])

    print(f"{output:.2f}")


if __name__ == "__main__":
    main()
