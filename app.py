import dearpygui.dearpygui as dpg
import time
import collections
import math
import threading
import arduinoSerialConnect
import pandas_excel


# Create context and viewport
dpg.create_context()
dpg.create_viewport(title='Graphing app', width=1366, height=768)

nsamples = 500
################################################################################################
##LC1
global data_y
global data_x
# Can use collections if you only need the last 100 samples
data_y = collections.deque([0.0, 0.0],maxlen=nsamples)
data_x = collections.deque([0.0, 0.0],maxlen=nsamples)

data_y = [0.0] * nsamples
data_x = [0.0] * nsamples
################################################################################################
##LC2
global data_y2
global data_x2
# Can use collections if you only need the last 100 samples
data_y2 = collections.deque([0.0, 0.0],maxlen=nsamples)
data_x2 = collections.deque([0.0, 0.0],maxlen=nsamples)

data_y2 = [0.0] * nsamples
data_x2 = [0.0] * nsamples
################################################################################################
##LC3
global data_y3
global data_x3
# Can use collections if you only need the last 100 samples
data_y3 = collections.deque([0.0, 0.0],maxlen=nsamples)
data_x3 = collections.deque([0.0, 0.0],maxlen=nsamples)

data_y3 = [0.0] * nsamples
data_x3 = [0.0] * nsamples


stop_event = threading.Event()
export_event = threading.Event()

global df

################################################################################################
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

def startPlotting():
    global thread, stop_event
    stop_event.clear()
    thread = threading.Thread(target=update_data)
    thread.start()

def stopPlotting():
    global stop_event
    stop_event.set()

    global data_x, data_y, data_x2, data_y2, data_y3, data_x3
    # Reset the data to empty lists or initial values
    data_x = [0.0] * nsamples
    data_y = [0.0] * nsamples
    data_x2 = [0.0] * nsamples
    data_y2 = [0.0] * nsamples
    data_y3 = [0.0] * nsamples
    data_x3 = [0.0] * nsamples

    # Update the plot with cleared data
    dpg.set_value('series_tag', [list(data_x), list(data_y)])
    dpg.fit_axis_data('x_axis')
    dpg.fit_axis_data('y_axis')
    dpg.set_value('series_tag2', [list(data_x2), list(data_y2)])
    dpg.fit_axis_data('x_axis2')
    dpg.fit_axis_data('y_axis2') 
    dpg.set_value('series_tag3', [list(data_x3), list(data_y3)])
    dpg.fit_axis_data('x_axis3')
    dpg.fit_axis_data('y_axis3')             
        

def calibrate_zero():
    arduinoSerialConnect.calibrateLoadCellZero(dpg.get_value("calibration_listbox"))


def calibrate_input():
    
    arduinoSerialConnect.calibrateLoadCellInput(dpg.get_value("calibration_listbox"), dpg.get_value("calibration"))

def startExporting():
    global export_event, df
    df = pandas_excel.createDataFrame()
    if (not export_event.is_set()): export_event.set()

def stopExporting():
    global export_event, df
    export_event.clear()
    pandas_excel.saveDataFrame(df, dpg.get_value("excel_name")+".xlsx")

################################################################################################
with dpg.window(label='Thrust stand data', no_resize=True, tag="window1", no_close=True, no_collapse=True, no_move=True, no_title_bar=True):
    dpg.add_text('Graphs:', )
    
    ######################################################
    #Windows for graphs
    ##LC1
    with dpg.child_window(label="Child Window", width=900, height=200):
        with dpg.plot(label="LC-1 Data", height=-1, width=-1):
            dpg.add_plot_legend()

        # REQUIRED: create x and y axes, set to auto scale.
            x_axis = dpg.add_plot_axis(dpg.mvXAxis, label='x', tag='x_axis')
            y_axis = dpg.add_plot_axis(dpg.mvYAxis, label='y', tag='y_axis')


        # series belong to a y axis. Note the tag name is used in the update
        # function update_data
            dpg.add_line_series(x=list(data_x),y=list(data_y), 
                            parent='y_axis', 
                            tag='series_tag')
    dpg.add_text("Data: ", tag="data1_tag")
################################################################################################
    ##LC2
    with dpg.child_window(label="Child Window", width=900, height=200):
        with dpg.plot(label="LC-2 Data", height=-1, width=-1):
            dpg.add_plot_legend()

        # REQUIRED: create x and y axes, set to auto scale.
            x_axis2 = dpg.add_plot_axis(dpg.mvXAxis, label='x', tag='x_axis2')
            y_axis2 = dpg.add_plot_axis(dpg.mvYAxis, label='y', tag='y_axis2')


        # series belong to a y axis. Note the tag name is used in the update
        # function update_data
            dpg.add_line_series(x=list(data_x2),y=list(data_y2), 
                             parent='y_axis2', 
                            tag='series_tag2')
    dpg.add_text("Data: ", tag="data2_tag")
################################################################################################
    ##LC3
    with dpg.child_window(label="Child Window", width=900, height=200):
        with dpg.plot(label="LC-3 Data", height=-1, width=-1):
            dpg.add_plot_legend()

        # REQUIRED: create x and y axes, set to auto scale.
            x_axis3 = dpg.add_plot_axis(dpg.mvXAxis, label='x', tag='x_axis3')
            y_axis3 = dpg.add_plot_axis(dpg.mvYAxis, label='y', tag='y_axis3')


        # series belong to a y axis. Note the tag name is used in the update
        # function update_data
            dpg.add_line_series(x=list(data_x3),y=list(data_y3), 
                             parent='y_axis3', 
                            tag='series_tag3')
    dpg.add_text("Data: ", tag="data3_tag")

    with dpg.child_window(label="Child Window", width=900, height=200):
        dpg.add_text("This is a graph window.")

