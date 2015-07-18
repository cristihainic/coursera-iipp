# implementation of card game - Memory

import simplegui
import random

first_deck = [1, 2, 3, 4, 5, 6, 7, 8]
second_deck = [1, 2, 3, 4, 5, 6, 7, 8]
memory_deck = first_deck + second_deck


# helper function to initialize globals
def new_game():
    global turns, exposed, state
    
    exposed = [False, False, False, False, False, False, False,
          False, False, False, False, False, False, False,
          False, False]
    turns = 0
    state = 0
    label.set_text("Turns = %r" % turns)
    random.shuffle(memory_deck)
    

def mouseclick(pos):
    global state, first_card_index, second_card_index, turns
    
    clicked = pos[0] // 50
    
    if not exposed[clicked]:
        if state == 0:
            first_card_index = clicked
            exposed[clicked] = True
            state = 1
        elif state == 1:
            second_card_index = clicked
            exposed[clicked] = True
            state = 2
            turns += 1
            label.set_text("Turns = %r" % turns)
        elif state == 2:
            if memory_deck[first_card_index] != memory_deck[second_card_index]:
                exposed[first_card_index], exposed[second_card_index] = False, False
            first_card_index = clicked
            exposed[clicked] = True
            state = 1
                              
# cards are logically 50x100 pixels in size    
def draw(canvas):       
    for i in range(len(memory_deck)):
        if exposed[i]:
            canvas.draw_text(str(memory_deck[i]), [50 * i, 85], 90, "White")   
        elif not exposed[i]:
            canvas.draw_line([25 + 50 * i, 0], [25 + 50 * i, 100], 49, "Green")


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric