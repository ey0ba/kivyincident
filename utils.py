from datetime import datetime
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

def get_current_datetime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")



def show_popup(message, title="Success"):
    """Display a popup with a given title and message."""
    layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
    label = Label(text=message, size_hint=(1, 0.8))
    button = Button(text="OK", size_hint=(1, 0.2))
    layout.add_widget(label)
    layout.add_widget(button)
    popup = Popup(title=title, content=layout, size_hint=(0.8, 0.4), auto_dismiss=False)
    button.bind(on_press=popup.dismiss)
    popup.open()


