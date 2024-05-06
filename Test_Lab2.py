import Lab2 as Lab2
def test_find_min_max():
    input_list=[20,10,30,50,80]
    test=90
    result=Lab2.find_min_max(input_list)
    assert(result==test)

def test_calc_average():
    input_list=[3,7,6,4]
    test=5
    result=Lab2.calc_average(input_list)
    assert(result==test)

def test_calc_median_temperature():
    input_list=[10,12,30,40,190]
    test=30
    result=Lab2.calc_median_temperature(input_list)
    assert(result==test)