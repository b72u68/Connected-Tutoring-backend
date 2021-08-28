from kivy.storage.jsonstore import JsonStore
from database import TutoringDatabase, Tutor, User, Take, Booking, TeachRecord, Subject, Class


class Database:
    def __init__(self):
        credentials = JsonStore('credentials.json')
        hostname = credentials['hostname']
        port = credentials['port']
        databasee = credentials['database']
        username = credentials['username']
        password = credentials['password']
        url = TutoringDatabase.construct_mysql_url(hostname, port, databasee, username, password)
        self.database = TutoringDatabase(url)
        self.session = self.database.create_session()


database = Database()


def get_tutor_by_user(username):
    return database.session.query(Tutor).filter(Tutor.user_name == username).one()


def get_profile(username):
    return database.session.query(Tutor).filter(User.user_name == username).one()


def post_booking_info(tutor_name, student_name, date, duration, subject_ID, location, status):
    tutor = database.session.query(Tutor).filter(Tutor.user_name == tutor_name).one()
    student = database.session.query(Tutor).filter(User.user_name == student_name).one()
    booking = Booking(booking_id=1, date=date, tutor=tutor, student=student, duration=duration,
                      subject_id=subject_ID, location=location, status=status)
    database.session.add(booking)
    database.session.commit()


def get_booking_by_tutor(tutor_name):
    tutor = database.session.query(Tutor).filter(Tutor.user_name == tutor_name).one()
    return database.session.query(Booking).filter(Booking.tutor == tutor).one()


def get_booking_by_student(user_name):
    student = database.session.query(User).filter(Tutor.user_name == user_name).one()
    return database.session.query(Booking).filter(Booking.student == student).one()


def get_tutors_by_subject(subject_name):
    subject = database.session.query(Subject).filter(Subject.name == subject_name).one()
    return subject.tutors


def get_tutors_by_location(location):
    return database.session.query(Tutor).filter(Tutor.location == location).all()


def get_tutors_by_rating(rating):
    teachrecord = database.session.query(TeachRecord).filter(TeachRecord.rate_totals == rating).one()
    return teachrecord.tutors


def get_tutors_by_active_status(boolean):
    return database.session.query(Tutor).filter(Tutor.status == boolean).all()


def get_tutors_by_first_name(first_name):
    return database.session.query(Tutor).filter(Tutor.first_name == first_name).all()


def get_tutors_by_last_name(last_name):
    return database.session.query(Tutor).filter(Tutor.last_name == last_name).all()


def get_live_classes():
    return database.session.query(Class).filter(Class.status == 'ACTIVE').all()


def get_open_classes():
    return database.session.query(Class).filter(Class.status == 'OPEN').all()


def get_classes_by_user(user_name):
    student = database.session.query(User).filter(Tutor.user_name == user_name).one()
    return student.classes


def main():
    pass


if __name__ == '__main__':
    main()
