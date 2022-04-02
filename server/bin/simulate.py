

import requests
import os
import random
from starlette.config import environ


# set test config
environ["DB_PASS"] = "rootsql"
environ["DB_HOST"] = "127.0.0.1"
environ["DB_NAME"] = "baking-db-test-" + str(random.random())
environ["DB_USER"] = "postgres"

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
WORDS = response.content.splitlines()

TOTAL_RECIPES = 2

URL = "http://localhost:8888"
# URL = "https://service.baking.reubinoff.com"

def get_types():
    from baking.routers.ingredients.enums import IngrediantType
    TYPES = list(map(str, IngrediantType))
    return TYPES

def get_words(num_of_words):
    return ' '.join([WORDS[random.randint(0, len(WORDS))].decode() for i in range(num_of_words)])

def create_recipes():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    files = [{'file': open(current_directory+'/test_a.jpeg', 'rb')}, {'file': open(current_directory+'/test_b.jpeg', 'rb')}]
    for i in range(1, TOTAL_RECIPES):
        p = []
        for j in range(1, random.randint(2, 5)):
            ingredients = []
            for k in range(1, random.randint(2, 7)):
                type = get_types()[random.randint(0, len(get_types())-1)]
                ingredients.append( {
                    "name": f"i_{get_words(random.randint(1,3))}_{k}",
                    "quantity": random.randint(1, 1000),
                    "units": "Grams",
                    "type": type,
                })
            p.append({
                "name": f"procedure_{i}_{j}",
                "description": get_words(random.randint(1, 10)),
                "order": j,
                "ingredients": ingredients
                })
            
        aaa = {
            "name": get_words(2),
            "description": get_words(10),
            "procedures": p
        }
        
        t = requests.post(f"{URL}/recipe", json=aaa)
        print(t.status_code)


    t = requests.get(
        f"{URL}/recipe?page=1&itemsPerPage=500")

    ids = [t["id"] for t in t.json()["items"]]
    print(t.status_code)
    for i in ids:
        t = requests.post(
            f"{URL}/recipe/{i}/img", files=files[i%2])
        
        print(t.status_code)


def delete_all_recipes():
    t = requests.get(
        f"{URL}/recipe?page=1&itemsPerPage=500")

    ids = [t["id"] for t in t.json()["items"]]
    print(t.status_code)
    for i in ids:
        t = requests.delete(f"{URL}/recipe/{i}")
        print(t.status_code)
    print(t.status_code)

if __name__ == "__main__":
    delete_all_recipes()
    create_recipes()