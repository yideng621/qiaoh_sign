

import os


FruitShareCodes=os.environ["FruitShareCodes"].split("&")
print("您的东东农场互助码")
print(FruitShareCodes)

PETSHARECODES=os.environ["PETSHARECODES"].split("&")
print("您的东东萌宠互助码")
print(PETSHARECODES)

PLANT_BEAN_SHARECODES=os.environ["PLANT_BEAN_SHARECODES"].split("&")
print("您的种豆得豆互助码")
print(PLANT_BEAN_SHARECODES)
