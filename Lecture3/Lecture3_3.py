
def find_cheapest(beers: dict):
    cheapest = float('inf')
    brand = ""
    for beer, values in beers.items():
        if values["price"]<cheapest:
            cheapest = values["price"]
            brand = beer
    return brand

def quality_for_money(beers: dict):
    best = 0
    brand = ""
    for beer, values in beers.items():
        if (values["quality"]/values["price"])>best:
            best = values["quality"]/values["price"]
            brand = beer
    return brand

beers = {
    "Starobrno": {"price": 12, "quality": 1},
    "Gambrinus": {"price": 25, "quality": 4},
    "Svijany": {"price": 44, "quality": 5},
    "Pilsner": {"price": 50, "quality": 5},
    "Argus": {"price": 14, "quality": 2},
}

cheapest=find_cheapest(beers)
best = quality_for_money(beers)
print("The cheapest beer is ",cheapest,"which costs ", beers[cheapest]["price"], "and has a quality: ", beers[cheapest]["quality"],"/5")
print("The quality for money beer is ",best,"which costs ", beers[best]["price"], "and has a quality: ", beers[best]["quality"],"/5")