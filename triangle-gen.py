#triangle-gen2

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
        
        #solved_angle_b = ( given_length_a / math.sin( given_angle_A ) ) * math.sin(given_angle_B)
        #solved_angle_b = ( given_length_a  * math.sin(given_angle_B) ) / math.sin( given_angle_A )
        #print(f"solved_angle_b: {solved_angle_b}")
        
        #step1 = given_length_a * math.sin(given_angle_B)
        step1 = math.sin(given_angle_B)
        print(f"step1: {step1}")

        #https://www.symbolab.com/solver/equation-calculator/%20%5Cfrac%7Bsin%5Cleft(A%5Cright)%7D%7Ba%7D%3D%5Cfrac%7Bsin%5Cleft(B%5Cright)%7D%7Bx%7D?or=input
        #https://www.symbolab.com/solver/equation-calculator/%20%5Cfrac%7Bsin%5Cleft(90%5Cright)%7D%7B10%7D%3D%5Cfrac%7Bsin%5Cleft(60%5Cright)%7D%7Bx%7D?or=input

        step2 = given_length_a * math.sin(given_angle_B)
        print(f"step2: {step2}")


        
        
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
