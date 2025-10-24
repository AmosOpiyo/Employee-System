from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class myapp(MDApp):
    def build(self):
        
        return MDLabel(text='Hi',halign='center')
    

myapp().run()
    

