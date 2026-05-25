#!/usr/bin/env python3

import gi

gi.require_version("Gtk", "4.0")
gi.require_version("WebKit", "6.0")

from gi.repository import Gtk, WebKit

class App(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="io.github.antonsergeev.Astrologion")

    def do_activate(self):
        win = Gtk.ApplicationWindow(application=self)
        win.set_title("Astrologion")
        win.set_default_size(1000, 700)

        web = WebKit.WebView()
        web.load_uri("file:///app/share/astrologion/index.html")

        win.set_child(web)
        win.present()

app = App()
app.run(None)
