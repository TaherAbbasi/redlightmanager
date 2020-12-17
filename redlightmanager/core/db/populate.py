from .location import Location
from .violation import Violation
from .state import State
from .violation_type import ViolationType
from .base import session_factory

def populate_database():

    session = session_factory()
    confirmed = ViolationType('عبور از چراغ قرمز'.encode("utf-8"), 'confirmed', 2004)
    stopped = ViolationType(r'توقف روی کانال عابر پیاده'.encode("utf-8"), 'stopped', 2152)

    session.add(confirmed)
    session.add(stopped)
    try:
        session.commit()
    except Exception as e:
        print(e)
    session.close()

if __name__ == "__main__":
    populate_database()