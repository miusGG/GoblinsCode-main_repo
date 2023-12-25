from random import *
from settings import set as s

blocks = ["dirt", "dirtwithwall", "dirtwithcorner", "dirtwithcorner2"]

lastRoom = False
roomsize = s["roomSize"] * 2 + 6
new_rooms = []
world_map = {
}
fug_map = {}
world_second_layer = {

}
world = {

}
collisions = [

]
doors = {
    "0" : {
        "0" : [[], []]
    }
}
rooms = {
    "0" : {
        "0" : 1
    }
}
doors2 = [
    (0, -1, 0, 1),
    (0, 1, 1, 0),
    (1, 0, 2, 3),
    (-1, 0, 3, 2)
]
pasages = [
    [
        [0, -s["roomSize"] - 1, blocks[0], 0],
        [-1, -s["roomSize"] - 1, blocks[0], 0],
        [0, -s["roomSize"] - 2, blocks[0], 0],
        [-1, -s["roomSize"] - 2, blocks[0], 0],
        [0, -s["roomSize"] - 3, blocks[0], 0],
        [-1, -s["roomSize"] - 3, blocks[0], 0],
        [-2, -s["roomSize"] - 2, blocks[1], 90],
        [1, -s["roomSize"] - 2, blocks[1], -90],
        [-2, -s["roomSize"] - 3, blocks[1], 90],
        [1, -s["roomSize"] - 3, blocks[1], -90],
        [-2, -s["roomSize"] - 1, blocks[3], 0],
        [1, -s["roomSize"] - 1, blocks[3], -90]
    ],
    [
        [0, s["roomSize"], blocks[0], 0],
        [-1, s["roomSize"], blocks[0], 0],
        [0, s["roomSize"] + 1, blocks[0], 0],
        [-1, s["roomSize"] + 1, blocks[0], 0],
        [0, s["roomSize"] + 2, blocks[0], 0],
        [-1, s["roomSize"] + 2, blocks[0], 0],
        [-2, s["roomSize"] + 1, blocks[1], 90],
        [1, s["roomSize"] + 1, blocks[1], -90],
        [-2, s["roomSize"] + 2, blocks[1], 90],
        [1, s["roomSize"] + 2, blocks[1], -90],
        [-2, s["roomSize"], blocks[3], 90],
        [1, s["roomSize"], blocks[3], 180]
    ],
    [
        [s["roomSize"], 0, blocks[0], 0],
        [s["roomSize"], -1, blocks[0], 0],
        [s["roomSize"] + 1, 0, blocks[0], 0],
        [s["roomSize"] + 1, -1, blocks[0], 0],
        [s["roomSize"] + 2, 0, blocks[0], 0],
        [s["roomSize"] + 2, -1, blocks[0], 0],
        [s["roomSize"] + 1, -2, blocks[1], 0],
        [s["roomSize"] + 1, 1, blocks[1], 180],
        [s["roomSize"] + 2, -2, blocks[1], 0],
        [s["roomSize"] + 2, 1, blocks[1], 180],
        [s["roomSize"], -2, blocks[3], -90],
        [s["roomSize"], 1, blocks[3], 180]
    ],
    [
        [-s["roomSize"] - 1, 0, blocks[0], 0],
        [-s["roomSize"] - 1, -1, blocks[0], 0],
        [-s["roomSize"] - 2, 0, blocks[0], 0],
        [-s["roomSize"] - 2, -1, blocks[0], 0],
        [-s["roomSize"] - 3, 0, blocks[0], 0],
        [-s["roomSize"] - 3, -1, blocks[0], 0],
        [-s["roomSize"] - 2, -2, blocks[1], 0],
        [-s["roomSize"] - 2, 1, blocks[1], 180],
        [-s["roomSize"] - 3, -2, blocks[1], 0],
        [-s["roomSize"] - 3, 1, blocks[1], 180],
        [-s["roomSize"] - 1, -2, blocks[3], 0],
        [-s["roomSize"] - 1, 1, blocks[3], 90]
    ]
]
dC = [
    [
        (-s["roomSize"] - 0.4, -s["roomSize"] - 3, s["roomSize"] - 1, 2.3),
        (-s["roomSize"] + s["roomSize"] + 1.4, -s["roomSize"] - 3, s["roomSize"] - 1, 2.3)
    ],
    [
        (-s["roomSize"] - 0.4, s["roomSize"] + 0.3, s["roomSize"] - 1, 2.7),
        (-s["roomSize"]+ s["roomSize"] + 1.4, s["roomSize"] + 0.3, s["roomSize"] - 1, 2.7)
    ],
    [
        (s["roomSize"] + 0.4, -s["roomSize"] - 1, 2.6, s["roomSize"] - 0.7),
        (s["roomSize"] + 0.4, -s["roomSize"] + s["roomSize"] + 1.3, 2.6, s["roomSize"] - 0.3)
    ],
    [
        (-s["roomSize"] - 3, -s["roomSize"] - 1, 2.6, s["roomSize"] - 0.7),
        (-s["roomSize"] - 3, -s["roomSize"] + s["roomSize"] + 1.3, 2.6, s["roomSize"] - 0.3)
    ]
]
gC = [
    (-2, -s["roomSize"] - 3, 4, 1),
    (-2, +s["roomSize"] + 2, 4, 1),
    (s["roomSize"] + 2, -2, 1, 4),
    (-s["roomSize"] - 3, -2, 1, 4),
]
wC = [
    (-s["roomSize"] - 1, -s["roomSize"] - 1, s["roomSize"] * 2 + 2, 0.3),   # 0
    (-s["roomSize"] - 1, s["roomSize"] + 0.3, s["roomSize"] * 2 + 2, 0.7),  # 1
    (s["roomSize"] + 0.4, -s["roomSize"] - 1, 0.6, s["roomSize"] * 2 + 2),  # 2
    (-s["roomSize"] - 1, -s["roomSize"] - 1, 0.6, s["roomSize"] * 2 + 2)    # 3
]

