import random

ds = "daptek,diyon,averill,adyo"
dsf = "thata,flori,kd,rayie"

# eh bukan belom
def GayPrediction ():
    heaven = []
    hell = []
    male = list(ds.split(",")) 
    female = list(dsf.split(","))
    total = male + female
    print(total)
    randomperson1 = random.choice(total)
    randomperson2 = random.choice(total)

    if randomperson1 in male and randomperson2 in female or randomperson2 in male and randomperson1 in female :
        print("Nice") # berarti normal dia hubungannya, kok lu lenovo legion sih tek bukan macbook emang iya, i named things wkkwk loh udahh benerr taroo di finct
        heaven.append(randomperson1 + randomperson2)
    elif randomperson1 == randomperson2 :
        print("Self Love")
        heaven.append(randomperson1)

    else : 
        print("Lu gay kocak")
        hell.append(randomperson1 + randomperson2)
    print(randomperson1 + " " + randomperson2)
    print(f"yang masuk neraka : {hell}, yang masuk surga :  {heaven}") # GW TELFON DYO, eh tapi kok printan nya ngga kespasi gara garaa , spasi dii dsf sama ds
GayPrediction() # udah coba bingung mau diapain wkwkk udahh yooo we have to sliip sabar caranya gimana
# oke selamat malam babai babai leave bng