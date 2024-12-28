from kivy.uix.screenmanager import Screen
from kivy.app import App

class HomeScreen(Screen):
    
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.username = ""

    def set_username(self, username):
        """Set the username and update the label in the home screen."""
        self.username = username
        if self.ids.get("username_label"):
            self.ids.username_label.text = f"Welcome, {username}!"
            
    def logout(self):
        """Handle user logout."""
        App.get_running_app().root.current = "login"  # Redirect to the login screen

        # Reset report incident screen
        report_screen = self.manager.get_screen("report")
        report_screen.reset_ui()


    def go_to_report(self):
        """Navigate to the Report Incident screen."""
        self.manager.current = "report"
