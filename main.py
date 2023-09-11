import pandas as pd
import numpy as np

car = pd.read_csv(r"https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv")
#print(car.head())
#print(car["mpg"])

def max_cars(x) -> float:
    x = car["mpg"].max()
    return x

max_cars()
