from Motion_Detector import df
from bokeh.plotting import figure , show, output_file
from bokeh.models import HoverTool, ColumnDataSource

#Convert df to String

df["Start_string"] = df["Start"].dt.strftime("%Y-%M-%D %H:%M:%S")
df["End_string"] = df["End"].dt.strftime("%Y-%M-%D %H:%M:%S")


# Collecting the data Source

cds = ColumnDataSource(df)


# Creating the Graph

p = figure(x_axis_type = "datetime" , sizing_mode='scale_width', height = 100 , width = 500 , title = "Motion Graph")
p.yaxis.minor_tick_line_color = None
p.ygrid[0].ticker.desired_num_ticks = 1
p.title.text_font_size = '20pt'
p.title.align = 'center'

#Creating the Hover Effect Over the Graph

hover = HoverTool(tooltips = [("Start", "@Start_string"), ("End", "@End_string")])
p.add_tools(hover)


q= p.quad(left = "Start", right = "End", bottom = 0 , top = 1, color = "green", source = cds)
output_file("Graph2.html")
show(p)