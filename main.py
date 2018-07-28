import liblo
from os.path import normpath, basename
from tkinter import *  # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)
from oled import OLED

class Aplicacion():

    def __init__(self):
        root = Tk()
        root.geometry('480x320')
        # root.configure(bg = BG_COLOR)
        root.title('Synth GUI')
        # root.attributes("-fullscreen", True)

        self.oled = OLED(root)
        #self.oled.pack(fill=X)
        self.oled.pack()

        frame = ttk.Frame(root)
        frame.pack(side=BOTTOM, fill=X)

        ttk.Button(frame, text='aux').pack(side=LEFT)
        ttk.Button(frame, text='up').pack(side=LEFT)
        ttk.Button(frame, text='down').pack(side=LEFT)
        ttk.Button(frame, text='sel').pack(side=LEFT)
        ttk.Button(frame, text='quit', command=root.destroy).pack(side=LEFT)

        try:
            # Create server
            server = liblo.ServerThread(4001)

            self.oled.add_osc_methods(server)

            # Register a fallback for unhandled messages
            server.add_method(None, None, self.fallback)

            # Start server
            server.start()
        except liblo.ServerError as err:
            print(err)
            sys.exit()

        root.mainloop()

    def fallback(self, path, args, types, src):
        print("got unknown message '%s' from '%s'" % (path, src.url))
        for a, t in zip(args, types):
            print("argument of type '%s': %s" % (t, a))

def main():
    mi_app = Aplicacion()
    return 0

if __name__ == '__main__':
    main()

