from sys import stderr
from datetime import date
from sqlalchemy.exc import SQLAlchemyError

from database import TutoringDatabase, User, Tutor, Subject, TeachRecord, Class, Take, Booking


def add_starter_data(session):
    first = Subject(name='math', level_education=14, description='free for all')
    session.add(first)
    cloey = User(user_name='Cloey', first_name='Cloey', last_name='Do', email='ll', password='32',
                 date_of_birth=date(2002, 1, 1), school='Harvard')
    session.add(cloey)
    harry = Tutor(user_name='HarryDo12', first_name='Harry', last_name='Do', email='ll', password='32',
                  date_of_birth=date(2002, 1, 1), school='Harvard', followers='2', hours='2', status=True)
    session.add(harry)
    booking = Booking(booking_id=1, date=date(2021, 9, 2), tutor=harry, student=cloey, duration=10,
                      subject_id='1', location='VN', status='ACCEPTED')
    session.add(booking)
    classs = Class(class_id=1, booking_id=1, status='ff')
    take1 = Take(user_name='Cloey', classs=classs)
    session.add(take1)
    take2 = Take(user_name='HarryDo12', classs=classs)
    session.add(take2)
    teaching_record = TeachRecord(subject=first, tutor=harry, teach_hours=23, total_students=22,
                                  price=22, rate_students=5, rate_totals=5)
    session.add(teaching_record)


def main():
    try:
        url = TutoringDatabase.construct_mysql_url('localhost', 3306, 'tutoring', 'root', 'cse1208')
        tutoring_database = TutoringDatabase(url)
        tutoring_database.ensure_tables_exist()
        print('Tables created.')
        session = tutoring_database.create_session()
        add_starter_data(session)
        session.commit()
        print('Records created.')
    except SQLAlchemyError as exception:
        print('Database setup failed!', file=stderr)
        print(f'Cause: {exception}', file=stderr)
        exit(1)


if __name__ == '__main__':
    main()
