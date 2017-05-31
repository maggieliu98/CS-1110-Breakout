# models.py
# Maggie Liu (ml958) and Ananya Mishra (am2723)
# December 8th, 2016
"""Models module for Breakout

This module contains the model classes for the Breakout game. That is anything that you
interact with on the screen is model: the paddle, the ball, and any of the bricks.

Technically, just because something is a model does not mean there has to be a special 
class for it.  Unless you need something special, both paddle and individual bricks could
just be instances of GRectangle.  However, we do need something special: collision 
detection.  That is why we have custom classes.

You are free to add new models to this module.  You may wish to do this when you add
new features to your game.  If you are unsure about whether to make a new class or 
not, please ask on Piazza."""
import random # To randomly generate the ball velocity
from constants import *
from game2d import *


# PRIMARY RULE: Models are not allowed to access anything except the module constants.py.
# If you need extra information from Play, then it should be a parameter in your method, 
# and Play should pass it as a argument when it calls the method.


class Paddle(GRectangle):
    """An instance is the game paddle.
    
    This class contains a method to detect collision with the ball, as well as move it
    left and right.  You may wish to add more features to this class.
    
    The attributes of this class are those inherited from GRectangle.
    
    LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    """
    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    
    # INITIALIZER TO CREATE A NEW PADDLE
    def __init__(self):
        """Initializer: Creates a game paddle."""
        
        GRectangle.__init__(self, width = PADDLE_WIDTH, height = PADDLE_HEIGHT,
                              bottom = PADDLE_OFFSET, x = GAME_WIDTH/2.0,
                              linecolor = colormodel.BLACK,
                              fillcolor = colormodel.BLACK)
    
    # METHODS TO MOVE THE PADDLE AND CHECK FOR COLLISIONS
    def movePaddle(self, value):
        """Moves the paddle based by a certain amount 'value'.
        
        Parameter value: The distance for the paddle to move
        Precondition: value is a number (int or float)"""
        
        minx = PADDLE_WIDTH/2.0
        maxx = GAME_WIDTH - PADDLE_WIDTH/2.0
        
        self.x += value
        
        if self.x < minx:
            self.x = minx
        
        if self.x > maxx:
            self.x = maxx
            
    def collidep(self, ball):
        """Returns True if the ball has collided with the paddle; False otherwise
        
        Parameter ball: the ball in the game
        Precondition: ball is an instance of class Ball"""
        
        if self.contains(ball.left, ball.bottom):
            return True
            
        if self.contains(ball.right, ball.bottom):
            return True
        
        return False
        
    # ADD MORE METHODS (PROPERLY SPECIFIED) AS NECESSARY

class Brick(GRectangle):
    """An instance is a brick.
    
    This class contains a method to detect collision with the ball.  You may wish to 
    add more features to this class.
    
    The attributes of this class are those inherited from GRectangle.
    
    LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    """
    
    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    
    # INITIALIZER TO CREATE A BRICK
    
    # METHOD TO CHECK FOR COLLISION
    def collideb(self, ball):
        """Returns True if the ball has collided with a brick; False otherwise.
        
        Parameter ball: the ball in the game
        Precondition: ball is an instance of class Ball"""
        
        if self.contains(ball.left, ball.bottom):
            return True
            
        if self.contains(ball.right, ball.bottom):
            return True
        
        if self.contains(ball.left, ball.top):
            return True
            
        if self.contains(ball.right, ball.top):
            return True
    
    # ADD MORE METHODS (PROPERLY SPECIFIED) AS NECESSARY

class Ball(GImage):
    """Instance is a game ball.
    
    We extend GEllipse because a ball must have additional attributes for velocity.
    This class adds this attributes and manages them.
    
    INSTANCE ATTRIBUTES:
        _vx [int or float]: Velocity in x direction 
        _vy [int or float]: Velocity in y direction

    
    The class Play will need to look at these attributes, so you will need
    getters for them.  However, it is possible to write this assignment with no
    setters for the velocities.
    
    How? The only time the ball can change velocities is if it hits an obstacle
    (paddle or brick) or if it hits a wall.  Why not just write methods for these
    instead of using setters?  This cuts down on the amount of code in Gameplay.
    
    NOTE: The ball does not have to be a GEllipse. It could be an instance
    of GImage (why?). This change is allowed, but you must modify the class
    header up above.
    
    LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    
        bounceSound [Sound object]: Sound produced when ball bounces off something
    """
    
    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    def getVX(self):
        """Returns the hidden attribute _vx"""
        return self._vx
    
    def getVY(self):
        """Returns the hidden attribute _vy"""
        return self._vy
    
    def setVX(self, value):
        """Sets the horizontal velocity as value
        
        Parameter value: the value to be set for _vx
        Precondition: value is a number (int or float)"""
        self._vx = value
        
    def setVY(self, value):
        """Sets the vertical velocity as value
        
        Parameter value: the value to be set for _vy
        Precondition: value is a number (int or float)"""
        self._vy = value 
    
    # INITIALIZER TO SET RANDOM VELOCITY
    def __init__(self):
        """Initializer: Creates a game ball."""
        
        #GEllipse.__init__(self, x = GAME_WIDTH/2.0, y = GAME_HEIGHT/2.0,
         #                 width = BALL_DIAMETER, height = BALL_DIAMETER,
          #                fillcolor = colormodel.BLACK)
        GImage.__init__(self, x = GAME_WIDTH/2.0, y = GAME_HEIGHT/2.0,
                        width = BALL_DIAMETER, height = BALL_DIAMETER,
                        source = 'walker-white.png')
        self._vx = random.uniform(2.0,4.0) 
        self._vx = self._vx * random.choice([-1, 1])
        self._vy = -BALL_SPEED
        self.bounceSound = Sound('bounce.wav')
    
    # METHODS TO MOVE AND/OR BOUNCE THE BALL
    
    # ADD MORE METHODS (PROPERLY SPECIFIED) AS NECESSARY

# IF YOU NEED ADDITIONAL MODEL CLASSES, THEY GO HERE