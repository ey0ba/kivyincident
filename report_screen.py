from kivy.uix.screenmanager import Screen
from utils import get_current_datetime, show_popup
from network import fetch_dropdown_data, submit_incident


class ReportIncidentScreen(Screen):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.username = ""  # Initialize username attribute

    def set_username(self, username):
        """Set the username for this screen."""
        self.username = username
        # Optionally display the username in the UI
        if self.ids.get("username_label"):
            self.ids.username_label.text = f"Logged in as: {username}"
            
    dropdown_data = {}

    def on_pre_enter(self):
        """Fetch dropdown data and set default date/time when entering the screen."""
        self.ids.incident_time_input.text = get_current_datetime()
        self.reset_ui()
        self.fetch_dropdown_data()
        
    def reset_ui(self):
        """Reset dropdowns and their headers."""
        self.ids.sex_dropdown.text = "Select Sex"
        self.ids.department_dropdown.text = "Select Department"
        self.ids.suspected_cause_dropdown.text = "Select Suspected Cause"
        self.ids.contributing_factor_dropdown.text = "Select Contributing Factor"
        self.ids.mitigating_factor_dropdown.text = "Select Mitigating Factor"
        self.ids.incident_type_dropdown.text = "Select Incident Type"
        self.ids.incident_outcome_dropdown.text = "Select Incident Outcome"
        self.ids.resulting_action_dropdown.text = "Select Resulting Action"
        self.ids.reporter_role_dropdown.text = "Select Reporter Role"
        self.ids.reporter_department_dropdown.text = "Select Reporter Department"
        self.ids.message_label.text = ""  # Clear feedback messages    

    def clear_fields(self):
        """Clear all input fields and reset dropdowns to their default states, including headers."""
        # Clear text inputs
        self.ids.incident_time_input.text = get_current_datetime()  # Reset to current datetime
        self.ids.age_input.text = ""
        self.ids.cause_other_input.text = ""
        self.ids.contributing_factor_other_input.text = ""
        self.ids.mitigating_factor_other_input.text = ""
        self.ids.reporter_name_input.text = ""
        self.ids.other_opinions_input.text = ""
        self.ids.message_label.text = ""  # Clear any feedback messages

        # Reset dropdown headers
        self.ids.sex_dropdown.text = "Select Sex"
        self.ids.department_dropdown.text = "Select Department"
        self.ids.suspected_cause_dropdown.text = "Select Suspected Cause"
        self.ids.contributing_factor_dropdown.text = "Select Contributing Factor"
        self.ids.mitigating_factor_dropdown.text = "Select Mitigating Factor"
        self.ids.incident_type_dropdown.text = "Select Incident Type"
        self.ids.incident_outcome_dropdown.text = "Select Incident Outcome"
        self.ids.resulting_action_dropdown.text = "Select Resulting Action"
        self.ids.reporter_role_dropdown.text = "Select Reporter Role"
        self.ids.reporter_department_dropdown.text = "Select Reporter Department"

        # Optionally, refresh dropdown values
        self.fetch_dropdown_data()  # Repopulate dropdown values if needed


    def fetch_dropdown_data(self):
        """Fetch dropdown data from the backend."""
        username = self.manager.get_screen("login").ids.username_input.text
        password = self.manager.get_screen("login").ids.password_input.text

        success, data_or_message = fetch_dropdown_data(username, password)
        if success:
            self.dropdown_data = data_or_message
            self.populate_dropdowns()
        else:
            self.ids.message_label.text = data_or_message

    def populate_dropdowns(self):
        """Populate dropdown fields with fetched data."""
        self.ids.sex_dropdown.values = [
            choice[1] for choice in self.dropdown_data.get("sex_choices", [])
        ]
        
        self.ids.department_dropdown.values = [
            item["name"] for item in self.dropdown_data.get("departments", [])
        ]
        self.ids.suspected_cause_dropdown.values = [
            item["name"] for item in self.dropdown_data.get("suspected_causes", [])
        ]
        self.ids.contributing_factor_dropdown.values = [
            item["name"] for item in self.dropdown_data.get("contributing_factors", [])
        ]
        self.ids.mitigating_factor_dropdown.values = [
            item["name"] for item in self.dropdown_data.get("mitigating_factors", [])
        ]
        self.ids.incident_type_dropdown.values = [
            item["name"] for item in self.dropdown_data.get("incident_types", [])
        ]
        self.ids.incident_outcome_dropdown.values = [
            item["name"] for item in self.dropdown_data.get("incident_outcomes", [])
        ]
        self.ids.resulting_action_dropdown.values = [
            item["name"] for item in self.dropdown_data.get("resulting_actions", [])
        ]
        self.ids.reporter_role_dropdown.values = [
            item["name"] for item in self.dropdown_data.get("reporter_roles", [])
        ]
        self.ids.reporter_department_dropdown.values = [
            item["name"] for item in self.dropdown_data.get("departments", [])
        ]

        
    def submit_incident(self):
        """Handle incident submission by sending a POST request to the API."""
        try:
            # Construct the payload
            data = {
            "incident_time": self.ids.incident_time_input.text.strip(),
            "age": int(self.ids.age_input.text) if self.ids.age_input.text.isdigit() else None,
            "sex": self.ids.sex_dropdown.text,
            "incident_locations": self.get_foreign_key_id("department_dropdown", "departments"),
            "suspected_cause": self.get_foreign_key_id("suspected_cause_dropdown", "suspected_causes"),
            "suspected_cause_other": self.ids.cause_other_input.text.strip(),
            "contributing_factor": self.get_foreign_key_id("contributing_factor_dropdown", "contributing_factors"),
            "contributing_factor_other": self.ids.contributing_factor_other_input.text.strip(),
            "mitigating_factor": self.get_foreign_key_id("mitigating_factor_dropdown", "mitigating_factors"),
            "mitigating_factor_other": self.ids.mitigating_factor_other_input.text.strip(),
            "incident_type": self.get_foreign_key_id("incident_type_dropdown", "incident_types"),
            "incident_outcome": self.get_foreign_key_id("incident_outcome_dropdown", "incident_outcomes"),
            "resulting_action": self.get_foreign_key_id("resulting_action_dropdown", "resulting_actions"),
            "reporter_name": self.ids.reporter_name_input.text.strip(),
            "reporter_role": self.get_foreign_key_id("reporter_role_dropdown", "reporter_roles"),
            "reporter_department": self.get_foreign_key_id("department_dropdown", "departments"),
            "other_opinions": self.ids.other_opinions_input.text.strip(),
        }
            
             #Validate required fields
            if not data["age"]:
                self.ids.message_label.text = "Age must be a valid number."
                return

            if data["sex"] not in ["Male", "Female", "Other"]:
                self.ids.message_label.text = "Please select a valid sex."
                return
            
            if not data["incident_locations"]:
                self.ids.message_label.text = "Incident location is required."
                return
            if not data["suspected_cause"]:
                self.ids.message_label.text = "Suspected cause is required."
                return
            if not data["contributing_factor"]:
                self.ids.message_label.text = "Contributing factor is required."
                return
            if not data["mitigating_factor"]:
                self.ids.message_label.text = "Mitigating factor is required."
                return
            if not data["incident_type"]:
                self.ids.message_label.text = "Incident type is required."
                return
            if not data["incident_outcome"]:
                self.ids.message_label.text = "Incident outcome is required."
                return
            if not data["resulting_action"]:
                self.ids.message_label.text = "Resulting action is required."
                return
            if not data["reporter_role"]:
                self.ids.message_label.text = "Reporter role is required."
                return
            if not data["reporter_department"]:
                self.ids.message_label.text = "Reporter department is required."
                return
            
        
           

            # Call the API with the constructed data
            username = self.manager.get_screen("login").ids.username_input.text
            password = self.manager.get_screen("login").ids.password_input.text
            success, message = submit_incident(data, username, password)
            if success:
                show_popup("Incident submitted successfully!")
                self.clear_fields()
            else:
                self.ids.message_label.text = message
                print(f"Submission failed: {message}")

        except Exception as e:
            print(f"Error in submit_incident: {e}")
            self.ids.message_label.text = f"Error: {e}"    
    
        
            
    def get_foreign_key_id(self, dropdown_id, key):
        """Get the selected value's ID from the dropdown data."""
        selected_name = self.ids[dropdown_id].text
        for item in self.dropdown_data.get(key, []):
            if item["name"] == selected_name:
                return item["id"]
        return None
