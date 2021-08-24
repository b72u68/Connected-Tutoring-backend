from sqlalchemy import create_engine, Column, Integer, Boolean, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref

Persisted = declarative_base()  # pylint: disable=invalid-name


class Subject(Persisted):
    __tablename__ = 'subjects'
    subject_id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    level_education = Column(String(50), nullable=False)
    description = Column(String(50), nullable=False)
    tutors = relationship('Tutor', uselist=True, secondary='teach_records')
    teach_records = relationship('TeachRecord', uselist=True, back_populates='subject')


class User(Persisted):
    __tablename__ = 'users'
    user_name = Column(String(50), primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(20), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    school = Column(String(30), nullable=False)
    location = Column(String(30))
    description = Column(String(2000))
    image = Column(String(2000))
    bookings = relationship('Booking', uselist=True, back_populates='student')
    tutors = relationship('Tutor', uselist=True, secondary='bookings')
    takes = relationship('Take', uselist=True, back_populates='user')


class Tutor(User):
    __tablename__ = 'tutors'
    user_name = Column(String(50), ForeignKey('users.user_name'), primary_key=True)
    followers = Column(Integer, nullable=False)
    hours = Column(Integer, nullable=False)
    status = Column(Boolean, nullable=False)
    subjects = relationship('Subject', uselist=True, secondary='teach_records')
    teach_records = relationship('TeachRecord', uselist=True, back_populates='tutor')
    bookings = relationship('Booking', uselist=True, back_populates='tutor')
    students = relationship('User', uselist=True, secondary='bookings')


class TeachRecord(Persisted):
    __tablename__ = 'teach_records'
    user_name = Column(String(50), ForeignKey('tutors.user_name', ondelete='CASCADE'), primary_key=True)
    tutor = relationship('Tutor', back_populates='teach_records')
    subject_id = Column(Integer, ForeignKey('subjects.subject_id', ondelete='CASCADE'), primary_key=True)
    subject = relationship('Subject', back_populates='teach_records')
    teach_hours = Column(Integer, nullable=False)
    total_students = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    rate_students = Column(Integer, nullable=False)
    rate_totals = Column(Integer, nullable=False)


class Booking(Persisted):
    __tablename__ = 'bookings'
    booking_id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    tutor_name = Column(String(50), ForeignKey('tutors.user_name', ondelete='CASCADE'))
    tutor = relationship('Tutor', back_populates='bookings', foreign_keys=[tutor_name])
    student_name = Column(String(50), ForeignKey('users.user_name', ondelete='CASCADE'))
    student = relationship('User', back_populates='bookings', foreign_keys=[student_name])
    duration = Column(Integer, nullable=False)
    subject_id = Column(Integer, ForeignKey('subjects.subject_id', ondelete='CASCADE'))
    location = Column(String(50), nullable=False)
    status = Column(String(10), nullable=False)  # enum value


class Class(Persisted):
    __tablename__ = 'classes'
    class_id = Column(Integer, primary_key=True)
    booking_id = Column(Integer, ForeignKey('bookings.booking_id', ondelete='CASCADE'), primary_key=True)
    status = Column(String(10), nullable=False)  # enum
    takes = relationship('Take', uselist=True, back_populates='classs')
    booking = relationship("Booking", backref=backref("classes", uselist=False))


class Take(Persisted):
    __tablename__ = 'takes'
    user_name = Column(String(50), ForeignKey('users.user_name', ondelete='CASCADE'), primary_key=True)
    user = relationship('User', back_populates='takes')
    class_id = Column(Integer, ForeignKey('classes.class_id', ondelete='CASCADE'), primary_key=True)
    classs = relationship('Class', back_populates='takes')
    review = Column(String(2000))
    user_rating = Column(Integer)


class TutoringDatabase(object):
    @staticmethod
    def construct_mysql_url(authority, port, database, username, password):
        return f'mysql+mysqlconnector://{username}:{password}@{authority}:{port}/{database}'

    @staticmethod
    def construct_in_memory_url():
        return 'sqlite:///'

    def __init__(self, url):
        self.engine = create_engine(url)  # an engine is like an endpoint, something to connect to
        self.Session = sessionmaker()  # create a class for connections to that endpoint / pylint: disable=invalid-name
        self.Session.configure(bind=self.engine)  # associate the class with the endpoint

    def ensure_tables_exist(self):
        Persisted.metadata.create_all(self.engine)  # create tables for all subclasses of Persisted

    def create_session(self):
        return self.Session()  # create a new session, which is like a connection to the database
