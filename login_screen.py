from kivy.uix.screenmanager import Screen
from network import login

class LoginScreen(Screen):
    def login(self):
        """Authenticate the user and handle login."""
        username = self.ids.username_input.text.strip()
        password = self.ids.password_input.text.strip()

        if not username or not password:
            self.ids.message_label.text = "Please enter both username and password."
            return

        success, response = login(username, password)
        if success:
            # Set the username in the home screen
            self.manager.get_screen("home").set_username(username)
            self.manager.current = "home"  # Navigate to report incident screen
        else:
            # Display error message if login fails
            self.ids.message_label.text = response  # Show the error message
