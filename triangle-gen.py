#triangle-gen1

#https://www.omnicalculator.com/math/trigonometry
#Trig from/using area - TODO 11:14am 7/11/2022 i1

#https://www.trigcalc.com/

import math

#def generate_triangle(config):
    #config - string of 3 characters, either L or A representing and storing the order of data of length or angle.
#def generate_triangle(isLAA, data):
#def generate_triangle(isLAA, lengths, angles):
def solve_trig_triangle(isLAA, lengths, angles):
    #isLAA - boolean.
    #True: treating triangle as length-angle-angle
    #False: treating triangle as length-length-angle

    #data - discontinued
    #lengths, angles - seperate arrays
    '''
    Types of triangle questions
    Length, angle, angle
    Length, length, angle
    '''

    #sin A / a = sin B / b = sin C / c

    #Data assignment by configuration
    if isLAA:
        given_length_a = lengths[0] #Known/Given values
        given_angle_A = angles[0]
        given_angle_B = angles[1]

        solved_angle_b = ( given_length_a / math.sin( given_angle_A ) ) * math.sin(given_angle_B)
        print(solved_angle_b)
        
    else: #LLA
        given_length_a = lengths[0]
        given_length_b = lengths[1]
        given_angle_B = angles[1]


    


def main():
    print("main function")
    generate_triangle(True, [10], [90, 60] )
    solve_trig_triangle(True, [10], [90, 60] )

if __name__ == "__main__":
    main()
