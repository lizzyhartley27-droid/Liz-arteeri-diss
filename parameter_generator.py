#!/usr/bin/env python3
from tkinter import *
from tkinter.ttk import Notebook


# Execute to init the GUI for generating both parameters.py and parameters_species_repository.py
#
# Buttons at the end of the GUI to i) generate the .py files from the selected settings, and ii) run main.py.

class ParameterGeneratorTab:
    def __init__(self, tab):
        self.window = tab
        self.row = 0
        self.column = 0
        self.background = "#363636"
        self.window.configure(bg=self.background)

class ChildWindow:
    def __init__(self, parent_obj):
        self.window = Frame(parent_obj.window)  # TODO: why was "Frame() necessary here?
        self.background = "#474747"
        self.window.configure(background=self.background, borderwidth=2, relief="ridge")
        self.parent_obj = parent_obj
        self.row = 0
        self.column = 0

def update_row(self):
    self.row += 1
    if hasattr(self, "parent_obj"):
        update_row(self.parent_obj)

def next_list(obj, label_text, option_list, row_value=None, col_value=None):
    if row_value is None:
        row_value = obj.row
    if col_value is None:
        col_value = obj.column
    window = obj.window
    l = Label(window, text=label_text, background=obj.background)
    l.grid(row=row_value, column=col_value)
    variable = StringVar(window)
    variable.set(option_list[0])  # default is True
    m = OptionMenu(window, variable, *option_list)
    m.grid(row=row_value, column=col_value+1)
    update_row(obj)
    return variable.get()

def next_entry(obj, label_text, row_value=None, col_value=None, default_value=""):
    if row_value is None:
        row_value = obj.row
    if col_value is None:
        col_value = obj.column
    window = obj.window
    l = Label(window, text=label_text, background=obj.background)
    l.grid(row=row_value, column=col_value)
    m = Entry(window)
    m.insert(END, default_value)
    m.grid(row=row_value, column=col_value+1)
    update_row(obj)
    return l, m

def next_checkbutton(obj, label_text, row_value=None, col_value=None):
    if row_value is None:
        row_value = obj.row
    if col_value is None:
        col_value = obj.column
    window = obj.window
    var = IntVar()
    l = Checkbutton(window, text=label_text, variable=var, background=obj.background)
    l.grid(row=row_value, column=col_value)
    update_row(obj)
    return l, var

def next_spinbox(obj, label_text, upper_limit, row_value=None, col_value=None):
    if row_value is None:
        row_value = obj.row
    if col_value is None:
        col_value = obj.column
    window = obj.window
    l = Label(window, text=label_text, background=obj.background)
    l.grid(row=row_value, column=col_value)
    m = Spinbox(window, from_=0, to=upper_limit)
    m.grid(row=row_value, column=col_value+1)
    update_row(obj)
    return m.get()

def update_tab(event, obj, attr_name, base_obj, is_activate, widget_type, widget_text_list):
    if hasattr(obj, attr_name):
        existing_list = getattr(obj, attr_name)
        for element in existing_list:
            for sub_element in element:
                try:
                    sub_element.destroy()
                except AttributeError:
                    pass
    existing_list = []
    if is_activate:
        for _, element in enumerate(base_obj.get()):
            widget_text = f"{widget_text_list[0]} {attr_name} {widget_text_list[1]} {element} {widget_text_list[2]}"
            if widget_type == "checkbox":
                temp_l, temp_m = next_checkbutton(obj=obj, label_text=widget_text)
            elif widget_type == "entry":
                temp_l, temp_m = next_entry(obj=obj, label_text=widget_text, col_value=2)
            else:
                raise TypeError("Unrecognized widget type")
            existing_list.append((temp_l, temp_m))
    setattr(obj, attr_name, existing_list)

