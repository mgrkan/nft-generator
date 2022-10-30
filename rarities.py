rarities = {
    "./Layers/1/0.png" : 5
} #Traits and rarity percents %, you don't need to set every trait

def check_rarity(total_assets, k, val, trait_list):
    rarity = (total_assets / 100) * val
    rarity = round(rarity)
    if trait_list.count(k) > rarity:
        continue