class Generate():
    def __init__(self):
        pass

    def addBlockToWorld(self, coords, block, rotate = 0):
        if (str(coords[0]) not in world):
            world[str(coords[0])] = {}
        world[str(coords[0])][str(coords[1])] = [block, rotate]

    def addBlockToSecondLayer(self, coords, block, rotate = 0):
        if (str(coords[0]) not in world_second_layer):
            world_second_layer[str(coords[0])] = {}
        world_second_layer[str(coords[0])][str(coords[1])] = [block, rotate]

    def generateRoom(self, c, args, fromr = None):
        global lastRoom
        if str(c[0]) not in world_map:
            world_map[str(c[0])] = {}
        if str(c[1]) not in world_map[str(c[0])]:
            world_map[str(c[0])][str(c[1])] = args
            world_map[str(c[0])][str(c[1])].append([])
        else:
            return 0
        self.doors = [0, 1, 2, 3]
        if (str(c[0]) in doors) and (str(c[1]) in doors[str(c[0])]):
            for i in doors[str(c[0])][str(c[1])][0]:
                world_map[str(c[0])][str(c[1])][2].append(i)
                self.doors.remove(i)
            for i in doors[str(c[0])][str(c[1])][1]:
                self.doors.remove(i)

        self.chance = randint(1, 100)
        shuffle(self.doors)
        self.generateDoors = []
        if (self.chance >= 90) and (len(self.doors) >= 3):
            self.generateDoors = self.doors[:3]
        elif (self.chance >= 60) and (len(self.doors) >= 2):
            self.generateDoors = self.doors[:2]
        elif (self.chance >= 0) and (len(self.doors) >= 1):
            self.generateDoors = self.doors[:1]

        if (rooms[str(c[0])][str(c[1])] == 15):
            if (not lastRoom):
                args[1] = 0
                lastRoom = True
        else:
            for i in self.generateDoors:
                world_map[str(c[0])][str(c[1])][2].append(i)

        for i in doors2:
            if (str(c[0] + i[0]) not in doors):
                doors[str(c[0] + i[0])] = {}
                rooms[str(c[0] + i[0])] = {}
            if (str(c[1] + i[1]) not in doors[str(c[0] + i[0])]):
                doors[str(c[0] + i[0])][str(c[1] + i[1])] = [[], []]
                rooms[str(c[0] + i[0])][str(c[1] + i[1])] = 0
            if i[2] in world_map[str(c[0])][str(c[1])][2]:
                doors[str(c[0] + i[0])][str(c[1] + i[1])][0].append(i[3])
                rooms[str(c[0] + i[0])][str(c[1] + i[1])] = rooms[str(c[0])][str(c[1])] + 1
            else:
                doors[str(c[0] + i[0])][str(c[1] + i[1])][1].append(i[3])
        print(len(self.doors))
        print(self.doors)
        print(world_map[str(c[0])][str(c[1])][2])
        print(rooms[str(c[0])][str(c[1])])
        print(doors[str(c[0])][str(c[1])])
        print(self.generateDoors)
        print(world_map[str(c[0])][str(c[1])][2])
        print()

        for i in range(-s["roomSize"], s["roomSize"]):
            for j in range(-s["roomSize"], s["roomSize"]):
                self.addBlockToWorld((i + c[0]*roomsize, j + c[1]*roomsize), blocks[0])

        self.addBlockToWorld((s["roomSize"] + c[0]*roomsize, -s["roomSize"] - 1 + c[1]*roomsize), blocks[2], -90)
        self.addBlockToWorld((-s["roomSize"] - 1 + c[0]*roomsize, -s["roomSize"] - 1 + c[1]*roomsize), blocks[2], 0)
        self.addBlockToWorld((-s["roomSize"] - 1 + c[0]*roomsize, s["roomSize"] + c[1]*roomsize), blocks[2], 90)
        self.addBlockToWorld((s["roomSize"] + c[0]*roomsize, s["roomSize"] + c[1]*roomsize), blocks[2], 180)

        for i in range(-s["roomSize"], s["roomSize"]):
            self.addBlockToWorld((i + c[0]*roomsize, -s["roomSize"] - 1 + c[1]*roomsize), blocks[1], 0)
            self.addBlockToWorld((-i - 1 + c[0]*roomsize, s["roomSize"] + c[1]*roomsize), blocks[1], 180)
            self.addBlockToWorld((s["roomSize"] + c[0]*roomsize, - i - 1 + c[1]*roomsize), blocks[1], -90)
            self.addBlockToWorld((- s["roomSize"] - 1 + c[0]*roomsize, i + c[1]*roomsize), blocks[1], 90)


        for i in world_map[str(c[0])][str(c[1])][2]:
            for j in pasages[i]:
                self.addBlockToWorld((j[0] + c[0]*roomsize, j[1] + c[1]*roomsize), j[2], j[3])

        for i in range(4):
            if i in world_map[str(c[0])][str(c[1])][2]:
                for j in range(len(dC[i])):
                    collisions.append([(dC[i][j][0] + c[0]*roomsize, dC[i][j][1] + c[1]*roomsize, dC[i][j][2], dC[i][j][3]), "stop"])
                if (fromr == None) or ((fromr != None) and (i != doors2[fromr][3])):
                    collisions.append([(gC[i][0] + c[0]*roomsize, gC[i][1] + c[1]*roomsize, gC[i][2], gC[i][3]), "generate", [c, i]])
            else:
                collisions.append([(wC[i][0] + c[0]*roomsize, wC[i][1] + c[1]*roomsize, wC[i][2], wC[i][3]), "stop"])

        self.generateFilling(args[1], c)
        self.generateFug()

    def generateFilling(self, type, c):
        if type == -1:
            for i in range(10):
                x = randint(-s["roomSize"], s["roomSize"] - 1)
                y = randint(-s["roomSize"], s["roomSize"] - 1)
                self.addBlockToSecondLayer((x + c[0] * roomsize, y + c[1] * roomsize), "frog", 0)
        if type == 0:
            for i in range(2):
                x = randint(-s["roomSize"], s["roomSize"] - 1)
                y = randint(-s["roomSize"], s["roomSize"] - 1)
                self.addBlockToSecondLayer((x + c[0] * roomsize, y + c[1] * roomsize), "frog", 0)

    def generateFug(self):
        for i in world_map:
            for j in world_map[i]:
                pass

def clearWorld():
    global world_map, world, fug_map, world_second_layer, collisions,  doors, rooms
    world_map.clear()
    fug_map.clear()
    world_second_layer.clear()
    world.clear()
    collisions.clear()
    doors.clear()
    rooms.clear()
    doors = {
        "0": {
            "0": [[], []]
        }
    }
    rooms = {
        "0": {
            "0": 1
        }
    }
gen = Generate()