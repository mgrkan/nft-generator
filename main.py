import os
from PIL import Image
import conf
import random
from rarities import *
import json


os.mkdir("./Output")
if conf.STARTS_FROM_ZERO:
    start = 0
else:
    start = 1
res = conf.RESOLUTION
color = (255, 255, 255)
output_dir = "./Output/"
ext = conf.EXTENSION

layers = sorted(os.listdir("./Layers"))
layer_amount = len(layers)

def naming(index):
    if conf.FIXED_DECIMALS != 0:
        zeros = (conf.FIXED_DECIMALS - len(str(index))) * "0"
        name = zeros + str(index)
        return conf.PROJECT_NAME + "#" +  name + ext
    else:
        return conf.PROJECT_NAME + "#" +  str(index) + ext


trait_check = []
exceeds_rarity = conf.LAYERS
print(exceeds_rarity)
trait_list = {}
global a
a = start
while a <= conf.ASSETS:
    img = Image.new("RGB", res , color)
    traits = []
    for i in layers:
        #choosing the trait
        y = os.listdir("./Layers/" + i)
        selection = random.choice(y)
        trait_location = "./Layers/" + i + "/" + selection
        #checking if the trait exceeds rarity
        check_rarity(conf.ASSETS, trait_location, trait_check, traits, selection, y, exceeds_rarity, i)
        #pasting the trait on top of the image
        trait_location = Image.open(trait_location)
        img.paste(trait_location, (0,0), mask=trait_location )
    #checking for incompatible traits
    check_exception(exceptions, traits)
    restack(traits, img, Image)
    if (unique(trait_list, traits)):
        trait_list[naming(a).replace(ext, "")] = traits
        img.save(os.path.join(output_dir, naming(a)))
        print(naming(a))
        a += 1
    else:
        print("image not unique. recreating")

with open("traits.json", "w") as f:
    f.write(json.dumps(trait_list))

