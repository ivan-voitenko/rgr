import time
from model import Model
from view import View


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def run(self):
        while True:
            choice = self.view.show_menu()
            if choice == '7':
                break
            if choice == '6':
                self.process_search_option()
            elif choice in ['1', '2', '3', '4', '5']:
                self.process_menu_choice(choice)
            else:
                self.view.show_message("Wrong choice. Try again.")

    def process_menu_choice(self, choice):
        while True:
            table = self.view.show_tables()
            if table == '7':
                break
            if choice == '1':
                self.process_add_option(table)
            elif choice == '2':
                self.process_add_random_option(table)
            elif choice == '3':
                self.process_view_option(table)
            elif choice == '4':
                self.process_update_option(table)
            elif choice == '5':
                self.process_delete_option(table)

    def process_add_option(self, table):
        if table == '1':
            self.view.show_message("\nAdding student:")
            self.add_student()
        elif table == '2':
            self.view.show_message("\nAdding grant:")
            self.add_grant()
        elif table == '3':
            self.view.show_message("\nAdding scholarship:")
            self.add_scholarship()
        elif table == '4':
            self.view.show_message("\nAdding grant application:")
            self.add_grant_application()
        elif table == '5':
            self.view.show_message("\nAdding scholarship application:")
            self.add_scholarship_application()
        elif table == '6':
            self.view.show_message("\nAdding selection criteria:")
            self.add_selection_criteria()
        else:
            self.view.show_message("Wrong choice. Try again.")

    def process_add_random_option(self, table):
        if table == '1':
            self.view.show_message("\nAdding random students:")
            self.add_random_students()
        elif table == '2':
            self.view.show_message("\nAdding random grants:")
            self.add_random_grants()
        elif table == '3':
            self.view.show_message("\nAdding random scholarships:")
            self.add_random_scholarships()
        elif table == '4':
            self.view.show_message("\nAdding random grant applications:")
            self.add_random_grant_applications()
        elif table == '5':
            self.view.show_message("\nAdding random scholarship applications:")
            self.add_random_scholarship_applications()
        elif table == '6':
            self.view.show_message("\nAdding random selection criterias:")
            self.add_random_selection_criterias()
        else:
            self.view.show_message("Wrong choice. Try again.")

    def process_view_option(self, table):
        if table == '1':
            self.view_students()
        elif table == '2':
            self.view_grants()
        elif table == '3':
            self.view_scholarships()
        elif table == '4':
            self.view_grant_applications()
        elif table == '5':
            self.view_scholarship_applications()
        elif table == '6':
            self.view_selection_criteria()
        else:
            self.view.show_message("Wrong choice. Try again.")

    def process_update_option(self, table):
        if table == '1':
            self.view.show_message("\nUpdating student:")
            self.update_student()
        elif table == '2':
            self.view.show_message("\nUpdating grant:")
            self.update_grant()
        elif table == '3':
            self.view.show_message("\nUpdating scholarship:")
            self.update_scholarship()
        elif table == '4':
            self.view.show_message("\nUpdating grant application:")
            self.update_grant_application()
        elif table == '5':
            self.view.show_message("\nUpdating scholarship application:")
            self.update_scholarship_application()
        elif table == '6':
            self.view.show_message("\nUpdating selection criteria:")
            self.update_selection_criteria()
        else:
            self.view.show_message("Wrong choice. Try again.")

    def process_delete_option(self, table):
        if table == '1':
            self.view.show_message("\nDeleting student:")
            self.delete_student()
        elif table == '2':
            self.view.show_message("\nDeleting grant:")
            self.delete_grant()
        elif table == '3':
            self.view.show_message("\nDeleting scholarship:")
            self.delete_scholarship()
        elif table == '4':
            self.view.show_message("\nDeleting grant application:")
            self.delete_grant_application()
        elif table == '5':
            self.view.show_message("\nDeleting scholarship application:")
            self.delete_scholarship_application()
        elif table == '6':
            self.view.show_message("\nDeleting selection criteria:")
            self.delete_selection_criteria()
        else:
            self.view.show_message("Wrong choice. Try again.")

    # Functions to add data to each table
    def add_student(self):
        try:
            lst = self.view.get_student_input()
            self.model.add_student(lst[0], lst[1], lst[2], lst[3])
            self.view.show_message("Student added successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def add_grant(self):
        try:
            lst = self.view.get_grant_input()
            self.model.add_grant(lst[0], lst[1], lst[2])
            self.view.show_message("Grant added successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def add_scholarship(self):
        try:
            lst = self.view.get_scholarship_input()
            self.model.add_scholarship(lst[0], lst[1], lst[2])
            self.view.show_message("Scholarship added successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def add_grant_application(self):
        try:
            lst = self.view.get_grant_application_input()
            self.model.add_grant_application(lst[0], lst[1], lst[2])
            self.view.show_message("Grant application added successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def add_scholarship_application(self):
        try:
            lst = self.view.get_scholarship_application_input()
            self.model.add_scholarship_application(lst[0], lst[1], lst[2])
            self.view.show_message("Scholarship application added successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def add_selection_criteria(self):
        try:
            lst = self.view.get_selection_criteria_input()
            self.model.add_selection_criteria(lst[0], lst[1], lst[2], lst[3])
            self.view.show_message("Selection criteria added successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    # Random data generation
    def add_random_students(self):
        number = self.view.get_number()
        self.model.generate_random_students(number)
        self.view.show_message("Random students added successfully!")

    def add_random_grants(self):
        number = self.view.get_number()
        self.model.generate_random_grants(number)
        self.view.show_message("Random grants added successfully!")

    def add_random_scholarships(self):
        number = self.view.get_number()
        self.model.generate_random_scholarships(number)
        self.view.show_message("Random scholarships added successfully!")

    def add_random_grant_applications(self):
        number = self.view.get_number()
        self.model.generate_random_grant_applications(number)
        self.view.show_message("Random grant applications added successfully!")

    def add_random_scholarship_applications(self):
        number = self.view.get_number()
        self.model.generate_random_scholarship_applications(number)
        self.view.show_message("Random scholarship applications added successfully!")

    def add_random_selection_criterias(self):
        number = self.view.get_number()
        self.model.generate_random_selection_criterias(number)
        self.view.show_message("Random selection criterias added successfully!")

    # View data from each table
    def view_students(self):
        students = self.model.get_all_students()
        self.view.show_students(students)

    def view_grants(self):
        grants = self.model.get_all_grants()
        self.view.show_grants(grants)

    def view_scholarships(self):
        scholarships = self.model.get_all_scholarships()
        self.view.show_scholarships(scholarships)

    def view_grant_applications(self):
        grant_applications = self.model.get_all_grant_applications()
        self.view.show_grant_applications(grant_applications)

    def view_scholarship_applications(self):
        scholarship_applications = self.model.get_all_scholarship_applications()
        self.view.show_scholarship_applications(scholarship_applications)

    def view_selection_criteria(self):
        selection_criteria = self.model.get_all_selection_criterias()
        self.view.show_selection_criteria(selection_criteria)

    # Update functions
    def update_student(self):
        try:
            sid = self.view.get_id()
            lst = self.view.get_student_input()
            self.model.update_student(lst[0], lst[1], lst[2], lst[3], sid)
            self.view.show_message("Customer updated successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def update_grant(self):
        try:
            gid = self.view.get_id()
            lst = self.view.get_grant_input()
            self.model.update_grant(lst[0], lst[1], lst[2], gid)
            self.view.show_message("Grant updated successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def update_scholarship(self):
        try:
            sid = self.view.get_id()
            lst = self.view.get_scholarship_input()
            self.model.update_scholarship(lst[0], lst[1], lst[2], sid)
            self.view.show_message("Scholarship updated successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def update_scholarship_application(self):
        try:
            aid = self.view.get_id()
            lst = self.view.get_scholarship_application_input()
            self.model.update_scholarship_application(lst[0], lst[1], lst[2], aid)
            self.view.show_message("Scholarship application updated successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def update_grant_application(self):
        try:
            aid = self.view.get_id()
            lst = self.view.get_grant_application_input()
            self.model.update_grant_application(lst[0], lst[1], lst[2], aid)
            self.view.show_message("Grant application updated successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def update_selection_criteria(self):
        try:
            cid = self.view.get_id()
            lst = self.view.get_selection_criteria_input()
            self.model.update_selection_criteria(lst[0], lst[1], lst[2], lst[3], cid)
            self.view.show_message("Selection criteria updated successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    # Delete functions
    def delete_student(self):
        sid = self.view.get_id()
        self.model.delete_student(sid)
        self.view.show_message("Student deleted successfully!")

    def delete_scholarship(self):
        sid = self.view.get_id()
        self.model.delete_scholarship(sid)
        self.view.show_message("Scholarship deleted successfully!")

    def delete_grant(self):
        gid = self.view.get_id()
        self.model.delete_grant(gid)
        self.view.show_message("Grant deleted successfully!")

    def delete_grant_application(self):
        aid = self.view.get_id()
        self.model.delete_grant_application(aid)
        self.view.show_message("Grant application deleted successfully!")

    def delete_scholarship_application(self):
        aid = self.view.get_id()
        self.model.delete_scholarship_application(aid)
        self.view.show_message("Scholarship application deleted successfully!")

    def delete_selection_criteria(self):
        cid = self.view.get_id()
        self.model.delete_selection_criteria(cid)
        self.view.show_message("Selection criteria deleted successfully!")

    # Search functions
    def process_search_option(self):
        option = self.view.show_search()
        start_time = time.time()

        if option == '1':
            self.show_student_grant()
        elif option == '2':
            self.show_student_scholarship()
        elif option == '3':
            self.show_scholarship_application()
        else:
            self.view.show_message("Invalid choice, returning to main menu.")
            return

        elapsed_time = (time.time() - start_time) * 1000
        print(f"Час виконання: {elapsed_time:.2f} мс")

    def show_student_grant(self):
        student_id = self.view.get_id()
        grants = self.model.get_student_grants(student_id)
        self.view.show_student_grant(grants)

    def show_student_scholarship(self):
        student_id = self.view.get_id()
        scholarships = self.model.get_student_scholarship(student_id)
        self.view.show_student_scholarship(scholarships)

    def show_scholarship_application(self):
        scholarship_id = self.view.get_id()
        applications = self.model.get_scholarship_application(scholarship_id)
        self.view.show_scholarship_application(applications)
