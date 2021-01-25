from hero import Hero
from maze_gen_recursive import make_maze_recursion
from copy import deepcopy
from random import randint

WALL_CHAR = "#"
SPACE_CHAR = "-"
HERO_CHAR = "H"
MON_CHAR = "M"
GOB_CHAR = "G"


class _Environment:
    """Environment includes Maze+Monster+Goblin"""
    def __init__(self, maze):
        self._environment = deepcopy(maze)

    def random_row(self, row):
        return randint(0,len(self._environment)-1)

    def start_coord(self,val):
        x = self.random_row(self._environment)
        y = self.random_row(self._environment)
        if self._environment[x][y] == 0:
            self._environment[x][y] = val
            return (x,y)
        else:
            return self.start_coord(val)

            
    def set_coord(self, x, y):
        return self._environment[x][y]

    def get_coord(self, x, y):
        return self._environment[x][y]

    def print_environment(self):
        """print out the environment in the terminal"""
        for row in self._environment:
            row_str = str(row)
            row_str = row_str.replace("1", WALL_CHAR)  # replace the wall character
            row_str = row_str.replace("0", SPACE_CHAR)  # replace the space character
            row_str = row_str.replace("2", HERO_CHAR)  # replace the hero character
            row_str = row_str.replace("3", MON_CHAR)  # replace the hero character
            row_str = row_str.replace("4", GOB_CHAR)  # replace the hero character

            print("".join(row_str))


class Game:

    _count = 0

    def __init__(self):
        self.myHero = Hero()
        self.mazeX = 17
        self.mazeY = 17
        self.maze = make_maze_recursion(self.mazeX,self.mazeY)
        self.MyEnvironment = _Environment(self.maze)  # initial environment is the maze itself


    def play(self):
        #while True:
        self.PLAYER = self.MyEnvironment.start_coord(2)
        print(self.PLAYER,99)
        for i in range(5):
            self.MyEnvironment.start_coord(3)
        for i in range(5):
            self.MyEnvironment.start_coord(4)
        self._count = 0
        if self._count < 1: #so it only prints out one
            self.MyEnvironment.print_environment()
            self.myHero.move_debug(self.MyEnvironment,self.PLAYER)  #this works in debug mode
            #self.MyEnvironment.set_coord(MyHero.move_debug.hero_x,MyHero.move_debug.hero_y)
            #self.myHero.move(self.MyEnvironment)
            self.MyEnvironment.print_environment()
            self._count += 1
            print("============================", self._count)


if __name__ == "__main__":

    myGame = Game()
    myGame.play()
    
