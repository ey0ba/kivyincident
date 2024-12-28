from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from screens import LoginScreen, HomeScreen, ReportIncidentScreen

# Load all the .kv files
Builder.load_file("login.kv")
Builder.load_file("home.kv")
Builder.load_file("report.kv")

class IncidentApp(App):
    def build(self):
        # Initialize the ScreenManager and add screens
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(ReportIncidentScreen(name="report"))

        sm.current = "login"  # Start with the login screen

        return sm

    def logout(self):
        """Handle user logout and redirect to the login screen."""
        self.root.current = "login"  # Redirect to the login screen


if __name__ == "__main__":
    IncidentApp().run()
