
#----------------------------------------------------------------------------------------------------
# Names(Group members)   :       Diya - 500190846, Jasmine Kaur Chana - 500189563, Madhav - 500191949
# Course                 :       Introduction to Computer Programming 01 (P00 Group 1
# Course Code            :       COMP1026
# Submitted to           :       Prof. Lilly Varghese
# Created                :       5/07/2021
# Project number         :       1
# About the Project      :       This is a menu-driven Group Project.
#----------------------------------------------------------------------------------------------------

print("|-----------------------|")
print("|                       |")
print("|                       |")
print("|       FITNESS-24      |")
print("|                       |")
print("|                       |")      
print("|-----------------------|")
print("                         ")
print("***IT'S NEVER TOO EARLY OR TOO LATE TO WORK TOWARDS BEING THE HEALTHIEST YOU***")

#enter your details
name = str(input("Enter your name : "))
print("      Your age determines how much you should consume.")
age = int(input("Enter your age : "))
print("      This will help us to personalize the app for you")
place = input("Enter your place: ")


print("\nHello "+ name+" !\n")
print("**Welcome to our Fitness World.**")
print("We are Fitness 24, your number 1 app dedicated towards providing the best healthy lifestyle while being at your comfort zones.\n")

while 1==1:   
    print(" Press 1 for ABOUT US")
    print(" Press 2 for TOOLS")
    print(" Press 3 for DIET PLAN SUGGESTION")
    print(" Press 4 for WORKOUT PLANS")
    print(" Press 5 for FEEDBACK")
    print(" Press 6 for COVID-19 GUIDELINES")
    print(" Press 7 for COVID-19 RECOVERY TIPS")
    print(" Press 8 for Our Developers")
    print(" Press 9 for Exit\n")

    a = int(input("Enter Number : "))


    if a==1:
        print("------------")
        print("|          |")
        print("| ABOUT US |")
        print("|          |")
        print("------------")



        while 1 == 1:
            print(" Press -1- for (About what our center can provide...Like EQUIPMENTS & TRAINERS.)")
            print(" Press -2- for (Location.)")
            print(" Press -3- for (Email and Contact details.)")
            print(" Press -4- for (About the app.)")
            print(" Press -5- for (What kind of fitness regiment we can provide and what makes us better than most of the rest.)")
            print(" Press -6- for Exit\n")
            f = int(input("Choose: "))

            if (f == 1):
                print("\n*****NUTRITIAN--FITNESS--YOGA*****\n")
                print("NUTRITION:- (Dietitians and Nutritionists)-- Want to lose weight, gain muscles, overcome medical conditions, or simply eat better? Get a certified dietitian to design a personalized diet plan that delivers results and fits into your lifestyle.")
                print("\nFITNESS:- (Personal Fitness Trainers)-- Our internationally certified personal fitness trainers will help you lose weight, build muscle, recover from physical injury, or medical conditions with personalized home and gym based workout plans.")
                print("\nYOGA:- (Fitness24 Yoga Instructors)-- Embrace the many benefits of Yoga. Manage stress, improve flexibility, accelerate your recovery from injuries, medical conditions, and more with the help of certified yoga instructors.\n")
            elif (f == 2):
                print("*****LOCATION***** ")
                print("Address: Singapore: Fitness24 Private Limited 20 Bendemeer Road, #03-12 BS Bendemeer Centre, Singapore 339914\n")
                print("Malaysia: Suite 28-1, Level 28, Vertical Corporate Tower B, Avenue 10, The Vertical, Bangsar South City, 8 Jalan Kerinchi, 59200 Kuala Lumpur\n")
            elif (f == 3):
                print("*****Email & Contact Details***** ")
                print("Email:- Support@fitness24.com")
                print("Call us at:- 1800 000 9501\n")
            elif (f == 4):
                print("*****About Fitness 24***** ")
                print("Here's How we Work for you towards a healthier lifestyle\n")
                print("Initializing with your personal details, we will track your progress by counting the food intake, water consumption, workouts and much more in order to keep you on track.\n")
                print("Personal training will also be involved in this journey by our professionalists. Proper workout routine will be set.\n ")
                print("Balance and Nutrition in the your diet will be the foremost priority, handles by our professional ditetians.\n")
                print("For better clearance you can check our FEEDBACK section.\n")
                print("Covid-19 reated guidelines and its recovery tips will also me found.\n")

            elif (f == 5):
                print("*****A CORPORATE WELLNESS PROGRAM THAT WORKS!*****")
                print("Improve your employee engagement with India's Largest & Most loved fitness app -FITNESS 24-.")
                print("INDIA'S FIRST CHOICE FOR WORKPLACE WELLNESS:-\n amdocs\nBMW\nCocaCola\nITC Limited\nNestle\nShell.")
                print("WHAT MAKES US EFFECTIVE THAN OTHERS? \n")
                print("(A)-App based Gamified Process:----- \nLeaderboard\nTeams\nModerated health clubs\nTasks & Objectives.\n")
                print("(B)-High Engagement:----- \nMarketing & Promotion\nFitness & Nutrition drives\nRegistration Kiosks\n Webinars & Lives.\n")
                print("(C)-Health Delivered:----- \nHighly qualified coaches\nDiet & Workout Plans\nContent educate users\nPersonalised coaching.\n")
                print("(D)-Measurable Impact:----- \nMonthly company report\nIndividual Progress\nActionable Insight\nDashboards.\n\n")

            elif f == 6:
                print("")
                break


    elif a==2:
        print("------------")
        print("|          |")
        print("|  TOOLS   |")
        print("|          |")
        print("------------") 

        # tools based on your requirement 

        while 1==1:
            print("\n1. Actual Body Weight Range")
            print("2. The Basal Metabolic Rate(BMR) Calculator")
            print("3. The Active Metabolic Rate(AMR) Calculator")
            print("4. The Body Mass Index(BMI) Calculator")
            print("5. Required Calories Calculator")
            print("6. Medical condtitions")
            print("7. Exit\n")

            # choose your option for calculating body weight range, BMR, AMR, BMI, calorie calculator and the medical conditions

            choose = int(input("What you want to calculate? "))

            if choose == 1:
                print("\n\n                                 Hey There!")
                print("We're happy that you have taken the first step towards healthier you.\n         We need a few details to kickstart your journey.")
                print("      This will helps us to calculate the target weight.")
                gender = str(input("  What's your Gender?(Female/Male) "))                                                # enter your gender/sex
                print("      Your age determines how much you should consume.")
                age = float(input("  What's your Age? "))                                                                 # enter your age
                print("\nYour height helps us to calculate important body stats to help you reachh your goal. ")
                height = float(input("  How tall are you?(In Centimeters) "))                                             # enter your height in centimeters
                print("This will help us determine your goal, and monitor your progress over time.")
                weight = float(input("  What's your current weight?(In kilograms) " ))                                    # enter your weight in kilograms

    # perfect body weight range according to the gender and height

                if gender == "Female" and height == 137:
                    print("Your weight perfectly aligned with your gender and height should fall between 28.5/34.9 kg ")
                elif gender == "Male" and height == 137:
                    print("Your weight perfectly aligned with your gender and height should fall between 28.5/34.9 kg ")
                elif gender == "Female" and height == 140:
                    print("Your weight perfectly aligned with your gender and height should fall between 30.8/37.6 kg ")
                elif gender == "Male" and height == 140:
                    print("Your weight perfectly aligned with your gender and height should fall between 30.8/38.1 kg ")
                elif gender == "Female" and height == 142:
                    print("Your weight perfectly aligned with your gender and height should fall between 32.6/39.9 kg ")
                elif gender == "Male" and height == 142:
                    print("Your weight perfectly aligned with your gender and height should fall between 33.5/40.8 kg ")
                elif gender == "Female" and height == 145:
                    print("Your weight perfectly aligned with your gender and height should fall between 34.9/42.6 kg ")
                elif gender == "Male" and height == 145:
                    print("Your weight perfectly aligned with your gender and height should fall between 35.8/43.9 kg ")
                elif gender == "Female" and height == 147:
                    print("Your weight perfectly aligned with your gender and height should fall between 36.4/44.9 kg ")
                elif gender == "Male" and height == 147:
                    print("Your weight perfectly aligned with your gender and height should fall between 38.5/46.7 kg ")
                elif gender == "Female" and height == 150:
                    print("Your weight perfectly aligned with your gender and height should fall between 39/47.6 kg ")
                elif gender == "Male" and height == 150:
                    print("Your weight perfectly aligned with your gender and height should fall between 40.8/49.9 kg ")
                elif gender == "Female" and height == 152:
                    print("Your weight perfectly aligned with your gender and height should fall between 40.8/49.9 kg ")
                elif gender == "Male" and height == 152:
                    print("Your weight perfectly aligned with your gender and height should fall between 43.1/53 kg ")
                elif gender == "Female" and height == 155:
                    print("Your weight perfectly aligned with your gender and height should fall between 43.1/52.6 kg ")
                elif gender == "Male" and height == 155:
                    print("Your weight perfectly aligned with your gender and height should fall between 45.8/55.8 kg ")
                elif gender == "Female" and height == 157:
                    print("Your weight perfectly aligned with your gender and height should fall between 44.9/54.9 kg ")
                elif gender == "Male" and height == 157:
                    print("Your weight perfectly aligned with your gender and height should fall between 48.1/58.9 kg ")
                elif gender == "Female" and height == 160:
                    print("Your weight perfectly aligned with your gender and height should fall between 47.2/57.6 kg ")
                elif gender == "Male" and height == 160:
                    print("Your weight perfectly aligned with your gender and height should fall between 50.8/61.6 kg ")
                elif gender == "Female" and height == 163:
                    print("Your weight perfectly aligned with your gender and height should fall between 49/59.9 kg ")
                elif gender == "Male" and height == 163:
                    print("Your weight perfectly aligned with your gender and height should fall between 53/64.8 kg ")
                elif gender == "Female" and height == 165:
                    print("Your weight perfectly aligned with your gender and height should fall between 51.2/62.6 kg ")
                elif gender == "Male" and height == 165:
                    print("Your weight perfectly aligned with your gender and height should fall between 55.3/68 kg ")
                elif gender == "Female" and height == 168:
                    print("Your weight perfectly aligned with your gender and height should fall between 53/64.8 kg ")
                elif gender == "Male" and height == 168:
                    print("Your weight perfectly aligned with your gender and height should fall between 58/70.7 kg ")
                elif gender == "Female" and height == 170:
                    print("Your weight perfectly aligned with your gender and height should fall between 55.3/67.6 kg ")
                elif gender == "Male" and height == 170:
                    print("Your weight perfectly aligned with your gender and height should fall between 60.3/73.9 kg ")
                elif gender == "Female" and height == 173:
                    print("Your weight perfectly aligned with your gender and height should fall between 57.1/69.8 kg ")
                elif gender == "Male" and height == 173:
                    print("Your weight perfectly aligned with your gender and height should fall between 63/76.6 kg ")
                elif gender == "Female" and height == 175:
                    print("Your weight perfectly aligned with your gender and height should fall between 59.4/72.6 kg ")
                elif gender == "Male" and height == 175:
                    print("Your weight perfectly aligned with your gender and height should fall between 65.3/79.8 kg ")
                elif gender == "Female" and height == 178:
                    print("Your weight perfectly aligned with your gender and height should fall between 61.2/74.8 kg ")
                elif gender == "Male" and height == 178:
                    print("Your weight perfectly aligned with your gender and height should fall between 67.6/83 kg ")
                elif gender == "Female" and height == 180:
                    print("Your weight perfectly aligned with your gender and height should fall between 63.5/77.5 kg ")
                elif gender == "Male" and height == 180:
                    print("Your weight perfectly aligned with your gender and height should fall between 70.3/85.7 kg ")
                elif gender == "Female" and height == 183:
                    print("Your weight perfectly aligned with your gender and height should fall between 65.3/79.8 kg ")
                elif gender == "Male" and height == 183:
                    print("Your weight perfectly aligned with your gender and height should fall between 72.6/88.9 kg ")
                elif gender == "Female" and height == 185:
                    print("Your weight perfectly aligned with your gender and height should fall between 67.6/82.5 kg ")
                elif gender == "Male" and height == 185:
                    print("Your weight perfectly aligned with your gender and height should fall between 75.3/91.6 kg ")
                elif gender == "Female" and height == 188:
                    print("Your weight perfectly aligned with your gender and height should fall between 69.4/84.8 kg ")
                elif gender == "Male" and height == 188:
                    print("Your weight perfectly aligned with your gender and height should fall between 77.5/94.8 kg ")
                elif gender == "Female" and height == 191:
                    print("Your weight perfectly aligned with your gender and height should fall between 71.6/87.5 kg ")
                elif gender == "Male" and height == 191:
                    print("Your weight perfectly aligned with your gender and height should fall between 79.8/98 kg ")
                elif gender == "Female" and height == 193:
                    print("Your weight perfectly aligned with your gender and height should fall between 73.5/89.8 kg ")
                elif gender == "Male" and height == 193:
                    print("Your weight perfectly aligned with your gender and height should fall between 82.5/100.6 kg ")
                elif gender == "Female" and height == 195:
                    print("Your weight perfectly aligned with your gender and height should fall between 75.7/92.5 kg ")
                elif gender == "Male" and height == 195:
                    print("Your weight perfectly aligned with your gender and height should fall between 84.8/103.8 kg ")
                elif gender == "Female" and height == 198:
                    print("Your weight perfectly aligned with your gender and height should fall between 77.5/94.8 kg ")
                elif gender == "Male" and height == 198:
                    print("Your weight perfectly aligned with your gender and height should fall between 87.5/106.5 kg ")
                elif gender == "Female" and height == 201:
                    print("Your weight perfectly aligned with your gender and height should fall between 79.8/97.5 kg ")
                elif gender == "Male" and height == 201:
                    print("Your weight perfectly aligned with your gender and height should fall between 89.8/109.7 kg ")
                elif gender == "Female" and height == 203:
                    print("Your weight perfectly aligned with your gender and height should fall between 81.6/99.8 kg ")
                elif gender == "Male" and height == 203:
                    print("Your weight perfectly aligned with your gender and height should fall between 92/112.9 kg ")
                elif gender == "Female" and height == 205:
                    print("Your weight perfectly aligned with your gender and height should fall between 83.9/102.5 kg ")
                elif gender == "Male" and height == 205:
                    print("Your weight perfectly aligned with your gender and height should fall between 94.8/115.6 kg ")
                elif gender == "Female" and height == 208:
                    print("Your weight perfectly aligned with your gender and height should fall between 85.7/104.8 kg ")
                elif gender == "Male" and height == 208:
                    print("Your weight perfectly aligned with your gender and height should fall between 97/118.8 kg ")
                elif gender == "Female" and height == 210:
                    print("Your weight perfectly aligned with your gender and height should fall between 88/107.5 kg ")
                elif gender == "Male" and height == 210:
                    print("Your weight perfectly aligned with your gender and height should fall between 99.8/121.5 kg ")
                elif gender == "Female" and height == 213:
                    print("Your weight perfectly aligned with your gender and height should fall between 89.8/109.7 kg ")
                elif gender == "Male" and height == 213:
                    print("Your weight perfectly aligned with your gender and height should fall between 102/124.7 kg ")
                print("\n---------------------------------------------------------------------------------------------\n")


            elif choose == 2:
                print("\n\n                                 Hey There!")
                print("We're happy that you have taken the first step towards healthier you.\n         We need a few details to kickstart your journey.")
                print("      This will helps us to calculate the target weight.")
                gender = str(input("  What's your Gender?(Female/Male) "))
                print("      Your age determines how much you should consume.")
                age = float(input("  What's your Age? "))
                print("\nYour height helps us to calculate important body stats to help you reachh your goal. ")
                height = float(input("  How tall are you?(In Centimeters) "))
                print("This will help us determine your goal, and monitor your progress over time.")
                weight = float(input("  What's your current weight?(In kilograms) " ))

    # based on the lifestyle choose an appropriate daily routine

                print("\nBased on your lifestyle, we can assess your daily calories requirement.")
                print("Choose any one: ")
                print("1. Little or No Activity")
                print("2. Lightly Active")
                print("3. Moderatively active")
                print("4. Active")
                print("5. Very Active")
                active = int(input("  How active you are? "))
                if active == 1:
                    print("Mostly sitting through the day(e.g. Desk job, Bank teller.)")
                elif active == 2:
                    print("Mostly standing through the day(e.g. Sales Associate, Teacher)")
                elif active == 3:
                    print("Mostly walking or doing physical activities through the day(e.g. Tour Guide, Waiter)")
                elif active == 4:
                    print("Mostly walking or doing exercise 6–7 days/week")
                elif active == 5:
                    print("Mostly doing heavy physical activities through the day(e.g. Gym, Instructor, Construction Worker)")

    # calculating BMR by age,gender and height

                BMR = 655.1+(9.563*weight)+(1.850*height)-(6.755 * age)
                BMR1 = 66.47+(13.75*weight)+(5.003*height)-(6.755 * age)

                if gender == "Female":
                    print("The Basal Metabolic Rate(BMR) of you is", BMR)
                else:
                    print("The Basal Metabolic Rate(BMR) of you is", BMR1)
                print("\n---------------------------------------------------------------------------------------------\n")


            elif choose == 3:
                print("\n\n                                 Hey There!")
                print("We're happy that you have taken the first step towardsa healthier you.\n         We need a few details to kickstart your journey.")
                print("      This will helps us to calculate the target weight.")
                gender = str(input("  What's your Gender?(Female/Male) "))
                print("      Your age determines how much you should consume.")
                age = float(input("  What's your Age? "))
                print("\nYour height helps us to calculate important body stats to help you reachh your goal. ")
                height = float(input("  How tall are you?(In Centimeters) "))
                print("This will help us determine your goal, and monitor your progress over time.")
                weight = float(input("  What's your current weight?(In kilograms) " ))

                BMR = 655.1+(9.563*weight)+(1.850*height)-(6.755 * age)
                BMR1 = 66.47+(13.75*weight)+(5.003*height)-(6.755 * age)

    # based on the above calculated BMR, active metabolic rate is calculated

                AMR = BMR*1.2
                AMR1 = BMR*1.375
                AMR2 = BMR*1.55
                AMR3 = BMR*1.725
                AMR4 = BMR*1.9

                amr = BMR1*1.2
                amr1 = BMR1*1.375
                amr2 = BMR1*1.55
                amr3 = BMR1*1.725
                amr4 = BMR1*1.9

                print("\nBased on your lifestyle, we can assess your daily calories requirement.")
                print("Choose any one: ")
                print("1. Little or No Activity")
                print("2. Lightly Active")
                print("3. Moderatively active")
                print("4. Active")
                print("5. Very Active")
                active = int(input("  How active you are? "))
                if active == 1:
                    print("Mostly sitting through the day(e.g. Desk job, Bank teller.)")
                elif active == 2:
                    print("Mostly standing through the day(e.g. Sales Associate, Teacher)")
                elif active == 3:
                    print("Mostly walking or doing physical activities through the day(e.g. Tour Guide, Waiter)")
                elif active == 4:
                    print("Mostly walking or doing exercise 6–7 days/week")
                elif active == 5:
                    print("Mostly doing heavy physical activities through the day(e.g. Gym, Instructor, Construction Worker)")


                if active == 1 and gender == "Female":
                    print("The Active Metabolic Rate(AMR) of you is", AMR)
                elif active == 1 and gender == "Male":
                    print("The Active Metabolic Rate(AMR) of you is", amr)
                elif active == 2 and gender == "Female":
                    print("The Active Metabolic Rate(AMR) of you is", AMR1)
                elif active == 2 and gender == "Male":
                    print("The Active Metabolic Rate(AMR) of you is", amr1)
                elif active == 3 and gender == "Female":
                    print("The Active Metabolic Rate(AMR) of you is", AMR2)
                elif active == 3 and gender == "Male":
                    print("The Active Metabolic Rate(AMR) of you is", amr2)
                elif active == 4 and gender == "Female":
                    print("The Active Metabolic Rate(AMR) of you is", AMR3)
                elif active == 4 and gender == "Male":
                    print("The Active Metabolic Rate(AMR) of you is", amr3)
                if active == 5 and gender == "Female":
                    print("The Active Metabolic Rate(AMR) of you is", AMR4)
                elif active == 5 and gender == "Male":
                    print("The Active Metabolic Rate(AMR) of you is", amr4)
                print("\n---------------------------------------------------------------------------------------------\n")


            elif choose == 4:
                print("\n\n                                 Hey There!")
                print("We're happy that you have taken the first step towards healthier you.\n         We need a few details to kickstart your journey.")
                print("      This will helps us to calculate the target weight.")
                gender = str(input("  What's your Gender?(Female/Male) "))
                print("      Your age determines how much you should consume.")
                age = float(input("  What's your Age? "))
                print("\nYour height helps us to calculate important body stats to help you reachh your goal. ")
                height = float(input("  How tall are you?(In Centimeters) "))
                print("This will help us determine your goal, and monitor your progress over time.")
                weight = float(input("  What's your current weight?(In kilograms) " ))

    # calculate BMI through height and weight

                BMI = (weight/height/height) * (10000)
                print("The calculated BMI according to your weight and height is", BMI)

    # BMI clasification into underweight, optimal, overweight and obese

                if BMI < 18.5:
                    print("You are Underweight.")
                    print("You have to gain some body fat in order for your better health.")
                elif BMI >= 18.5 and BMI < 25:
                    print("You are Optimal")
                    print("You have to maintain your body fat for your better health. ")
                elif BMI >= 25 and BMI < 30:
                    print("You are Overweight")
                    print("You have to lose your body fat for your better health.")
                else:
                    print("You are Obese")
                    print("You have to highly lose your body fat for your better health.")
                print("\n---------------------------------------------------------------------------------------------\n")


            elif choose == 5:
                print("\n\n                                Hey There!")
                print("We're happy that you have taken the first step towards healthier you.\n         We need a few details to kickstart your journey.")
                print("      This will helps us to calculate the target weight.")
                gender = str(input("  What's your Gender?(Female/Male) "))
                print("      Your age determines how much you should consume.")
                age = float(input("  What's your Age? "))
                print("\nYour height helps us to calculate important body stats to help you reachh your goal. ")
                height = float(input("  How tall are you?(In Centimeters) "))
                print("This will help us determine your goal, and monitor your progress over time.")
                weight = float(input("  What's your current weight?(In kilograms) " ))

    # calorie maintainance based on lifestyle trends and body weight

                print("\nCALORIE MAINTAINANCE")
                print("---------------------\n")
                print("This helps you to maintain the number of calories your body needs to support energy expenditure.")

                print("1. Light Active")
                print("2. Active")
                print("3. Very Active\n")

                choose1 = int(input("Choose your Category: "))

                if choose1 == 1:
                    mainCal = weight * 22 * 1.45
                    print("The maintainance calorie for you is", mainCal)
                elif choose1 == 2:
                    mainCal = weight * 22 * 1.6
                    print("The maintainance calorie for you is", mainCal)
                else:
                    mainCal = weight * 22 * 2
                    print("The maintainance calorie for you is", mainCal)


                print("\nCalorie Breakdown")
                print("------------------\n")
                print("Calories are the amount of energy released when your body breaks down (digests and absorbs) food. There are different calorie requirements for different people.")

    # choose preference what you want to do for your body

                print("What you want to do? \n")
                print("1. Gain weight")
                print("2. Maintain weight")
                print("3. Lose weight\n")

                choose2 = int(input("Choose your preference: "))

    # according to the preference, amount of proteins, fats and carbohydrates needed

                if choose2 == 1:
                    reqCal = round((mainCal + 200),2)
                    Protein = round((weight * 2.2),2)
                    fat = round((0.25 * reqCal),2)
                    carbs = round((reqCal - (Protein + fat)),2)
                    print("Required amount of Proteins, Fats and Carbohydrates your body needs")
                    print("-----------------------------")
                    print("|Proteins|Fats|Carbohydrates|")
                    print("-----------------------------")
                    print("|",Protein,"|",fat,"|",carbs,"|")
                    print("-----------------------------")

                elif choose2 == 2:
                    reqCal = round((mainCal),2)
                    Protein = round((weight * 2),2)
                    fat = round((0.19 * reqCal),2)
                    carbs = round((reqCal - (Protein + fat)),2)
                    print("Required amount of Proteins, Fats and Carbohydrates your body needs")
                    print("-----------------------------")
                    print("|Proteins|Fats|Carbohydrates|")
                    print("-----------------------------")
                    print("|",Protein,"|",fat,"|",carbs,"|")
                    print("-----------------------------")

                else:
                    reqCal = round((mainCal - 200),2)
                    Protein = round((weight * 1.8),2)
                    fat = round((0.15 * reqCal),2)
                    carbs = round((reqCal - (Protein + fat)),2)
                    print("Required amount of Proteins, Fats and Carbohydrates your body needs")
                    print("-----------------------------")
                    print("|Proteins|Fats|Carbohydrates|")
                    print("-----------------------------")
                    print("|",Protein,"|",fat,"|",carbs,"|")
                    print("-----------------------------")
                print("\n---------------------------------------------------------------------------------------------\n")


            # medical issues lists

            elif choose == 6:
                print("This info will help us guide you to your fitness goals safely and quickly. ")
                print("1.  None")
                print("2.  Diabetes")
                print("3.  High Cholestrol")
                print("4.  Hypertension")
                print("5.  PCOS")
                print("6.  Thyroid")
                print("7.  Physical Injury")
                print("8.  Exercise stress/anxiety")
                print("9.  Sleep Issues")
                print("10. Depression")
                print("11. Anger issues")
                
                a = int(input("Choose: "))
                if a == 1:
                    print("You are more precious to this world than you'll ever know.\nIf you don't have your health, you don't have anything\nMaintain your health.")


    # precautions for Diabetes

                elif a == 2:
                    print("PREVENTIONS")
                    print("1. Make a commitment to managing your diabetes - Monitor your blood sugar, and follow your doctor's instructions for managing your blood sugar level.")
                    print("2. Don't smoke")
                    print("3. Keep your blood pressure and cholesterol under control")
                    print("4. Schedule regular physicals and eye exams")
                    print("5. Keep your vaccines up to date")
                    print("6. Take care of your teeth")
                    print("7. Pay attention to your feet")
                    print("8. Consider a daily aspirin")
                    print("9. If you drink alcohol, do so responsibly")
                    print("10. Take stress seriously")
                    print("\nYou are more precious to this world than you'll ever know.\nIf you don't have your health, you don't have anything\nTake care of you health.")

                elif a == 3:
                    print("PREVENTIONS")
                    print("1. Eat a low-salt diet that emphasizes fruits, vegetables and whole grains")
                    print("2. Limit the amount of animal fats and use good fats in moderation")
                    print("3. Lose extra pounds and maintain a healthy weight")
                    print("4. Quit smoking")
                    print("5. Exercise on most days of the week for at least 30 minutes")
                    print("6. Drink alcohol in moderation, if at all")
                    print("7. Manage stress")
                    print("\nYou are more precious to this world than you'll ever know.\nIf you don't have your health, you don't have anything\nTake care of you health.")


                elif a == 4:
                    print("PREVENTIONS")
                    print("1. Maintain a healthy weight.")
                    print("2. Eat a balanced diet.")
                    print("3. Cut back on salt.")
                    print("4. Limit alcohol.")
                    print("5. Exercise regularly.")
                    print("6. Manage stress.")
                    print("7. Monitor your blood pressure.")
                    print("\nYou are more precious to this world than you'll ever know.\nIf you don't have your health, you don't have anything\nTake care of you health.")


                elif a == 5:
                    print("PREVENTIONS")
                    print("1. Over-the-counter medication")
                    print("2. Massage")
                    print("3. Exercise and stretching")
                    print("4. Heat: Heat increases blood flow, helping to reduce pain.")
                    print("5. Relaxation techniques: Relaxation techniques, such as meditation, yoga, and deep breathing, may help relieve anxiety and reduce the intensity of the pain.")
                    print("6. Weight loss")
                    print("7. Dietary changes")
                    print("\nYou are more precious to this world than you'll ever know.\nIf you don't have your health, you don't have anything\nTake care of you health.")


                elif a == 6:
                    print("PREVENTIONS")
                    print("1. Avoid Processed Food: A lot of chemicals can alter the thyroid hormone production. One needs to avoid any kind of processed food; they are on the edge of the thyroid disorder.")
                    print("2. Avoid Soy: Limit the soy intake as it alters the hormone production.")
                    print("3. Stop Smoking: The toxins released during smoking can make the thyroid gland over sensitive which can lead to thyroid disorders.")
                    print("4. Reduce Stress: Stress is one of the major contributors in many health disorders including thyroid disease.")
                    print("\nYou are more precious to this world than you'll ever know.\nIf you don't have your health, you don't have anything\nTake care of you health.")


                elif a == 7:
                    print("PREVENTIONS")
                    print("1. Strengthen muscles: Conditioning exercises during practice strengthens muscles used in play.")
                    print("2. Increase flexibility: Stretching exercises after games or practice can increase flexibility. ")
                    print("3. Take breaks: Rest periods during practice and games can reduce injuries and prevent heat illness.")
                    print("4. Play safe.")
                    print("5. Do not play through pain.")
                    print("6. Avoid heat illness by drinking plenty of fluids before, during and after exercise or play; decrease or stop practices or competitions during high heat/humidity periods; wear light clothing.")
                    print("7. Use the proper technique. This should be reinforced during the playing season.")
                    print("\nYou are more precious to this world than you'll ever know.\nIf you don't have your health, you don't have anything\nTake care of you health.")


                elif a == 8:
                    print("PREVENTIONS")
                    print("1. Take a yoga class: Yoga has become a popular method of stress relief and exercise among all age groups.")
                    print("2. Learn to avoid procrastination")
                    print("3. Laugh: It’s hard to feel anxious when you’re laughing. It’s good for your health.")
                    print("4. Chew gum")
                    print("5. Write it down: One way to handle stress is to write things down.")
                    print("6. Reduce your caffeine intake")
                    print("7. Exercise")
                    print("\nYou are more precious to this world than you'll ever know.\nIf you don't have your health, you don't have anything\nTake care of you health.")


                elif a == 9:
                    print("PREVENTIONS")
                    print("1. Try to go to sleep at the same time each night and get up at the same time each morning.")
                    print("2. Don't eat a heavy meal late in the day.")
                    print("3. Try not to take naps during the day because naps may make you less sleepy at night.")
                    print("4. Avoid using your bed for anything other than sleep.")
                    print("5. Follow a routine to help you relax and wind down before sleep, such as reading a book, listening to music, or taking a bath.")
                    print("6. Make your sleeping place comfortable. Be sure that it is dark, quiet, and not too warm or too cold.")
                    print("7. Avoid caffeine, nicotine, and alcohol late in the day.")
                    print("\nYou are more precious to this world than you'll ever know.\nIf you don't have your health, you don't have anything\nTake care of you health.")


                elif a == 10:
                    print("PREVENTIONS")
                    print("1. Self-help: Regular exercise, getting enough sleep, and spending time with people you care about can improve depression symptoms.")
                    print("2. Counseling: Counseling or psychotherapy is talking with a mental health professional. ")
                    print("3. Alternative medicine: People with mild depression or ongoing symptoms can improve their well-being with complementary therapy.")
                    print("4. Medication: Prescription medicine called antidepressants can help change brain chemistry that causes depression")
                    print("5. Medication: Prescription medicine called antidepressants can help change brain chemistry that causes depression")
                    print("\nYou are more precious to this world than you'll ever know.\nIf you don't have your health, you don't have anything\nTake care of you health.")


                elif a == 11:
                    print("PREVENTIONS")
                    print("1. Think before you speak")
                    print("2. Once you're calm, express your anger")
                    print("3. Get some exercise")
                    print("4. Take a timeout")
                    print("5. Don't hold a grudge")
                    print("6. Use humor to release tension")
                    print("7. Practice relaxation skills")
                    print("\nYou are more precious to this world than you'll ever know.\nIf you don't have your health, you don't have anything\nTake care of you health.")





            elif choose == 7:
                break


    elif a==3:
        print("--------------------------")
        print("|                        |")
        print("|  DIET PLAN SUGGESTION  |")
        print("|                        |")
        print("--------------------------\n")

        while 1==1:

            print("PLease Tell us what do you want to do:- \n")
            print("1. Do you want to Loose Weight")
            print("2. Do you want to Stay Fit and Healthy")
            print("3. Do you want to Build Muscles")
            print("4. Do you want to Gain Weight")
            print("5. Exit\n")

            y= int(input("PLease Enter your Choice Here:- "))



            while y==1:
                n= str(input("\nPease Enter the day of the week whose Diet Regiment you want to see in small letters or if you want to see the Regiment of the whole week type 'full':- "))

                if (n == "sunday"):
                    print ("\n\n6:30 AM Cucumber Detox Water (1 glass)\n8:00 AM  Oats Porridge in Skimmed Milk (1 bowl), Mixed Nuts (25 grams)")
                    print("12:00 PM  Skimmed Milk Paneer (100 grams)\n2:00 PM Mixed Vegetable Salad (1 katori)\n2:10 PM  Dal(1 katori)Gajar Matar Sabzi (1 katori)/nRoti (1 roti/chapati)\n")
                    print("4:00 PM	Cut Fruits (1 cup) Buttermilk (1 glass)")
                    print("5:30 PM	Tea with Less Sugar and Milk (1 teacup)")
                    print("8:50 PM	Mixed Vegetable Salad (1 katori)")
                    print("9:00 PM	Dal (1 katori) Lauki Sabzi (1 katori)")
                    print("Roti (1 roti/chapati)")
                    break
                elif (n=="monday"):
                    print("\n\n6:30 AM	Cucumber Detox Water (1 glass)")
                    print("8:00 AM	Curd (1.5 katori) Mixed Vegetable Stuffed Roti (2 pieces)")
                    print("12:00 PM	Skimmed Milk Paneer (100 grams)")
                    print("2:00 PM	Mixed Vegetable Salad (1 katori)")
                    print("2:10 PM	Lentil Curry (0.75 bowl) Methi Rice (0.5 katori)")
                    print("4:00 PM	Apple (0.5 small (2-3/4″ dia)) Buttermilk (1 glass)")
                    print("5:30 PM	Coffee with Milk and Less Sugar (0.5 tea cup)")
                    print("8:50 PM	Mixed Vegetable Salad (1 katori)")
                    print("9:00 PM	Sauteed Vegetables with Paneer (1 katori) Roti (1 roti/chapati)")
                    print("Green Chutney (2 tablespoon)")
                    break
                elif (n=="tuesday"):
                    print("\n\n6:30 AM	Cucumber Detox Water (1 glass)")
                    print("8:00 AM	Skim Milk Yoghurt (1 cup (8 fl oz)) Multigrain Toast (2 toast)")
                    print("12:00 PM	Skimmed Milk Paneer (100 grams)")
                    print("2:00 PM	Mixed Vegetable Salad (1 katori)")
                    print("2:10 PM	Sauteed Vegetables with Paneer (1 katori) Roti (1 roti/chapati) Green Chutney (2 tablespoon)")
                    print("4:00 PM	Banana (0.5 small (6″ to 6-7/8″ long)) Buttermilk (1 glass)")
                    print("5:30 PM	Tea with Less Sugar and Milk (1 teacup)")
                    print("8:50 PM	Mixed Vegetable Salad (1 katori)")
                    print("9:00 PM	Lentil Curry (0.75 bowl) Methi Rice (0.5 katori)")
                    break
                elif (n=='wednesday'):
                    print("\n\n6:30 AM	Cucumber Detox Water (1 glass)")
                    print("8:00 AM	Fruit and Nuts Yogurt Smoothie (0.75 glass) Egg Omelette (1 serve(one egg))")
                    print("12:00 PM	Skimmed Milk Paneer (100 grams)")
                    print("2:00 PM	Mixed Vegetable Salad (1 katori)")
                    print("2:10 PM	Green Gram Whole Dal Cooked (1 katori) Bhindi sabzi (1 katori) Roti (1 roti/chapati)")
                    print("4:00 PM	Orange (1 fruit (2-5/8″ dia)) Buttermilk (1 glass)")
                    print("5:30 PM	Coffee with Milk and Less Sugar (0.5 teacup)")
                    print("8:50 PM	Mixed Vegetable Salad (1 katori)")
                    print("9:00 PM	Palak Chole (1 bowl) Steamed Rice (0.5 katori)")
                    break
                elif (n=="thrusday"):
                    print("\n\n6:30 AM	Cucumber Detox Water (1 glass)")
                    print("8:00 AM	Skimmed Milk (1 glass) Peas Poha (1.5 katori)")
                    print("12:00 PM	Skimmed Milk Paneer (100 grams)")
                    print("2:00 PM	Mixed Vegetable Salad (1 katori)")
                    print("2:10 PM	Low Fat Paneer Curry (1.5 katori) Missi Roti (1 roti)")
                    print("4:00 PM	Papaya (1 cup 1″ pieces) Buttermilk (1 glass)")
                    print("5:30 PM	Tea with Less Sugar and Milk (1 teacup)")
                    print("8:50 PM	Mixed Vegetable Salad (1 katori)")
                    print("9:00 PM	Curd (1.5 katori) Aloo Baingan Tamatar Ki Sabzi (1 katori) Roti (1 roti/chapati)")
                    break
                elif (n=="friday"):
                    print("\n\n6:30 AM	Cucumber Detox Water (1 glass)")
                    print("8:00 AM	Mixed Sambar (1 bowl) Idli (2 idli)")
                    print("12:00 PM	Skimmed Milk Paneer (100 grams)")
                    print("2:00 PM	Mixed Vegetable Salad (1 katori)")
                    print("2:10 PM	Curd (1.5 katori) Aloo Baingan Tamatar Ki Sabzi (1 katori) Roti (1 roti/chapati)")
                    print("4:00 PM	Cut Fruits (1 cup) Buttermilk (1 glass)")
                    print("5:30 PM	Coffee with Milk and Less Sugar (0.5 tea cup)")
                    print("8:50 PM	Mixed Vegetable Salad (1 katori)")
                    print("9:00 PM	Green Gram Whole Dal Cooked (1 katori)Bhindi sabzi (1 katori) Roti (1 roti/chapati)")
                    break
                elif (n=="saturday"):
                    print("\n\n6:30 AM	Cucumber Detox Water (1 glass)")
                    print("8:00 AM	Besan Chilla (2 cheela) Green Garlic Chutney (3 tablespoon)")
                    print("12:00 PM	Skimmed Milk Paneer (100 grams)")
                    print("2:00 PM	Mixed Vegetable Salad (1 katori)")
                    print("2:10 PM	Palak Chole (1 bowl) Steamed Rice (0.5 katori)")
                    print("4:00 PM	Apple(0.5 small (2-3/4″ dia)) Buttermilk (1 glass)")
                    print("5:30 PM	Tea with Less Sugar and Milk (1 teacup)")
                    print("8:50 PM	Mixed Vegetable Salad (1 katori)")
                    print("9:00 PM	Low Fat Paneer Curry (1 katori) Missi Roti (1 roti)")
                    break
                elif (n=="full"):
                    print("\n\nSunday\n")
                    print ("\n\n6:30 AM Cucumber Detox Water (1 glass)\n8:00 AM  Oats Porridge in Skimmed Milk (1 bowl), Mixed Nuts (25 grams)")
                    print("12:00 PM  Skimmed Milk Paneer (100 grams)\n2:00 PM Mixed Vegetable Salad (1 katori)\n2:10 PM  Dal(1 katori)Gajar Matar Sabzi (1 katori)/nRoti (1 roti/chapati)\n")
                    print("4:00 PM	Cut Fruits (1 cup) Buttermilk (1 glass)")
                    print("5:30 PM	Tea with Less Sugar and Milk (1 teacup)")
                    print("8:50 PM	Mixed Vegetable Salad (1 katori)")
                    print("9:00 PM	Dal (1 katori) Lauki Sabzi (1 katori)")
                    print("\n\nmonday\n")
                    print("\n\n6:30 AM	Cucumber Detox Water (1 glass)")
                    print("8:00 AM	Curd (1.5 katori) Mixed Vegetable Stuffed Roti (2 pieces)")
                    print("12:00 PM	Skimmed Milk Paneer (100 grams)")
                    print("2:00 PM	Mixed Vegetable Salad (1 katori)")
                    print("2:10 PM	Lentil Curry (0.75 bowl) Methi Rice (0.5 katori)")
                    print("4:00 PM	Apple (0.5 small (2-3/4″ dia)) Buttermilk (1 glass)")
                    print("5:30 PM	Coffee with Milk and Less Sugar (0.5 tea cup)")
                    print("8:50 PM	Mixed Vegetable Salad (1 katori)")
                    print("9:00 PM	Sauteed Vegetables with Paneer (1 katori) Roti (1 roti/chapati)")
                    print("Green Chutney (2 tablespoon)")
                    print("\n\ntuesday\n")
                    print("\n\n6:30 AM	Cucumber Detox Water (1 glass)")
                    print("8:00 AM	Skim Milk Yoghurt (1 cup (8 fl oz)) Multigrain Toast (2 toast)")
                    print("12:00 PM	Skimmed Milk Paneer (100 grams)")
                    print("2:00 PM	Mixed Vegetable Salad (1 katori)")
                    print("2:10 PM	Sauteed Vegetables with Paneer (1 katori) Roti (1 roti/chapati) Green Chutney (2 tablespoon)")
                    print("4:00 PM	Banana (0.5 small (6″ to 6-7/8″ long)) Buttermilk (1 glass)")
                    print("5:30 PM	Tea with Less Sugar and Milk (1 teacup)")
                    print("8:50 PM	Mixed Vegetable Salad (1 katori)")
                    print("9:00 PM	Lentil Curry (0.75 bowl) Methi Rice (0.5 katori)")
                    print("\n\nwednesday\n")
                    print("\n\n6:30 AM	Cucumber Detox Water (1 glass)")
                    print("8:00 AM	Fruit and Nuts Yogurt Smoothie (0.75 glass) Egg Omelette (1 serve(one egg))")
                    print("12:00 PM	Skimmed Milk Paneer (100 grams)")
                    print("2:00 PM	Mixed Vegetable Salad (1 katori)")
                    print("2:10 PM	Green Gram Whole Dal Cooked (1 katori) Bhindi sabzi (1 katori) Roti (1 roti/chapati)")
                    print("4:00 PM	Orange (1 fruit (2-5/8″ dia)) Buttermilk (1 glass)")
                    print("5:30 PM	Coffee with Milk and Less Sugar (0.5 teacup)")
                    print("8:50 PM	Mixed Vegetable Salad (1 katori)")
                    print("9:00 PM	Palak Chole (1 bowl) Steamed Rice (0.5 katori)")
                    print("\n\nthursday\n")
                    print("\n\n6:30 AM	Cucumber Detox Water (1 glass)")
                    print("8:00 AM	Skimmed Milk (1 glass) Peas Poha (1.5 katori)")
                    print("12:00 PM	Skimmed Milk Paneer (100 grams)")
                    print("2:00 PM	Mixed Vegetable Salad (1 katori)")
                    print("2:10 PM	Low Fat Paneer Curry (1.5 katori) Missi Roti (1 roti)")
                    print("4:00 PM	Papaya (1 cup 1″ pieces) Buttermilk (1 glass)")
                    print("5:30 PM	Tea with Less Sugar and Milk (1 teacup)")
                    print("8:50 PM	Mixed Vegetable Salad (1 katori)")
                    print("9:00 PM	Curd (1.5 katori) Aloo Baingan Tamatar Ki Sabzi (1 katori) Roti (1 roti/chapati)")
                    print("\n\nfriday\n")
                    print("\n\n6:30 AM	Cucumber Detox Water (1 glass)")
                    print("8:00 AM	Mixed Sambar (1 bowl) Idli (2 idli)")
                    print("12:00 PM	Skimmed Milk Paneer (100 grams)")
                    print("2:00 PM	Mixed Vegetable Salad (1 katori)")
                    print("2:10 PM	Curd (1.5 katori) Aloo Baingan Tamatar Ki Sabzi (1 katori) Roti (1 roti/chapati)")
                    print("4:00 PM	Cut Fruits (1 cup) Buttermilk (1 glass)")
                    print("5:30 PM	Coffee with Milk and Less Sugar (0.5 tea cup)")
                    print("8:50 PM	Mixed Vegetable Salad (1 katori)")
                    print("9:00 PM	Green Gram Whole Dal Cooked (1 katori)Bhindi sabzi (1 katori) Roti (1 roti/chapati)")
                    print("\n\nsaturday\n")
                    print("\n\n6:30 AM	Cucumber Detox Water (1 glass)")
                    print("8:00 AM	Besan Chilla (2 cheela) Green Garlic Chutney (3 tablespoon)")
                    print("12:00 PM	Skimmed Milk Paneer (100 grams)")
                    print("2:00 PM	Mixed Vegetable Salad (1 katori)")
                    print("2:10 PM	Palak Chole (1 bowl) Steamed Rice (0.5 katori)")
                    print("4:00 PM	Apple(0.5 small (2-3/4″ dia)) Buttermilk (1 glass)")
                    print("5:30 PM	Tea with Less Sugar and Milk (1 teacup)")
                    print("8:50 PM	Mixed Vegetable Salad (1 katori)")
                    print("9:00 PM	Low Fat Paneer Curry (1 katori) Missi Roti (1 roti)")
                    break


            while y==2:
                m= str(input("\nPease Enter the day of the week whose Diet Regiment you want to see in small letters or if you want to see the Regiment of the whole week type 'full':-"))

                if (m == "sunday"):
                        print("\n\nBreakfast")
                        print("One grapefruit")
                        print("Two poached eggs (or fried in a non-stick pan)")
                        print("Two slices whole-grain toast with one pat of butter each")
                        print("One cup low-fat milk")
                        print("One cup of black coffee or herbal tea")
                        print("\nSnack")
                        print("One banana")
                        print("One cup plain yogurt with two tablespoons honey")
                        print("Glass of water")
                        print("\nLunch")
                        print("Chicken breast (6-ounce portion), baked or roasted (not breaded or fried)")
                        print("Large garden salad with tomato and onion with one cup croutons, topped with one tablespoon oil and vinegar (or salad dressing)")
                        print("Glass of water")
                        print("\nSnack")
                        print("One cup carrot slices")
                        print("Three tablespoons hummus")
                        print("One-half piece of pita bread")
                        print("Glass of water or herbal tea")
                        print("\nDinner")
                        print("One cup steamed broccoli")
                        print("One cup of brown rice")
                        print("Halibut (four-ounce portion)")
                        print("Small garden salad with one cup spinach leaves, tomato, and onion topped with two tablespoons oil and vinegar or salad dressing")
                        print("One glass white wine (regular or dealcoholized)")
                        print("Sparkling water with lemon or lime slice")
                        print("\nSnack")
                        print("One cup blueberries")
                        print("Two tablespoons whipped cream (the real stuff—whip your own or buy in a can)")
                        print("Glass of water")
                        break

                elif (m == "monday"):
                        print("\n\nBreakfast")
                        print("One whole-wheat English muffin with two tablespoons peanut butter")
                        print("One orange")
                        print("Large glass (12 ounces) non-fat milk")
                        print("One cup of black coffee or herbal tea")
                        print("\nSnack")
                        print("Two oatmeal cookies with raisins")
                        print("Glass of water, hot tea, or black coffee")
                        print("\nLunch")
                        print("A turkey sandwich (six ounces of turkey breast meat, large tomato slice, green lettuce and mustard on two slices of whole wheat bread")
                        print("One cup low-sodium vegetable soup")
                        print("Glass of water")
                        print("\nSnack")
                        print("One cup (about 30) grapes")
                        print("Glass of water or herbal tea")
                        print("\nDinner")
                        print("Five-ounce sirloin steak")
                        print("One cup mashed potatoes")
                        print("One cup cooked spinach")
                        print("One cup green beans")
                        print("One glass beer (regular, lite or non-alcohol)")
                        print("Sparkling water with lemon or lime slice")
                        print("\nSnack")
                        print("Two slices whole wheat bread with two tablespoons jam (any variety of fruit)")
                        print("One cup non-fat milk")
                        print("Glass of water")
                        break

                elif (m == "tuesday"):
                        print("\n\nBreakfast")
                        print("One medium bran muffin")
                        print("One serving turkey breakfast sausage")
                        print("One orange")
                        print("One cup non-fat milk")
                        print("One cup black coffee or herbal tea")
                        print("\nSnack")
                        print("One fresh pear")
                        print("One cup of flavored soy milk")
                        print("Glass of water, hot tea, or black coffee")
                        print("\nLunch")
                        print("Low sodium chicken noodle soup with six saltine crackers")
                        print("One medium apple")
                        print("Water")
                        print("\nSnack")
                        print("One apple")
                        print("One slice Swiss cheese")
                        print("Sparkling water with lemon or lime slice")
                        print("\nDinner")
                        print("8-ounce serving of turkey breast meat")
                        print("One cup baked beans")
                        print("One cup cooked carrots")
                        print("One cup cooked kale")
                        print("One glass of wine")
                        print("\nSnack")
                        print("One cup of frozen yogurt")
                        print("One cup fresh raspberries")
                        break

                elif (m == "wednesday"):
                        print("\n\nBreakfast")
                        print("One cup whole wheat flakes with one cup non-fat milk and one teaspoon sugar")
                        print("One banana")
                        print("One slice whole-grain toast with one tablespoon peanut butter")
                        print("One cup of black coffee or herbal tea")
                        print("\nSnack")
                        print("One cup grapes and one tangerine")
                        print("Glass of water, hot tea, or black coffee")
                        print("\nLunch")
                        print("Tuna wrap with one wheat flour tortilla, one-half can water-packed tuna (drained), one tablespoon mayonnaise, lettuce, and sliced tomato")
                        print("One sliced avocado")
                        print("One cup non-fat milk")
                        print("\nSnack")
                        print("One cup cottage cheese (1-percent fat)")
                        print("One fresh pineapple slice")
                        print("Four graham crackers")
                        print("Sparkling water with lemon or lime slice")
                        print("\nDinner")
                        print("One serving lasagna")
                        print("Small garden salad with tomatoes and onions topped with one tablespoon salad dressing")
                        print("One cup non-fat milk")
                        print("\nSnack")
                        print("One apple")
                        print("One cup non-fat milk")
                        break

                elif (m == "thursday"):
                        print("\n\nBreakfast")
                        print("One piece of French toast with one tablespoon maple syrup")
                        print("One scrambled or poached egg")
                        print("One serving turkey bacon")
                        print("One cup orange juice")
                        print("One cup black coffee or herbal tea")
                        print("/nSnack")
                        print("One cup sliced carrots")
                        print("One cup cauliflower pieces")
                        print("Two tablespoons ranch dressing")
                        print("Glass of water, hot tea, or black coffee")
                        print("/nLunch")
                        print("Veggie burger on a whole grain bun")
                        print("One cup northern (or other dry) beans")
                        print("One cup non-fat milk")
                        print("/nSnack")
                        print("One apple")
                        print("One pita with two tablespoons hummus")
                        print("Sparkling water with lemon or lime slice")
                        print("/nDinner")
                        print("One trout filet")
                        print("One cup green beans")
                        print("One cup brown rice")
                        print("One small garden salad with two tablespoons salad dressing")
                        print("One glass of beer")
                        print("Sparkling water with lemon or lime slice")
                        print("/nSnack")
                        print("One cup cottage cheese")
                        print("One fresh peach")
                        break

                elif (m == "friday"):
                        print("\n\nBreakfast")
                        print("One cup corn flakes with two teaspoons sugar and one cup non-fat milk")
                        print("One banana")
                        print("One hard-boiled egg")
                        print("One cup black coffee or herbal tea")
                        print("\nSnack")
                        print("One cup plain yogurt with one tablespoon honey, one-half cup blueberries, and one tablespoon almonds")
                        print("Glass of water, hot tea, or black coffee")
                        print("\nLunch")
                        print("One cup whole wheat pasta with one-half cup red pasta sauce")
                        print("Medium garden salad with tomatoes and onions and two tablespoons salad dressing")
                        print("Glass of water")
                        print("\nSnack")
                        print("One and one-half cup cottage cheese")
                        print("One fresh peach")
                        print("Glass of water")
                        print("\nDinner")
                        print("Four and one-half ounce serving of pork loin")
                        print("Small garden salad with tomatoes and onions topped with two tablespoons oil and vinegar (or salad dressing)")
                        print("One small baked sweet potato")
                        print("One cup asparagus")
                        print("One glass wine (regular or dealcoholized)")
                        print("Sparkling water with lemon or lime slice")
                        print("\nSnack")
                        print("Five graham crackers")
                        print("One cup non-fat milk")
                        print("One cup strawberries")
                        break

                elif (m == "saturday"):
                        print("\n\nBreakfast")
                        print("One cup cooked oatmeal with one-half cup blueberries, one-half cup non-fat milk, and one tablespoon almond slivers")
                        print("Two slices turkey bacon")
                        print("One cup non-fat milk to drink")
                        print("One cup black coffee or herbal tea")
                        print("\nSnack")
                        print("One cup plain yogurt with one tablespoon honey, one-half cup strawberries, and two tablespoons almond slivers")
                        print("Glass of water, hot tea, or black coffee")
                        print("\nLunch")
                        print("Six-ounce baked chicken breast")
                        print("Large garden salad with tomatoes and onions and two tablespoons salad dressing")
                        print("One baked sweet potato")
                        print("One whole-wheat dinner roll.")
                        print("Glass of water")
                        print("\nSnack")
                        print("One cup raw broccoli florets")
                        print("One cup raw sliced carrot")
                        print("Two tablespoons veggie dip or salad dressing")
                        print("One fresh peach")
                        print("Glass of water")
                        print("\nDinner")
                        print("3-ounce serving of baked or grilled salmon")
                        print("One-half cup black beans")
                        print("One cup Swiss chard")
                        print("One cup brown rice")
                        print("One whole wheat dinner roll with a pat of butter")
                        print("Sparkling water with lemon or lime slice")
                        print("\nSnack")
                        print("One Orange")
                        break

                elif (m == "full"):
                        print("\n\n\nSunday")
                        print("\n\nBreakfast")
                        print("One grapefruit")
                        print("Two poached eggs (or fried in a non-stick pan)")
                        print("Two slices whole-grain toast with one pat of butter each")
                        print("One cup low-fat milk")
                        print("One cup of black coffee or herbal tea")
                        print("\nSnack")
                        print("One banana")
                        print("One cup plain yogurt with two tablespoons honey")
                        print("Glass of water")
                        print("\nLunch")
                        print("Chicken breast (6-ounce portion), baked or roasted (not breaded or fried)")
                        print("Large garden salad with tomato and onion with one cup croutons, topped with one tablespoon oil and vinegar (or salad dressing)")
                        print("Glass of water")
                        print("\nSnack")
                        print("One cup carrot slices")
                        print("Three tablespoons hummus")
                        print("One-half piece of pita bread")
                        print("Glass of water or herbal tea")
                        print("\nDinner")
                        print("One cup steamed broccoli")
                        print("One cup of brown rice")
                        print("Halibut (four-ounce portion)")
                        print("Small garden salad with one cup spinach leaves, tomato, and onion topped with two tablespoons oil and vinegar or salad dressing")
                        print("One glass white wine (regular or dealcoholized)")
                        print("Sparkling water with lemon or lime slice")
                        print("\nSnack")
                        print("One cup blueberries")
                        print("Two tablespoons whipped cream (the real stuff—whip your own or buy in a can)")
                        print("Glass of water")

                        print("\n\n\nmonday")
                        print("\n\nBreakfast")
                        print("One whole-wheat English muffin with two tablespoons peanut butter")
                        print("One orange")
                        print("Large glass (12 ounces) non-fat milk")
                        print("One cup of black coffee or herbal tea")
                        print("\nSnack")
                        print("Two oatmeal cookies with raisins")
                        print("Glass of water, hot tea, or black coffee")
                        print("\nLunch")
                        print("A turkey sandwich (six ounces of turkey breast meat, large tomato slice, green lettuce and mustard on two slices of whole wheat bread")
                        print("One cup low-sodium vegetable soup")
                        print("Glass of water")
                        print("\nSnack")
                        print("One cup (about 30) grapes")
                        print("Glass of water or herbal tea")
                        print("\nDinner")
                        print("Five-ounce sirloin steak")
                        print("One cup mashed potatoes")
                        print("One cup cooked spinach")
                        print("One cup green beans")
                        print("One glass beer (regular, lite or non-alcohol)")
                        print("Sparkling water with lemon or lime slice")
                        print("\nSnack")
                        print("Two slices whole wheat bread with two tablespoons jam (any variety of fruit)")
                        print("One cup non-fat milk")
                        print("Glass of water")

                        print("\n\n\ntuesday")
                        print("\n\nBreakfast")
                        print("One medium bran muffin")
                        print("One serving turkey breakfast sausage")
                        print("One orange")
                        print("One cup non-fat milk")
                        print("One cup black coffee or herbal tea")
                        print("\nSnack")
                        print("One fresh pear")
                        print("One cup of flavored soy milk")
                        print("Glass of water, hot tea, or black coffee")
                        print("\nLunch")
                        print("Low sodium chicken noodle soup with six saltine crackers")
                        print("One medium apple")
                        print("Water")
                        print("\nSnack")
                        print("One apple")
                        print("One slice Swiss cheese")
                        print("Sparkling water with lemon or lime slice")
                        print("\nDinner")
                        print("8-ounce serving of turkey breast meat")
                        print("One cup baked beans")
                        print("One cup cooked carrots")
                        print("One cup cooked kale")
                        print("One glass of wine")
                        print("\nSnack")
                        print("One cup of frozen yogurt")
                        print("One cup fresh raspberries")

                        print("\n\n\nwednesday")
                        print("\n\nBreakfast")
                        print("One cup whole wheat flakes with one cup non-fat milk and one teaspoon sugar")
                        print("One banana")
                        print("One slice whole-grain toast with one tablespoon peanut butter")
                        print("One cup of black coffee or herbal tea")
                        print("\nSnack")
                        print("One cup grapes and one tangerine")
                        print("Glass of water, hot tea, or black coffee")
                        print("\nLunch")
                        print("Tuna wrap with one wheat flour tortilla, one-half can water-packed tuna (drained), one tablespoon mayonnaise, lettuce, and sliced tomato")
                        print("One sliced avocado")
                        print("One cup non-fat milk")
                        print("\nSnack")
                        print("One cup cottage cheese (1-percent fat)")
                        print("One fresh pineapple slice")
                        print("Four graham crackers")
                        print("Sparkling water with lemon or lime slice")
                        print("\nDinner")
                        print("One serving lasagna")
                        print("Small garden salad with tomatoes and onions topped with one tablespoon salad dressing")
                        print("One cup non-fat milk")
                        print("\nSnack")
                        print("One apple")
                        print("One cup non-fat milk")

                        print("\n\n\nthursday")
                        print("/n/nBreakfast")
                        print("One piece of French toast with one tablespoon maple syrup")
                        print("One scrambled or poached egg")
                        print("One serving turkey bacon")
                        print("One cup orange juice")
                        print("One cup black coffee or herbal tea")
                        print("/nSnack")
                        print("One cup sliced carrots")
                        print("One cup cauliflower pieces")
                        print("Two tablespoons ranch dressing")
                        print("Glass of water, hot tea, or black coffee")
                        print("/nLunch")
                        print("Veggie burger on a whole grain bun")
                        print("One cup northern (or other dry) beans")
                        print("One cup non-fat milk")
                        print("/nSnack")
                        print("One apple")
                        print("One pita with two tablespoons hummus")
                        print("Sparkling water with lemon or lime slice")
                        print("/nDinner")
                        print("One trout filet")
                        print("One cup green beans")
                        print("One cup brown rice")
                        print("One small garden salad with two tablespoons salad dressing")
                        print("One glass of beer")
                        print("Sparkling water with lemon or lime slice")
                        print("/nSnack")
                        print("One cup cottage cheese")
                        print("One fresh peach")

                        print("\n\n\nfriday")
                        print("\n\nBreakfast")
                        print("One cup corn flakes with two teaspoons sugar and one cup non-fat milk")
                        print("One banana")
                        print("One hard-boiled egg")
                        print("One cup black coffee or herbal tea")
                        print("\nSnack")
                        print("One cup plain yogurt with one tablespoon honey, one-half cup blueberries, and one tablespoon almonds")
                        print("Glass of water, hot tea, or black coffee")
                        print("\nLunch")
                        print("One cup whole wheat pasta with one-half cup red pasta sauce")
                        print("Medium garden salad with tomatoes and onions and two tablespoons salad dressing")
                        print("Glass of water")
                        print("\nSnack")
                        print("One and one-half cup cottage cheese")
                        print("One fresh peach")
                        print("Glass of water")
                        print("\nDinner")
                        print("Four and one-half ounce serving of pork loin")
                        print("Small garden salad with tomatoes and onions topped with two tablespoons oil and vinegar (or salad dressing)")
                        print("One small baked sweet potato")
                        print("One cup asparagus")
                        print("One glass wine (regular or dealcoholized)")
                        print("Sparkling water with lemon or lime slice")
                        print("\nSnack")
                        print("Five graham crackers")
                        print("One cup non-fat milk")
                        print("One cup strawberries")

                        print("\n\n\nsaturday")
                        print("\n\nBreakfast")
                        print("One cup cooked oatmeal with one-half cup blueberries, one-half cup non-fat milk, and one tablespoon almond slivers")
                        print("Two slices turkey bacon")
                        print("One cup non-fat milk to drink")
                        print("One cup black coffee or herbal tea")
                        print("\nSnack")
                        print("One cup plain yogurt with one tablespoon honey, one-half cup strawberries, and two tablespoons almond slivers")
                        print("Glass of water, hot tea, or black coffee")
                        print("\nLunch")
                        print("Six-ounce baked chicken breast")
                        print("Large garden salad with tomatoes and onions and two tablespoons salad dressing")
                        print("One baked sweet potato")
                        print("One whole-wheat dinner roll.")
                        print("Glass of water")
                        print("\nSnack")
                        print("One cup raw broccoli florets")
                        print("One cup raw sliced carrot")
                        print("Two tablespoons veggie dip or salad dressing")
                        print("One fresh peach")
                        print("Glass of water")
                        print("\nDinner")
                        print("3-ounce serving of baked or grilled salmon")
                        print("One-half cup black beans")
                        print("One cup Swiss chard")
                        print("One cup brown rice")
                        print("One whole wheat dinner roll with a pat of butter")
                        print("Sparkling water with lemon or lime slice")
                        print("\nSnack")
                        print("One Orange")
                        break


            while y==3:
                g= str(input("\nPease Enter the day of the week whose Diet Regiment you want to see in small letters or if you want to see the Regiment of the whole week type 'full':-"))


                if (g == "sunday"):
                        print("\nBreakfast: scrambled eggs, stir-fried veggies, and oatmeal")
                        print("Snack: whey protein shake")
                        print("Lunch: grilled chicken breast, mixed greens, and baked sweet potato")
                        print("Snack: hard-boiled egg(s) and carrot sticks")
                        print("Dinner: broiled fish, green beans with brown rice\n")
                        break

                elif (g == "monday"):
                        print("\nBreakfast: protein pancakes with fresh berries")
                        print("Snack: apple slices and almonds")
                        print("Lunch: lean ground beef burger on lettuce with tomato, onion, and green beans")
                        print("Snack: protein shake")
                        print("Dinner: shrimp stir-fried with bell pepper and brown rice over spinach\n")
                        break

                elif (g == "tuesday"):
                        print("\nBreakfast: Greek yogurt, almonds or walnuts, whole grain granola, and fresh berries")
                        print("Snack: protein shake")
                        print("Lunch: grilled fish with a spinach salad and broccoli")
                        print("Snack: egg white omelet with bell peppers and mushrooms")
                        print("Dinner: chicken breast topped with fresh salsa with a sweet potato and a side salad\n")
                        break

                elif (g == "wednesday"):
                        print("\nBreakfast: oatmeal with berries and scrambled egg whites")
                        print("Snack: turkey breast with carrots and celery")
                        print("Lunch: sirloin steak with broccoli and mushrooms")
                        print("Snack: apples with natural nut butter")
                        print("Dinner: broiled fish, brown rice, and a mixed green salad\n")
                        break

                elif (g == "thursday"):
                        print("\nBreakfast: protein shake with oatmeal")
                        print("Snack: hard-boiled egg whites with sliced peppers and cucumbers")
                        print("Lunch: grilled chicken with white bean and tomato salad")
                        print("Snack: greek yogurt with berries and nuts")
                        print("Dinner: grilled fish with quinoa and green beans\n")
                        break


                elif (g == "friday"):
                        print("\nBreakfast: scrambled egg whites with cheese, peppers, herbs, and Ezekiel bread")
                        print("Snack: protein shake")
                        print("Lunch: grilled chicken breast with bell peppers, black beans, and onions over romaine lettuce")
                        print("Snack: apple and almonds")
                        print("Dinner: sirloin steak with sweet potato and asparagus\n")
                        break

                elif (g == "saturday"):
                        print("\nBreakfast: Greek yogurt with whole grain granola and berries")
                        print("Snack: turkey breast with carrots and celery sticks")
                        print("Lunch: grilled chicken breast over spinach with sliced strawberries and almonds")
                        print("Snack: protein shake")
                        print("Dinner: shrimp stir-fried with peppers, onions, and broccoli over brown rice\n")
                        break

                elif (g == "full"):

                        print("\n\n\nSunday")
                        print("\nBreakfast: scrambled eggs, stir-fried veggies, and oatmeal")
                        print("Snack: whey protein shake")
                        print("Lunch: grilled chicken breast, mixed greens, and baked sweet potato")
                        print("Snack: hard-boiled egg(s) and carrot sticks")
                        print("Dinner: broiled fish, green beans with brown rice\n")

                        print("\n\nMonday")
                        print("\nBreakfast: protein pancakes with fresh berries")
                        print("Snack: apple slices and almonds")
                        print("Lunch: lean ground beef burger on lettuce with tomato, onion, and green beans")
                        print("Snack: protein shake")
                        print("Dinner: shrimp stir-fried with bell pepper and brown rice over spinach\n")

                        print("\n\nTuesday")
                        print("\nBreakfast: Greek yogurt, almonds or walnuts, whole grain granola, and fresh berries")
                        print("Snack: protein shake")
                        print("Lunch: grilled fish with a spinach salad and broccoli")
                        print("Snack: egg white omelet with bell peppers and mushrooms")
                        print("Dinner: chicken breast topped with fresh salsa with a sweet potato and a side salad\n")

                        print("\n\nWednesday")
                        print("\nBreakfast: oatmeal with berries and scrambled egg whites")
                        print("Snack: turkey breast with carrots and celery")
                        print("Lunch: sirloin steak with broccoli and mushrooms")
                        print("Snack: apples with natural nut butter")
                        print("Dinner: broiled fish, brown rice, and a mixed green salad\n")

                        print("\n\nThursday")
                        print("\nBreakfast: protein shake with oatmeal")
                        print("Snack: hard-boiled egg whites with sliced peppers and cucumbers")
                        print("Lunch: grilled chicken with white bean and tomato salad")
                        print("Snack: Greek yogurt with berries and nuts")
                        print("Dinner: grilled fish with quinoa and green beans\n")

                        print("\n\nFriday")
                        print("\nBreakfast: scrambled egg whites with cheese, peppers, herbs, and Ezekiel bread")
                        print("Snack: protein shake")
                        print("Lunch: grilled chicken breast with bell peppers, black beans, and onions over romaine lettuce")
                        print("Snack: apple and almonds")
                        print("Dinner: sirloin steak with sweet potato and asparagus\n")

                        print("\n\nSaturday")
                        print("\nBreakfast: Greek yogurt with whole grain granola and berries")
                        print("Snack: turkey breast with carrots and celery sticks")
                        print("Lunch: grilled chicken breast over spinach with sliced strawberries and almonds")
                        print("Snack: protein shake")
                        print("Dinner: shrimp stir-fried with peppers, onions, and broccoli over brown rice\n")
                        break

            while y==4:
                l= str(input("\nPease Enter the day of the week whose Diet Regiment you want to see in small letters or if you want to see the Regiment of the whole week type 'full':-"))


                if (l == "sunday"):
                        print("\nBreakfast: 1 cup of oats with 1 cup of dairy or plant-based milk, 1 sliced banana, and 2 tablespoons of peanut butter")
                        print("Snack: trail mix made with 1 cup of dry cereal, 1/4 cup of granola, 1/4 cup of dried fruit, and 20 nuts")
                        print("Lunch: 1 cup of spaghetti with 3/4 cups of tomato sauce and 4 ounces of cooked ground beef, as well as 1 medium breadstick with 1 tablespoon of butter")
                        print("Snack: 1 cup of cottage cheese and 1/2 cup of blueberries")
                        print("Dinner: 4 ounces of salmon, 1 cup of brown rice, and 5 asparagus spears\n")
                        break
                elif (l == "monday"):
                        print("\nBreakfast: smoothie made with 2 cups of dairy or plant-based milk, 1 cup of yogurt, 1 cup of blueberries, and 2 tablespoons of almond butter")
                        print("Snack: 1 granola bar, 1 piece of fruit, and 2 pieces of string cheese")
                        print("Lunch: 12-inch sub sandwich with meat, cheese, and veggies with 3 ounces of baby carrots, 2 tablespoons of hummus, and apple slices on the side")
                        print("Snack: 1 scoop of whey protein powder mixed in 1 cup of dairy or plant-based milk")
                        print("Dinner: 4-ounce sirloin steak, 1 medium-sized baked potato with 1 tablespoon of butter, and 1 cup of broccoli\n")
                        break

                elif (l == "tuesday"):
                        print("\nBreakfast: 3 whole eggs, 1 apple, and 1 cup of oatmeal made with 1 cup of dairy or plant-based milk")
                        print("Snack: 1 cup of plain yogurt with 1/4 cup of granola and 1/2 cup of raspberries")
                        print("Lunch: 6-ounce chicken breast, 1 medium-sized sweet potato, 3/4 cup of green beans, and 1 ounce of nuts")
                        print("Snack: 1/2 cup of chickpeas atop greens")
                        print("Dinner: burrito bowl with 6 ounces of chopped sirloin steak, 1/2 cup of black beans, 1/2 cup of brown rice, \n1 cup of shredded lettuce and spinach, and 2 tablespoons of salsa\n")
                        break
                elif (l == "wednesday"):
                        print("\nBreakfast: 3 whole-wheat waffles with 2 tablespoons of peanut butter, 1 orange, and 2 cups of dairy or plant-based milk")
                        print("Snack: 1 nut-based granola bar and 1 ounce of almonds")
                        print("Lunch: 6-ounce 90%-lean burger on a whole-wheat bun with 1 tomato slice and lettuce leaf, \nas well as 1 1/2 cup (86 grams) of homemade sweet potato fries cooked in olive oil")
                        print("Snack: 1 cup of Greek yogurt and 1 cup (140 grams) of strawberries")
                        print("Dinner: 4-ounce chicken breast, 1/2 cup of quinoa, and 1 1/3 cups of sugar snap peas\n")
                        break
                elif (l == "thursday"):
                        print("\nBreakfast: 3-egg omelet with sliced onions, red and green bell peppers, and 1/4 cup of shredded cheese with 2 cups of dairy or plant-based milk to drink")
                        print("Snack: 2 tablespoons of peanut butter and 1 banana on 1 slice of whole-wheat bread")
                        print("Lunch: 8 ounces of tilapia fillets, 1/4 cup of lentils, and a salad topped with 1/4 cup of walnuts")
                        print("Snack: 2 sliced, hard-boiled eggs atop a mixed green salad")
                        print("Dinner: turkey chili made with a 4-ounce turkey breast, chopped onions, garlic, celery, and sweet peppers, 1/2 cup of canned,")
                        print("diced tomatoes, and 1/2 cup of cannellini beans, topped with 1/4 cup of shredded cheese. Add oregano, bay leaves, chili powder, and cumin as desired for taste.\n")
                        break
                elif (l == "friday"):
                        print("\nBreakfast: 3 whole eggs, 1 apple, and 1 cup of oatmeal made with 1 cup of dairy or plant-based milk")
                        print("Snack: 1 cup of plain yogurt with 1/4 cup of granola and 1/2 cup of raspberries")
                        print("Lunch: 6-ounce chicken breast, 1 medium-sized sweet potato, 3/4 cup of green beans, and 1 ounce of nuts")
                        print("Snack: 1/2 cup of chickpeas atop greens")
                        print("Dinner: burrito bowl with 6 ounces of chopped sirloin steak, 1/2 cup of black beans, 1/2 cup of brown rice, 1 cup of shredded lettuce and spinach, and 2 tablespoons of salsa\n")
                        break
                elif (l == "saturday"):
                        print("\nBreakfast: 3 whole-wheat waffles with 2 tablespoons of peanut butter, 1 orange, and 2 cups of dairy or plant-based milk")
                        print("Snack: 1 nut-based granola bar and 1 ounce of almonds")
                        print("Lunch: 6-ounce 90%-lean burger on a whole-wheat bun with 1 tomato slice and lettuce leaf, \nas well as 1 1/2 cup (86 grams) of homemade sweet potato fries cooked in olive oil")
                        print("Snack: 1 cup of Greek yogurt and 1 cup (140 grams) of strawberries")
                        print("Dinner: 4-ounce chicken breast, 1/2 cup of quinoa, and 1 1/3 cups of sugar snap peas\n")
                        break

                elif (l == "full"):
                        print("\n\n\nSunday")
                        print("\nBreakfast: 1 cup of oats with 1 cup of dairy or plant-based milk, 1 sliced banana, and 2 tablespoons of peanut butter")
                        print("Snack: trail mix made with 1 cup of dry cereal, 1/4 cup of granola, 1/4 cup of dried fruit, and 20 nuts")
                        print("Lunch: 1 cup of spaghetti with 3/4 cups of tomato sauce and 4 ounces of cooked ground beef, as well as 1 medium breadstick with 1 tablespoon of butter")
                        print("Snack: 1 cup of cottage cheese and 1/2 cup of blueberries")
                        print("Dinner: 4 ounces of salmon, 1 cup of brown rice, and 5 asparagus spears\n")

                        print("\n\nMonday")
                        print("\nBreakfast: smoothie made with 2 cups of dairy or plant-based milk, 1 cup of yogurt, 1 cup of blueberries, and 2 tablespoons of almond butter")
                        print("Snack: 1 granola bar, 1 piece of fruit, and 2 pieces of string cheese")
                        print("Lunch: 12-inch sub sandwich with meat, cheese, and veggies with 3 ounces of baby carrots, 2 tablespoons of hummus, and apple slices on the side")
                        print("Snack: 1 scoop of whey protein powder mixed in 1 cup of dairy or plant-based milk")
                        print("Dinner: 4-ounce sirloin steak, 1 medium-sized baked potato with 1 tablespoon of butter, and 1 cup of broccoli\n")

                        print("\n\nTuesday")
                        print("\nBreakfast: 3 whole eggs, 1 apple, and 1 cup of oatmeal made with 1 cup of dairy or plant-based milk")
                        print("Snack: 1 cup of plain yogurt with 1/4 cup of granola and 1/2 cup of raspberries")
                        print("Lunch: 6-ounce chicken breast, 1 medium-sized sweet potato, 3/4 cup of green beans, and 1 ounce of nuts")
                        print("Snack: 1/2 cup of chickpeas atop greens")
                        print("Dinner: burrito bowl with 6 ounces of chopped sirloin steak, 1/2 cup of black beans, 1/2 cup of brown rice, \n1 cup of shredded lettuce and spinach, and 2 tablespoons of salsa\n")

                        print("\n\nWednesday")
                        print("\nBreakfast: 3 whole-wheat waffles with 2 tablespoons of peanut butter, 1 orange, and 2 cups of dairy or plant-based milk")
                        print("Snack: 1 nut-based granola bar and 1 ounce of almonds")
                        print("Lunch: 6-ounce 90%-lean burger on a whole-wheat bun with 1 tomato slice and lettuce leaf, \nas well as 1 1/2 cup (86 grams) of homemade sweet potato fries cooked in olive oil")
                        print("Snack: 1 cup of Greek yogurt and 1 cup (140 grams) of strawberries")
                        print("Dinner: 4-ounce chicken breast, 1/2 cup of quinoa, and 1 1/3 cups of sugar snap peas\n")

                        print("\n\nThursday")
                        print("\nBreakfast: 3-egg omelet with sliced onions, red and green bell peppers, and 1/4 cup of shredded cheese with 2 cups of dairy or plant-based milk to drink")
                        print("Snack: 2 tablespoons of peanut butter and 1 banana on 1 slice of whole-wheat bread")
                        print("Lunch: 8 ounces of tilapia fillets, 1/4 cup of lentils, and a salad topped with 1/4 cup of walnuts")
                        print("Snack: 2 sliced, hard-boiled eggs atop a mixed green salad")
                        print("Dinner: turkey chili made with a 4-ounce turkey breast, chopped onions, garlic, celery, and sweet peppers, 1/2 cup of canned,")
                        print("diced tomatoes, and 1/2 cup of cannellini beans, topped with 1/4 cup of shredded cheese. Add oregano, bay leaves, chili powder, and cumin as desired for taste.\n")

                        print("\n\nFriday")
                        print("\nBreakfast: 3 whole eggs, 1 apple, and 1 cup of oatmeal made with 1 cup of dairy or plant-based milk")
                        print("Snack: 1 cup of plain yogurt with 1/4 cup of granola and 1/2 cup of raspberries")
                        print("Lunch: 6-ounce chicken breast, 1 medium-sized sweet potato, 3/4 cup of green beans, and 1 ounce of nuts")
                        print("Snack: 1/2 cup of chickpeas atop greens")
                        print("Dinner: burrito bowl with 6 ounces of chopped sirloin steak, 1/2 cup of black beans, 1/2 cup of brown rice, 1 cup of shredded lettuce and spinach, and 2 tablespoons of salsa\n")

                        print("\n\nSaturday")
                        print("\nBreakfast: 3 whole-wheat waffles with 2 tablespoons of peanut butter, 1 orange, and 2 cups of dairy or plant-based milk")
                        print("Snack: 1 nut-based granola bar and 1 ounce of almonds")
                        print("Lunch: 6-ounce 90%-lean burger on a whole-wheat bun with 1 tomato slice and lettuce leaf, \nas well as 1 1/2 cup (86 grams) of homemade sweet potato fries cooked in olive oil")
                        print("Snack: 1 cup of Greek yogurt and 1 cup (140 grams) of strawberries")
                        print("Dinner: 4-ounce chicken breast, 1/2 cup of quinoa, and 1 1/3 cups of sugar snap peas\n")
                        break

            if y==5:
                break

    #   https://www.verywellfit.com
    #   https://www.healthline.com
    #   https://www.medicalnewstoday.com

    elif a==4:
        print("--------------------")
        print("|                  |")
        print("|  WORKOUT PLANS   |")
        print("|                  |")
        print("--------------------")
        while 1==1:
            print("PLease tell us what you need to do:-")
            print("\n1. Loose Weight")
            print("2. Build Muscle")
            print("3. Stay fit")
            print("4. Exit")

            k = int(input("\nEnter your choice here:-"))

            while k == 1:
                h = str(input("\nPease Enter the day of the week whose Exercise Regiment you want to see in small letters or if you want to see the Regiment of the whole week type 'full':-"))

                if (h == "sunday"):
                    print("\n\nsunday")
                    print("1. Russian/Mason Twist")
                    print("2. Knee Push-Ups")
                    print("3. Alternating Reverse Lunge")
                    print("4. Reverse Crunch")
                    print("5. Knee Touches in Place")
                    break

                elif (h == "monday"):
                    print("\n\nMonday :\n\n")
                    print("1. Leg Raise")
                    print("2. Plank")
                    print("3. Hip Extensions left side")
                    print("4. Hip Extensions right side")
                    print("5. March in Place\n")
                    break

                elif (h == "tuesday"):
                    print("Tuesday :\n")
                    print("1. Military Press")
                    print("2. Plié/Sumo Squat")
                    print("3. Stiff Legged Deadlift with Dumbbells")
                    print("4. Heel Touches")
                    print("5. High Knees in Place\n")
                    break

                elif (h == "wednesday"):
                    print("Wednesday :\n")
                    print("1. Goblet Squat")
                    print("2. Knee Touches in Place")
                    print("3. Tricep Kickbacks")
                    print("4. Rear Leg Extension left leg")
                    print("5. Rear Leg Extension right leg\n")
                    break

                elif (h == "thursday"):
                    print("Thursday :\n")
                    print("Rest Day – Take a brisk 30 minute walk\n")
                    break

                elif (h == "friday"):
                    print("Friday :\n")
                    print("1. March in Place")
                    print("2. Traditional Crunch")
                    print("3. Chair Squat")
                    print("4. Wall Push-Up")
                    print("5. Bodyweight Glute Bridge\n")
                    break

                elif (h == "saturday"):
                    print("Saturday :\n")
                    print("1. Toe Reach")
                    print("2. Alternating Lunges")
                    print("3. Lying Oblique Twist")
                    print("4. Body Weight Squat")
                    print("5. High Knees in Place\n")
                    break

                elif (h == "full"):
                    print("\n\nsunday")
                    print("1. Russian/Mason Twist")
                    print("2. Knee Push-Ups")
                    print("3. Alternating Reverse Lunge")
                    print("4. Reverse Crunch")
                    print("5. Knee Touches in Place")

                    print("\n\nMonday :\n\n")
                    print("1. Leg Raise")
                    print("2. Plank")
                    print("3. Hip Extensions left side")
                    print("4. Hip Extensions right side")
                    print("5. March in Place\n")

                    print("Tuesday :\n")
                    print("1. Military Press")
                    print("2. Plié/Sumo Squat")
                    print("3. Stiff Legged Deadlift with Dumbbells")
                    print("4. Heel Touches")
                    print("5. High Knees in Place\n")

                    print("Wednesday :\n")
                    print("1. Goblet Squat")
                    print("2. Knee Touches in Place")
                    print("3. Tricep Kickbacks")
                    print("4. Rear Leg Extension left leg")
                    print("5. Rear Leg Extension right leg\n")

                    print("Thursday :\n")
                    print("Rest Day – Take a brisk 30 minute walk\n")

                    print("Friday :\n")
                    print("1. March in Place")
                    print("2. Traditional Crunch")
                    print("3. Chair Squat")
                    print("4. Wall Push-Up")
                    print("5. Bodyweight Glute Bridge\n")

                    print("Saturday :\n")
                    print("1. Toe Reach")
                    print("2. Alternating Lunges")
                    print("3. Lying Oblique Twist")
                    print("4. Body Weight Squat")
                    print("5. High Knees in Place\n")
                    break

            # https://skinnyms.com/7-day-weight-loss-workout-challenge-for-beginners/

            while k == 2:
                o = str(input(
                    "\nPease Enter the day of the week whose Exercise Regiment you want to see in small letters or if you want to see the Regiment of the whole week type 'full':-"))

                if (o == "sunday"):
                    print("\n\nSunday Workout: Chest And Back\n")
                    print("1 Bench press:-              5 Sets	       8  Reps	    2010 Tempo	     60sec Rest")
                    print("2 Lat pull-down:-	        5 Sets	       8  Reps	    2011 Tempo	     60sec Rest")
                    print("3 Cable cross-over:-	        5 Sets	       12 Reps	    2010 Tempo	     60sec Rest")
                    print("4 Straight-arm pull-down:-	5 Sets	       12 Reps	    2011 Tempo	     60sec Rest")
                    print("5A Incline dumbbell press:-	5 Sets	       12 Reps	    2010 Tempo	     30sec Rest")
                    print("5B Prone dumbbell row:-	5 Sets	       12 Reps	    2011 Tempo	     60sec Rest")
                    break


                elif (o == "monday"):
                    print("\n\nMonday Workout: Rest Day\n")
                    print("This is a rest day, this help the ftique muscles to recover and build strong")
                    break


                elif (o == "tuesday"):
                    print("\n\nTuesday Workout: Legs And Shoulders\n")
                    print("1 Squat:-	                5 Sets	       8  Reps      2010 Tempo	      60sec Rest")
                    print("2 Overhead press:-	        5 Sets	       8  Reps	    2010 Tempo	      60sec Rest")
                    print("3 Leg extension	:-	5 Sets         12 Reps	    2011 Tempo	      60sec Rest")
                    print("4 Hamstring curl:-	        5 Sets	       12 Reps	    2011 Tempo	      60sec Rest")
                    print("5A Seated overhead press:-	5 Sets	       12 Reps	    2010 Tempo	      30sec Rest")
                    print("5B Seated lat raise:-	5 Sets	       12 Reps	    2011 Tempo	      60sec Rest")
                    break


                elif (o == "wednesday"):
                    print("\n\nwednesday Workout: Rest Day\n")
                    print("This is a rest day, this help the ftique muscles to recover and build strong")
                    break


                elif (o == "thursday"):
                    print("\n\nThursday Workout: Back And Arms\n")
                    print("1 Triceps dip:-	        5 Sets         8  Reps	    2010 Tempo	      60sec Rest")
                    print("2 Underhand lat pull-down:-	5 Sets	       8  Reps	    2011 Tempo	      60sec Rest")
                    print("3 Seated row:-               5 Sets	       12 Reps	    2011 Tempo	      60sec Rest")
                    print("4 Incline dumbbell curl:-	5 Sets	       12 Reps	    2011 Tempo	      60sec Rest")
                    print("5A Cable biceps curl:-       5 Sets	       12 Reps	    2011 Tempo	      30sec Rest")
                    print("5B Cable triceps press:-     5 Sets	       12 Reps	    2011 Tempo	      60sec Rest")
                    break

                elif (o == "friday"):
                    print("\n\nFRiday Workout: Rest Day\n")
                    print("This is a rest day, this help the ftique muscles to recover and build strong")
                    break

                elif (o == "saturday"):
                    print("\n\nFriday Workout: Chest And Shoulders\n")
                    print("1 Incline bench press:-      5 Sets         8  Reps	    2010 Tempo	      60sec Rest")
                    print("2 Dumbbell pull-over:-       5 Sets	       8  Reps	    2011 Tempo	      60sec Rest")
                    print("3 EZ-bar upright row:-	5 Sets 	       12 Reps	    2011 Tempo	      60sec Rest")
                    print("4 Dumbbell lateral raise:-	5 Sets	       12 Reps	    2011 Tempo	      60sec Rest")
                    print("5A Incline dumbbell flys:-	5 Sets	       12 Reps	    2010 Tempo	      30sec Rest")
                    print("5B Press-up:-	        5 Sets	       12 Reps	    2010 Tempo	      60sec Rest")
                    break


                elif (o == "full"):
                    print("\n\nSunday Workout: Chest And Back\n")
                    print(
                        "1 Bench press:-	        5 Sets	       8  Reps	    2010 Tempo	     60sec Rest")
                    print("2 Lat pull-down:-	        5 Sets	       8  Reps	    2011 Tempo	     60sec Rest")
                    print("3 Cable cross-over:-	        5 Sets	       12 Reps	    2010 Tempo	     60sec Rest")
                    print("4 Straight-arm pull-down:-	5 Sets	       12 Reps	    2011 Tempo	     60sec Rest")
                    print("5A Incline dumbbell press:-	5 Sets	       12 Reps	    2010 Tempo	     30sec Rest")
                    print("5B Prone dumbbell row:-	5 Sets	       12 Reps	    2011 Tempo	     60sec Rest")

                    print("\n\n\Monday Workout: Rest Day\n")
                    print("This is a rest day, this help the ftique muscles to recover and build strong")

                    print("\n\n\Tuesday Workout: Legs And Shoulders\n")
                    print("1 Squat:-	                5 Sets	       8  Reps      2010 Tempo	      60sec Rest")
                    print("2 Overhead press:-	        5 Sets	       8  Reps	    2010 Tempo	      60sec Rest")
                    print("3 Leg extension:-	        5 Sets         12 Reps	    2011 Tempo	      60sec Rest")
                    print("4 Hamstring curl:-	        5 Sets	       12 Reps	    2011 Tempo	      60sec Rest")
                    print("5A Seated overhead press:-	5 Sets	       12 Reps	    2010 Tempo	      30sec Rest")
                    print("5B Seated lat raise:-	5 Sets	       12 Reps	    2011 Tempo	      60sec Rest")

                    print("\n\n\wednesday Workout: Rest Day\n")
                    print("This is a rest day, this help the ftique muscles to recover and build strong")

                    print("\n\nThursday Workout: Back And Arms\n")
                    print("1 Triceps dip:-	        5 Sets         8  Reps	    2010 Tempo	      60sec Rest")
                    print("2 Underhand lat pull-down:-	5 Sets	       8  Reps	    2011 Tempo	      60sec Rest")
                    print("3 Seated row:-	        5 Sets	       12 Reps	    2011 Tempo	      60sec Rest")
                    print("4 Incline dumbbell curl:-	5 Sets	       12 Reps	    2011 Tempo	      60sec Rest")
                    print("5A Cable biceps curl:-       5 Sets	       12 Reps	    2011 Tempo	      30sec Rest")
                    print("5B Cable triceps press:-     5 Sets	       12 Reps	    2011 Tempo	      60sec Rest")

                    print("\n\nFRiday Workout: Rest Day\n")
                    print("This is a rest day, this help the ftique muscles to recover and build strong")

                    print("\n\nFriday Workout: Chest And Shoulders\n")
                    print("1 Incline bench press:-      5 Sets         8  Reps	    2010 Tempo	      60sec Rest")
                    print("2 Dumbbell pull-over:-	5 Sets	       8  Reps	    2011 Tempo	      60sec Rest")
                    print("3 EZ-bar upright row:-	5 Sets 	       12 Reps	    2011 Tempo	      60sec Rest")
                    print("4 Dumbbell lateral raise:-	5 Sets	       12 Reps	    2011 Tempo	      60sec Rest")
                    print("5A Incline dumbbell flye:-	5 Sets	       12 Reps	    2010 Tempo	      30sec Rest")
                    print("5B Press-up:-	        5 Sets	       12 Reps	    2010 Tempo	      60sec Rest")
                    break

            while k == 3:
                t = str(input("\nPease Enter the day of the week whose Exercise Regiment you want to see in small letters or if you want to see the Regiment of the whole week type 'full':-"))

                if (t == "sunday"):
                    print("\n\nSunday")
                    print("Cardio Steady pace:-")
                    print("Running at a steady pace for 30min without stopping")
                    break

                elif (t == "monday"):
                    print("\n\nMonday")
                    print("Strength Workout 1:-")
                    print("1. Dumbell Press Squat")
                    print("2. Ball Push-UP")
                    print("3. Bulgarian Split Squat")
                    print("4. Dumbell Clean and Press")
                    break

                elif (t == "tuesday"):
                    print("\n\nTuesday")
                    print("Cardio Intervals:-")
                    print("0:00-5:00: Walk at 3.5-3.8 mph (RPE 4)")
                    print("5:00-5:20: Sprint at 6.5-8.0 mph (RPE 9)")
                    print("5:20-6:50: Recover by walking at 3.0-3.5 mph (RPE 3)")
                    print("6:50-10:30: Repeat sprint series 2 more times, alternating 20-second sprints with 90 seconds of recovery.")
                    print("10:30-15:00: Walk at 3.5-3.8 mph (RPE 4)")
                    break

                elif (t == "wednesday"):
                    print("\n\nWednesday")
                    print("This is a rest day, this help the ftique muscles to recover and build strong")
                    break


                elif (t == "thursday"):
                    print("\n\nThursday")
                    print("Cardio Intervals")
                    print("0:00-5:00: Walk at 3.5-3.8 mph (RPE 4")
                    print("5:00-5:20: Sprint at 6.5-8.0 mph (RPE 9)")
                    print("5:20-6:50: Recover by walking at 3.0-3.5 mph (RPE 3)")
                    print("6:50-10:30: Repeat sprint series 2 more times, alternating 20-second sprints with 90 seconds of recovery.")
                    print("10:30-15:00: Walk at 3.5-3.8 mph (RPE 4)")
                    break

                elif (t == "friday"):
                    print("\n\nFriday")
                    print("Strength Workout 2:-")
                    print("1. Dynamic Lunge")
                    print("2. Opposite Arm/Left Lift")
                    print("3. Step-up")
                    print("4.Prone Jackknife")
                    break

                elif (t == "saturday"):
                    print("\n\nSaturday")
                    print("This is a rest day, this help the ftique muscles to recover and build strong")
                    break

                elif (t == "full"):
                    print("\n\nSunday")
                    print("Cardio Steady pace:-")
                    print("Running at a steady pace for 30min without stopping")

                    print("\n\nMonday")
                    print("Strength Workout 1:-")
                    print("1. Dumbell Press Squat")
                    print("2. Ball Push-UP")
                    print("3. Bulgarian Split Squat")
                    print("4. Dumbell Clean and Press")

                    print("\n\nTuesday")
                    print("Cardio Intervals:-")
                    print("0:00-5:00: Walk at 3.5-3.8 mph (RPE 4)")
                    print("5:00-5:20: Sprint at 6.5-8.0 mph (RPE 9)")
                    print("5:20-6:50: Recover by walking at 3.0-3.5 mph (RPE 3)")
                    print("6:50-10:30: Repeat sprint series 2 more times, alternating 20-second sprints with 90 seconds of recovery.")
                    print("10:30-15:00: Walk at 3.5-3.8 mph (RPE 4)")

                    print("\n\nWednesday")
                    print("This is a rest day, this help the ftique muscles to recover and build strong")

                    print("\n\nThursday")
                    print("Cardio Intervals")
                    print("0:00-5:00: Walk at 3.5-3.8 mph (RPE 4")
                    print("5:00-5:20: Sprint at 6.5-8.0 mph (RPE 9)")
                    print("5:20-6:50: Recover by walking at 3.0-3.5 mph (RPE 3)")
                    print("6:50-10:30: Repeat sprint series 2 more times, alternating 20-second sprints with 90 seconds of recovery.")
                    print("10:30-15:00: Walk at 3.5-3.8 mph (RPE 4)")

                    print("\n\nFriday")
                    print("Strength Workout 2:-")
                    print("1. Dynamic Lunge")
                    print("2. Opposite Arm/Left Lift")
                    print("3. Step-up")
                    print("4.Prone Jackknife")

                    print("\n\nSaturday")
                    print("Cardio Steady pace:-")
                    print("Running at a steady pace for 30min without stopping")
                    break

            if k == 4:
                break

            ##https://www.shape.com/fitness/workouts/4-week-workout-plan



    elif a==5:
        print("--------------")
        print("|            |")
        print("|  FEEDBACK  |")
        print("|            |")
        print("--------------\n")

        print("Chris Hemsworth: ")
        print("The most difficult part about diet is a plan, which is provided by Fitness 24 in a great manner.\n")

        print("Gary Vaynerchuk (GaryVee): ")
        print("In my fat to fit journey I have gone through many apps which gives you diet plans as well as workout plans but till now I have not seen a genuine app.\nBut as I came across this app named Fitness 24 I was extremely happy with the workout as well as diet plans, I followed them and have lost around 45kg in the last year.\n")

        print("Hritik Roshan: ")
        print("Its a great app for tracking meals and helps to maintain a diet in anyway possible.\n")

        feedback = input("Write your feedback: ")

        print("Your feedback:", feedback, "\n")


    elif a==6:
        print("---------------------------")
        print("|                         |")
        print("|   COVID-19 GUIDELINES   |")
        print("|                         |")
        print("---------------------------")

        c_guidelines = int(input("Enter 1 to continue:- "))
        while c_guidelines == 1:
            print("Enter 1 for - TEST")
            print("Enter 2 for - TRACK")
            print("Enter 3 for - TREAT")
            print("Enter 4 for - VACCINATION")
            print("Enter 5 to EXIT")
            guide = int(input("Choose: "))
            if (guide == 1):
                print("****************************************TEST***************************************")
                print("+---------------------------------------------------------------------------------+")
                print("| 1)Ensure tests being conducted are uniformly distributed across all districts,  |")
                print("| with adequate testing to be done reporting a higher number of cases.            |")
                print("| 2)The proportion of RC-PCR tests in the total mix to be scaled up, on a best    |")
                print("| effort basis, to 70% or more.                                                   |")
                print("| 3)States & UTs, where the proportion of RT-PCR tests is less, to reach the      |")
                print("| prescribed level.                                                               |")
                print("+---------------------------------------------------------------------------------+")
            elif (guide == 2):
                print("**************************************TRACK****************************************")
                print("+---------------------------------------------------------------------------------+")
                print("| 1)New positive cases to be isolated & their contacts to be traced at the        |")
                print("| earliest and to be isolated/ quarantined.                                       |")
                print("| -The prescribed containment measures to be implemented in containment zones.    |")
                print("| 2)Containment zones to be carefully demarcated by the district authorities, at  |")
                print("| the micro level, taking into consideration the guideline prescribed by misistry.|")
                print("| 3)List of containment zones to be noticed on the website by respective district |")
                print("| collectors & by states/UTs, to be shared with health ministry on regular basis. |")
                print("| Within the dearcated containment zones, ures, to be strictly followed under:-   |")
                print("| 1)Only essential activites to be allowed in containment zones                   |")
                print("| 2)No movement of people in or out of these zones, expect for medical            |")
                print("|  emergencies & for essential goods & servic                                     |")
                print("| 3)Intensive house-to-house surveillance by surveillance teams.                  |")
                print("| 4)Testing to be carried out as per prescribed protocol.                         |")
                print("| 5)Listing of contacts of persons found positive, along with their tracking,     |")
                print("| identification quarentine & follow up of contacts for 14 da                     |")
                print("| 6) 80% of contacts to be traced in 72 hours.                                    |")
                print("+---------------------------------------------------------------------------------+")
            elif (guide == 3):
                print("************************************TREAT*******************************************")
                print("+----------------------------------------------------------------------------------+")
                print("| 1)Quick isolation of COVID19 patients to be ensured in treatment facilities/home.|")
                print("| 2)Clinical interventions as prescribed to be administered.                       |")
                print("| 3)The concerned agencies to ensure adequate availability of COVID-19 dedicated   |")
                print("|  health & logistics based on their assessment of the case trajectory.            |")
                print("| 4)Effective infection,prevention & control practices to be followed in treatement|")
                print("|  facilities and by the healthcare workers & professionals.                       |")
                print("+----------------------------------------------------------------------------------+")
            elif (guide == 4):
                print("*******************************VACCINATION******************************************")
                print("+----------------------------------------------------------------------------------+")
                print("| 1)The national expert group on vaccine administration for COVID-19 (NEGVAC)      |")
                print("| provides guidance on prioritization of popular groups, procurement & inventory   |")
                print("| management, and vaccine selection, delivery and tracking.                        |")
                print("| 2)All state/UTs to rapidly step up the pace of vaccination,to cover all priority |")
                print("| groups, as recommended by NEGVAC & approved by the Central Govt, urgently and in |")
                print("| an expeditious manner.                                                           |")
                print("+----------------------------------------------------------------------------------+")
            elif guide == 5:
                break
            else:
                print("!!You entered a wrong input!!")


    elif a==7:
        print("-----------------------------")
        print("|                           |")
        print("|  COVID-19 RECOVERY TIPS   |")
        print("|                           |")
        print("-----------------------------")

        print("**Keep your hands clean and away from your face :-")
        print('1--Frequently wash your hands with soap and water for at least 20 seconds, especially after being in close contact or in the same room as the sick person.')
        print('2--If soap and water are not available, use a hand sanitizer that contains at least 60% alcohol.')
        print('3--Avoid touching your eyes, nose and mouth.\n\n')
        print('**Wear a face mask :-')
        print('1--If you need to be in the same room with the person who is ill and he or she is not able to wear a face mask, wear a face mask.')
        print('2--Stay atleast 6 feet away from the ill person.')
        print('3--Do not touch or handle your mask while you are using it. If your mask gets wet or dirty, replace it with a clean, dry mask.')
        print('4--Throw away the used mask and wash your hands.\n\n')
        print('**Clean your home frequently :- ')
        print('1--Every day, use household cleaning sprays or wipes to clean surfaces that are often touched, including counters, tabletops and doorknobs.')
        print('2--Avoid cleaning the sick person separate room and bathroom. Set aside bedding and utensils for the sick person only to use.\n\n')
        print('**Be careful with laundry :- ')
        print('1--Do not shake dirty laundry. Use regular detergent to wash the sick person laundry. Use the warmest setting you can.')
        print('2--Wash your hands after putting clothes in the dryer. Thoroughly dry clothes.')
        print('3--If you are handling clothing that has been soiled by the sick person, wear disposable gloves and keep the items away from your body.')
        print('4--Wash your hands after removing the gloves. Place dirty gloves and masks in a waste bin with a lid in the sick person room.')
        print('5--Clean and disinfect clothes hampers and wash your hands afterward.\n\n')
        print('**Be careful with dishes :- ')
        print('1--Wear gloves when handling dishes, cups or utensils used by the sick person. ')
        print('2--Wash the items with soap and hot water or in the dishwasher. ')
        print('3--Clean your hands after taking off the gloves or handling used items.\n\n')
        print('**Avoid direct contact with the sick person bodyily fluids :-')
        print('1--Wear disposable gloves and a face mask when providing oral and respiratory care and when handling stool, urine or other waste.')
        print('2--Wash your hands before and after removing your gloves and mask.')
        print('3--Donot reuse your mask or gloves.\n\n')
        print('**Avoid having unnecessary visitors in your home :-')
        print('1--Do not allow visitors until the sick person has completely recovered and has no signs or symptoms of COVID-19.\n\n')

    elif a==8:
        print("---------------------------")
        print("|                         |")
        print("|      OUR DEVELOPERS     |")
        print("|                         |")
        print("---------------------------")
        print("")
        ourDev = ["1. Diya "]
        for x in ourDev:
          print(x)
          print("")


    elif a==9:
        break

    else:
        print("Sorry! you entered a wrong input number.")

