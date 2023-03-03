from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

WINDOW_SIZE = 700
ANGLE1 = 90
ANGLE2 = 90
ANGLE3 = 90
ANGLE4 = 90
ANGLE5 = 90
ANGLE6 = 90
ANGLE7 = 90
ANGLE8 = 90

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-3000, 3000, -3000, 3000)

def drawSun():
    x = 0.0
    y = 0.0

    glClear(GL_COLOR_BUFFER_BIT)

    # Sun
    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)
    for i in range(0, 361, 1):
        glVertex2f(100 * math.cos(math.pi * i / 180.0) + x, 100 * math.sin(math.pi * i / 180.0) + y)
    glEnd()

def drawPlanet(R,r, angle):

    x = R*math.cos(math.pi*angle/180.0)
    y = R*math.sin(math.pi*angle/180.0)

    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)
    for i in range(0, 361, 1):
        glVertex2f(r * math.cos(math.pi * i / 180.0) + x, r * math.sin(math.pi * i / 180.0) + y)
    glEnd()


def drawSolar():

    drawSun()

    global ANGLE1
    global ANGLE2
    global ANGLE3
    global ANGLE4
    global ANGLE5
    global ANGLE6
    global ANGLE7
    global ANGLE8

    glColor3f(0.5, 0.5, 0.5)     #Mercury
    drawPlanet(300, 50, ANGLE1)
    glColor3f(1.0, 0.68, 0.4)     #Venus
    drawPlanet(500, 70, ANGLE2)
    glColor3f(0.0, 1.0, 1.0)     #Earth
    drawPlanet(900, 100, ANGLE3)
    glColor3f(0.8, 0.0, 0.0)     #Mars
    drawPlanet(1100, 100, ANGLE4)
    glColor3f(1.0, 0.5, 0.0)     #Jupiter
    drawPlanet(1600, 200, ANGLE5)
    glColor3f(1.0, 0.8, 0.0)     #Saturn
    drawPlanet(1900, 150, ANGLE6)
    glColor3f(0.0, 1.0, 1.0)     #Uranus
    drawPlanet(2300, 100, ANGLE7)
    glColor3f(0.0, 0.0, 1.0)     #Neptune
    drawPlanet(2700, 100, ANGLE8)

    glutSwapBuffers()


'''
    #Mercury
    x=150
    y=150
    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)
    for i in range(0, 361, 1):
        glVertex2f(50 * math.cos(math.pi * i / 180.0) + x, 50 * math.sin(math.pi * i / 180.0) + y)
    glEnd()

    #Venus
    x= 275
    y= 275
    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)
    for i in range(0, 361, 1):
        glVertex2f(50 * math.cos(math.pi * i / 180.0) + x, 50 * math.sin(math.pi * i / 180.0) + y)
    glEnd()

    #Earth
    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)
    for i in range(0, 361, 1):
        glVertex2f(50 * math.cos(math.pi * i / 180.0) + x, 50 * math.sin(math.pi * i / 180.0) + y)
    glEnd()
'''

def animate(temp):
    global ANGLE1
    global ANGLE2
    global ANGLE3
    global ANGLE4
    global ANGLE5
    global ANGLE6
    global ANGLE7
    global ANGLE8
   #glRotatef(-1,0,0,1)

    ANGLE1 -= 1
    ANGLE2 -= 2
    ANGLE3 -= 3
    ANGLE4 -= 4
    ANGLE5 -= 5
    ANGLE6 -= 6
    ANGLE7 -= 7
    ANGLE8 -= 8



    glutTimerFunc(100, animate, 0)
    glutPostRedisplay()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(WINDOW_SIZE, WINDOW_SIZE)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Solar System")
    glutDisplayFunc(drawSolar)
    glutTimerFunc(0, animate, 0)
    init()
    glutMainLoop()
main()