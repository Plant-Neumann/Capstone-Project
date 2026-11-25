import sqlite3

conn = sqlite3.connect("water_tracking.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS water_tracking(
        id INTEGER PRIMARY KEY,
        date TEXT NOT NULL,
        entry_time TEXT NOT NULL,
        water_ozs REAL NOT NULL,
        water_cups REAL NOT NULL
    )
""")

conn.commit()

def get_daily_total(date: str) -> float:
    conn = sqlite3.connect("water_tracking.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT SUM(water_ozs)
        FROM water_tracking
        WHERE date = ?
    """, (date,))

    total = cursor.fetchone()[0]

    conn.close()

    return total if total else 0.0

def new_entry(date: str, entry_time: str, water_ozs: int, water_cups: int) -> None:
    conn = sqlite3.connect("water_tracking.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO water_tracking
        (date, entry_time, water_ozs, water_cups)
        VALUES (?, ?, ?, ?)
    """, (date, entry_time, water_ozs, water_cups))

    conn.commit()
    conn.close()

def edit_entry(entry_id: int, date: str, entry_time: str, water_ozs: int, water_cups: int) -> None:
    conn = sqlite3.connect("water_tracking.db")
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE water_tracking
        SET
            date = ?,
            entry_time = ?,
            water_ozs = ?,
            water_cups = ?
        WHERE id = ? 
    """, (
        date,
        entry_time,
        water_ozs,
        water_cups,
        entry_id  
))
    conn.commit()
    conn.close()

def delete_entry(entry_id: int) -> None: 
    conn = sqlite3.connect("water_tracking.db")
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM water_tracking WHERE id = ?
        """, (entry_id)) 

    conn.commit() 
    conn.close()

def all_entries(): 
        conn = sqlite3.connect("water_tracking.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM water_tracking")
        entries = (cursor.fetchall())
        conn.close()
        return entries

def get_entry(entry_id: int):
    conn = sqlite3.connect("water_tracking.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT *
        FROM water_tracking
        WHERE id = ?
    """, (entry_id,))
    entry = cursor.fetchone()
    conn.close()
    return entry 

def main():
    new_entry(
        "2026-11-13",
        "06:00 AM",
        16,
        2
    )
    edit_entry(
        1,
        "2026-11-13",
        "2:00 PM",
        4,
        2
    )

    conn = sqlite3.connect("water_tracking.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM water_tracking")
    print(cursor.fetchall())

    conn.close()

if __name__ == "__main__":
    main()