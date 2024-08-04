import random
import opensimplex
import blocks
import math

def generate(chunkx, chunky, seed):
    res = [[blocks.Air((x, y)) for y in range(16)]for x in range(16)]
    floor = [[blocks.StoneFloor((x, y)) for y in range(16)]for x in range(16)]
    opensimplex.seed(seed)
    random.seed(seed)
    watermap_seed = random.randint(-9999, 9999)
    random.seed(((seed * chunkx * chunky + chunkx + chunky + seed + 8) * 15) % 9999)
    #генерация пещер
    for x in range(16):
        for y in range(16):
            x2 = (x + chunkx * 16) / 25
            y2 = (y + chunky * 16) / 25
            if not (opensimplex.noise2(x2, y2) >= -0.1 and opensimplex.noise2(x2, y2) <= 0.4):
                res[x][y] = blocks.Stone((x, y))
    #выбор количества руд
    rand_number = random.randint(1, 100)
    if rand_number <= 50:
        count_of_ores = 0
    elif rand_number <= 75:
        count_of_ores = 1
    else:
        count_of_ores = 2
    #генерация руд
    for i in range(count_of_ores):
        rand_number = random.randint(1, 100)
        if rand_number <= 65:
            ore_type = "coal"
        elif rand_number <= 90:
            ore_type = "iron"
        else:
            ore_type = "copper"
        ore_pos = [
            random.randint(0, 15),
            random.randint(0, 15)
            ]
        for x in range(-1, 2):
            for y in range(-1, 2):
                x2 = ore_pos[0] + x
                y2 = ore_pos[1] + y
                try:
                    if random.randint(0, 1) == 1 and res[x2][y2].name == "stone" and x2 > 0 and y2 > 0:
                        if ore_type == "coal":
                            ore = blocks.CoalOre((x2, y2))
                        elif ore_type == "iron":
                            ore = blocks.IronOre((x2, y2))
                        elif ore_type == "copper":
                            ore = blocks.CopperOre((x2, y2))
                        res[x2][y2] = ore
                except:
                    a = 1
    #генерация земли
    opensimplex.seed(watermap_seed)
    for x in range(16):
        for y in range(16):
            x2 = (x + chunkx * 16) / 10
            y2 = (y + chunky * 16) / 10
            noiseresult = opensimplex.noise2(x2, y2)
            if noiseresult >= 0.65 and res[x][y].name == "stone":
                res[x][y] = blocks.Soil((x, y))
    #генерация озер
    watermap = [[0 for y in range(16)]for x in range(16)]
    for x in range(16):
        for y in range(16):
            x2 = (x + chunkx * 16) / 50
            y2 = (y + chunky * 16) / 50
            noiseresult = opensimplex.noise2(x2, y2)
            watermap[x][y] = noiseresult
            if noiseresult >= 0.7:
                floor[x][y] = blocks.SoilFloor((x, y))
                if res[x][y].name == "stone":
                    res[x][y] = blocks.Soil((x, y))
            if noiseresult >= 0.75:
                floor[x][y] = blocks.Water((x, y), (9, 0))
                res[x][y] = blocks.Air((x, y))
            if noiseresult >= 0.77:
                floor[x][y] = blocks.Water((x, y), (1, 0))
                res[x][y] = blocks.Air((x, y))
    return(res, floor)
