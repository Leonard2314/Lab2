import statistics
def display_main_menu():
        print("Enter some numbers separated by commas (e.g. 5, 67,")
def get_user_input():
        print('Enter the numbers')
        x = input()
        print('Your numbers are ' + x)
        y = x.split(",")
        print(y)
        mylist=[]
        for x in y:
            mylist.append(float(x))
        return mylist

def calc_average(mylist):
        print("calc_average")
        average=sum(mylist)/len(mylist)
        print(average)
        return average 
def find_min_max(mylist):
        print("find_min_max")
        print("minimum is ",min(mylist))
        print("maximum is ",max(mylist))
        return min(mylist)+max(mylist)

def sort_temperature(mylist):
        print("sort_temperature")
        print(sorted(mylist))
def calc_median_temperature(mylist):
        print("calc_median_temperature")
        print(statistics.median(mylist))
        return statistics.median(mylist)

if __name__ == "__main__":
   display_main_menu()
   z = get_user_input()
   calc_average(z)
   sort_temperature(z)
   find_min_max(z)
   calc_median_temperature(z)

