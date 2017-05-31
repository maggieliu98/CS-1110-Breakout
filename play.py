# play.py
# Ananya Mishra (am2723) and Maggie Liu (ml958)
# December 8th, 2016
"""Subcontroller module for Breakout

This module contains the subcontroller to manage a single game in the Breakout App. 
Instances of Play represent a single game.  If you want to restart a new game, you are 
expected to make a new instance of Play.

The subcontroller Play manages the paddle, ball, and bricks.  These are model objects.  
Their classes are defined in models.py.

Most of your work on this assignment will be in either this module or models.py.
Whether a helper method belongs in this module or models.py is often a complicated
issue.  If you do not know, ask on Piazza and we will answer."""
from constants import *
from game2d import *
from models import *


# PRIMARY RULE: Play can only access attributes in models.py via getters/setters
# Play is NOT allowed to access anything in breakout.py (Subcontrollers are not
# permitted to access anything in their parent. To see why, take CS 3152)

class Play(object):
    """An instance controls a single game of breakout.
    
    This subcontroller has a reference to the ball, paddle, and bricks. It animates the 
    ball, removing any bricks as necessary.  When the game is won, it stops animating.  
    You should create a NEW instance of Play (in Breakout) if you want to make a new game.
    
    If you want to pause the game, tell this controller to draw, but do not update.  See 
    subcontrollers.py from Lecture 25 for an example.
    
    INSTANCE ATTRIBUTES:
        _paddle [Paddle]: the paddle to play with 
        _bricks [list of Brick]: the list of bricks still remaining 
        _ball   [Ball, or None if waiting for a serve]:  the ball to animate
    
    As you can see, all of these attributes are hidden.  You may find that you want to
    access an attribute in class Breakout. It is okay if you do, but you MAY NOT ACCESS 
    THE ATTRIBUTES DIRECTLY. You must use a getter and/or setter for any attribute that 
    you need to access in Breakout.  Only add the getters and setters that you need for 
    Breakout.
    
    You may change any of the attributes above as you see fit. For example, you may want
    to add new objects on the screen (e.g power-ups).  If you make changes, please list
    the changes with the invariants.
                  
    LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    
    """
    
    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    def getBricks(self):
        """Returns the list attribute _bricks"""
        
        return self._bricks

    # INITIALIZER (standard form) TO CREATE PADDLES AND BRICKS
    def __init__(self):
        """Initializer: Creates a list of bricks and a Paddle while
        assigning _ball to None"""
        
        # creation of bricks
        self._bricks = []
        vbob = GAME_HEIGHT-BRICK_Y_OFFSET
        v = 0
        for b in range(BRICK_ROWS):
            color = BRICK_COLORS[v]
            hbob = BRICK_SEP_H/2.0
            for b in range(BRICKS_IN_ROW):
                x = Brick(left = hbob, top = vbob, width = BRICK_WIDTH,
                               height = BRICK_HEIGHT, fillcolor = color,
                               linecolor = color)
                self._bricks.append(x)
                hbob = hbob + BRICK_WIDTH + BRICK_SEP_H
            vbob = vbob - BRICK_HEIGHT - BRICK_SEP_V
            v = v + 1
            if v == 10:
                v = 0
        
        # creation of paddle
        self._paddle = Paddle()
        # creation of ball
        self._ball = None
 
    # UPDATE METHODS TO MOVE PADDLE, SERVE AND MOVE THE BALL
    
    def updatePaddle(self, input):
        """Moves the paddle based on an arrow key press.
        
        If the left arrow key is pressed down, the paddle moves left until
        either it hits the left wall or the key is released. Similarly, if the
        right arrow key is pressed down, the paddle moves right until either
        it hits the right wall or the key is released.
        
        Parameter input: The user input
        Precondition: input is an instance of GInput"""
        
        newpos = 0
        
        if input.is_key_down('right') == True:
            newpos = PADDLE_SPEED
        
        if input.is_key_down('left') == True:
            newpos = -PADDLE_SPEED

        self._paddle.movePaddle(newpos)
               
    def serveBall(self):
        """Assigns an instance of Ball to the attribute _ball."""
        
        self._ball = Ball()
   
    def updateBall(self):
        """Moves, bounces, and collides the ball."""
        
        # moves the ball
        self.moveBall()
        # bounces the ball
        self.bounceBall()
        # collides ball with paddle
        self.collideBall()
        
    # DRAW METHOD TO DRAW THE PADDLES, BALL, AND BRICKS
    def drawBricks(self, view):
        """Draws the bricks in Breakout
        
        Parameter view: the game view
        Precondition: view is an instance of GView"""
        
        for x in self._bricks:
            x.draw(view)
    
    def drawPaddle(self,view):
        """Draws the paddle in Breakout
        
        Parameter view: the game view
        Precondition: view is an instance of GView"""
        
        self._paddle.draw(view)    

    def drawBall(self,view):
        """Draws the ball in Breakout
        
        Parameter view: the game view
        Precondition: view is an instance of GView"""
        
        self._ball.draw(view)
       
    # HELPER METHODS FOR PHYSICS AND COLLISION DETECTION
    def moveBall(self):
        """Moves the ball by changing its x and y coordinates"""
        
        self._ball.x += self._ball.getVX()
        self._ball.y += self._ball.getVY()
    
    def bounceBall(self):
        """Bounces the ball when it hits the top wall or the side walls."""
        
        if self._ball.top >= GAME_HEIGHT:
            self._ball.setVY(-self._ball.getVY())      
            
        if self._ball.left <= 0:
            self._ball.setVX(-self._ball.getVX())
            
        if self._ball.right >= GAME_WIDTH:
            self._ball.setVX(-self._ball.getVX())
            
    def collideBall(self):
        """Provides for collisions of the ball with either the paddle or the
        bricks.
        
        If the ball hits the paddle, it bounces off it. If the ball hits a brick,
        it bounces off and the brick disappears."""
        
        if self._paddle.collidep(self._ball) == True:
            self._ball.bounceSound.play()
            self._ball.setVY(-self._ball.getVY())
            
        for x in self._bricks:
            if x.collideb(self._ball) == True:
                self._ball.bounceSound.play()
                self._bricks.remove(x)
                self._ball.setVY(-self._ball.getVY()) 
         
    # ADD ANY ADDITIONAL METHODS (FULLY SPECIFIED) HERE
