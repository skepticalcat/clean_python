import pandas as pd


def data():
    csv = pd.read_csv("data/starbucks-menu-nutrition-drinks.csv")
    df_w_nl = csv.replace("-", None)

    naughty_cols = [x for x in df_w_nl.columns if x != "Drink name"]
    df_w_nl_fl = df_w_nl.astype({x: "Float64" for x in naughty_cols})
    return df_w_nl_fl



dataframe = data()
sugarbomb = dataframe[dataframe["Carb. (g)"] == dataframe["Carb. (g)"].max()]["Drink name"].values[0]

print(f"The most sugary drink is {sugarbomb}")

####

low_cal_drinks = dataframe[dataframe["Calories"] < 50]
low_cal_drinks_1 = low_cal_drinks.sort_values("Calories")
low_cal_drinks_2 = low_cal_drinks_1[:3]

print("The three drinks with the lowest calories are:")
low_cal_drinks_2.apply(lambda row: print("\t", row["Drink name"]), axis=1)

####

carbcal = dataframe["Carb. (g)"].corr(dataframe["Calories"]) # correlation between sugars and calories
print(f"Correlation between sugars and calories is {carbcal}")
