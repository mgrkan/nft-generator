import os
from PIL import Image
import conf
import random
from rarities import rarities, check_rarity


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

trait_list = []
exceeds_rarity = conf.LAYERS
print(exceeds_rarity)
img = Image.new("RGB", res , color)
global a
a = start
while a <= conf.ASSETS:
    for i in layers:
        y = os.listdir("./Layers/" + i)
        selection = random.choice(y) #Rarityi aşanları ayrı listeye ekle sonra o listedekilerden farklı gelene dek random seçtir veya bu fordan başla random farklı sonuç vermeyebilir
        trait_location = "./Layers/" + i + "/" + selection
        trait_list.append(trait_location)
        try:
            val = rarities.get(trait_location)
            amount = check_rarity(conf.ASSETS, trait_location, val, trait_list, a)
            print(trait_location,"rarity:", val,"amount:", amount)
            if amount >= trait_list.count(trait_location):
                exceeds_rarity[int(i)].append(trait_location)
                print("exceeded rarity")
                print(exceeds_rarity)
        except:
            pass
        trait_location = Image.open(trait_location)
        #img.paste(trait_location, (0,0), mask=trait_location )
            
    #img.save(os.path.join(output_dir, naming(a)))
    print(naming(a))
    a += 1
