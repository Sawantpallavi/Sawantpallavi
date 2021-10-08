import json
x={
"BMI":[
        {"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
        { "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
        { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
        { "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
        {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
        {"Gender": "Female",  "HeightCm": 167, "WeightKg": 82}
    ]
}
print(json.dumps(x))

height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kg: "))

bmi = weight/height
print("Your BMI is: {0} and you are: ".format(bmi), end='')

if ( bmi < 16):
   print("severely underweight")

elif ( bmi >= 16 and bmi < 18.5):
   print("underweight")

elif ( bmi >= 18.5 and bmi < 25):
   print("Healthy")

elif ( bmi >= 25 and bmi < 30):
   print("overweight")

elif ( bmi >=30):
   print("severely overweight")
