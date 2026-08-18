#Database connection testing
from db.session import SessionLocal
from db.models import Swing
import datetime

session = SessionLocal()

new_swing = Swing(date = datetime.date.today(), notes = "test swing from offline work")
session.add(new_swing)
session.commit()

result = session.query(Swing).all()
for swing in result:
    print(swing.id, swing.date, swing.notes)

session.close()