from tkinter import *
import sys
import numpy as np
from changeable_option_menu import ChangeableOptionMenu


class Window:
    def __init__(self, proxy):
        self.proxy = proxy
        window = Tk(className=' Filtering Proxy')
        self.window = window
        window.protocol("WM_DELETE_WINDOW", self.close)
        Frame(window, width=300, height=1, bg='white').grid(column=0, row=0)
        Frame(window, width=200, height=1, bg='white').grid(column=1, row=0)
        Frame(window, width=50, height=1, bg='white').grid(column=2, row=0)
        Frame(window, width=50, height=20, bg='white').grid(column=0, row=4)
        Frame(window, width=50, height=20, bg='white').grid(column=0, row=6)

        self.act_variable = IntVar()
        self.act_variable.trace('w', self._on_activation_change)
        self.act_checkbox = Checkbutton(window, text='Active ?', variable=self.act_variable, onvalue=1, offvalue=0,
                                        height=5, width=10)
        self.act_checkbox.grid(column=1, row=1)

        self.cat_variable = StringVar(window)
        self.cat_variable.trace('w', self._on_category_change)
        cat_id_list = []
        for cat_id, cat in enumerate(self.proxy.webservers_categories[:, 0]):
            cat_id_list.append(self._get_option_name(cat_id, cat))
        if len(cat_id_list) > 0:
            self.cat_variable.set(cat_id_list[0])
        self.cat_list_menu = ChangeableOptionMenu(window, self.cat_variable, *cat_id_list)
        self.cat_list_menu.grid(column=0, row=1)

        self.new_cat_entry = Entry(window, width=20)
        self.new_cat_entry.grid(column=0, row=2)
        Button(window, text='Add Category', command=self._add_category).grid(column=1, row=2)

        self.webserver_list_menu = None
        self._update_webservers_list()

        self.new_ws_entry = Entry(window, width=20)
        self.new_ws_entry.grid(column=0, row=3)
        Button(window, text='Add Web-Server', command=self._add_webserver).grid(column=1, row=3)

    def show(self):
        self.window.mainloop()

    def _on_category_change(self, *ignored_args):
        cat_id = self._cat_id_getter()
        if self.proxy.webservers_categories[cat_id][1]:
            self.act_checkbox.select()
        else:
            self.act_checkbox.deselect()

        self._update_webservers_list()

    def _update_webservers_list(self):
        if self.webserver_list_menu is not None:
            self.webserver_list_menu.grid_remove()

        self.webserver_list_menu = Listbox(self.window)

        for ws_id, ws in enumerate(self.proxy.webservers_categories[self._cat_id_getter(), 2]):
            self.webserver_list_menu.insert(ws_id, ws)
        self.webserver_list_menu.grid(column=0, row=5)

    def _on_activation_change(self, *ignored_args):
        cat_id = self._cat_id_getter()
        self.proxy.webservers_categories[cat_id][1] = int(self.act_variable.get()) != 0
        print(self.proxy.webservers_categories, '\n')

    def _cat_id_getter(self):
        return int(self.cat_variable.get().split('- ')[0]) - 1

    def _add_category(self):
        new_cat_title = self.new_cat_entry.get()
        if len(new_cat_title) == 0:
            return
        self.new_cat_entry.delete(0, len(new_cat_title))
        cat_list = self.proxy.webservers_categories.tolist()
        cat_list.append([new_cat_title, False, []])
        self.proxy.webservers_categories = np.array(cat_list, dtype=object)
        self.cat_list_menu.add_option(self._get_option_name(len(self.proxy.webservers_categories) - 1, new_cat_title))

    def _add_webserver(self):
        self.proxy.webservers_categories[self._cat_id_getter(), 2].append(
            self._webserver_getter(self.new_ws_entry.get()))
        self._update_webservers_list()
        self.new_ws_entry.delete(0, len(self.new_ws_entry.get()))

    @staticmethod
    def _webserver_getter(webserver):
        return webserver

    @staticmethod
    def _get_option_name(o_id, o_name):
        return str(o_id + 1) + '- ' + o_name  # no- title

    def close(self):
        self.proxy.on_exit()
        sys.exit()

