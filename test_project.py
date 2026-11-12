from project import is_won, take, move, parse_command

def test_is_won():
    level = {"win_room": "hod_cabin"}
    assert is_won(level, {"room": "hod_cabin"}) == True
    assert is_won(level, {"room": "gate"}) == False
    assert is_won(level, {"room": "canteen"}) == False
    assert is_won(level, {"room": "corridor"}) == False
    assert is_won(level, {"room": "library"}) == False
    assert is_won(level, {"room": "lab"}) == False
    assert is_won(level, {"room": "staff_corridor"}) == False


def test_parse_command():
    assert parse_command(" GO East") == ("go", "east")
    assert parse_command("look") == ("look", None)
    assert parse_command("") == (None, None)
    assert parse_command("take id card") == ("take", "card")
    assert parse_command("pick up chai") == ("pick", "chai")


def test_take():
    level = {"rooms": {"canteen": {"items": ["card", "chai"]}}}
    state = {"room": "canteen", "inventory": []}
    state, message = take(level, state, "card")

    assert "card" in state["inventory"]
    assert "card" not in level["rooms"]["canteen"]["items"]
    assert message == "You picked up the card."

    state, message = take(level, state, "banana")
    assert message == "There's no banana here."
    assert "banana" not in state["inventory"]

    level = {"rooms": {"gate": {"items": ["cape"]}}}
    state = {"room": "gate", "inventory": []}
    state, message = take(level, state, "cape")

    assert "cape" in state["inventory"]
    assert "cape" not in level["rooms"]["gate"]["items"]


def test_move():
    level = {"rooms": {
        "gate":     {"exits": {"north": "corridor"},
                     "locked": {"north": "card"},
                     "locked_text": {"north": "Need card."}},
        "corridor": {"exits": {"south": "gate", "east": "lab"}},
        "lab":      {"exits": {"west": "corridor"},
                     "dark": True,
                     "dark_text": "Too dark."}
    }}
    state = {"room": "gate", "inventory": []}

    
    state, message = move(level, state, "west")
    assert state["room"] == "gate"
    assert message == "You can't go that way."

    
    state, message = move(level, state, "north")
    assert state["room"] == "gate"
    assert message == "Need card."

    
    state["inventory"].append("card")
    state, message = move(level, state, "north")
    assert state["room"] == "corridor"

    
    state, message = move(level, state, "east")
    assert state["room"] == "corridor"
    assert message == "Too dark."

    
    state["inventory"].append("flashlight")
    state, message = move(level, state, "east")
    assert state["room"] == "lab"