import os
from PIL import Image
import conf
import random


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
        return conf.PROJECT_NAME + "#" +  name + ".png"
    else:
        return conf.PROJECT_NAME + "#" +  str(index) + ".png"

img = Image.new("RGB", res , color)
for a in range(start, conf.ASSETS):
    for i in layers:
        y = os.listdir("./Layers/" + i)
        selection = random.randint(0, len(y)-1)
        trait_location = "./Layers/" + i + "/" + y[selection]
        trait_location = Image.open(trait_location)
        img.paste(trait_location, (0,0), mask=trait_location )
        #print("Selected", y[selection], "from", i)
            
    img.save(os.path.join(output_dir, naming(a)))
