import gi
gi.require_version('Gtk', '3.0')
gi.require_version('GtkLayerShell','0.1')
from gi.repository import Gtk, GtkLayerShell, Gdk

class TaskBar(Gtk.Window):
    def __init__(self, pos='left'):
        super().__init__()
        self.GTK = GtkLayerShell
        self.GTK.init_for_window(self)
        self.GTK.auto_exclusive_zone_enable(self)
        self.box = Gtk.Box(spacing=6)
        self.box.set_name("box")
        self.label = Gtk.Label(label="Trial")
        self.label.set_angle(90)
        self.label.set_halign(Gtk.Align.END)
        self.box.add(self.label)
        self.add(self.box)
        self.set_orientation(pos)
        #self.GTK.set_margin(self, self.GTK.Edge.LEFT,10)
        #self.GTK.set_margin(self, self.GTK.Edge.RIGHT,10)
        self.show_all()
        Gtk.main()

    def set_orientation(self, position):
        orientation = {'top': self.GTK.Edge.TOP,
                       'bottom': self.GTK.Edge.BOTTOM,
                       'left': self.GTK.Edge.LEFT,
                       'right': self.GTK.Edge.RIGHT}

        if position not in orientation.keys():
            raise KeyError(f"the value {position} is not accepted for position value. Only the values top, bottom, left, right are accepted")
        
        GtkLayerShell.set_anchor(self, orientation[position], True)
        return f" orientation:{position}"


sample = TaskBar()