def prepare_main_tab(tab):
    main_tab = ParameterGeneratorTab(tab)

    next_list(main_tab, "Is simulation?", ["True", "False"])
    next_spinbox(main_tab, "Number of transient steps:", 10000000)
    next_spinbox(main_tab, "Number of recorded time steps:", 10000000)
    next_spinbox(main_tab, "Number of patches:", 10000000)
    next_list(main_tab, "Model time type:", ["discrete", "continuous"])
    next_entry(main_tab, "Euler step:")
    next_spinbox(main_tab, "Steps to days:", 10000000)

    # Ecological priorities:
    f1 = ChildWindow(parent_obj=main_tab)
    f1.window.grid(row=main_tab.row, column=0, columnspan=2)
    f1a = Label(f1.window, text="Eco-priorities:", background=f1.background)
    f1a.grid(row=0, column=0)
    next_spinbox(f1, "Growth:", 3, col_value=1)
    next_spinbox(f1, "Foraging:", 3, col_value=1)
    next_spinbox(f1, "Dispersal:", 3, col_value=1)
    next_spinbox(f1, "Direct Impact:", 3, col_value=1)

    next_spinbox(main_tab, "Max centrality measure:", 10000000)
    next_spinbox(main_tab, "Assumed max path length:", 10000000)
    next_list(main_tab, "Is save adjacency variables?", ["True", "False"])
    next_list(main_tab, "Is load adjacency variables?", ["True", "False"])
    species_obj = next_entry(main_tab, "Species types (enter as a comma-separated list):")[1]
    habitat_obj = next_entry(main_tab, "Habitat types (enter as a comma-separated list):")[1]

    # generated spec - feeding
    f2 = ChildWindow(parent_obj=main_tab)
    f2.window.grid(row=main_tab.row, column=0, columnspan=3)
    f2a = Label(f2.window, text="Generated spec:", background=f2.background)
    f2a.grid(row=0, column=0)
    f2b = Label(f2.window, text="Feeding:", background=f2.background)
    f2b.grid(row=0, column=1)
    next_list(f2, "Is species scores specified?", ["True", "False"], col_value=2)
    next_entry(f2, "Min score:", col_value=2, default_value="None")
    next_entry(f2, "Max score:", col_value=2, default_value="None")
    generator_window.bind_all('<Return>', lambda event: update_tab(
        event=event, obj=f2, attr_name="feeding_scores", base_obj=habitat_obj, is_activate=True, widget_type="entry",
        widget_text_list=["Species", "for habitat", " (enter as comma-separated list):"]), add="+")


    # generated spec - traversal
    f3 = ChildWindow(parent_obj=main_tab)
    f3.window.grid(row=main_tab.row, column=0, columnspan=3)
    f3a = Label(f3.window, text="Generated spec:", background=f3.background)
    f3a.grid(row=0, column=0)
    f3b = Label(f3.window, text="Traversal:", background=f3.background)
    f3b.grid(row=f3.row, column=1)
    next_list(f3, "Is species scores specified?", ["True", "False"], col_value=2)
    next_entry(f3, "Min score:", col_value=2, default_value="None")
    next_entry(f3, "Max score:", col_value=2, default_value="None")
    generator_window.bind_all('<Return>', lambda event: update_tab(
        event=event, obj=f3, attr_name="traversal_scores", base_obj=habitat_obj, is_activate=True, widget_type="entry",
        widget_text_list=["Species", " for habitat", "(enter as comma-separated list):"]), add="+")

    # Initial generation
    generator_window.bind_all('<Return>', lambda event: update_tab(
        event=event, obj=main_tab, attr_name="species", base_obj=species_obj, is_activate=True, widget_type="checkbox",
        widget_text_list=["Tick to include", "", "in initial generation."]), add="+")
    generator_window.bind_all('<Return>', lambda event: update_tab(
        event=event, obj=main_tab, attr_name="habitat", base_obj=habitat_obj, is_activate=True, widget_type="checkbox",
        widget_text_list=["Tick to include", "", "in initial generation."]), add="+")

    init_prob = next_checkbutton(main_tab, "Set initial habitat probabilities?")[1]

    # produce settings for each habitat probability:
    generator_window.bind_all('<Return>', lambda event: update_tab(
        event=event, obj=main_tab, attr_name="habitat_prob", base_obj=habitat_obj, is_activate=init_prob.get(),
        widget_type="entry", widget_text_list=["", "", "initial probability:"]), add="+")

    next_list(main_tab, "Calculate Hurst exponent?", ["True", "False"])
    next_list(main_tab, "Record vectors of distance metric linear models?", ["True", "False"])

    # Complexity?
    f4 = ChildWindow(parent_obj=main_tab)
    f4.window.grid(row=main_tab.row, column=0, columnspan=3)  # this is what makes the child window appear in the tab!
    f4a = Label(f4.window, text="Complexity analysis:", background=f4.background)
    f4a.grid(row=0, column=0)
    next_spinbox(f4, "Number of cluster sample draws:", 10000, col_value=1)
    next_spinbox(f4, "Number of attempts per cluster sample draw:", 10000, col_value=1)
    next_spinbox(f4, "Maximum delta:", 10000, col_value=1)
    next_list(f4, "Is partition analysis?", ["True", "False"], col_value=1)
    next_spinbox(f4, "Number of evolutionary partitions:", 10000, col_value=1)
    next_spinbox(f4, "Number of regular partitions:", 10000, col_value=1)
    next_entry(f4, "Partition success threshold:", col_value=1)

