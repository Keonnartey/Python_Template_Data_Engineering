from main import max_cars
import pandas as pd

def test_max():
    cars = pd.read_csv(r"https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv")
    target_column = "mpg"
    max_mpg = max_cars(cars, target_column)

    max_mpg = max_cars(cars, target_column)
    calculated_max = cars[target_column].max()
    assert calculated_max == max_mpg

if __name__ == "__main__":
    test_max()
