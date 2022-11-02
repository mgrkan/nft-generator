rarities = {
    "./Layers/0/0.png" : 10
} #Traits and rarity percents %, you don't need to set every trait
#0-100 - 100 means the trait can exist in all assets, 0 means it can't exist in any

def check_rarity(total_assets, k, val, trait_list, a):
    rarity = (total_assets / 100) * val
    rarity = round(rarity)
    return rarity
