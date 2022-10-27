import os
from PIL import Image
import conf
import random

#os.mkdir("./Output")
res = conf.RESOLUTION
color = (255,55,105, 255)
output_dir = "./Output/"

layers = os.listdir("./Layers")
layer_amount = len(layers)

def naming(index):
    return conf.PROJECT_NAME + str(index) + ".png"

img = Image.new("RGBA", res , color)
for a in range(0, conf.ASSETS):
    for i in layers:
        y = os.listdir("./Layers/" + i)
        selection = random.randint(0, len(y)-1)
        trait_location = "./Layers/" + i + "/" + y[selection]
        trait_location = Image.open(trait_location)
        img.paste(trait_location, (0,0), mask=trait_location )
        #print("Selected", y[selection], "from", i)
            
    img.save(os.path.join(output_dir, naming(a)))
