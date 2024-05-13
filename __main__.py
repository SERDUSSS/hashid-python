# curl 'https://hashes.com/es/api/identifier?hash=de41a78c493da23f00e0f7343c9aeaed:88581&extended=true' 

import requests
import json
import sys


def parse_options():
    if len(sys.argv) != 2:
        sys.exit("Error, argumentos invalidos")

def main():
    parse_options()
    hash = sys.argv[1]
    response = requests.get(f"https://hashes.com/es/api/identifier?hash={hash}&extended=true").text
    data = json.loads(response)

    if data["success"]:
        print(data["algorithms"])
    else:
        print("Unknown hash")

if __name__ == "__main__":
    main()
