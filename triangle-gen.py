#triangle-gen3

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
        
        #solved_angle_b = ( given_length_a  * math.sin(given_angle_B) ) / math.sin( given_angle_A )
        #print(f"solved_angle_b: {solved_angle_b}")

        #https://stackoverflow.com/questions/18583214/calculate-angle-of-triangle-python
        '''
        A = 7
        B = 7
        C = 9.899
        from math import acos, degrees
        degrees(acos((A * A + B * B - C * C)/(2.0 * A * B)))
        '''

        #https://github.com/Steenaire/triangle-calculator
        #https://github.com/Steenaire/triangle-calculator/blob/ff8a7978b08f2866634b3373a06da0be4200000d/draw-a-triangle-34.py#L29
        '''
        def LawOfSines(side, angleA, angleC):
        newSide = abs(side*(math.sin(math.radians(angleA)))/math.sin(math.radians(angleC)))
        return newSide
        '''
        #solved_angle_b = abs(given_length_a * (math.sin(math.radians(given_angle_A)))/math.sin(math.radians(given_angle_B) )) ##May be wrong bcause using angle B and not C at end
        #print(f"solved_angle_b: {solved_angle_b}")

        solved_angle_b = ( given_length_a  * math.sin(math.radians(given_angle_B)) ) / math.sin( math.radians(given_angle_A) )
        print(f"solved_angle_b: {solved_angle_b}")

        

        
       


        
        
    else: #LLA
        given_length_a = lengths[0]
        given_length_b = lengths[1]
        given_angle_B = angles[1]


    


def main():
    print("main function")
    #generate_triangle(True, 10, [90, 60] )
    solve_trig_triangle(True, 10, [90, 60] )
    print(  "Correct answer: " + str( 5 * ( 3**(1/2) ) )  )
    #solve_trig_triangle(True, [10], [60, 90] )
    

if __name__ == "__main__":
    main()
