def add_booking(name, phone, address, date, time):
    c.execute("INSERT INTO bookings (name, phone, address, date, time) VALUES (?, ?, ?, ?, ?)",
              (name, phone, address, date, time))
    conn.commit()

def get_bookings():
    c.execute("SELECT * FROM bookings")
    return c.fetchall()
