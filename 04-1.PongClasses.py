import simplegui
import random

# globals
WIDTH = 600
HEIGHT = 400

class ImageInfo:
    def __init__(self, center, size, radius = 0):
        self.center = center
        self.size = size
        self.radius = radius
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

# images and sounds
ball_info = ImageInfo([20,20], [40, 40], 20)
ball_image = simplegui.load_image('http://www.rxsport.co.uk/product_images/uploaded_images/rb-gradient5.png')

paddle_info = ImageInfo([4, 40], [8, 80])
paddle_image = simplegui.load_image('https://www.dropbox.com/s/2sr9vy2cfe2gulp/paddle.png?dl=1')

hit_sound = simplegui.load_sound('https://www.freesound.org/data/previews/73/73565_701056-lq.mp3')
hit_sound.set_volume(0.7)
# Copyright © 2011 Varazuvi™ www.varazuvi.com
score_sound = simplegui.load_sound('http://www.freesound.org/data/previews/145/145440_2615119-lq.mp3')

# helper function to bounce ball off top/bottom
def bounce(ball, field):
    if ball.get_position()[1] - ball.get_radius() <= 0 or ball.get_position()[1] + ball.get_radius() >= field.height - 1:
            ball.vel[1] = -ball.vel[1]

# helper functions to check if ball hits paddles and update score
def check_left(ball, field):
    if ball.get_position()[0] - ball.get_radius() <= left_paddle.get_width():
        if ball.get_position()[1] - left_paddle.get_vposition() in range(-(left_paddle.image_center[1] + ball.get_radius()), left_paddle.image_center[1] + ball.get_radius()):
            ball.vel[0] = -ball.vel[0] * 1.1
            hit_sound.rewind()
            hit_sound.play()
        else:
            field.right_score()
            score_sound.rewind()
            score_sound.play()
            ball.spawn('right')
            
def check_right(ball, field):            
    if ball.get_position()[0] + ball.get_radius() >= field.width - 1 - right_paddle.get_width():
        if ball.get_position()[1] - right_paddle.get_vposition() in range(-(right_paddle.image_center[1] + ball.get_radius()), right_paddle.image_center[1] + ball.get_radius()):
            ball.vel[0] = -ball.vel[0] * 1.1
            hit_sound.rewind()
            hit_sound.play()
        else:
            field.left_score()
            score_sound.rewind()
            score_sound.play()
            ball.spawn('left')
            
# Field class
class Field:
    def __init__(self, width, height, gutter, score):
        self.width = width
        self.height = height
        self.gutter = gutter
        self.score = [score[0], score[1]]
        
    def draw(self, canvas):
        canvas.draw_line([self.width / 2, 0],[self.width / 2, self.height], 1, "White")
        canvas.draw_line([self.gutter, 0],[self.gutter, self.height], 1, "White")
        canvas.draw_line([self.width - self.gutter, 0],[self.width - self.gutter, self.height], 1, "White")
        canvas.draw_circle([self.width / 2, self.height / 2], self.height / 6, 1, "White")
        canvas.draw_text(str(self.score[0]), (self.width/2 - 100, 80), 32, "White")
        canvas.draw_text(str(self.score[1]), (self.width/2 + 75, 80), 32, "White")
        
    def left_score(self):
        self.score[0] += 1
        
    def right_score(self):
        self.score[1] += 1

# Ball class
class Ball:
    def __init__(self, pos, vel, image, info):
        self.pos = [pos[0], pos[1]]
        self.vel = [vel[0], vel[1]]
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        
    def draw(self, canvas):
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size)
                
    def spawn(self, direction):
        self.pos = [WIDTH / 2, HEIGHT / 2]
        if direction == 'right':
            self.vel = [random.randrange(2,4), -random.randrange(1,3)]
        elif direction == 'left':
            self.vel = [-random.randrange(2,4), -random.randrange(1,3)]
            
    def update(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
          
    def get_position(self):
        return self.pos
    
    def get_radius(self):
        return self.radius
            
# Paddle class
class Paddle:
    def __init__(self, pos, vel, image, info):
        self.pos = [pos[0], pos[1]]
        self.vel = [vel[0], vel[1]]
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        
    def draw(self, canvas):
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size)
        if self.pos[1] <= self.image_center[1]:
            self.pos[1] = self.image_center[1]
        elif self.pos[1] >= HEIGHT - self.image_center[1]:
            self.pos[1] = HEIGHT - self.image_center[1]
        
    def update(self):
        self.pos[1] += self.vel[1]
        
    def move(self, direction):
        if direction == 'up':
            self.vel[1] = -3
        if direction == 'down':
            self.vel[1] = 3
            
    def stop(self):
        self.vel[1] = 0
    
    def get_vposition(self):
        return self.pos[1]
        
    def get_width(self):
        return self.image_size[0]

# Handler to draw on canvas
def draw(canvas):
    main_field.draw(canvas)
    pong_ball.draw(canvas)
    pong_ball.update()
    left_paddle.draw(canvas)
    right_paddle.draw(canvas)
    left_paddle.update()
    right_paddle.update()
    bounce(pong_ball, main_field)
    check_right(pong_ball, main_field)
    check_left(pong_ball, main_field)
    
# Key handlers to control paddles
def keydown(key):
    if key == simplegui.KEY_MAP["w"]:
        left_paddle.move('up')
    elif key == simplegui.KEY_MAP["s"]:
        left_paddle.move('down')
        
    if key == simplegui.KEY_MAP["up"]:
        right_paddle.move('up')
    elif key == simplegui.KEY_MAP["down"]:
        right_paddle.move('down')
        
def keyup(key):
    if key == simplegui.KEY_MAP["w"] or key == simplegui.KEY_MAP["s"]:
        left_paddle.stop()
        
    if key == simplegui.KEY_MAP["up"] or key == simplegui.KEY_MAP["down"]:
        right_paddle.stop()

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keyup_handler(keyup)
frame.set_keydown_handler(keydown)

# initialize field, ball and paddles
main_field = Field(WIDTH, HEIGHT, 8, [0, 0])
pong_ball = Ball([WIDTH / 2, HEIGHT / 2], [0, 0], ball_image, ball_info)
left_paddle = Paddle([4, HEIGHT / 2], [0, 0], paddle_image, paddle_info)
right_paddle = Paddle([WIDTH - 4, HEIGHT / 2], [0, 0], paddle_image, paddle_info)

# Start the frame animation
frame.start()
pong_ball.spawn(random.choice(('right', 'left')))