#####################################################
    #window for settings

def arduino_Connect():
    arduinoSerialConnect.Connect()
    time.sleep(1)
    if(arduinoSerialConnect.arduino_connected == True):
        dpg.set_value("arduino_status_tag", "arduino status: Connected")
    else:
        dpg.set_value("arduino_status_tag", "arduino status: Not connected")


with dpg.window(label='Settings', tag="window2", no_resize=True, no_close=True, no_collapse=True, no_move=True, no_title_bar=True):
    dpg.add_text('Settings:', )
    dpg.add_button(label="Connect to arduino", callback=arduino_Connect, width=-1, height=50)
    dpg.add_text("arduino status: ", tag="arduino_status_tag")
    dpg.add_spacer(height=10)
    dpg.add_button(label="start plotting", callback=startPlotting, width=-1, height=50)
    dpg.add_spacer(height=10)
    dpg.add_button(label="stop plotting", width=-1, height=50, callback=stopPlotting)
    dpg.add_spacer(height=10)
    dpg.add_text("Calibration:")
    dpg.add_input_int( tag="calibration", default_value=100, width=320)
    dpg.add_listbox(items=["LC_1", "LC_2", "LC_3"], tag="calibration_listbox", width=320)
    dpg.add_button(label="calibrate zero", width=-1, height=50, tag="calibrate_zero_button", callback=calibrate_zero)
    dpg.add_button(label="calibrate input value", width=-1, height=50, tag="calibrate_input_button", callback=calibrate_input)
    dpg.add_spacer(height=20)
    dpg.add_text("Excel save file name:")
    dpg.add_input_text(tag="excel_name", default_value="test", width=320)
    dpg.add_button(label="Start exporting", width=-1, height=50, tag="start_exporting_button", callback=startExporting)
    dpg.add_spacer(height=10)
    dpg.add_button(label="Stop exporting", width=-1, height=50, tag="stop_exporting_button", callback=stopExporting)
 

# Position the windows
position_windows()

# Set the callback to reposition the windows when the viewport is resized
dpg.set_viewport_resize_callback(position_windows)

################################################################################################
################################################################################################
################################################################################################
##   Update function   ##
def update_data():

    sample = 1
    t0 = time.time()
    frequency=1.0
    while not stop_event.is_set():

        try:
            LC_1, LC_2, LC_3 = arduinoSerialConnect.decodeSerialData(arduinoSerialConnect.getSerialData())
            try:
                LC_1f = float(LC_1)
                LC_2f = float(LC_2)
                LC_3f = float(LC_3)
            except:
                LC_1f = 0
                LC_2f = 0
                LC_3f = 0
            #print(LC_1," ", LC_2," ",LC_3)
        except:
            print("No data")
            LC_1f = 0
            LC_2f = 0
            LC_3f = 0
            LC_1 = "0"
            LC_2 = "0"
            LC_3 = "0"

        # Get new data sample. Note we need both x and y values
        # if we want a meaningful axis unit.
        y = LC_1f
        y2 = LC_2f
        y3 = LC_3f
        t = time.time() - t0
        #y = math.sin(5.0 * math.pi * frequency * t + 600) ####TESTING SIN FUNCTION
        ################################################################################################
        ##LC1
        data_x.append(t)
        data_y.append(y)
        
        #set the series x and y to the last nsamples
        dpg.set_value('series_tag', [list(data_x[-nsamples:]), list(data_y[-nsamples:])])          
        dpg.fit_axis_data('x_axis')
        dpg.fit_axis_data('y_axis')
        dpg.set_value("data1_tag", "Data: " + LC_1) #show data under graph
        ################################################################################################
        ##LC2
        data_x2.append(t)
        data_y2.append(y2)
        
        #set the series x and y to the last nsamples
        dpg.set_value('series_tag2', [list(data_x2[-nsamples:]), list(data_y2[-nsamples:])])          
        dpg.fit_axis_data('x_axis2')
        dpg.fit_axis_data('y_axis2')
        dpg.set_value("data2_tag", "Data: " + LC_2) #show data under graph
        ################################################################################################
        ##LC3
        data_x3.append(t)
        data_y3.append(y3)
        
        #set the series x and y to the last nsamples
        dpg.set_value('series_tag3', [list(data_x3[-nsamples:]), list(data_y3[-nsamples:])])          
        dpg.fit_axis_data('x_axis3')
        dpg.fit_axis_data('y_axis3')
        dpg.set_value("data3_tag", "Data: " + LC_3) #show data under graph
        ################################################################################################
        ################################################################################################
        ################################################################################################
        ##Exporting:
        if(export_event.is_set()):
            #try:
            global df
            df = pandas_excel.appendDataFrame(df, LC_1f, LC_2f, LC_3f, t)
                #pandas_excel.saveDataFrame(df, dpg.get_value("excel_name")+".xlsx")
            #except:
                #df = pandas_excel.createDataFrame()
                #time.sleep(0.01)
                #df = pandas_excel.appendDataFrame(df, LC_1f, LC_2f, LC_3f, t)
                #pandas_excel.saveDataFrame(df, dpg.get_value("excel_name")+".xlsx")

        ################################################################################################

        time.sleep(0.01)
        sample=sample+1

        


# Start Dear PyGui
dpg.setup_dearpygui()
dpg.show_viewport()


dpg.start_dearpygui()

dpg.destroy_context()