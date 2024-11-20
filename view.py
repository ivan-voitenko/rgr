class View:
    def show_menu(self):
        self.show_message("\nМеню:")
        self.show_message("1. Додати рядок")
        self.show_message('2. Генерувати рандомізовані дані')
        self.show_message("3. Показати таблицю")
        self.show_message("4. Редагувати рядок")
        self.show_message("5. Видалити рядок")
        self.show_message("6. Пошук")
        self.show_message("7. Вихід")
        return input("Виберіть пункт: ")

    def show_tables(self):
        self.show_message("\nТаблиці:")
        self.show_message("1. Students")
        self.show_message("2. Grants")
        self.show_message("3. Scholarships")
        self.show_message("4. Grant applications")
        self.show_message("5. Scholarship applications")
        self.show_message("6. Selection criteria")
        self.show_message("7. Повернутися до меню")
        return input("Оберіть потрібну таблицю: ")

    def show_search(self):
        self.show_message("\nПошук:")
        self.show_message("1. Student grant")
        self.show_message("2. Student scholarship")
        self.show_message("3. Scholarship application")
        return input("Виберіть пункт: ")

    def show_grants(self, grants):
        print("\nGrants:")
        for grant in grants:
            print(f"ID: {grant[0]}, Name: {grant[1]}, Total: {grant[2]}, Organisation: {grant[3]}")

    def show_scholarships(self, scholarships):
        print("\nScholarships:")
        for scholarship in scholarships:
            print(f"ID: {scholarship[0]}, Name: {scholarship[1]}, Total: {scholarship[2]}, Type: {scholarship[3]}")

    def show_students(self, students):
        print("\nStudents:")
        for student in students:
            print(f"ID: {student[0]}, Name: {student[1]}, Birthday: {student[2]}, Faculty: {student[3]}, Age: {student[4]}")

    def show_grant_applications(self, grant_applications):
        print("\nGrant applications:")
        for grant_application in grant_applications:
            print(f"ID: {grant_application[0]}, Status: {grant_application[1]}, Student ID: {grant_application[2]}, Grant ID: {grant_application[3]}")

    def show_scholarship_applications(self, scholarship_applications):
        print("\nScholarship applications:")
        for scholarship_application in scholarship_applications:
            print(f"ID: {scholarship_application[0]}, Status: {scholarship_application[1]}, Student ID: {scholarship_application[2]}, Scholarship ID: {scholarship_application[3]}")

    def show_selection_criteria(self, selection_criterias):
        print("\nGrants:")
        for selection_criteria in selection_criterias:
            print(f"ID: {selection_criteria[0]}, Description: {selection_criteria[1]}, Type: {selection_criteria[2]}, Grant ID: {selection_criteria[3]}, Scholarship ID: {selection_criteria[4]}")

    def get_student_input(self):
        while True:
            name = input("Enter student name: ")
            if name.strip():
                break
            else:
                print("Name cannot be empty.")
        while True:
            birthday = input("Enter student birthday (yyyy-mm-dd): ")
            if birthday.strip():
                break
            else:
                print("Birthday cannot be empty.")
        while True:
            faculty = input("Enter student faculty: ")
            if faculty.strip():
                break
            else:
                print("Faculty cannot be empty.")
        while True:
            try:
                age = int(input("Enter student age: "))
                break
            except ValueError:
                print("Age must be a number.")
        return [name, birthday, faculty, age]

    def get_grant_input(self):
        while True:
            name = input("Enter grant name: ")
            if name.strip():
                break
            else:
                print("Name cannot be empty.")
        while True:
            try:
                total = int(input("Enter grant total: "))
                break
            except ValueError:
                print("Total must be a number.")
        while True:
            organisation = input("Enter grant organisation: ")
            if organisation.strip():
                break
            else:
                print("Organisation cannot be empty.")

        return [name, total, organisation]

    def get_scholarship_input(self):
        while True:
            name = input("Enter scholarship name: ")
            if name.strip():
                break
            else:
                print("Name cannot be empty.")
        while True:
            try:
                total = int(input("Enter scholarship total: "))
                break
            except ValueError:
                print("Total must be a number.")
        while True:
            type = input("Enter scholarship type: ")
            if type.strip():
                break
            else:
                print("Type cannot be empty.")

        return [name, total, type]

    def get_grant_application_input(self):
        while True:
            status = input("Enter grant application status (T/F): ")
            if status.strip() and (status == 'T' or status == 'F'):
                break
            else:
                print("Status cannot be empty.")
        while True:
            try:
                student_id = int(input("Enter grant application student ID: "))
                break
            except ValueError:
                print("Student ID must be a number.")
        while True:
            try:
                grant_id = int(input("Enter grant application grant ID: "))
                break
            except ValueError:
                print("Grant ID must be a number.")

        return [status, student_id, grant_id]

    def get_scholarship_application_input(self):
        while True:
            status = input("Enter scholarship application status (T/F): ")
            if status.strip() and (status == 'T' or status == 'F'):
                break
            else:
                print("Status cannot be empty.")
        while True:
            try:
                student_id = int(input("Enter scholarship application student ID: "))
                break
            except ValueError:
                print("Student ID must be a number.")
        while True:
            try:
                scholarship_id = int(input("Enter scholarship application scholarship ID: "))
                break
            except ValueError:
                print("Scholarship ID must be a number.")

        return [status, student_id, scholarship_id]

    def get_selection_criteria_input(self):
        while True:
            description = input("Enter selection criteria description: ")
            if description.strip():
                break
            else:
                print("Description cannot be empty.")
        while True:
            type = input("Enter selection criteria type: ")
            if type.strip():
                break
            else:
                print("Type cannot be empty.")
        while True:
            try:
                grant_id = int(input("Enter scholarship application grant ID or -1 if this criteria for scholarship: "))
                break
            except ValueError:
                print("Student ID must be a number.")
        if grant_id == -1:
            while True:
                try:
                    scholarship_id = int(input("Enter scholarship application scholarship ID: "))
                    break
                except ValueError:
                    print("Scholarship ID must be a number.")
        else:
            scholarship_id = 0

        return [description, type, grant_id, scholarship_id]

    def get_id(self):
        while True:
            try:
                id = int(input("Enter ID: "))
                break
            except ValueError:
                print("It must be a number.")
        return id

    def show_message(self, message):
        print(message)

    def get_number(self):
        while True:
            try:
                number = int(input("Enter the number: "))
                break
            except ValueError:
                print("It must be a number.")
        return number

    def show_student_grant(self, grants):
        if not grants:
            print("No grants found for the specified student.")
            return

        print("Grants for the student:")
        print(f"{'Grant ID':<10} {'Grant Name':<30} {'Total':<10} {'Organisation':<15}")
        print("-" * 70)
        for grant in grants:
            grant_id, grant_name, total, organisation = grant
            print(f"{grant_id:<10} {grant_name:<30} {total:<10} {organisation:<15}")

    def show_student_scholarship(self, scholarships):
        if not scholarships:
            print("No grants found for the specified student.")
            return

        print("Scholarships for the student:")
        print(f"{'Scholarship ID':<10} {'Scholarship Name':<30} {'Total':<10} {'Type':<15}")
        print("-" * 70)
        for scholarship in scholarships:
            scholarship_id, scholarship_name, total, type = scholarship
            print(f"{scholarship_id:<10} {scholarship_name:<30} {total:<10} {type:<15}")

    def show_scholarship_application(self, applications):
        if not applications:
            print("No grants found for the specified student.")
            return

        print("Scholarships for the student:")
        print(f"{'Scholarship ID':<10} {'Scholarship Name':<30} {'Student ID':<10} {'Scholarship ID':<10}")
        print("-" * 70)
        for application in applications:
            application_id, status, student_id, scholarship_id = application
            print(f"{scholarship_id:<10} {status:<30} {student_id:<10} {scholarship_id:<10}")
