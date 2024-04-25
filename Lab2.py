
def calculate_bmi(height,weight):
        
        print("Height="+ str(height))
        print("Weight="+ str(weight))
        bmi= weight/(height*height)
        print("BMI IS="+str(bmi))
        if bmi<18.5:
                print("person is under weight")
        elif (bmi>=18.5 and bmi<=25):
                print("person if normal weight")
        elif(bmi>25.0):
                print("person is overweight")


calculate_bmi(weight = 57, height =1.73)

