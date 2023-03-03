from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
WINDOW_SIZE=500
x=0.0
y=0.0
mode=1.0

def init():
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)

def drawball():
    global x
    global y
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1.0,0.0,0.0)
    glVertex2f(x,y)
    for i in range(0,361,1):
        glVertex2f(60*math.cos(math.pi*i/180)+x,60*math.sin(math.pi*i/180)+y)
    glEnd()
    glutSwapBuffers()
def animate(temp):
    global mode,y

    if(mode==1):
        if(y>250):
            mode=0
        else:
            y=y+1
    else:
        if(y==0):
            mode=1
        else:
            y=y-1
    glutTimerFunc(int(1000/100),animate,0)
    glutPostRedisplay()

def main():
    glutInit(sys.argv)
    glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
    glutInitWindowPosition(0,0)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("ball")
    glutDisplayFunc(drawball)
    glutTimerFunc(0,animate,0)
    glutIdleFunc(drawball)
    init()
    glutMainLoop()
main()