def prepare_graph_tab(tab):
    graph_tab = ParameterGeneratorTab(tab)
    next_spinbox(graph_tab, "Spatial test set number:", 10000000)
    next_entry(graph_tab, "Spatial description:")
    next_list(graph_tab, "Graph type:", [ "manual", "lattice", "line", "ring", "star", "random",
                                          "small_world", "scale_free", "cluster", "erdos_renyi_random",
                                          "balanced_tree", "power_law_tree", "cliquey_network", "rgg"])
    next_list(graph_tab, "Graph layout:", ["grid", "tree", "space_filling_curve", "spiral",
                                           "cliquey_network", "ring", "star", "rgg"])
    # TODO: adjacency manual specification (True/false and create some kind of matrix input - of checkboxes??? - if yes)

    pass

def create_tab(window):
    # create a (scrollable) canvas
    canvas = Canvas(window)
    canvas.config(scrollregion=canvas.bbox('all'))

    # create a fixed frame
    frame = Frame(canvas)
    frame.pack(expand=1, fill='both')

    # create the scrollbar
    vsb = Scrollbar(window, orient='vertical', command=canvas.yview)
    vsb.pack(side='right', fill='y')

    # configure
    canvas.configure(yscrollcommand=vsb.set, scrollregion=canvas.bbox("all"))
    canvas.create_window((0, 0), window=frame, anchor="nw")
    canvas.pack(side='left', fill='both', expand=1)
    frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))
    canvas.bind_all('<MouseWheel>', lambda event: on_vertical(event, canvas=canvas), add="+")
    return frame

def on_vertical(event, canvas):
    canvas.yview_scroll(-1 * event.delta, 'units')

def onFrameConfigure(canvas):
    # Reset the scroll region to encompass the inner frame
    canvas.configure(scrollregion=canvas.bbox("all"))

generator_window = Tk()
generator_window.geometry("1000x800")
generator_window.title("Arteeri Parameter Generator")

# create the notebook
parameter_tabs = Notebook(generator_window)

# Create the tabs
main_para_tab = Frame(parameter_tabs)
graph_para_tab = Frame(parameter_tabs)
plot_save_para_tab = Frame(parameter_tabs)

# Add them to the window
parameter_tabs.add(main_para_tab, text="Main")
parameter_tabs.add(graph_para_tab, text="Graph")
parameter_tabs.add(plot_save_para_tab, text="Plot")

# Packing to make tabs visible in the notebook widget
parameter_tabs.pack(expand=1, fill="both")

# populate the frame
prepare_main_tab(create_tab(main_para_tab))
prepare_graph_tab(create_tab(graph_para_tab))


# Run the window
generator_window.mainloop()