#turtle-drawing
#https://docs.python.org/3/library/turtle.html
from turtle import *

def draw_triangle():#config, data):
    #config - string defining type of triangle layout
    #data - array containing relevant data
    #labels - extra array that changes or replaces the labels of data

    #from turtle import *
    #t = turtle.Turtle() #https://realpython.com/beginners-guide-python-turtle/
    color('red', 'yellow')
    begin_fill()
    while True:
        forward(200)
        left(170)
        if abs(pos()) < 1:
            break
    end_fill()
    done()
    

def main():
    print("main function")
    draw_triangle()

if __name__ == "__main__":
    main()
