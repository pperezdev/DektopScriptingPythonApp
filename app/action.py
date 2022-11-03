import pydirectinput  
import subprocess
import os
from pynput.mouse import Listener
import time

class Action():
    def __init__(self, name, description, fct, args, kwargs, waiting=0.5):
        self.name = name
        self.name_upper = name.upper()
        self.description = description
        self.fct = fct
        self.waiting = waiting
        self.args = args
        self.kwargs = kwargs
    
    def open_app(self, path, application, *args, **kwargs):
        os.chdir(path)
        app_process = subprocess.Popen(application)
    
    def get_mouse_position(self):
        print("POSITIONS MOUSE: ", pydirectinput.position())
        
    def click_button_at_coordinate(self, x, y, *args, **kwargs):
        pydirectinput.moveTo(x, y) 
        pydirectinput.click()
        
    def input_value_at_coordinate(self, x, y, value, *args, **kwargs):
        self.click_button_at_coordinate(x, y)
        pydirectinput.write(value)
        
    def test(self, text, *args, **kwargs):
        print(text)        
        
    def action(self):
        print("--- ACTION ", self.name_upper, " STARTED ---")
        fct = getattr(self, self.fct)
        val = fct(*self.args, **self.kwargs)
        time.sleep(self.waiting)
        print("--- ACTION ", self.name_upper, " IS DONE ---")
        print(" ")
        return val
    
    def on_click(self, x, y, button, pressed):
        print("x:", x)
        print("y:", y)
        print("pressed:", pressed)
        print("button:", button)
    
    def rec(self):
        with Listener(on_click=self.on_click) as listener:
            listener.join()

        