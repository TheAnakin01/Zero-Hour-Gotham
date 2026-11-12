import json

def main():
    level = load_level("level.json")
    state = {"room": level["start"],"inventory":[], "visited":[]}
    sentences = ["pick", "grab", "take"]
    print(describe(level, state))
    while True:
        text = input("> ")
        verb, noun = parse_command(text)
        if verb is None:
            continue
        if verb == "quit":
            break
        if verb == "go":
            state, message = move(level, state, noun)
            print(message)
            print(describe(level, state))
            if is_won(level, state):
                break
        elif verb in sentences:
            state, message = take(level, state, noun)
            print(message)
        elif verb == "inventory":
            print(state["inventory"])
        else:
            print("I don't understand.")
        

def load_level(path):
    with open(path, "r", encoding="utf-8") as file:
        level = json.load(file)
        return level

    
def describe(level, state):
    location = state["room"]
    if location not in state["visited"]:
        description1 = level["rooms"][location]["description"]
        state["visited"].append(location)
    else:
        description1 = level["rooms"][location]["short"]
    exits = level["rooms"][location]["exits"]
    direction = "Exits: "  + ", ".join(exits)
    describe1 = description1 + "\n" + direction
    items = level["rooms"][location]["items"]
    elongated_items = "Items: " + ", ".join(items)
    len_items = len(items)
    if len_items != 0:
        describe1 = description1 + "\n" + direction + "\n" + elongated_items
    return describe1


def parse_command(text):
    list_text = text.lower().split()
    if len(list_text) == 0:
        verb = None
        noun = None
        return verb, noun
    elif len(list_text) == 1:
        verb = list_text[0]
        noun = None
        return verb, noun
    else: 
        verb = list_text[0]
        noun = list_text[-1]
        return verb, noun


def move(level, state, direction):
    current = state["room"]
    current_exit = level["rooms"][current]["exits"]
    inventory = state["inventory"]
    if direction not in current_exit:
        return state, "You can't go that way."
    if "locked" in level["rooms"][current]:
        if direction in level["rooms"][current]["locked"]:
            need = level["rooms"][current]["locked"][direction]
            text = level["rooms"][current]["locked_text"][direction]  
            if need not in inventory:
                return state, text

    target = current_exit[direction]
    target_room = level["rooms"][target]
    if target_room.get("dark", False) and "flashlight" not in inventory:
        return state, target_room["dark_text"]

    state["room"] = current_exit[direction]
    return state, f"You go {direction}."


def take(level, state, item):
    location = state["room"]
    items = level["rooms"][location]["items"]
    if item in items:
        items.remove(item)
        state["inventory"].append(item)
        return state, f"You picked up the {item}."
    else:
        return state, f"There's no {item} here."


def is_won(level, state):
    if state["room"] == level["win_room"]:
        return True
    else:
        return False


if __name__ == "__main__":
    main()