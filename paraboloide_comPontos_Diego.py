from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

x0 = -1
y0 = -1
xf = 1
yf = 1
dx = 0.1
dy = 0.1

def f(x,y):
    # Paraboloide Circular
    return x**2+y**2

def f2(x,y):
    # Paraboloide Hiberbolico
    return x**2-y**2


def desenhaSuperficie():
    glBegin(GL_POINTS)
    x = x0
    while x < xf:
        y = y0
        while y < yf:
            z = f(x,y)
            glVertex3f(x,y,z)
            y += dy
        x += dx
    glEnd()

a = 0

def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) #buffer gerencia objetos visiveis e nao visiveis
    glPushMatrix()
    glRotatef(-a,1,0,0)
    desenhaSuperficie()
    glPopMatrix()
    glutSwapBuffers()
    a += 1
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("Superficie")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,100.0)
#gluOrtho2D (-2, 2, -2, 2)
glTranslatef(0.0,0.0,-5)
glutTimerFunc(50,timer,1)
glutMainLoop()


