import pyxel
import math
from characters import Character
from bullets import Bullets
from ascii import ASCII
from enemy import Enemy

class Player(Character):
    """
    Class that manages the player and inherits the characteristics of the class Character.
    """

    def __init__(self,
                 window_width: int,
                 window_height: int,
                 color: int = 7, # white
                 hp: int = 10, # health points
                 hp_max: int = 10, # max health points
                 attack: int = 1, # amount of hp that the player removes to the enemies touched by a bullet
                 speed: int = 4, # speed at which the player moves (in cartesian coordinates)
                 shield: int = 0, # reduces the damage taken
                 fire_rate: int = 60, # number of frames counted each time a bullet is shot
                 xp: int = 0) -> None: # amount of experience points collected by the player
        """
        Initialize the class Player.

        Args:
            color (int): The player color.
            hp (int): The player hp.
            attack (int): The player attack.
            speed (int): The player speed.
            shield (int): The player shield.
            fire_rate (int): The player fire rate.
            xp (int): The player xp.
        """

        super().__init__(color, hp, hp_max, attack, speed, shield, fire_rate, xp) #calls the __init__ method of the parent class
        
        self.ascii: ASCII = ASCII()

        #initializes the attributes related to the window
        self.WINDOW_WIDTH: int = window_width # width of the window
        self.WINDOW_HEIGHT: int = window_height # height of the window
        
        # player's starting position
        self.player_x: int = self.WINDOW_WIDTH // 2
        self.player_y: int = self.WINDOW_HEIGHT // 2

        self.SIZE: int = 20 # distance from the pole in polar coodinates (also size)
        self.took_damage: bool = False
        self.count: int = 0

        #initializes the attributes related to the enemies
        self.enemies_array: list[Enemy] = []
        self.enemies_damage: int = 0
        self.ENEMY_SIZE: int = 0

        self.bullets: Bullets = Bullets(self.player_x, self.player_y) # creates the objet Bullets

        self.teta: float = 0.0  # default orientation to avoid draw() crash

        self.time = 0

    def player_movements(self) -> None:
        """
        Move the player according to the arrow keys pressed and stops it when it is about to go out of bounds.
        """

        if (pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D)) and self.player_x < self.WINDOW_WIDTH:
            self.player_x += self.skills["speed"] # moves to the right
            #print("right")
            for enemy in self.enemies_array:
                if enemy["x"] <= self.player_x+self.SIZE and enemy["y"] <= self.player_y+self.SIZE and enemy["x"]+self.ENEMY_SIZE >= self.player_x and enemy["y"]+self.ENEMY_SIZE >= self.player_y:
                    self.player_x -= self.skills["speed"]
                    #print("blocked right")
        if (pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_Q)) and self.player_x > 0:
            self.player_x -= self.skills["speed"] # moves to the left
            #print("left")
            for enemy in self.enemies_array:
                if enemy["x"] <= self.player_x+self.SIZE and enemy["y"] <= self.player_y+self.SIZE and enemy["x"]+self.ENEMY_SIZE >= self.player_x and enemy["y"]+self.ENEMY_SIZE >= self.player_y:
                    self.player_x += self.skills["speed"]
                    #print("blocked left")
        if (pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.KEY_S)) and self.player_y < self.WINDOW_HEIGHT:
            self.player_y += self.skills["speed"] # moves down
            #print("down")
            for enemy in self.enemies_array:
                if enemy["x"] <= self.player_x+self.SIZE and enemy["y"] <= self.player_y+self.SIZE and enemy["x"]+self.ENEMY_SIZE >= self.player_x and enemy["y"]+self.ENEMY_SIZE >= self.player_y:
                    self.player_y -= self.skills["speed"]
                    #print("blocked down")
        if (pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_Z)) and self.player_y > 0:
            self.player_y -= self.skills["speed"] # moves up
            #print("up")
            for enemy in self.enemies_array:
                if enemy["x"] <= self.player_x+self.SIZE and enemy["y"] <= self.player_y+self.SIZE and enemy["x"]+self.ENEMY_SIZE >= self.player_x and enemy["y"]+self.ENEMY_SIZE >= self.player_y:
                    self.player_y -= self.skills["speed"]
                    #print("blocked up")

    def damage(self) -> None:
        """
        Checks collision between the player and every enemy, then applies damage and handles temporary invincibility.
        """

        #print(self.took_damage)
        for enemy in self.enemies_array:
            if enemy["x"] <= self.player_x+self.SIZE and enemy["y"] <= self.player_y+self.SIZE and enemy["x"]+self.ENEMY_SIZE >= self.player_x and enemy["y"]+self.ENEMY_SIZE >= self.player_y and self.took_damage == False: #checks collision and if the player is invincible
                #print("hp before dmg", self.skills["hp"])
                self.skills["hp"] = self.receive_damage(self.enemies_damage, self.skills["hp"], self.skills["shield"]) #damages the player
                #print("hp after dmg", self.skills["hp"])
                self.color = 13 #turns the player grey to show that he is now invincible and that he took some damage
                self.took_damage = True #turns on the invincibility
            
            if self.took_damage == False:
                self.count = 0 #puts the frame counter back to 0 when the invincibility is turned off

            elif self.took_damage == True:
                self.count += 1 #counts the number of frames since the invincibility is turned on

            if self.count >= 60: #checks if 1 second had passed since the invinbility is turned on
                self.color = 7 #turns the player back to white
                self.took_damage = False #turns off the invincibility

    def add_xp(self, amount: int) -> None:
        """
        Method that adds xp.

        Args:
            amount (int): The amount of xp to add.
        """

        #print("before", self.xp)
        self.xp += amount
        #print("after", self.xp)

    def update(self, enemies_array: list[Enemy], enemies_size: int, enemies_attack: int, window_width: int, window_height: int) -> None:
        """
        Method that updates everything inside and is called infinitely in the class Game.

        Args:
            enemies_array (list[Enemy]): Array containing the enemies created and still alive.
            enemies_size (int): Size of the enemies.
            enemies_attack (int): Amount of hp that the enemies remove to the player when they collide with them.
            window_width (int): Width of the window.
            window_height (int): Height of the window.
        """

        #print("Player update works")
        #updates the attributes related to the enemies
        self.enemies_array = enemies_array
        self.ENEMY_SIZE = enemies_size
        self.enemies_damage = enemies_attack

        #updates the attributes related to the window
        self.WINDOW_WIDTH = window_width
        self.WINDOW_HEIGHT = window_height

        self.player_movements() # moves the player

        self.damage() #damages the player

        # gives the position of the player to the bullet
        self.bullets.player_x = self.player_x
        self.bullets.player_y = self.player_y

        # calculates the teta between the position of the mouse and the position of the player (polar coordinates)
        self.teta: float = self.teta_calculation((pyxel.mouse_x, pyxel.mouse_y), (self.player_x, self.player_y))
        #print(self.teta)
        self.bullets.update(self.polar_to_cartesian, enemies_array, enemies_size, window_width, window_height, self.skills["fire_rate"], self.teta) # updates the bullets

    def draw(self) -> None:
        """
        Method that draws the objects on the window and is called infinitely in the class Game.
        """

        #print("Player draw works")
        self.time += 1

        # conversion of polar coordinates into cartesian coordinates for the vertex of the triangle that is orientated to the mouse
        p1: tuple[float, float] = self.polar_to_cartesian(self.teta, self.SIZE)
        #print(p1)
        # conversion for the other vertexes of the triangle (with an offset of 3pi/4)
        p2: tuple[float, float] = self.polar_to_cartesian(self.teta, self.SIZE, 3*math.pi/4)
        #print(p2)
        p3: tuple[float, float] = self.polar_to_cartesian(self.teta, self.SIZE, -3*math.pi/4)
        #print(p3)

        # drawing of the triangle/player
        pyxel.tri(self.player_x + p1[0], self.player_y + p1[1],
                  self.player_x + p2[0], self.player_y + p2[1],
                  self.player_x + p3[0], self.player_y + p3[1],
                  self.color)
        
        self.bullets.draw() # draws the bullets

        self.draw_hp()
        self.draw_xp()
        self.draw_time(self.time // 3600, (self.time // 60) % 60)

    def draw_hp(self) -> None:
        """
        Method that draws the hp on the window.
        """

        color = pyxel.COLOR_GREEN

        hp = self.skills["hp"]

        if hp > 7:
            color = pyxel.COLOR_GREEN
            #print(f"{hp} HP")
        elif hp > 5:
            color = pyxel.COLOR_YELLOW
            #print(f"{hp} HP")
        elif hp > 3:
            color = pyxel.COLOR_ORANGE
            #print(f"{hp} HP")
        else:
            color = pyxel.COLOR_RED
            #print(f"{hp} HP")
    
        self.ascii.text(25, 25, f"{hp} HP", color)
        #print(f"{hp} HP")
    
    def draw_xp(self) -> None:
        """
        Method that draws the xp on the window.
        """

        color = pyxel.COLOR_YELLOW
        self.ascii.text(1050, 25, f"{self.xp} XP", color)
        #print(f"{self.xp} XP")

    def draw_time(self, minutes: int, seconds: int) -> None:
        """
        Method that draws the time on the window.

        Args:
            minutes (int): The number of minutes.
            seconds (int): The number of seconds.
        """

        color = pyxel.COLOR_LIGHT_BLUE
        self.ascii.text(585, 25, f"{minutes:02}:{seconds:02}", color)
        #print(f"{minutes:02}:{seconds:02}")