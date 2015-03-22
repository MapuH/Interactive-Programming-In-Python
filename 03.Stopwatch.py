# template for "Stopwatch: The Game"
import simplegui

# define global variables
time = 0
tries = 0
hits = 0
running = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    deciseconds = t % 10
    seconds = (t / 10) % 60
    minutes = (t / 10) / 60
    return "%s:%02d.%s" % (minutes, seconds, deciseconds)

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global running
    timer.start()
    running = True

def stop():
    global hits, tries, running
    timer.stop()
    if running:
        tries += 1
        if time % 10 == 0:
            hits += 1
    running = False

def reset():
    global time, hits, tries, running
    timer.stop()
    time = 0
    hits = 0
    tries = 0
    running = False

# define event handler for timer with 0.1 sec interval
def tick():
    global time
    time += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(time), (105, 90), 36, "Black")
    canvas.draw_text(('%s/%s' % (hits, tries)), (245, 30), 24, "Yellow")

    
# create frame and register event handlers
f = simplegui.create_frame("Stopwatch", 300, 150)
f.set_canvas_background("Gray")
f.add_button("Start", start, 100)
f.add_button("Stop", stop, 100)
f.add_button("Reset", reset, 100)
f.set_draw_handler(draw)

timer = simplegui.create_timer(100, tick)

# start frame
f.start()
