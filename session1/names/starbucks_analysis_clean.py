import pandas as pd


def load_data_from_csv():
    raw_dataframe = pd.read_csv("data/starbucks-menu-nutrition-drinks.csv")
    raw_dataframe_with_none_values = raw_dataframe.replace("-", None)

    non_string_columns = [x for x in raw_dataframe_with_none_values.columns if x != "Drink name"]
    cleaned_dataframe = raw_dataframe_with_none_values.astype({x: "Float64" for x in non_string_columns})
    return cleaned_dataframe



starbucks_drinks_df = load_data_from_csv()
drink_with_highest_sugar_name = starbucks_drinks_df[starbucks_drinks_df["Carb. (g)"] == starbucks_drinks_df["Carb. (g)"].max()]["Drink name"].values[0]

print(f"The most sugary drink is {drink_with_highest_sugar_name}")

####

low_calorie_drinks = starbucks_drinks_df[starbucks_drinks_df["Calories"] < 50]
low_calorie_drinks_sorted = low_calorie_drinks.sort_values("Calories")
top_three_low_calorie_drinks = low_calorie_drinks_sorted[:3]

print("The three drinks with the lowest calories are:")
top_three_low_calorie_drinks.apply(lambda row: print("\t", row["Drink name"]), axis=1)

####

pearson_correlation_carb_calories = starbucks_drinks_df["Carb. (g)"].corr(starbucks_drinks_df["Calories"])
print(f"Correlation between sugars and calories is {pearson_correlation_carb_calories}")
