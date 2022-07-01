print("Hello World")
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1]== 'Denver':
        print(counties[1])
if counties[2] != 'Jefferson':
        print(counties[2])
#What is the score?
score = int(input("What is your test score?"))

#Determine the grade

if score >= 90:
        print('Your grade is an A.')

else:
    if score >= 80:
        print('Your grade is a B.')
    
    else:
        if score >= 70:
            print('Your grade is a C.')
        
        else:
            if score >= 60:
                print('Your score is a D.')

            else:
                print('Your score is an F.')


#What is the score?

score = int(input("What is your test score? "))

#Determine the grade.

if score >= 90:
    print('Your grade is an A.')

elif score >= 80:
    print('Your grade is a B.')

elif score >= 70:
    print('Your grade is a C.')

elif score >= 60:
    print('Your grade is a D.')

else:
    print('Your grade is an F.')

counties = ["Arapahoe","Denver","Jefferson"]

if "El Paso" in counties:
    print("El Paso is in the list of counties.")

else:
    print("El Paso is not the list of counties.")

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list")

else:
    print("Arapahoe or El Paso is not in the list of counties.")
    
for county in counties:
    print(county)

numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)


counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}


for county in counties_dict:
    print(county)
