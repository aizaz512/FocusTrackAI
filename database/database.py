import sqlite3


class Database:

    def __init__(self):

        self.connection = sqlite3.connect(
            "focustrack.db",
            check_same_thread=False
        )

        self.cursor = self.connection.cursor()

        self.create_table()

    def create_table(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS sessions(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            date TEXT,

            start_time TEXT,

            end_time TEXT,

            duration REAL,

            average_focus INTEGER,

            blink_count INTEGER,

            phone_count INTEGER,

            status TEXT

        )
        """)

        self.connection.commit()

    def insert_session(
        self,
        date,
        start_time,
        end_time,
        duration,
        average_focus,
        blink_count,
        phone_count,
        status
    ):

        self.cursor.execute("""
        INSERT INTO sessions(
            date,
            start_time,
            end_time,
            duration,
            average_focus,
            blink_count,
            phone_count,
            status
        )
        VALUES(?,?,?,?,?,?,?,?)
        """,
        (
            date,
            start_time,
            end_time,
            duration,
            average_focus,
            blink_count,
            phone_count,
            status
        ))

        self.connection.commit()

    def get_all_sessions(self):

        self.cursor.execute("SELECT * FROM sessions")

        return self.cursor.fetchall()

    def close(self):

        self.connection.close()