# Zero Hour Gotham
#### Video Demo : <PASTE YOUR YOUTUBE LINK HERE>
#### Description : Zero Hour Gotham: a JSON-driven text adventure engine in Python.

## The story
Zero Hour Gotham is a text adventure game starring my friend Mr. Karan Sasane, aka 'The Batman'.
It is 11 PM, and Karan has just found out he is on Prof. Varsha's attendance defaulter list.
The list is released at Zero Hour (midnight), so Karan has to sneak through the college campus,
reach the HOD's cabin and remove his name from the list before Prof. Varsha stops him.

Along the way, his friends help him: Gururaj hands him his Batman cape at the gate, Kushal has
his forgotten ID card in the canteen, Vishwesh gives him a flashlight in the library, Abhijit
tosses him the HOD's key in the dark computer lab, and Ajinkya is waiting in the HOD's cabin.

## How to play
Run `python project.py`. The game describes each room, its exits and its items.
Commands:
- `go <direction>`: move to another room
- `take <item>` (or `pick` / `grab`): pick up an item. Some items are needed to unlock doors.
- `inventory`: show the items you are carrying
- `help`: show the list of commands
- `quit`: exit the game

To win, the player must reach the HOD's cabin.

## Folder Structure
```
zero_hour_gotham/
├── project.py          # the game engine and main loop
├── test_project.py     # pytest tests
├── level.json          # the whole story: rooms, items, locks
├── requirements.txt    # pytest
└── README.md
```

## Files
**project.py** contains the game. `main` loads the level, creates the player's state
(current room, inventory and visited rooms), prints the first room, and then runs a loop
that reads each command and sends it to the right function. The other functions are:
- `load_level(path)`: opens `level.json` and loads the whole level into a dictionary
- `describe(level, state)`: returns the room's text (long on the first visit, short after), plus its exits and items
- `parse_command(text)`: cleans up the player's input and splits it into a verb and a noun
- `move(level, state, direction)`: checks whether the direction exists, whether it is locked, and whether the next room is dark, then moves the player
- `take(level, state, item)`: moves an item from the room's item list into the inventory
- `is_won(level, state)`: checks whether the player is in the win room

**level.json** stores the whole story: the rooms, their descriptions (long and short),
exits, items, locked doors with their custom messages, and the dark room.
The game starts in `gate`, and the win room is `hod_cabin`.

**test_project.py** tests `parse_command`, `take`, `move` and `is_won` with pytest,
using small fake levels instead of the real story. For example, `test_move` checks
that the player can't walk in a direction that doesn't exist, can't pass a locked
door without the right item, can't enter a dark room without the flashlight, and
can move once they have the item.

**requirements.txt** lists `pytest`, which is needed to run the tests.
The game itself only uses Python's built-in `json` module.

## Technologies Used
- Python 3
- `json` (built-in) to load the story from `level.json`
- `pytest` for automated tests

## How to Run the Tests
```
pip install -r requirements.txt
pytest test_project.py
```

## Future Improvements
- A Zero Hour clock: every move costs 5 minutes, and the player loses at midnight
- Prof. Varsha catches the player if they enter her corridor without the chai
- ZERO HOUR GOTHAM 2: THE PRACTICALS, loaded as a second level file
- A `look` command to read the long description again
- Colors in the terminal with the `rich` library