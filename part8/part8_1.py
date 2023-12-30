"""Please write a function named smallest_average(person1: dict, person2: dict, person3: dict), which takes three dictionary objects as its arguments.

Each dictionary object contains values mapped to the following keys:

"name": The name of the contestant
"result1": the first result of the contestant (an integer between 1 and 10)
"result2": the second result of the contestant (as above)
"result3": the third result of the contestant (as above)
The function should calculate the average of the three results for each contestant, and then return the contestant whose average result was the smallest. The return value should be the entire dictionary object containing the contestant's information.

You may assume there will be no ties, i.e. a single contestant will have the smallest average result."""


def smallest_average(p1,p2,p3):
    p1_avg = (p1['result1']+p1['result2']+p1['result3'])/3
    p2_avg = (p2['result1']+p2['result2']+p2['result3'])/3
    p3_avg = (p3['result1']+p3['result2']+p3['result3'])/3
    min_avg = p1_avg
    min_p = p1
    if(p2_avg<min_avg):
        min_avg = p2_avg
        min_p = p2
    elif(p3_avg<min_avg):
        min_avg = p3_avg
        min_p = p3
    return min_p


p1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
p2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
p3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

print(smallest_average(p1,p2,p3))