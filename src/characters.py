import math

class Character:
    """
    Class that manages characters (for the player and enemies).
    """

    def __init__(self,
                 color: int,
                 hp: int,
                 hp_max: int,
                 attack: int,
                 speed: int,
                 shield: int,
                 fire_rate: int,
                 xp: int) -> None:
        """
        Args:
            color (int): Character color.
            hp (int): Current health of the character.
            hp_max (int): Maximum health of the character.
            attack (int): Base attack damage the character can inflict.
            speed (int): Movement speed of the character.
            shield (int): Amount of damage the character can block before losing hp.
            fire_rate (int): Delay between attacks.
            xp (int): Experience points awarded when the character is defeated.
        """

        self.color: int = color
        self.xp: int = xp
        self.skills: dict[str, int] = {
            "hp": hp,
            "hp_max": hp_max,
            "attack": attack,
            "shield": shield,
            "speed": speed,
            "fire_rate": fire_rate
        }

    def teta_calculation(self, coord1: tuple[float, float], coord2: tuple[float, float]) -> float:
        """
        Method that calculates teta, direction from the pole relative to the direction of the polar axis (polar coordinates), according to two tuples of coordinates.

        Args:
            coord1 (tuple[float, float]): Origin point (x1, y1) from which the direction is measured.
            coord2 (tuple[float, float]): Target point (x2, y2) toward which the direction is calculated.

        Returns:
            float: Angle teta in radians in the range [-π, π], representing the direction from coord1 to coord2.
        """

        dx: float = coord1[0] - coord2[0] # distance between x of coord1 and x of coord2
        dy: float = coord1[1] - coord2[1] # distance between y of coord1 and y of coord2
        teta: float = math.atan2(dy, dx) # calculation of teta
        return teta
    
    def polar_to_cartesian(self, teta: float, r: float, offset: float = 0) -> tuple[float, float]:
        """
        Method that turns polar coordinates into cartesian coordinates.

        Args:
            teta (float): Angle in radians representing the polar coordinate
            r (int): size or distance from the origin.
            offset (float, optional): Additional angular shift in radians applied to teta. Useful in the draw method of the Player class. Defaults to 0.

        Returns:
            tuple[float, float]: tuple containing the (x, y) cartesian coordinates corresponding to the given polar coordinates.
        """

        x: float = math.cos(teta + offset) * r # calculates x according to the polar coordinates given (if given an offset, adds it to the operation)
        y: float = math.sin(teta + offset) * r # calculates y according to the polar coordinates given (if given an offset, adds it to the operation)
        return (x, y)

    def receive_damage(self, amount: int, hp: int, shield: int) -> int:
        """
        Apply damage based on incoming damage and shield percentage.

        Args:
            amount (int): The raw amount of damage inflicted.
            hp (int): The current hp.
            shield (int): The shield percentage reducing incoming damage (0-100).

        Returns:
            int: The updated hp after applying damage (minimum 0).
        """
        hp -= round(amount * (1 - shield / 100))
        if hp < 0:
            hp = 0
        
        return hp