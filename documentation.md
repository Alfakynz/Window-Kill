# Quadratic Invaders

## ASCII Objects

```python
class ASCII()
```

Class that manages the ASCII font.

#### \_\_init\_\_

```python
def __init__() -> None
```

For each character, see ascii.txt (not included into the documentation, see the repo on [GitHub](https://github.com/Alfakynz/Quadratic-Invaders)).
Each character is represented by an array of 3 strings (top, middle, bottom).

#### convert

```python
def convert(string: str) -> list[str]
```

Convert each character into an ASCII font. For each character, get the top/mid/bottom part of letters from self.alphabet.

**Arguments**:

- `string` _str_ - The string to convert.

**Returns**:

- `list[str]` - An array with top/mid/bottom of the string for each character.

#### text

```python
def text(x: float, y: float, text: str, color: int) -> None
```

Display a converted text with pyxel. Display the top/mid/bottom parts of the ASCII font one below the other.

**Arguments**:

- `x` _float_ - The x location of the text.
- `y` _float_ - The y location of the text.
- `text` _str_ - The text to convert.
- `color` _int_ - The color to use.

## Character Objects

```python
class Character()
```

Class that manages characters (for the player and enemies).

#### \_\_init\_\_

```python
def __init__(color: int, hp: int, hp_max: int, attack: int, speed: int,
             shield: int, fire_rate: int, xp: int) -> None
```

**Arguments**:

- `color` _int_ - Character color.
- `hp` _int_ - Current health of the character.
- `hp_max` _int_ - Maximum health of the character.
- `attack` _int_ - Base attack damage the character can inflict.
- `speed` _int_ - Movement speed of the character.
- `shield` _int_ - Amount of damage the character can block before losing hp.
- `fire_rate` _int_ - Delay between attacks.
- `xp` _int_ - Experience points awarded when the character is defeated.

#### teta\_calculation

```python
def teta_calculation(coord1: tuple[float, float],
                     coord2: tuple[float, float]) -> float
```

Method that calculates teta, direction from the pole relative to the direction of the polar axis (polar coordinates), according to two tuples of coordinates.

**Arguments**:

- `coord1` _tuple[float, float]_ - Origin point (x1, y1) from which the direction is measured.
- `coord2` _tuple[float, float]_ - Target point (x2, y2) toward which the direction is calculated.

**Returns**:

- `float` - Angle teta in radians in the range [-π, π], representing the direction from coord1 to coord2.

#### polar\_to\_cartesian

```python
def polar_to_cartesian(teta: float,
                       r: float,
                       offset: float = 0) -> tuple[float, float]
```

Method that turns polar coordinates into cartesian coordinates.

**Arguments**:

- `teta` _float_ - Angle in radians representing the polar coordinate
- `r` _int_ - size or distance from the origin.
- `offset` _float, optional_ - Additional angular shift in radians applied to teta. Useful in the draw method of the Player class. Defaults to 0.

**Returns**:

  tuple[float, float]: tuple containing the (x, y) cartesian coordinates corresponding to the given polar coordinates.

#### receive\_damage

```python
def receive_damage(amount: int, hp: int, shield: int) -> int
```

Apply damage based on incoming damage and shield percentage.

**Arguments**:

- `amount` _int_ - The raw amount of damage inflicted.
- `hp` _int_ - The current hp.
- `shield` _int_ - The shield percentage reducing incoming damage (0-100).

**Returns**:

- `int` - The updated hp after applying damage (minimum 0).

## Control Objects

```python
class Control()
```

Class that manages the control screen

#### \_\_init\_\_

```python
def __init__() -> None
```

Create the control informations

#### toggle\_menu

```python
def toggle_menu() -> None
```

A function to toggle on/off the controls view

#### update

```python
def update(menu) -> None
```

Handle user input to quit the controls.

**Arguments**:

- `menu` _Menu_ - The main menu to return to.

#### draw

```python
def draw() -> None
```

Draw the controls.

## Enemy Objects

```python
class Enemy(TypedDict)
```

An enemy with their characteristics.

**Arguments**:

- `x` _float_ - The x position.
- `y` _float_ - The y position.
- `reverse` _bool_ - Repulse effect when the enemy touches the player.
- `teta` _float_ - The direction from the pole relative to the direction of the polar axis.
- `count_bullet` _int_ - The time after having touched a bullet.
- `bullet_touched` _bool_ - True if collided with a bullet, False otherwise.
- `color` _int_ - The enemy color.
- `hp` _int_ - The enemy hp.
- `attack` _int_ - The enemy attack.
- `speed` _float_ - The enemy speed.
- `shield` _int_ - The enemy shield.
- `fire_rate` _float_ - The enemy fire rate.
- `xp` _int_ - The enemy xp.
- `knockback_speed` _float_ - Speed at which the enemy is knockbacked when they collide with the player.

## Menu Objects

```python
class Menu()
```

Class that displays the menu.

#### \_\_init\_\_

```python
def __init__() -> None
```

Create the menu.

#### toggle\_menu

```python
def toggle_menu() -> None
```

A function to toggle on/off the menu

#### update

```python
def update(controls: Control, game) -> None
```

Handle user input to navigate.

**Arguments**:

- `controls` _Control_ - The controls menu.
- `game` _Game_ - The main game instance.

#### draw

```python
def draw(game) -> None
```

Draw the menu.

## Skill Objects

```python
class Skill()
```

Class that manages the skills.

#### \_\_init\_\_

```python
def __init__(name: str,
             description: str,
             price: int,
             amount: int,
             level: int = 0) -> None
```

Create a skill with a name, description, price, amount and level.

**Arguments**:

- `name` _str_ - The skill name.
- `description` _str_ - The skill description.
- `price` _int_ - The skill price.
- `amount` _int_ - The skill amount represents how much the skill increases.
- `level` _int_ - The skill level, 0 by default.

## Bullets Objects

```python
class Bullets()
```

Class that manages the bullets shot by the player.

#### \_\_init\_\_

```python
def __init__(player_x: int, player_y: int) -> None
```

Initializes the class Bullet.

**Arguments**:

- `player_x` _int_ - Player x position.
- `player_y` _int_ - Player y position.

#### bullets\_creation

```python
def bullets_creation() -> None
```

Creates bullets every time a specific amount of frames is counted and when left click is continuously pressed.

#### bullets\_movements

```python
def bullets_movements(polar_to_cartesian: Callable) -> None
```

Moves the bullet towards the place the mouse clicked and removes it when it goes out of bounds.

**Arguments**:

- `polar_to_cartesian` _Callable_ - A Callable function that converts polar coordinates into cartesian coordinates.

#### update

```python
def update(polar_to_cartesian: Callable, enemies_array: list[Enemy],
           enemies_size: int, window_width: int, window_height: int,
           fire_rate: int, teta: float) -> None
```

Method that updates everything inside and is called infinitely in the class Player.

**Arguments**:

- `polar_to_cartesian` _Callable_ - A callable function
- `enemies_array` _list[Enemy]_ - Array containing the enemies created and still alive.
- `enemies_size` _int_ - Size of the enemies.
- `window_width` _int_ - Width of the window.
- `window_height` _int_ - Height of the window.
- `fire_rate` _int_ - Number of frames counted each time a bullet is shot.
- `teta` _float_ - value of teta between the position of the mouse and the position of the player

#### draw

```python
def draw() -> None
```

Method that draws the bullets on the window and is called infinitely in the class Player.

## Player Objects

```python
class Player(Character)
```

Class that manages the player and inherits the characteristics of the class Character.

#### \_\_init\_\_

```python
def __init__(window_width: int,
             window_height: int,
             color: int = 7,
             hp: int = 10,
             hp_max: int = 10,
             attack: int = 1,
             speed: int = 4,
             shield: int = 0,
             fire_rate: int = 60,
             xp: int = 0) -> None
```

Initialize the class Player.

**Arguments**:

- `color` _int_ - The player color.
- `hp` _int_ - The player hp.
- `attack` _int_ - The player attack.
- `speed` _int_ - The player speed.
- `shield` _int_ - The player shield.
- `fire_rate` _int_ - The player fire rate.
- `xp` _int_ - The player xp.

#### player\_movements

```python
def player_movements() -> None
```

Move the player according to the arrow keys pressed and stops it when it is about to go out of bounds.

#### damage

```python
def damage() -> None
```

Checks collision between the player and every enemy, then applies damage and handles temporary invincibility.

#### add\_xp

```python
def add_xp(amount: int) -> None
```

Method that adds xp.

**Arguments**:

- `amount` _int_ - The amount of xp to add.

#### update

```python
def update(enemies_array: list[Enemy], enemies_size: int, enemies_attack: int,
           window_width: int, window_height: int) -> None
```

Method that updates everything inside and is called infinitely in the class Game.

**Arguments**:

- `enemies_array` _list[Enemy]_ - Array containing the enemies created and still alive.
- `enemies_size` _int_ - Size of the enemies.
- `enemies_attack` _int_ - Amount of hp that the enemies remove to the player when they collide with them.
- `window_width` _int_ - Width of the window.
- `window_height` _int_ - Height of the window.

#### draw

```python
def draw() -> None
```

Method that draws the objects on the window and is called infinitely in the class Game.

#### draw\_hp

```python
def draw_hp() -> None
```

Method that draws the hp on the window.

#### draw\_xp

```python
def draw_xp() -> None
```

Method that draws the xp on the window.

#### draw\_time

```python
def draw_time(minutes: int, seconds: int) -> None
```

Method that draws the time on the window.

**Arguments**:

- `minutes` _int_ - The number of minutes.
- `seconds` _int_ - The number of seconds.

## Upgrade Objects

```python
class Upgrade()
```

Class that displays the upgrade menu.

#### \_\_init\_\_

```python
def __init__(player: Player) -> None
```

Create the upgrade menu to buy skills upgrades.

**Arguments**:

- `player` _Player_ - The Player.

#### increase

```python
def increase(skill: str) -> None
```

Increase the selected skill of the player if he has enough XP.

**Arguments**:

- `skill` _str_ - The skill to improve

#### update

```python
def update() -> None
```

Handle user input to navigate and purchase upgrades.

#### draw

```python
def draw() -> None
```

Draw the upgrade menu.

#### draw\_hp

```python
def draw_hp(x: int, y: int) -> None
```

Method that draws the hp on the window.

**Arguments**:

- `x` _int_ - The x position of the text.
- `y` _int_ - The y position of the text.

#### draw\_time

```python
def draw_time(x: int, y: int) -> None
```

Method that draws the time on the window.

**Arguments**:

- `x` _int_ - The x position of the text.
- `y` _int_ - The y position of the text.

## Enemies Objects

```python
class Enemies(Character)
```

Class that manages the enemies and inherits the characteristics of the class Character.

#### \_\_init\_\_

```python
def __init__(player: Player,
             color: int = 4,
             hp: int = 1,
             hp_max: int = 1,
             attack: int = 1,
             speed: int = 2,
             shield: int = 0,
             fire_rate: int = 60,
             xp: int = 1) -> None
```

Initializes the class Enemies

**Arguments**:

- `color` _int_ - Character color (not yet implemented).
- `hp` _int_ - Current health of the character.
- `hp_max` _int_ - Maximum health of the character.
- `attack` _int_ - Base attack damage the character can inflict.
- `speed` _int_ - Movement speed of the character.
- `shield` _int_ - Amount of damage the character can block before losing hp.
- `fire_rate` _int_ - Delay between attacks.
- `xp` _int_ - Experience points awarded when the character is defeated.

#### enemies\_creation

```python
def enemies_creation() -> None
```

"
Creates an enemy on a random side of the map every time a specific amount of frames is counted.

#### enemies\_movements

```python
def enemies_movements() -> None
```

Moves the enemies towards the player.

#### player\_collision

```python
def player_collision() -> None
```

Method that checks the collisions between enemies and the player.

#### bullet\_collision

```python
def bullet_collision(player: Player) -> None
```

Method that checks the collision between enemies and the bullets.

#### enemies\_upgrade

```python
def enemies_upgrade(in_control: bool, in_menu: bool,
                    in_upgrade_menu: bool) -> None
```

Method that upgrades a skill of the enemies every 10 seconds.

**Arguments**:

- `in_control` _bool_ - True if the control menu is displayed, False otherwise
- `in_menu` _bool_ - True if the main menu is displayed, False otherwise
- `in_upgrade_menu` _bool_ - True if the upgrade menu is displayed, False otherwise

#### update

```python
def update(player_x: int, player_y: int, player_size: int, player_attack: int,
           bullets_array: list[list[float]], bullet_size: int,
           window_width: int, window_height: int, in_control: bool,
           in_menu: bool, in_upgrade_menu: bool) -> None
```

Method that updates everything inside and is called infinitely in the class Game.

**Arguments**:

- `player_x` _int_ - X position of the player.
- `player_y` _int_ - Y position of the player.
- `player_size` _int_ - Size of the player.
- `player_attack` _int_ - Amount of hp that the player removes to an enemy when a bullet collides with them.
- `bullets_array` _list[list[float, float, float]]_ - Array containing the bullets shot and still in the window.
- `bullet_size` _int_ - Size of the bullets.
- `window_width` _int_ - Width of the window.
- `window_height` _int_ - Height of the window.
- `in_control` _bool_ - True if the control menu is displayed, False otherwise
- `in_menu` _bool_ - True if the main menu is displayed, False otherwise
- `in_upgrade_menu` _bool_ - True if the upgrade menu is displayed, False otherwise

#### draw

```python
def draw() -> None
```

Method that draws the enemies on the window and is called infinitely in the class Game.

## Game Objects

```python
class Game()
```

Class that manages the game in general.

#### \_\_init\_\_

```python
def __init__() -> None
```

Initialize the class Player.

#### update

```python
def update() -> None
```

Method that calls all the update methods of every class and is called infinitely by Pyxel.

#### draw

```python
def draw() -> None
```

Method that calls all the draw methods of every class and is called infinitely by Pyxel.

#### load\_image\_as\_array

```python
def load_image_as_array(path: str, color: int = 12) -> list[list[int]]
```

Load an image and convert it to a 2D array of pixel colors based on transparency.
Open the image using PIL, then get the image size and create a 2D array where each pixel is represented by the specified color if its alpha value is above a threshold, otherwise 0 (transparent).

**Arguments**:

- `path` _str_ - The file path to the image.
- `color` _int_ - The color to use for non-transparent pixels.

**Returns**:

- `list[list[int]]` - A 2D array representing the image pixels.

#### draw\_cursor

```python
def draw_cursor(x, y) -> None
```

Draw a custom cursor at the specified position. Used to replace the default mouse cursor.

**Arguments**:

- `x` _int_ - the x-coordinate to draw the cursor.
- `y` _int_ - the y-coordinate to draw the cursor.

#### restart\_game

```python
def restart_game() -> None
```

Restart the game to its initial state.

#### test

```python
def test(name: str, test1, test2) -> None
```

Function to test 2 args with an assert.

**Arguments**:

- `name` _str_ - Name of the test.
- `test1` _any_ - The first item to test
- `test2` _any_ - The second item to test

#### jeux\_de\_test

```python
def jeux_de_test() -> None
```

Function that tests most functions in the project.