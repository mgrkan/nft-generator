import os
from PIL import Image
import conf
import random
from rarities import rarities, check_rarity
import json


os.mkdir("./Output")
if conf.STARTS_FROM_ZERO:
    start = 0
else:
    start = 1
res = conf.RESOLUTION
color = (255, 255, 255)
output_dir = "./Output/"

layers = sorted(os.listdir("./Layers"))
layer_amount = len(layers)

def naming(index):
    if conf.FIXED_DECIMALS != 0:
        zeros = (conf.FIXED_DECIMALS - len(str(index))) * "0"
        name = zeros + str(index)
        return conf.PROJECT_NAME + "#" +  name + ".jpeg"
    else:
        return conf.PROJECT_NAME + "#" +  str(index) + ".jpeg"

trait_check = []
exceeds_rarity = conf.LAYERS
print(exceeds_rarity)
trait_list = {}
img = Image.new("RGB", res , color)
global a
a = start
while a <= conf.ASSETS:
    traits = []
    for i in layers:
        y = os.listdir("./Layers/" + i)
        selection = random.choice(y)
        trait_location = "./Layers/" + i + "/" + selection
        try:
            val = rarities.get(trait_location)
            amount = check_rarity(conf.ASSETS, trait_location, val, trait_check, a)
            print(trait_location,"rarity:", val,"amount:", amount)
            if amount <= trait_check.count(trait_location):
                exceeds_rarity[int(i)].append(trait_location)
                print("exceeded rarity")
                print(exceeds_rarity)
                y.remove(selection)
                new_selection = random.choice(y)
                trait_location = "./Layers/" + i + "/" + new_selection
                traits.append(new_selection.replace(".png", ""))
            else:
                traits.append(selection.replace(".png", ""))
                
        except:
            traits.append(selection.replace(".png", ""))
            pass

        trait_check.append(trait_location)
        trait_location = Image.open(trait_location)
        img.paste(trait_location, (0,0), mask=trait_location )
    trait_list[naming(a).replace(".jpeg", "")] = traits
    img.save(os.path.join(output_dir, naming(a)))
    print(naming(a))
    a += 1
with open("traits.json", "w") as f:
    f.write(json.dumps(trait_list))
