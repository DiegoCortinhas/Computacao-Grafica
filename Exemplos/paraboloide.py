import sys
import sdl2
from OpenGL.GL import *
from OpenGL.GLU import *

# pip install PyOpenGL
# pip install PySDL2

x0 = -4.0
xf = 4.0
y0 = -4.0
yf = 4.0
qtx = 20
qty = 20
dx = (xf-x0)/qtx
dy = (yf-y0)/qty

def f(x,y):
    return x**2 - y**2

ax = 0
ay = 0
def desenha():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glRotate(ax,1,0,0)
    glRotate(ay,0,1,0)
    y = y0
    for i in range(0,qty):
        x = x0
        glColor3f(1-(i/qty),0,(i/qty))
        # Começa a quad_strip
        glBegin(GL_QUAD_STRIP)
        for j in range(0,qtx):
            # emitir o vertice 2j
            glVertex3f(x,y,f(x,y))
            # emitir o vertice 2j+1
            glVertex3f(x,y+dy,f(x,y+dy))
            x += dx
        glVertex3f(xf,y,f(xf,y))
        glVertex3f(xf,y+dy,f(xf,y+dy))
        glEnd()
        y += dy
    glPopMatrix()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

sdl2.SDL_Init(sdl2.SDL_INIT_EVERYTHING)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_MAJOR_VERSION, 2)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_MINOR_VERSION, 0)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_PROFILE_MASK,sdl2.SDL_GL_CONTEXT_PROFILE_CORE)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_DOUBLEBUFFER, 1)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_DEPTH_SIZE, 24)
sdl2.SDL_GL_SetSwapInterval(1)
window = sdl2.SDL_CreateWindow(b"Paraboloide", sdl2.SDL_WINDOWPOS_CENTERED, sdl2.SDL_WINDOWPOS_CENTERED, WINDOW_WIDTH, WINDOW_HEIGHT, sdl2.SDL_WINDOW_OPENGL | sdl2.SDL_WINDOW_SHOWN)

if not window:
    sys.stderr.write("Error: Could not create window\n")
    exit(1)
glcontext = sdl2.SDL_GL_CreateContext(window)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,200.0)
glTranslatef(0.0,0.0,-60)

running = True
event = sdl2.SDL_Event()
while running:
    while sdl2.SDL_PollEvent(ctypes.byref(event)) != 0:
        if event.type == sdl2.SDL_QUIT:
            running = False
        if event.type == sdl2.events.SDL_KEYDOWN:
            print("SDL_KEYDOWN")
            if event.key.keysym.sym == sdl2.SDLK_ESCAPE:
                running = False
            if event.key.keysym.sym == sdl2.SDLK_DOWN:
                ax += 1
            if event.key.keysym.sym == sdl2.SDLK_UP:
                ax -= 1
            if event.key.keysym.sym == sdl2.SDLK_LEFT:
                ay += 1
            if event.key.keysym.sym == sdl2.SDLK_RIGHT:
                ay -= 1
        if (event.type == sdl2.SDL_MOUSEMOTION):
            print("SDL_MOUSEMOTION")
        if (event.type == sdl2.SDL_MOUSEBUTTONDOWN):
            print("SDL_MOUSEBUTTONDOWN")
    desenha()
    sdl2.SDL_GL_SwapWindow(window)