from OpenGL.GL import *
from OpenGL.GLUT import *
from math import *
import numpy as np

'''
def y_matrix():
    glColor3f(0.7, 0.7, 0.7)
    glBegin(GL_LINES)
    for x in np.arange(0.1, 1, 0.1):
        if x==0.4:
            glColor3f(1.0, 0.0, 0.0)
        glVertex(x, 1)
        glVertex(x, -1)
        glVertex(-x, 1)
        glVertex(-x, -1)
        glColor3f(0.7, 0.7, 0.7)
    glEnd()

def x_matrix():
    glColor3f(0.7, 0.7, 0.7)
    glBegin(GL_LINES)
    for y in np.arange(0.1, 1, 0.1):
        if y==0.8:
            glColor3f(1.0, 0.0, 0.0)
        glVertex(1, y)
        glVertex(-1, y)
        glVertex(1, -y)
        glVertex(-1, -y)
        glColor3f(0.7, 0.7, 0.7)
    glEnd()
'''

def cubic_bezier_curve(p, r, g, b, draw_mode):
    glColor3f(r, g, b)
    glBegin(draw_mode)
    for t in np.arange(0, 1.001, 0.001):
        Bx=((1-t)**3)*p[0] + 3*((1-t)**2)*t*p[2] + 3*(1-t)*(t**2)*p[4] + (t**3)*p[6]
        By=((1-t)**3)*p[1] + 3*((1-t)**2)*t*p[3] + 3*(1-t)*(t**2)*p[5] + (t**3)*p[7] 
        glVertex(Bx, By)
    glEnd()
        

def quad_bezier_curve(p, r, g, b, draw_mode):
    glColor3f(r, g, b)
    glBegin(draw_mode)
    for t in np.arange(0, 1.001, 0.001):
        Bx = ((1-t)**2)*p[0] + 2*(1-t)*t*p[2] + (t**2)*p[4]
        By = ((1-t)**2)*p[1] + 2*(1-t)*t*p[3] + (t**2)*p[5]
        glVertex(Bx, By)
    glEnd()

def solding_quad_bezier(fp, sp, r, g, b,):
    glColor3f(r, g, b)
    glBegin(GL_LINES)
    for t in np.arange(0, 1.001, 0.001):
        FBx = ((1-t)**2)*fp[0] + 2*(1-t)*t*fp[2] + (t**2)*fp[4]
        FBy = ((1-t)**2)*fp[1] + 2*(1-t)*t*fp[3] + (t**2)*fp[5]
        SBx = ((1-t)**2)*sp[0] + 2*(1-t)*t*sp[2] + (t**2)*sp[4]
        SBy = ((1-t)**2)*sp[1] + 2*(1-t)*t*sp[3] + (t**2)*sp[5]
        glVertex(FBx, FBy)
        glVertex(SBx, SBy)
    glEnd()

def solding_cubic_bezier(fp, sp, r, g, b,):
    glColor3f(r, g, b)
    glBegin(GL_LINES)
    for t in np.arange(0, 1.001, 0.001):
        FBx=((1-t)**3)*fp[0] + 3*((1-t)**2)*t*fp[2] + 3*(1-t)*(t**2)*fp[4] + (t**3)*fp[6]
        FBy=((1-t)**3)*fp[1] + 3*((1-t)**2)*t*fp[3] + 3*(1-t)*(t**2)*fp[5] + (t**3)*fp[7]
        SBx=((1-t)**3)*sp[0] + 3*((1-t)**2)*t*sp[2] + 3*(1-t)*(t**2)*sp[4] + (t**3)*sp[6]
        SBy=((1-t)**3)*sp[1] + 3*((1-t)**2)*t*sp[3] + 3*(1-t)*(t**2)*sp[5] + (t**3)*sp[7]
        glVertex(FBx, FBy)
        glVertex(SBx, SBy)
    glEnd()
    
def draw():
    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)

