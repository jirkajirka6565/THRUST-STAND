import dearpygui.dearpygui as dpg
import time
import collections
import math
import threading

# Create context and viewport
dpg.create_context()
dpg.create_viewport(title='Graphing app', width=1366, height=768)

nsamples = 100

global data_y
global data_x
# Can use collections if you only need the last 100 samples
data_y = collections.deque([0.0, 0.0],maxlen=nsamples)
data_x = collections.deque([0.0, 0.0],maxlen=nsamples)

data_y = [0.0] * nsamples
data_x = [0.0] * nsamples

def position_windows():
    # Get viewport dimensions
    viewport_width = dpg.get_viewport_width()
    viewport_height = dpg.get_viewport_height()

    # Define the size of the windows
    window1_width = 1000
    window1_height = dpg.get_viewport_height()
    window2_width = dpg.get_viewport_width() - window1_width
    window2_height = dpg.get_viewport_height()

    # Set position for the first window
    pos_x_window1 = 0
    pos_y_window1 = 0

    # Position the first window
    dpg.set_item_pos("window1", [pos_x_window1, pos_y_window1])
    dpg.set_item_width("window1", window1_width)
    dpg.set_item_height("window1", window1_height)

    # Position the second window to the right of the first window
    pos_x_window2 = pos_x_window1 + window1_width
    pos_y_window2 = pos_y_window1

    # Ensure the second window fits within the viewport
    if pos_x_window2 + window2_width > viewport_width:
        pos_x_window2 = viewport_width - window2_width

    dpg.set_item_pos("window2", [pos_x_window2, pos_y_window2])
    dpg.set_item_width("window2", window2_width)
    dpg.set_item_height("window2", window2_height)


with dpg.window(label='Thrust stand data', no_resize=True, tag="window1", no_close=True, no_collapse=True, no_move=True, no_title_bar=True):
    dpg.add_text('Graphs:', )
    
    ######################################################
    #Windows for graphs
    with dpg.child_window(label="Child Window", width=900, height=200):
        with dpg.plot(label="Real-Time Data", height=-1, width=-1):
            dpg.add_plot_legend()

        # REQUIRED: create x and y axes, set to auto scale.
            x_axis = dpg.add_plot_axis(dpg.mvXAxis, label='x', tag='x_axis')
            y_axis = dpg.add_plot_axis(dpg.mvYAxis, label='y', tag='y_axis')


        # series belong to a y axis. Note the tag name is used in the update
        # function update_data
            dpg.add_line_series(x=list(data_x),y=list(data_y), 
                            label='Temp', parent='y_axis', 
                            tag='series_tag')

    with dpg.child_window(label="Child Window", width=900, height=200):
        dpg.add_text("This is a graph window.")

    with dpg.child_window(label="Child Window", width=900, height=200):
        dpg.add_text("This is a graph window.")

    with dpg.child_window(label="Child Window", width=900, height=200):
        dpg.add_text("This is a graph window.")

#####################################################
    #window for settings
with dpg.window(label='Settings', tag="window2", no_resize=True, no_close=True, no_collapse=True, no_move=True, no_title_bar=True):
    dpg.add_text('Settings:', )



# Position the windows
position_windows()

# Set the callback to reposition the windows when the viewport is resized
dpg.set_viewport_resize_callback(position_windows)

def update_data():
    sample = 1
    t0 = time.time()
    frequency=1.0
    while True:

        # Get new data sample. Note we need both x and y values
        # if we want a meaningful axis unit.
        t = time.time() - t0
        y = math.sin(2.0 * math.pi * frequency * t)
        data_x.append(t)
        data_y.append(y)
        
        #set the series x and y to the last nsamples
        dpg.set_value('series_tag', [list(data_x[-nsamples:]), list(data_y[-nsamples:])])          
        dpg.fit_axis_data('x_axis')
        dpg.fit_axis_data('y_axis')
        
        time.sleep(0.01)
        sample=sample+1



# Start Dear PyGui
dpg.setup_dearpygui()
dpg.show_viewport()

thread = threading.Thread(target=update_data)
thread.start()

dpg.start_dearpygui()

dpg.destroy_context()