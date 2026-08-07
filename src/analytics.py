"""
analytics.py

Performs analytics on saved study sessions.
"""

import sqlite3


class Analytics:

    def __init__(self):

        self.connection = sqlite3.connect(
            "focustrack.db",
            check_same_thread=False
        )

        self.cursor = self.connection.cursor()

    def total_sessions(self):

        self.cursor.execute(
            "SELECT COUNT(*) FROM sessions"
        )

        return self.cursor.fetchone()[0]

    def average_focus(self):

        self.cursor.execute(
            "SELECT AVG(average_focus) FROM sessions"
        )

        value = self.cursor.fetchone()[0]

        if value is None:
            return 0

        return round(value,2)

    def total_blinks(self):

        self.cursor.execute(
            "SELECT SUM(blink_count) FROM sessions"
        )

        value = self.cursor.fetchone()[0]

        if value is None:
            return 0

        return value

    def total_phone_usage(self):

        self.cursor.execute(
            "SELECT SUM(phone_count) FROM sessions"
        )

        value = self.cursor.fetchone()[0]

        if value is None:
            return 0

        return value

    def total_duration(self):

        self.cursor.execute(
            "SELECT SUM(duration) FROM sessions"
        )

        value = self.cursor.fetchone()[0]

        if value is None:
            return 0

        return value

    def focus_history(self):

        self.cursor.execute(
            """
            SELECT date, average_focus
            FROM sessions
            ORDER BY id
            """
        )

        return self.cursor.fetchall()

    def close(self):

        self.connection.close()