##    glColor3f(0, 0, 0)
##    glBegin(GL_LINES)
##    glVertex(0, 1)
##    glVertex(0, -1)
##    glVertex(1, 0)
##    glVertex(-1, 0)
##    glEnd()

    #XY_GRID
    ##x_matrix()
    ##y_matrix()

    #ARMS
    quad_bezier_curve([-0.4, -0.6, 0.0, 1.0, 0.4, -0.6], 0.0, 0.0, 0.0, GL_POLYGON)
    quad_bezier_curve([0.4, -0.3, 0.0, 0.6, -0.4, -0.3], 0.7, 0.7, 0.7, GL_POLYGON)#ARM_SOLDING
    solding_quad_bezier([0.31, -0.35, 0.25, -0.25, 0.19, -0.19], [0.195, -0.4, 0.2, -0.4, 0.19, -0.19], 0.0, 0.0, 0.0)
    solding_quad_bezier([-0.31, -0.35, -0.25, -0.25, -0.19, -0.19], [-0.195, -0.4, -0.2, -0.4, -0.19, -0.19], 0.0, 0.0, 0.0)

    #RIGHT
    quad_bezier_curve([0.275, -0.3, 0.3, -0.25, 0.375, -0.25], 0.2, 0.2, 0.2, GL_POLYGON)#HAND_SOLDING_1
    cubic_bezier_curve([0.275, -0.3, 0.33, -0.4, 0.497, -0.5, 0.375, -0.25], 0.2, 0.2, 0.2, GL_POLYGON)#HAND_SOLDING_2_!
    cubic_bezier_curve([0.4, -0.3, 0.5, -0.6, 0.2, -0.5, 0.3, -0.43], 0.2, 0.2, 0.2, GL_POLYGON)#HAND_SOLDING_3
    cubic_bezier_curve([0.3, -0.45, 0.25, -0.4, 0.25, -0.35, 0.31, -0.35], 0.2, 0.2, 0.2, GL_POLYGON)#HAND_SOLDING_4
    cubic_bezier_curve([0.3, -0.45, 0.35, -0.4, 0.35, -0.35, 0.31, -0.35], 0.2, 0.2, 0.2, GL_POLYGON)#HAND_SOLDING_5_!
    
    quad_bezier_curve([0.275, -0.3, 0.3, -0.25, 0.375, -0.25], 0.0, 0.0, 0.0, GL_POINTS)#HAND_BORDERS_1
    cubic_bezier_curve([0.4, -0.3, 0.5, -0.6, 0.2, -0.5, 0.3, -0.43], 0.0, 0.0, 0.0, GL_POINTS)#HAND_BORDERS_3
    cubic_bezier_curve([0.3, -0.45, 0.25, -0.4, 0.25, -0.35, 0.31, -0.35], 0.0, 0.0, 0.0, GL_POINTS)#HAND_BORDERS_4
    quad_bezier_curve([0.4, -0.3, 0.0, 0.6, -0.4, -0.3], 0.0, 0.0, 0.0, GL_POINTS)#ARM_OUTER_BORDERS
    quad_bezier_curve([0.31, -0.35, 0.25, -0.25, 0.19, -0.19], 0.0, 0.0, 0.0, GL_POINTS)#ARM_INSIDE_BORDERS
    
    #LIFT
    quad_bezier_curve([-0.275, -0.3, -0.3, -0.25, -0.375, -0.25], 0.2, 0.2, 0.2, GL_POLYGON)#HAND_SOLDING_1
    cubic_bezier_curve([-0.275, -0.3, -0.33, -0.4, -0.497, -0.5, -0.375, -0.25], 0.2, 0.2, 0.2, GL_POLYGON)#HAND_SOLDING_2_!
    cubic_bezier_curve([-0.4, -0.3, -0.5, -0.6, -0.2, -0.5, -0.3, -0.43], 0.2, 0.2, 0.2, GL_POLYGON)#HAND_SOLDING_3
    cubic_bezier_curve([-0.3, -0.45, -0.25, -0.4, -0.25, -0.35, -0.31, -0.35], 0.2, 0.2, 0.2, GL_POLYGON)#HAND_SOLDING_4
    cubic_bezier_curve([-0.3, -0.45, -0.35, -0.4, -0.35, -0.35, -0.31, -0.35], 0.2, 0.2, 0.2, GL_POLYGON)#HAND_SOLDING_5_!
    
    quad_bezier_curve([-0.275, -0.3, -0.3, -0.25, -0.375, -0.25], 0.0, 0.0, 0.0, GL_POINTS)#HAND_BORDERS_1
    cubic_bezier_curve([-0.4, -0.3, -0.5, -0.6, -0.2, -0.5, -0.3, -0.43], 0.0, 0.0, 0.0, GL_POINTS)#HAND_BORDERS_3
    cubic_bezier_curve([-0.3, -0.45, -0.25, -0.4, -0.25, -0.35, -0.31, -0.35], 0.0, 0.0, 0.0, GL_POINTS)#HAND_BORDERS_4
    quad_bezier_curve([-0.31, -0.35, -0.25, -0.25, -0.19, -0.19], 0.0, 0.0, 0.0, GL_POINTS)#ARM_INSIDE_BORDERS
    ######################################

    #ENHANCEMENT
    solding_quad_bezier([0.15, 0.0, 0.17, -0.1, 0.28, -0.29], [0.19, -0.19, 0.24, -0.25, 0.28, -0.29], 0.6, 0.6, 0.6)
    solding_quad_bezier([-0.15, 0.0, -0.17, -0.1, -0.28, -0.29], [-0.19, -0.19, -0.24, -0.25, -0.28, -0.29], 0.6, 0.6, 0.6)
    #quad_bezier_curve([0.15, 0.0, 0.17, -0.1, 0.28, -0.29], 0.0, 0.0, 0.0, GL_POINTS)
    #quad_bezier_curve([0.19, -0.19, 0.24, -0.25, 0.28, -0.29], 1.0, 1.0, 0.0, GL_POINTS)
    
    
    #CHEST_LOGO
    quad_bezier_curve([0.15, 0.0, 0.2, -0.22, 0.2, -0.3], 0.0, 0.0, 0.0, GL_POINTS)#R_CURVE
    quad_bezier_curve([-0.15, 0.0, -0.2, -0.22, -0.2, -0.3], 0.0, 0.0, 0.0, GL_POINTS)#L_CURVE
    
    solding_quad_bezier([0.1, -0.03, 0.17, -0.13, 0.1, -0.23], [-0.1, -0.03, -0.17, -0.13, -0.1, -0.23], 0.2, 0.2, 0.2)#LOGO_SOLDING
    quad_bezier_curve([0.1, -0.03, 0.17, -0.13, 0.1, -0.23], 0.0, 0.0, 0.0, GL_POINTS)#LOGO_R_OUTER_CURVE
    quad_bezier_curve([-0.1, -0.03, -0.17, -0.13, -0.1, -0.23], 0.0, 0.0, 0.0, GL_POINTS)#LOGO_L_OUTER_CURVE
    
    solding_quad_bezier([0.1, -0.03, 0.1, -0.1, 0.025, -0.1], [-0.1, -0.03, -0.1, -0.1, -0.025, -0.1], 0.7, 0.7, 0.7)
    quad_bezier_curve([0.1, -0.03, 0.1, -0.1, 0.025, -0.1], 0.0, 0.0, 0.0, GL_POINTS)#LOGO_R_UPPER_CURVE
    quad_bezier_curve([-0.1, -0.03, -0.1, -0.1, -0.025, -0.1], 0.0, 0.0, 0.0, GL_POINTS)#LOGO_L_UPPER_CURVE

    solding_quad_bezier([0.025, -0.1, 0.025, -0.075, 0.025, -0.05], [-0.025, -0.1, -0.025, -0.075, -0.025, -0.05], 0.2, 0.2, 0.2)
    quad_bezier_curve([0.025, -0.1, 0.025, -0.075, 0.025, -0.05], 0.0, 0.0, 0.0, GL_POINTS)#LOGO_RL_UPPER_CURVE
    quad_bezier_curve([-0.025, -0.1, -0.025, -0.075, -0.025, -0.05], 0.0, 0.0, 0.0, GL_POINTS)#LOGO_LR_UPPER_CURVE


    quad_bezier_curve([-0.025, -0.05, 0.0, -0.1, 0.025, -0.05], 0.7, 0.7, 0.7, GL_POLYGON)#SOLDING_MIDDLE_CURVE
    quad_bezier_curve([-0.025, -0.05, 0.0, -0.1, 0.025, -0.05], 0.0, 0.0, 0.0, GL_POINTS)#MIDDLE_CURVE

    solding_quad_bezier([0.1, -0.23, 0.075, -0.15, 0.05, -0.23], [0.1, -0.23, 0.075, -0.25, 0.05, -0.23], 0.7, 0.7, 0.7)#POL_LINE
    quad_bezier_curve([0.1, -0.23, 0.075, -0.15, 0.05, -0.23], 0.0, 0.0, 0.0, GL_POINTS)#FIRST_R_CURVE
    quad_bezier_curve([0.1, -0.23, 0.075, -0.25, 0.05, -0.23], 0.7, 0.7, 0.7, GL_POINTS)#INVERSE_FIRST_R_CURVE
    solding_quad_bezier([-0.1, -0.23, -0.075, -0.15, -0.05, -0.23], [-0.1, -0.23, -0.075, -0.25, -0.05, -0.23], 0.7, 0.7, 0.7)#POL_LINE
    quad_bezier_curve([-0.1, -0.23, -0.075, -0.15, -0.05, -0.23], 0.0, 0.0, 0.0, GL_POINTS)#FIRST_L_CURVE
    quad_bezier_curve([-0.1, -0.23, -0.075, -0.25, -0.05, -0.23], 0.7, 0.7, 0.7, GL_POINTS)#INVERSE_FIRST_L_CURVE

    solding_quad_bezier([0.05, -0.23, 0.025, -0.18, 0.0, -0.25], [-0.05, -0.23, -0.025, -0.18, 0.0, -0.25], 0.2, 0.2, 0.2)#R_L
    quad_bezier_curve([0.05, -0.23, 0.025, -0.18, 0.0, -0.25], 0.7, 0.7, 0.7, GL_POLYGON)
    quad_bezier_curve([0.05, -0.23, 0.025, -0.18, 0.0, -0.25], 0.0, 0.0, 0.0, GL_POINTS)#SECOND_R_CURVE
    quad_bezier_curve([-0.05, -0.23, -0.025, -0.18, 0.0, -0.25], 0.7, 0.7, 0.7, GL_POLYGON)
    quad_bezier_curve([-0.05, -0.23, -0.025, -0.18, 0.0, -0.25], 0.0, 0.0, 0.0, GL_POINTS)#SECOND_L_CURVE
    ######################################

    
    #SHORT
    solding_quad_bezier([0.2, -0.3, 0.0, -0.38, -0.2, -0.3], [0.195, -0.25, 0.0, -0.32, -0.195, -0.25], 1.0, 1.0, 0.0)
    quad_bezier_curve([0.2, -0.3, 0.0, -0.38, -0.2, -0.3], 0.0, 0.0, 0.0, GL_POINTS)#LOWER_SHORT_LINE
    quad_bezier_curve([0.195, -0.25, 0.0, -0.32, -0.195, -0.25], 0.0, 0.0, 0.0, GL_POINTS)#UPPER_SHORT_LINE
    quad_bezier_curve([0.2, -0.3, 0.21, -0.275, 0.195, -0.25], 0.0, 0.0, 0.0, GL_POINTS)#R_SHORT_CURVE
    quad_bezier_curve([-0.2, -0.3, -0.21, -0.275, -0.195, -0.25], 0.0, 0.0, 0.0, GL_POINTS)#L_SHORT_CURVE

    solding_quad_bezier([0.2, -0.3, 0.25, -0.5, 0.23, -0.65], [0.05, -0.45, 0.08, -0.65, 0.05, -0.7], 0.7, 0.7, 0.7)#R_
    solding_quad_bezier([-0.2, -0.3, -0.25, -0.5, -0.23, -0.65], [-0.05, -0.45, -0.08, -0.65, -0.05, -0.7], 0.7, 0.7, 0.7)
    solding_quad_bezier([0.22, -0.4, 0.125, -0.425, 0.05, -0.45], [0.2, -0.3, 0.0, -0.38, -0.2, -0.3], 0.2, 0.2, 0.2)#R
    solding_quad_bezier([-0.05, -0.45, -0.125, -0.425, -0.22, -0.4], [0.2, -0.3, 0.0, -0.38, -0.2, -0.3], 0.2, 0.2, 0.2)
    solding_quad_bezier([0.05, -0.45, 0.0, -0.47, -0.05, -0.45], [0.195, -0.4, 0.0, -0.45, -0.195, -0.4], 0.2, 0.2, 0.2)#B
    solding_cubic_bezier([0.23, -0.65, 0.17, -0.7, 0.2, -0.8, 0.05, -0.7],[0.23, -0.55, 0.17, -0.4, 0.2, -0.65, 0.061, -0.6], 0.2, 0.2, 0.2)
    solding_cubic_bezier([-0.23, -0.65, -0.17, -0.7, -0.2, -0.8, -0.05, -0.7],[-0.23, -0.55, -0.17, -0.4, -0.2, -0.65, -0.061, -0.6], 0.2, 0.2, 0.2)
    
    quad_bezier_curve([0.2, -0.3, 0.25, -0.5, 0.23, -0.65], 0.0, 0.0, 0.0, GL_POINTS)#R_OUTER_LEG_CURVE
    quad_bezier_curve([0.05, -0.45, 0.08, -0.65, 0.05, -0.7], 0.0, 0.0, 0.0, GL_POINTS)#R_INNER_LEG_CURVE
    quad_bezier_curve([0.05, -0.45, 0.125, -0.425, 0.22, -0.4], 0.0, 0.0, 0.0, GL_POINTS)#R_SHORT
    quad_bezier_curve([0.05, -0.45, 0.0, -0.47, -0.05, -0.45], 0.0, 0.0, 0.0, GL_POINTS)#BETWEEN_LEGS
    cubic_bezier_curve([0.23, -0.65, 0.45, -0.7, 0.25, -0.9, 0.05, -0.7], 0.2, 0.2, 0.2, GL_POLYGON)#SOLDING_SHOES
    cubic_bezier_curve([0.23, -0.65, 0.45, -0.7, 0.25, -0.9, 0.05, -0.7], 0.0, 0.0, 0.0, GL_POINTS)#R_SHOES
    cubic_bezier_curve([0.23, -0.55, 0.17, -0.4, 0.2, -0.65, 0.061, -0.6], 0.0, 0.0, 0.0, GL_POINTS)#UPPER_BORDER
    ##cubic_bezier_curve([0.23, -0.65, 0.17, -0.7, 0.2, -0.8, 0.05, -0.7], 0.0, 0.0, 0.0, GL_POINTS)
    
    quad_bezier_curve([-0.2, -0.3, -0.25, -0.5, -0.23, -0.65], 0.0, 0.0, 0.0, GL_POINTS)#L_OUTER_LEG_CURVE
    quad_bezier_curve([-0.05, -0.45, -0.08, -0.65, -0.05, -0.7], 0.0, 0.0, 0.0, GL_POINTS)#L_INNER_LEG_CURVE
    quad_bezier_curve([-0.05, -0.45, -0.125, -0.425, -0.22, -0.4], 0.0, 0.0, 0.0, GL_POINTS)#L_SHORT
    cubic_bezier_curve([-0.23, -0.65, -0.45, -0.7, -0.25, -0.9, -0.05, -0.7], 0.2, 0.2, 0.2, GL_POLYGON)#SOLDING_SHOES
    cubic_bezier_curve([-0.23, -0.65, -0.45, -0.7, -0.25, -0.9, -0.05, -0.7], 0.0, 0.0, 0.0, GL_POINTS)#L_SHOES
    cubic_bezier_curve([-0.23, -0.55, -0.17, -0.4, -0.2, -0.65, -0.061, -0.6], 0.0, 0.0, 0.0, GL_POINTS)#LOWER_BORDER
    ######################################

    #BACK
    quad_bezier_curve([-0.23, -0.57, -0.3, -0.5, -0.4, -0.6], 1.0, 1.0, 1.0, GL_POLYGON)#L
    quad_bezier_curve([-0.23, -0.57, -0.25, -0.73, -0.4, -0.6], 1.0, 1.0, 1.0, GL_POLYGON)
    quad_bezier_curve([-0.23, -0.57, -0.3, -0.5, -0.4, -0.6], 0.0, 0.0, 0.0, GL_POINTS)

    quad_bezier_curve([-0.06, -0.6, 0.0, -0.55, 0.06, -0.6], 1.0, 1.0, 1.0, GL_POLYGON)#M
    quad_bezier_curve([-0.06, -0.6, 0.0, -0.55, 0.06, -0.6], 0.0, 0.0, 0.0, GL_POINTS)

    quad_bezier_curve([0.23, -0.6, 0.3, -0.5, 0.4, -0.6], 1.0, 1.0, 1.0, GL_POLYGON)#R
    quad_bezier_curve([0.23, -0.6, 0.3, -0.5, 0.4, -0.6], 0.0, 0.0, 0.0, GL_POINTS)
    #quad_bezier_curve([-0.4, -0.6, 0.0, 1.0, 0.4, -0.6], 0.15, 0.15, 0.15, GL_POINTS)#B
    ######################################
    
    #NECK
    quad_bezier_curve([0.2, 0.07, 0.0, -0.05, -0.2, 0.07], 0.15, 0.15, 0.15, GL_POLYGON)
    quad_bezier_curve([0.2, 0.07, 0.0, -0.05, -0.2, 0.07], 0.0, 0.0, 0.0, GL_POINTS)
    ######################################
    
    #HEAD
    cubic_bezier_curve([0.4, 0.2, 0.4, 0.0, -0.4, 0.0, -0.4, 0.2], 0.2, 0.2, 0.2, GL_POLYGON)#BEHIND_MOUTH_SOLDING
    cubic_bezier_curve([0.4, 0.2, 0.4, 0.0, -0.4, 0.0, -0.4, 0.2], 0.0, 0.0, 0.0, GL_POINTS)#BEHIND_MOUTH_BORDERS
    solding_quad_bezier([0.4, 0.19, 0.45, 0.5, 0.4, 0.8], [-0.4, 0.19, -0.45, 0.5, -0.4, 0.8], 0.2, 0.2, 0.2)#SOLDING_ALMOST_FACE
    quad_bezier_curve([0.4, 0.19, 0.45, 0.5, 0.4, 0.8], 0.0, 0.0, 0.0, GL_POINTS)#R_FACE_CURVE
    quad_bezier_curve([-0.4, 0.19, -0.45, 0.5, -0.4, 0.8], 0.0, 0.0, 0.0, GL_POINTS)#L_FACE_CURVE
    
    #EAR
    solding_quad_bezier([0.4, 0.8, 0.35, 0.7, 0.3, 0.6], [-0.4, 0.8, -0.35, 0.7, -0.3, 0.6], 0.15, 0.15, 0.15)
    quad_bezier_curve([0.4, 0.8, 0.35, 0.7, 0.3, 0.6], 0.17, 0.17, 0.17, GL_POINTS)
    quad_bezier_curve([-0.4, 0.8, -0.35, 0.7, -0.3, 0.6], 0.17, 0.17, 0.17, GL_POINTS)
    
    solding_quad_bezier([0.4, 0.8, 0.3, 0.7, 0.2, 0.6], [-0.4, 0.8, -0.3, 0.7, -0.2, 0.6], 1.0, 1.0, 1.0)
    quad_bezier_curve([0.4, 0.8, 0.3, 0.7, 0.2, 0.6], 0.0, 0.0, 0.0, GL_POINTS)
    quad_bezier_curve([-0.4, 0.8, -0.3, 0.7, -0.2, 0.6], 0.0, 0.0, 0.0, GL_POINTS)
    
    quad_bezier_curve([0.3, 0.6, 0.0, 0.7, -0.3, 0.6], 0.2, 0.2, 0.2, GL_POLYGON)
    quad_bezier_curve([0.3, 0.6, 0.0, 0.7, -0.3, 0.6], 0.0, 0.0, 0.0, GL_POINTS)

    #MOUTH
    solding_quad_bezier([0.25, 0.25, 0.0, 0.05, -0.25, 0.25], [0.25, 0.08, 0.0, 0.028, -0.25, 0.08], 1.0, 0.9, 0.7)
    quad_bezier_curve([0.25, 0.08, 0.0, 0.028, -0.25, 0.08], 0.0, 0.0, 0.0, GL_POINTS)
    
    solding_quad_bezier([0.25, 0.25, 0.27, 0.12, 0.25, 0.08], [-0.25, 0.25, -0.27, 0.12, -0.25, 0.08], 1.0, 0.9, 0.7)
    quad_bezier_curve([0.25, 0.25, 0.27, 0.12, 0.25, 0.08], 0.0, 0.0, 0.0, GL_POINTS)
    quad_bezier_curve([-0.25, 0.25, -0.27, 0.12, -0.25, 0.08], 0.0, 0.0, 0.0, GL_POINTS)
    
    solding_quad_bezier([0.25, 0.25, 0.125, 0.225, 0.0, 0.2], [-0.25, 0.25, -0.125, 0.225, 0.0, 0.2], 0.2, 0.2, 0.2)
    quad_bezier_curve([0.25, 0.25, 0.125, 0.225, 0.0, 0.2], 0.0, 0.0, 0.0, GL_POINTS)
    quad_bezier_curve([-0.25, 0.25, -0.125, 0.225, 0.0, 0.2], 0.0, 0.0, 0.0, GL_POINTS)
    
    #LIPS
    cubic_bezier_curve([0.0, 0.15, -0.2, 0.0, -0.2, 0.25, 0.0, 0.15], 1.0, 1.0, 1.0, GL_POLYGON) #TEETH_CCOLOR
    quad_bezier_curve([0.15, 0.17, 0.075, 0.1, 0.0, 0.15], 0.0, 0.0, 0.0, GL_POINTS)
    quad_bezier_curve([-0.15, 0.12, -0.08, 0.135, -0.03, 0.16], 0.0, 0.0, 0.0, GL_POINTS) #TEETH_LINE
    cubic_bezier_curve([0.0, 0.15, -0.2, 0.0, -0.2, 0.25, 0.0, 0.15], 0.0, 0.0, 0.0, GL_POINTS) #TEETH_BORDER
    
    #EYE
    solding_cubic_bezier([0.1, 0.4, 0.2, 0.35, 0.15, 0.5, 0.3, 0.5], [0.1, 0.4, 0.15, 0.25, 0.32, 0.25, 0.3, 0.5], 0.15, 0.15, 0.15)
    #cubic_bezier_curve([0.1, 0.4, 0.15, 0.25, 0.32, 0.25, 0.3, 0.5], 0.0, 0.0, 0.0, GL_POINTS) #BELOW_EYE
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_POLYGON)
    for i in np.arange(0, 2*pi, 0.001):
        x=0.065*cos(i)
        y=0.065*sin(i)    
        glVertex(x+0.22, y+0.37)
    glEnd()
    cubic_bezier_curve([0.1, 0.4, 0.2, 0.35, 0.15, 0.5, 0.3, 0.5], 0.0, 0.0, 0.0, GL_POINTS) #SINE
    
    solding_cubic_bezier([-0.1, 0.4, -0.2, 0.35, -0.15, 0.5, -0.3, 0.5], [-0.1, 0.4, -0.15, 0.25, -0.32, 0.25, -0.3, 0.5], 0.15, 0.15, 0.15)
    #cubic_bezier_curve([-0.1, 0.4, -0.15, 0.25, -0.32, 0.25, -0.3, 0.5], 0.0, 0.0, 0.0, GL_POINTS) #BELOW_EYE
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_POLYGON)
    for i in np.arange(0, 2*pi, 0.001):
        x=0.065*cos(i)
        y=0.065*sin(i)    
        glVertex(x-0.22, y+0.37)
    glEnd()
    cubic_bezier_curve([-0.1, 0.4, -0.2, 0.35, -0.15, 0.5, -0.3, 0.5], 0.0, 0.0, 0.0, GL_POINTS) #SINE
    ######################################
    
    glFlush()
    

glutInit()
glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
glutInitWindowSize(500, 500)
glutCreateWindow(b"BATMAN")
glutDisplayFunc(draw)
glutMainLoop()
