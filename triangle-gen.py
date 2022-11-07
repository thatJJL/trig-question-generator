#triangle-gen4
#Clean up

#https://www.omnicalculator.com/math/trigonometry
#Trig from/using area - TODO 11:14am 7/11/2022 i1

#https://www.trigcalc.com/

import math

def solve_trig_triangle(is_LAA, lengths, angles):
    #isLAA - boolean.
    #True: treating triangle as length-angle-angle
    #False: treating triangle as length-length-angle

    #lengths, angles - seperate arrays
    '''
    Types of triangle questions
    Length, angle, angle
    Length, length, angle
    '''

    #variables for test validation
    do_tests = False
    final_length_a = None
    final_length_b = None
    final_length_c = None
    final_angle_A = None
    final_angle_B = None
    final_angle_C = None
    list_of_tests = [ #Could create list at beginning of doing tests and then check by using "in" keyword. Is None in list of tests. However, adding test variables in the same section as where they are declared is more intuative.
        final_length_a, #Unless python could instead have a list of pointers pointing towards the variables instead of storing the array as a new set of variables.
        final_length_b,
        final_length_c,
        final_angle_A,
        final_angle_B,
        final_angle_C,
        ]

    #Data validation
    if isinstance(lengths, int): #Repack integers into arrays
        lengths = [lengths]
    if isinstance(angles, int):
        angles = [angles]

    #sin A / a = sin B / b = sin C / c

    #Data assignment by configuration
    if is_LAA:
        given_length_a = lengths[0] #Known/Given values
        given_angle_A = angles[0]
        given_angle_B = angles[1]

        print(f"given_length_a: {given_length_a}")
        print(f"given_angle_A: {given_angle_A}")
        print(f"given_angle_B: {given_angle_B}")
        

        solved_angle_B = ( given_length_a  * math.sin(math.radians(given_angle_B)) ) / math.sin( math.radians(given_angle_A) )
        print(f"solved_angle_B: {solved_angle_B}")
        final_angle_B = solved_angle_B 

        

        
       


        
        
    else: #LLA
        given_length_a = lengths[0]
        given_length_b = lengths[1]
        given_angle_B = angles[1]



    #Tests
    for t in list_of_tests:
        #print( str( isinstance(t, None) ) )
        print(  (t == None) == False ) #WIP############################
    print("Tests complete - passed if all are true")


    


def main():
    print("main function")
    #generate_triangle(True, 10, [90, 60] )
    solve_trig_triangle(True, 10, [90, 60] )
    print(  "Correct answer: " + str( 5 * ( 3**(1/2) ) )  )
    #solve_trig_triangle(True, [10], [60, 90] )
    

if __name__ == "__main__":
    main()
