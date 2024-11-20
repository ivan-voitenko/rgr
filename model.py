import psycopg2


class Model:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname='postgres',
            user='postgres',
            password='12345',
            host='127.0.0.1',
            port=8080
        )

    # Student table methods
    def add_student(self, name, birthday, faculty, age):
        c = self.conn.cursor()
        c.execute('INSERT INTO "students" ("name", "birthday", "faculty", "age") VALUES (%s, %s, %s, %s)',
                  (name, birthday, faculty, age))
        self.conn.commit()

    def generate_random_students(self, number):
        c = self.conn.cursor()
        c.execute("""
            WITH random_names AS (
                SELECT unnest(ARRAY['Ivan', 'Oleg', 'Olena', 'Sofia', 'Andriy']) AS name,
                       unnest(ARRAY['FPM', 'RTF', 'FBMI', 'IXF', 'PBF']) AS faculty
            )
            INSERT INTO "students" (name, birthday, faculty, age)
            SELECT
                (SELECT name FROM random_names ORDER BY random() LIMIT 1) as name,
                current_date - floor(random() * 365)::int AS birthday,
                (SELECT faculty FROM random_names ORDER BY random() LIMIT 1) AS faculty,
                floor(random() * 70 + 10)::int AS age
            FROM generate_series(1, %s) AS s(i);
        """, (number,))
        self.conn.commit()

    def get_all_students(self):
        with self.conn.cursor() as cursor:
            cursor.execute('SELECT * FROM "students" ORDER BY id ASC')
            return cursor.fetchall()

    def update_student(self, name, birthday, faculty, age, sid):
        c = self.conn.cursor()
        c.execute('UPDATE "students" SET "name"=%s, "birthday"=%s, "faculty"=%s, "age"=%s WHERE "id"=%s',
                  (name, birthday, faculty, age, sid))
        self.conn.commit()

    def delete_student(self, sid):
        c = self.conn.cursor()
        c.execute('DELETE FROM "students" WHERE "id"=%s', (sid,))
        self.conn.commit()

    # Grants table methods
    def add_grant(self, name, total, organisation):
        c = self.conn.cursor()
        c.execute('INSERT INTO "grants" ("name", "total", "organisation") VALUES (%s, %s, %s)',
                  (name, total, organisation))
        self.conn.commit()

    def generate_random_grants(self, number):
        c = self.conn.cursor()
        c.execute("""
            WITH names AS (
                SELECT unnest(ARRAY['Grant 1', 'Grant 2', 'Grant 3', 'Grant 4', 'Grant 5']) AS name,
                       unnest(ARRAY['Org 1', 'Org 2', 'Org 3', 'Org 4', 'Org 5']) AS organisation
            )
            INSERT INTO "grants" (name, total, organisation)
            SELECT
                (SELECT name FROM names ORDER BY random() LIMIT 1) AS name,
                floor(random() * 5000 + 50)::float AS total,
                (SELECT organisation FROM names ORDER BY random() LIMIT 1) AS organisation
            FROM generate_series(1, %s) AS s(i);
        """, (number,))
        self.conn.commit()

    def get_all_grants(self):
        with self.conn.cursor() as cursor:
            cursor.execute('SELECT * FROM "grants" ORDER BY id ASC')
            return cursor.fetchall()

    def update_grant(self, name, total, organisation, gid):
        c = self.conn.cursor()
        c.execute('UPDATE "grants" SET "name"=%s, "total"=%s, "organisation"=%s WHERE "id"=%s',
                  (name, total, organisation, gid))
        self.conn.commit()

    def delete_grant(self, gid):
        c = self.conn.cursor()
        c.execute('DELETE FROM "grants" WHERE "id"=%s', (gid,))
        self.conn.commit()

    # Scholarships table methods
    def add_scholarship(self, name, total, type):
        c = self.conn.cursor()
        c.execute('INSERT INTO "scholarships" ("name", "total", "type") VALUES (%s, %s, %s)',
                  (name, total, type))
        self.conn.commit()

    def generate_random_scholarships(self, number):
        c = self.conn.cursor()
        c.execute("""
            WITH names AS (
                SELECT unnest(ARRAY['Scholarship 1', 'Scholarship 2', 'Scholarship 3', 'Scholarship 4', 'Scholarship 5']) AS name,
                       unnest(ARRAY['Social', 'Government', 'President']) AS type
            )
            INSERT INTO "scholarships" (name, total, type)
            SELECT
                (SELECT name FROM names ORDER BY random() LIMIT 1) AS name,
                floor(random() * 5000 + 50)::float AS total,
                (SELECT type FROM names ORDER BY random() LIMIT 1) AS type
            FROM generate_series(1, %s) AS s(i);
        """, (number,))
        self.conn.commit()

    def get_all_scholarships(self):
        with self.conn.cursor() as cursor:
            cursor.execute('SELECT * FROM "scholarships" ORDER BY id ASC')
            return cursor.fetchall()

    def update_scholarship(self, name, total, type, sid):
        c = self.conn.cursor()
        c.execute('UPDATE "scholarships" SET "name"=%s, "total"=%s, "type"=%s WHERE "id"=%s',
                  (name, total, type, sid))
        self.conn.commit()

    def delete_scholarship(self, sid):
        c = self.conn.cursor()
        c.execute('DELETE FROM "scholarships" WHERE "id"=%s', (sid,))
        self.conn.commit()

    # grant_application table methods
    def add_grant_application(self, status, student_id, grant_id):
        c = self.conn.cursor()
        c.execute('INSERT INTO "grant_application" ("status", "student_id", "grant_id") VALUES (%s, %s, %s)',
                  (status, student_id, grant_id))
        self.conn.commit()

    def generate_random_grant_applications(self, number):
        c = self.conn.cursor()
        c.execute("""
            INSERT INTO "grant_application" (status, student_id, grant_id)
            SELECT
                (floor(random() * 2)::int)::bool AS status,
                floor(random() * (SELECT COUNT(*) FROM students) + 1)::int AS student_id,
                floor(random() * (SELECT COUNT(*) FROM grants) + 1)::int AS grant_id
            FROM generate_series(1, %s) AS s(i);
        """, (number,))
        self.conn.commit()

    def get_all_grant_applications(self):
        with self.conn.cursor() as cursor:
            cursor.execute('SELECT * FROM "grant_application" ORDER BY id ASC')
            return cursor.fetchall()

    def update_grant_application(self, status, student_id, grant_id, aid):
        c = self.conn.cursor()
        c.execute('UPDATE "grant_application" SET "status"=%s, "student_id"=%s, "grant_id"=%s WHERE "id"=%s',
                  (status, student_id, grant_id, aid))
        self.conn.commit()

    def delete_grant_application(self, aid):
        c = self.conn.cursor()
        c.execute('DELETE FROM "grant_application" WHERE "id"=%s', (aid,))
        self.conn.commit()

    # scholarship_application table methods
    def add_scholarship_application(self, status, student_id, scholarship_id):
        c = self.conn.cursor()
        c.execute('INSERT INTO "scholarship_application" ("status", "student_id", "scholarship_id") VALUES (%s, %s,%s)',
                  (status, student_id, scholarship_id))
        self.conn.commit()

    def generate_random_scholarship_applications(self, number):
        c = self.conn.cursor()
        c.execute("""
            INSERT INTO "scholarship_application" (status, student_id, scholarship_id)
            SELECT
                (floor(random() * 2)::int)::bool AS status,
                floor(random() * (SELECT COUNT(*) FROM students) + 1)::int AS student_id,
                floor(random() * (SELECT COUNT(*) FROM scholarships) + 1)::int AS scholarship_id
            FROM generate_series(1, %s) AS s(i);
        """, (number,))
        self.conn.commit()

    def get_all_scholarship_applications(self):
        with self.conn.cursor() as cursor:
            cursor.execute('SELECT * FROM "scholarship_application" ORDER BY id ASC')
            return cursor.fetchall()

    def update_scholarship_application(self, status, student_id, scholarship_id, aid):
        c = self.conn.cursor()
        c.execute('UPDATE "scholarship_application" SET "status"=%s, "student_id"=%s, "scholarship_id"=%s WHERE "id"=%s',
                  (status, student_id, scholarship_id, aid))
        self.conn.commit()

    def delete_scholarship_application(self, aid):
        c = self.conn.cursor()
        c.execute('DELETE FROM "scholarship_application" WHERE "id"=%s', (aid,))
        self.conn.commit()

    # selection_criteria table methods
    def add_selection_criteria(self, description, type, grant_id, scholarship_id):
        c = self.conn.cursor()
        c.execute('INSERT INTO "selection_criteria" ("description", "type", "grant_id", "scholarship_id") VALUES (%s, %s, %s, %s)',
                  (description, type, grant_id, scholarship_id))
        self.conn.commit()

    def generate_random_selection_criterias(self, number):
        c = self.conn.cursor()
        c.execute("""
            WITH names AS (
                SELECT unnest(ARRAY['description 1', 'description 2', 'description 3', 'description 4', 'Scholarship 5']) AS description,
                       unnest(ARRAY['type 1', 'type 2', 'type 3']) AS type
            )
            INSERT INTO "selection_criteria" (description, type, grant_id, scholarship_id)
            SELECT
                (SELECT description FROM names ORDER BY random() LIMIT 1) AS description,
                (SELECT type FROM names ORDER BY random() LIMIT 1) AS type,
                floor(random() * (SELECT COUNT(*) FROM students) + 1)::int AS grant_id,
                floor(random() * (SELECT COUNT(*) FROM scholarships) + 1)::int AS scholarship_id
            FROM generate_series(1, %s) AS s(i);
        """, (number,))
        self.conn.commit()

    def get_all_selection_criterias(self):
        with self.conn.cursor() as cursor:
            cursor.execute('SELECT * FROM "selection_criteria" ORDER BY id ASC')
            return cursor.fetchall()

    def update_selection_criteria(self, description, type, grant_id, scholarship_id, cid):
        c = self.conn.cursor()
        c.execute('UPDATE "selection_criteria" SET "description"=%s, "type"=%s, "grant_id"=%s, "scholarship_id"=%s WHERE "id"=%s',
                  (description, type, grant_id, scholarship_id, cid))
        self.conn.commit()

    def delete_selection_criteria(self, cid):
        c = self.conn.cursor()
        c.execute('DELETE FROM "selection_criteria" WHERE "id"=%s', (cid,))
        self.conn.commit()

    # search table methods
    def get_student_grants(self, student_id):
        c = self.conn.cursor()
        query = """
            SELECT grants.id, grants.name, grants.total, grants.organisation FROM grants
            JOIN grant_application ON grants.id = grant_application.grant_id 
            WHERE grant_application.student_id = %s
            ORDER BY grant_application.id DESC;
        """
        c.execute(query, (student_id,))
        return c.fetchall()

    def get_student_scholarship(self, student_id):
        c = self.conn.cursor()
        query = """
            SELECT scholarships.id, scholarships.name, scholarships.total, scholarships.type FROM scholarships
            JOIN scholarship_application ON scholarships.id = scholarship_application.scholarship_id 
            WHERE scholarship_application.student_id = %s
            ORDER BY scholarship_application.id DESC;
        """
        c.execute(query, (student_id,))
        return c.fetchall()

    def get_scholarship_application(self, scholarship_id):
        c = self.conn.cursor()
        query = """
            SELECT scholarships.id, scholarships.name, scholarships.total, scholarships.type FROM scholarships
            JOIN scholarship_application ON scholarships.id = scholarship_application.scholarship_id 
            WHERE scholarship_application.id = %s
            ORDER BY scholarship_application.id DESC;
        """
        c.execute(query, (scholarship_id,))
        return c.fetchall()
