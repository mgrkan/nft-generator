import os
import random

rarities = {
    "./Layers/1/0.png" : 6
} #Traits and rarity percents %, you don't need to set every trait
#0-100 - 100 means the trait can exist in all assets, 0 means it can't exist in any

exceptions = [
    {(2,8) : [[(4,10)], True]},
    {(1,11) : [[(3,1), (3,2), (3,3)], False]}
]


def check_rarity(total_assets, trait_location, trait_check, traits, selection, y):
    try:
        #find the max amount of assets that can include the trait
        val = rarities.get(trait_location)
        amount = round((total_assets / 100) * val)
        print(trait_location,"rarity:", val,"amount:", amount)
        if amount <= trait_check.count(trait_location):
            exceeds_rarity[int(i)].append(trait_location)
            print("exceeded rarity")
            print(exceeds_rarity)
            y.remove(selection)
            new_selection = random.choice(y)
            print(new_selection)
            trait_location = "./Layers/" + i + "/" + new_selection
            traits.append(new_selection.replace(".png", ""))
        else:
            traits.append(selection.replace(".png", ""))
            
    except:
        traits.append(selection.replace(".png", ""))
        
    finally:
        trait_check.append(trait_location)
        

def check_exception(exceptions, traits):
    a = 0
    for i in exceptions:
        key = list(i.keys())[0]
        value = i[key][0]
        compatibility = i[key][1]
        new_value = []
        if compatibility == True:
            for i in value:
                fi = "./Layers/" + str(i[0]) + "/"
                for x in os.listdir(fi):
                    if x != str(i[1]) + ".png":
                        x = x.replace(".png", "")
                        x = int(x)
                        x = (i[0], x)
                        new_value.append(x)
            exceptions[a] = {key: [new_value, False]}
        a += 1
    
    for i in exceptions:
        key = list(i.keys())[0]
        value = i[key][0]
        if traits[key[0]] == str(key[1]):
            flag = 0
            for q in value:
                if traits[q[0]] == str(q[1]):
                    flag = 1
            if flag == 0:
                continue
            else:
                unique_layers = []
                a = "a"
                for x in value:
                    b = x[0]
                    if (a != b) & (a != "a"):
                        unique_layers.append(a)
                        unique_layers.append(b)
                    a = x[0]
                unique_layers = list(set(unique_layers))
                if unique_layers == []:
                    unique_layers = [b]
                compatibles = []
                    
                for y in unique_layers:
                    all_traits = []
                    [all_traits.append((y, int(lay.replace(".png", "")))) for lay in os.listdir("./Layers/" + str(y))]
                    compatibles.append(list(set(all_traits) - set(value)))
                        
                    
                print(compatibles, traits)
                for j in compatibles:
                    selection = random.choice(j)
                    print(selection)
                    print("incompatible traits" , traits)
                    traits[selection[0]] = str(selection[1])     
                    print("updated traits" , traits)

def restack(traits, img, Image):   
    n = 0
    for i in traits:
        location = "./Layers/" + str(n) + "/" + i + ".png"
        location = Image.open(location)
        img.paste(location, (0,0), mask=location)
        n += 1   
