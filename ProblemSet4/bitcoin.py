import sys
import requests
 
# command line argument with number of bitcoin x they want to buy
while True:
    try:
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=2856c97eb07509100c8e5e4b493208169aed5fd1b6d97ecdeeaa33c606a984a1")
        o = response.json()
        price = float(o["data"]["priceUsd"])
        if len(sys.argv) == 1:
            sys.exit("Missing command-line argument")
        elif len(sys.argv) > 2:
            sys.exit("To many arugments in command-line arguments")
        else:
            x = float(sys.argv[1])
            output = x * price
            print(f"${output:,.4f}")
            break
    except (ValueError, requests.RequestException):
        sys.exit("Command-line argument is not a number")