import requests
import math
import time

BOT_ID = "DZUKEL_test"
BOT_KEY = "KEY3321"
ARENA_ID = "Valhalla_calling"
ARENA_KEY = "arena321"
arena_id = "6752e3a7e057a15f2ddc11ec"
bot_id = "6752d8f2a62067adad4d0c4b"

"""

print("----1----")
url_arenas = "https://hamer.rcenter.cz/api/arena"
response = requests.get(url_arenas)

if response.status_code == 200:
    arenas = response.json()
    print(f"There are {len(arenas)} arenas available.")
else:
    print(f"Failed to fetch arenas. Status code: {response.status_code}")

print("----2----")
url_player = "https://hamer.rcenter.cz/api/player"
payload = {
    "name": BOT_ID, 
    "key": BOT_KEY     
}

response = requests.post(url_player, json=payload)
bot_id = 0
if response.status_code == 200:
    bot_data = response.json()
    bot_id = bot_data['_id']
    print(f"Bot created successfully! Bot ID: {bot_id}")
else:
    print(f"Failed to create bot. Status code: {response.status_code}, Message: {response.text}")


print("----3----")
url_create_arena = "https://hamer.rcenter.cz/api/arena"
arena_payload = {
    "name": ARENA_ID,  
    "key": ARENA_KEY     
}

response = requests.post(url_create_arena, json=arena_payload)
arena_id = ""
if response.status_code == 200:
    arena_data = response.json()
    arena_id = arena_data["_id"]
    print(f"Arena created successfully! Arena ID: {arena_id}")
else:
    print(f"Failed to create arena. Status code: {response.status_code}, Message: {response.text}")

    
"""
url_assign_bot = "https://hamer.rcenter.cz/api/arena/" + arena_id
bot_payload = {
    "_id": bot_id,      
    "key": BOT_KEY     
}
headers = {
    "Content-Type": "application/json",
    "Arena-API-Key": ARENA_KEY  
}


response = requests.put(url_assign_bot, json=bot_payload, headers=headers)


if response.status_code == 200:
    print(f"Bot successfully assigned to the arena!")
else:
    print(f"Failed to assign bot. Status code: {response.status_code}, Message: {response.text}")





ARENA_URL = f"https://hamer.rcenter.cz/api/arena/{arena_id}"
PLAYER_URL = f"https://hamer.rcenter.cz/api/player/{bot_id}"

bot_headers = {
    "Content-Type": "application/json",
    "Player-API-Key": BOT_KEY
}


def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


def normalize_vector(dx, dy):
    magnitude = math.sqrt(dx**2 + dy**2)
    if magnitude == 0:
        return 0, 0
    return dx / magnitude, dy / magnitude

while True:
    arena_response = requests.get(ARENA_URL, headers={"Arena-API-Key": ARENA_KEY})
    if arena_response.status_code != 200:
        print(f"Failed to fetch arena data: {arena_response.text}")
        break

    arena_data = arena_response.json()
    bot = next((p for p in arena_data["players"] if p["_id"] == bot_id), None)
    if not bot:
        print("Bot not found in the arena.")
        break

    bot_x, bot_y, bot_radius = bot["position"]["x"], bot["position"]["y"], bot["radius"]
    foods = arena_data["foods"]
    other_players = arena_data["players"]


    nearest_food = None
    min_distance = float("inf")
    for food in foods:
        distance = calculate_distance(bot_x, bot_y, food["position"]["x"], food["position"]["y"])
        if distance < min_distance:
            nearest_food = food
            min_distance = distance

    if not nearest_food:
        print("No food available.")


    danger_bots = [
        player for player in other_players
        if player["_id"] != BOT_ID and player["radius"] >= 2 * bot_radius
    ]
    safe_food = nearest_food
    for danger_bot in danger_bots:
        danger_distance = calculate_distance(bot_x, bot_y, danger_bot["position"]["x"], danger_bot["position"]["y"])
        if danger_distance < bot_radius + danger_bot["radius"]:
            safe_food = None
            print("Avoiding danger bot!")

    if not safe_food:
        print("No safe food available.")
    else:
        dx, dy = safe_food["position"]["x"] - bot_x, safe_food["position"]["y"] - bot_y
        print(f"Moving bot towards food at ({safe_food["position"]['x']}, {safe_food["position"]['y']})")
        move_x, move_y = normalize_vector(dx, dy)


    move_payload = {
        "move": {
            "x": move_x,
            "y": move_y
        }
    }

    move_response = requests.put(PLAYER_URL, json=move_payload, headers=bot_headers)
    if move_response.status_code != 200:
        print(f"Failed to move bot: {move_response.text}")
        break

    time.sleep(0.1)
