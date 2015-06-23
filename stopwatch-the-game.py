# template for "Stopwatch: The Game"
import simplegui

# define global variables
unit = 0
times_stopped = 0
times_won = 0


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(unit):
    global D
    A = unit // 600
    whole_seconds = unit // 10
    part_two = whole_seconds % 60
    B = part_two // 10
    C = part_two % 10
    D = unit % 10
    return str(A) + ":" + str(B) + str(C) + "." + str(D)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    
def stop():
    global times_stopped
    global times_won
    global D
    if timer.is_running() == True:
        timer.stop()
        if D == 0:
            times_won += 1
            times_stopped += 1
            return times_won, times_stopped
        else:
            times_stopped += 1
            return times_stopped
    else:
        pass
       
def reset():
    global unit
    global times_stopped
    global times_won
    times_won = 0
    times_stopped = 0
    unit = 0
    return unit, times_stopped, times_won

# define event handler for timer with 0.1 sec interval

def milliseconds():
    global unit
    unit += 1
    return unit

# define draw handler
def draw(canvas):
    canvas.draw_text(format(unit), [100, 150], 40, 'White')
    canvas.draw_text("Won / Total: " + str(times_won) + " / " 
                     + str(times_stopped), [210, 30], 12, 'Red')
    
# create frame
timer = simplegui.create_timer(100, milliseconds)
f = simplegui.create_frame("Stopwatch: The Game", 300, 300)

# register event handlers
f.set_draw_handler(draw)
f.add_button("Start", start, 200)
f.add_button("Stop", stop, 200)
f.add_button("Reset", reset, 200)

# start frame
f.start()

# Please remember to review the grading rubric
