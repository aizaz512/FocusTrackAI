from database.database import Database

db = Database()

db.insert_session(
    "2026-08-06",
    "08:00",
    "08:45",
    45,
    93,
    32,
    2,
    "Focused"
)

print(db.get_all_sessions())

db.close()