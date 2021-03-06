try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

message = "Welcome!"

# Handlers for mouse click
def click():
    global message
    message = "Good job!"

def reset():
	global message
	message = "Welcome!"

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, [50,112], 48, "Red")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)
frame.add_button("Click me", click)
frame.add_button("Reset", reset)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
