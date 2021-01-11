from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

vertices = (
    ( 1,-1,-1),
    ( 1, 1,-1),
    (-1, 1,-1),
    (-1,-1,-1),
    ( 1,-1, 1),
    ( 1, 1, 1),
    (-1,-1, 1),
    (-1, 1, 1),
    )

linhas = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7),
    )

faces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    )

cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1) )

a=0

def drawPyramid():
    # Desenho da base
    glPushMatrix()
    glTranslatef(-4,0,0)
    glRotatef(-a,0,0,1)
    base()
    lateral()
    glPopMatrix()

def lateral():
    glBegin(GL_TRIANGLE_FAN)
    i=0
    glVertex3f(0,4,0)
    glColor3f(0.7,0.5,0.6)
    i = 0
    r = 2
    a = (2*math.pi)/5
    for i in range(0,5):
        x = r*math.cos(a*i)
        y = 0    
        z = r*math.sin(a*i)
        glVertex3f(x,y,z)
        
    glEnd()

def base():
    glBegin(GL_POLYGON)
    i = 0
    r = 2
    a = (2*math.pi)/5
    for i in range(0,5):
        x = r*math.cos(a*i)
        y = 0    
        z = r*math.sin(a*i)
        glColor3fv((x,y,z))
        glVertex3f(x,y,z)
    glEnd()

def draw():
    global a
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    drawPyramid()
    glutSwapBuffers()
    a += 1


def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)


# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("PIRAMIDE")
glutDisplayFunc(draw)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-20)
glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()


