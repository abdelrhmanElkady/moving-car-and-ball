from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

def MyInit():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60 , 1 , 1 , 30)
    gluLookAt(8,9,10,
              0,0,0,
    0,1,0)

    glClearColor(0.8,0.7,0,1)
    glClear(GL_COLOR_BUFFER_BIT)



x=0
angle=0
forward=0
F=0
K=0
Y=0
def ARROW_KEYS(key,x,y):
    global K
    global F

    if key== GLUT_KEY_LEFT:
        K-=1
        F=90


    elif key == GLUT_KEY_RIGHT:
        K+=1
        F=90

    draw()

def draw():
    global angle
    global x
    global forward
    global F
    global Y


    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT)





    #road
    glLoadIdentity()
    glRotate(F,0,1,0)


    glBegin(GL_QUADS)
    glColor3f(0.8,0.9,0.9)
    glVertex(200, 0, -3)
    glVertex(-100, 0, -3)
    glVertex(-100, 0, 3)
    glVertex(200, 0, 3)



    glColor3f(1,1,1)
    glVertex(100, 0, -1)
    glVertex(-20, 0, -1)
    glVertex(-20, 0, 1)
    glVertex(100, 0, 1)




    glEnd()




 # body
    glLoadIdentity()
    glRotate(F,0,1,0)
    glColor3f(1, 0, 0)
    glTranslate(x,0,K)
    glScale(1, 0.25, 0.5)
    glutWireCube(5)

    glLoadIdentity()
    glRotate(F,0,1,0)
    glTranslate(x,5*0.25,K)
    glScale(0.5, 0.25, 0.5)
    glutWireCube(5)

    # light

    glLoadIdentity()
    glRotate(F,0,1,0)
    glColor3f(0.8, 1, 0)
    glTranslate(x + 2.8, 0, 1+K)
    glutWireSphere(0.3, 100, 100)

    glLoadIdentity()
    glRotate(F,0,1,0)
    glColor3f(0.8, 1, 0)
    glTranslate(x + 2.8, 0, -0.8+K)
    glutWireSphere(0.3, 100, 100)


#wheels

    glColor3f(1,0,1)
    glLoadIdentity()
    glRotate(F,0,1,0)
    glTranslate(x+1.25,-5*0.25*.5,5*0.5*0.5+K)
    glRotate(angle,0,0,1)
    glutWireTorus(0.15,0.5,12,10)

    glColor3f(1, 0, 1)
    glLoadIdentity()
    glRotate(F,0,1,0)
    glTranslate(x+-1.25, -5 * 0.25 * .5, 5 * 0.5 * 0.5+K)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.15, 0.5, 12, 10)

    glColor3f(1, 0, 1)
    glLoadIdentity()
    glRotate(F,0,1,0)
    glTranslate(x+1.25, -5 * 0.25 * .5, -5 * 0.5 * 0.5+K)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.15, 0.5, 12, 10)

    glColor3f(1, 0, 1)
    glLoadIdentity()
    glRotate(F,0,1,0)
    glTranslate(x+-1.25, -5 * 0.25 * .5, 5 * 0.5 * -0.5+K)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.15, 0.5, 12, 10)


#moving ball
    glLoadIdentity()
    glColor3f(0, 1, 0)
    glRotate(F,0,1,0)
    glTranslate(-x, 0, 0)
    glutSolidSphere(0.5, 100, 100)



    glutSwapBuffers()
    glBegin(GL_LINES)

    if forward:
        angle -= 0.1
        x += 0.009
        Y += 0.025

        if x > 10:
            forward = False
    else:
        angle += 0.1
        x -= 0.009
        Y -= 0.025

        if x < -20:
            forward = True










    glEnd()

glutInit()

glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(700, 700)
glutCreateWindow(b"Moving Car program")
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutSpecialFunc(ARROW_KEYS)
MyInit()
glutMainLoop()
