import pyxel
from player import Player
from skill import Skill
from ascii import ASCII

class Upgrade:
    """
    Class that displays the upgrade menu.
    """

    def __init__(self, player: Player) -> None:
        """
        Create the upgrade menu to buy skills upgrades.

        Args:
            player (Player): The Player.
        """

        self.player: Player = player
        self.upgrades: dict[str, Skill] = {
            "attack": Skill("attack", "Increase your attack by 1", 10, 1),
            "hp_max": Skill("hp max", "Increase your health by 1", 25, 1),
            "shield": Skill("shield", "Increase your shield by 5", 50, 5),
            "speed": Skill("speed", "Increase your speed by 1", 5, 1),
            "fire_rate": Skill("fire rate", "Increase your fire rate by 2", 10, -2),
        }
        self.ascii: ASCII = ASCII()
        self.x: int = 25
        self.y: int = 25
        self.color: int = pyxel.COLOR_GREEN
        self.selected_index: int = 0
        self.skill_names: list = list(self.upgrades.keys())
        self.message = ""

    def increase(self, skill: str) -> None:
        """
        Increase the selected skill of the player if he has enough XP.
        
        Args:
            skill (str): The skill to improve
        """

        # Skill not found
        if skill not in self.upgrades:
            #print(skill)
            self.message = "Skill not found"
            self.color = pyxel.COLOR_RED
            return

        upgrade = self.upgrades[skill]

        # Insufficient XP
        if self.player.xp < upgrade.price:
            #print(player.xp)
            #print(upgrade.price)
            self.message = "Insufficient XP"
            self.color = pyxel.COLOR_RED
            return
        
        #speed maxed out (lower or equal to 15)
        if skill == "speed" and upgrade.level == 11:
            #print(upgrade.level)
            #print(self.player.skills[skill])
            self.message = "Skill maxed out"
            return
        
        #shield maxed out (lower or equal to 95)
        if skill == "shield" and upgrade.level == 19:
            #print(upgrade.level)
            #print(self.player.skills[skill])
            self.message = "Skill maxed out"
            return
        
        #fire rate maxed out (higher or equal to 10)
        if skill == "fire rate" and upgrade.level == 25:
            #print(upgrade.level)
            #print(self.player.skills[skill])
            self.message = "Skill maxed out"
            return
        
        #print("xp before upgraded", self.player.xp)
        self.player.xp -= upgrade.price
        #print("xp after upgraded", self.player.xp)
        #print("skill before upgraded", self.player.skills[skill])
        self.player.skills[skill] += upgrade.amount
        #print("skill after upgraded", self.player.skills[skill])

        if skill == "hp_max":
            #print("hp before upgraded", self.player.skills["hp"])
            self.player.skills["hp"] = self.player.skills["hp_max"]
            #print("hp after upgraded", self.player.skills["hp"])

        #print("price before upgraded", upgrade.price)
        upgrade.price = int(upgrade.price * 1.5)
        #print("price after upgraded", upgrade.price)
        upgrade.level += 1
        #print(upgrade.level)

        self.message = f"{upgrade.name} upgraded to level {upgrade.level}"
        self.color = pyxel.COLOR_LIGHT_BLUE
        return

    def update(self) -> None:
        """
        Handle user input to navigate and purchase upgrades.
        """

        #print("Upgrade update works")
        # Navigate the upgrade menu
        if pyxel.btnp(pyxel.KEY_DOWN) or pyxel.btnp(pyxel.KEY_S):
            #print("down")
            self.selected_index = (self.selected_index + 1) % len(self.skill_names)
            #print(self.selected_index)
        if pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.KEY_Z):
            #print("up")
            self.selected_index = (self.selected_index - 1) % len(self.skill_names)
            #print(self.selected_index)

        # Purchase the selected upgrade
        if pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.KEY_F):
            #print("purchased")
            selected_skill = self.skill_names[self.selected_index]
            self.increase(selected_skill)

    def draw(self) -> None:
        """
        Draw the upgrade menu.
        """

        #print("Upgrade draw works")
        pyxel.cls(0)
        self.y = 25
        self.ascii.text(self.x, self.y, "--- Upgrade Menu ---", pyxel.COLOR_YELLOW)
        self.y += 60
        self.draw_time(self.x, self.y)
        self.y += 30
        self.draw_hp(self.x, self.y)
        self.y += 30
        self.ascii.text(self.x, self.y, f"XP: {self.player.xp}", pyxel.COLOR_YELLOW)

        self.y += 60

        # Display each upgrade option
        for i, skill_name in enumerate(self.skill_names):
            upgrade = self.upgrades[skill_name]
            color = pyxel.COLOR_LIME if i == self.selected_index else pyxel.COLOR_WHITE
            self.ascii.text(20, self.y, upgrade.name, color)
            self.ascii.text(225, self.y, f"Lv.{upgrade.level}:", color)
            self.ascii.text(350, self.y, upgrade.description, color)
            self.ascii.text(900, self.y, f"({upgrade.price})", color)
            self.y += 30
            #print(upgrade.name)
            #print(f"Lv.{upgrade.level}:")
            #print(upgrade.description)
            #print(f"({upgrade.price})")

        self.y += 30
        self.ascii.text(self.x, self.y, "Press ENTER to buy", pyxel.COLOR_DARK_BLUE)
        self.y += 30
        self.ascii.text(self.x, self.y, "Use ZQSD or the arrow keys to select something else", pyxel.COLOR_DARK_BLUE)
        self.y += 30
        self.ascii.text(self.x, self.y, "Press E or ESCAPE to close", pyxel.COLOR_DARK_BLUE)

        self.y += 60
        self.ascii.text(self.x, self.y, self.message, self.color)

    def draw_hp(self, x: int, y: int) -> None:
        """
        Method that draws the hp on the window.

        Args:
            x (int): The x position of the text.
            y (int): The y position of the text.
        """

        color = pyxel.COLOR_GREEN

        hp = self.player.skills["hp"]

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

        self.ascii.text(x, y, f"HP: {hp}", color)
        #print(f"{hp} HP")

    def draw_time(self, x: int, y: int) -> None:
        """
        Method that draws the time on the window.
        Args:
            x (int): The x position of the text.
            y (int): The y position of the text.
        """

        minutes = self.player.time // 3600
        seconds = (self.player.time // 60) % 60
        color = pyxel.COLOR_LIGHT_BLUE
        self.ascii.text(x, y, f"Time: {minutes:02}:{seconds:02}", color)
        #print(f"Time: {minutes:02}:{seconds:02}")