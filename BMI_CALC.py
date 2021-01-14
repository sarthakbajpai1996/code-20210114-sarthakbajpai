import json
import pandas as pd

json_data = '[{"Gender": "Male", "HeightCm": 171,"WeightKg": 96 },\
				{ "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },\
				{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },\
				{ "Gender": "Female", "HeightCm": 166, "WeightKg": 62},\
				{"Gender": "Female", "HeightCm": 150, "WeightKg": 70},\
				{"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]'


HEALTH_RISK_DATA = {
					"Underweight":'Malnutrition risk',
					"Normal Weight":'Low risk',
					"OverWeight":'Enhanced risk',
					"Moderatly obese":'Medium risk',
					"Severely obese":'High risk',
					"Very Severely obese":'Very high risk',
					}


def calculate_bmi(df):
	df["BMI"] = (df["WeightKg"]) / ((df["HeightCm"])/100)
	return df

def bmi_category(df):
	"""
	BMI CATEGORY:

		Underweight: less than or equal to 18.4
		Normal Weight: between 18.5 to 24.9
		OverWeight: between 25 to 29.9
		Moderatly obese: between 30 to 34.9
		Severely obese: between 35 to 39.9 
		Very Severely obese: more than or equal to 40
	"""
	df.loc[(df['BMI']<=18.4) , ['BMI CATEGORY']] = 'Underweight'
	df.loc[(df['BMI']>=18.5)&(df['BMI']<=24.9), ['BMI CATEGORY', "Health risk"]] = 'Normal Weight'
	df.loc[(df['BMI']>=25)&(df['BMI']<=29.9), ['BMI CATEGORY', "Health risk"]] = 'OverWeight'
	df.loc[(df['BMI']>=30)&(df['BMI']<=34.9), ['BMI CATEGORY', "Health risk"]] = 'Moderatly obese'
	df.loc[(df['BMI']>=35)&(df['BMI']<=39.9), ['BMI CATEGORY', "Health risk"]] = 'Severely obese'
	df.loc[(df['BMI']>=40), ['BMI CATEGORY', "Health risk"]] = 'Very Severely obese'

	return df

def health_risk(df):
	df["Health risk"] = df["Health risk"].map(HEALTH_RISK_DATA)
	return df

def main_handler(data):
	df = pd.read_json(data)
	df["BMI"] = ""
	df["BMI CATEGORY"] = ""
	df["Health risk"] = ""
	calculate_bmi(df)
	bmi_category(df)
	health_risk(df)
	print(df)


if __name__ == '__main__':
	main_handler(json_data)
