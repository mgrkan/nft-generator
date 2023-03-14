import os
import random

rarities = {
    "./Layers/6/7.png" : 0
} #Traits and rarity percents %, you don't need to set every trait
#0-100 - 100 means the trait can exist in all assets, 0 means it can't exist in any


def unique(trait_list, traits):
    if traits in trait_list.values():
        return False
    else: return True


def check_rarity(total_assets, trait_location, trait_check, traits, selection, y, exceeds_rarity, i):
    try:
        #find the max amount of assets that can include the trait
        val = rarities.get(trait_location)
        amount = round((total_assets / 100) * val)
        print(trait_location,"rarity:", val,"amount:", amount)
        check = trait_check.count(trait_location)
        if amount <= check:
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