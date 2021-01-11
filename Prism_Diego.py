from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

a=0
def lateral_Prisma():

    glColor3f(0.7,0.5,0.6)
    r=1.0
    h=4
    n=10
    a = (2*math.pi)/n
    glBegin(GL_QUAD_STRIP)
    for i in range(0, n+1):
        x = r * math.cos(a*i)
        z = r * math.sin(a*i)
        glVertex3f(x, 0, z)
        glVertex3f(x, h, z)
    glEnd()


def base_Prisma():
    glColor3f(0.2, 0.2, 0.3)
    glBegin(GL_POLYGON)
    i = 0
    r = 1.0
    h=10
    n=10
    a = (2*math.pi)/n
    for i in range(0,n+1):
        x = r*math.cos(a*i)
        y = 0
        z = r*math.sin(a*i)
        glVertex3f(x, y, z)
    glEnd()

    glColor3f(0.6, 0.2, 0.2)
    glBegin(GL_POLYGON)
    for i in range(0,n+1):
        x = r * math.cos(a * i)
        y = 4
        z = r * math.sin(a * i)
        glVertex3f(x, y, z)
    glEnd()


def draw():
    global a
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glTranslatef(-2, 0, 0)
    glRotatef(-a, 0, 0, 1)
    #glTranslated(1.5, 1.1, 2.75)
    #glRotated(180, 0, 1, 0)
    lateral_Prisma()
    base_Prisma()
    glPopMatrix() #restaura o estado antes da transformação
    glutSwapBuffers()
    a += 1

def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# Main Program
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800, 600)
glutCreateWindow("PRISMA")
glutDisplayFunc(draw)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-20)
glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()

