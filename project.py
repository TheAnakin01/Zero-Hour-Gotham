import json

def main():
    level = load_level("level.json")
    state = {"room": level["start"],"inventory":[]}
    print(describe(level, state))
    while True:
        text = input("> ")
        if text == "quit":
            break
        print(parse_command(text))
        

def load_level(path):
    with open(path, "r") as file:
        level = json.load(file)
        return level

    
def describe(level, state):
    location = state["room"]
    description = level["rooms"][location]["description"]
    exits = level["rooms"][location]["exits"]
    direction = ", ".join(exits)
    describe1 = description + "\n" + direction
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
    elif len(list_text) == 2:
        verb = list_text[0]
        noun = list_text[1]
        return verb, noun


if __name__ == "__main__":
    main()