import tkinter as tk


class ChangeableOptionMenu(tk.OptionMenu):
    def __init__(self, master, variable, value, *values, **kwargs):
        self._command = kwargs.get("command")
        self.variable = variable
        tk.OptionMenu.__init__(self, master, variable, value, *values, **kwargs)

    def add_option(self, label):
        self["menu"].add_command(label=label, command=tk._setit(self.variable, label, self._command))
