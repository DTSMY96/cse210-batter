from game.actor import Actor
from game.point import Point
from game.constants import IMAGE_BRICK

class brick(Actor):

    def __init__(self):
        super().__init__()
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)
        self._width = ""
        self._height = ""
        self.set_image(IMAGE_BRICK)
        

       




