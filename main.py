from microbit import *
# import bluetooth
import inkybit

def display_message(message):
    max_params_width = 250
    max_params_height = 122
    border_thickness = 10
    inkybit.draw_rectangle(0, 0, max_params_width, border_thickness, color=inkybit.ACCENT, filled=True)
    inkybit.draw_rectangle(0, border_thickness, max_params_width, max_params_height - 2*border_thickness, color=inkybit.BLACK, filled=True)
    inkybit.draw_rectangle(0, max_params_height - border_thickness, max_params_width, border_thickness, color=inkybit.ACCENT, filled=True)
    
    text_size = inkybit.TEXT_LARGE
    text_height = 20
    line_spacing = 5
    
    words = message.split()
    
    position_y = border_thickness + line_spacing
    position_x = 5
    
    less_x = max_params_width - position_x
    max_line_length = int(less_x/text_height)
    
    lines = []
    i = 0
    
    temp_line_list = []
    
    for word in words:
        temp_line_list.append(word)
        if len(" ".join(temp_line_list)) > max_line_length:
            temp_line_list.pop()
            line = " ".join(temp_line_list)
            lines.append(line)
            temp_line_list = [word]
    
    last_line = " ".join(temp_line_list)
    lines.append(last_line)
    
    for line in lines:
        inkybit.write(line.upper(), position_x, position_y, color=inkybit.WHITE, text_size=text_size)
        position_y += text_height + line_spacing
    
    inkybit.show()

# def bluetooth.on_bluetooth_connected(body):
    #     display_message(body)

display_message("I am a very silly goose")
