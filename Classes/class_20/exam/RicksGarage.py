

class RicksGarage:
    hm_robots = 0

    def __init__(self):
        self.robots_names = {}
        self.robots_places = {}

    def add_robot(self, robot):
        next_place = len(self.robots_names)
        self.robots_names[robot.name] = robot
        self.robots_places[next_place] = robot

    def remove_robot(self, robot_name):
        robot = self.robots_names[robot_name]
        for key, val in self.robots_places.items():
            if val == robot:
                self.robots_places[key] = None

        del self.robots_names[robot_name]

    def use_robot(self, name):
        robot = self.robots_names[name]
        robot.run()

    def describe(self):
        for robot_place, robot in self.robots_places.items():
            print("{}\t-->\t{}".format(robot_place, robot.name))



class LittleRobot:

    def __init__(self, name, purpose):
        self.name     = name
        self.purpose  = purpose

    def run(self):
        print("Im a standart robot, not doing anything")


class ButterRobot(LittleRobot):
    def run(self):
        print("Passing the butter.")

class YellingRobot(LittleRobot):
    def run(self):
        print("Get out of here jerry!")

garage = RicksGarage()

yelling_robot = YellingRobot("JerryYeller", "Yell at Jerry")

little_robot = ButterRobot('Butter', "Pass the butter")

garage.add_robot(yelling_robot)
garage.add_robot(little_robot)

garage.describe()

garage.use_robot('Butter')

