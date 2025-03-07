from sqlalchemy.exc import IntegrityError
from models import session, Donor


donors_list = []


def add_donor(donor):
    first_name, last_name, age, email = donor.first_name, donor.last_name, donor.age, donor.email

    global donors_list

    if any(donor[3] == email for donor in donors_list):
        print(f"User {email} alreasy exists")
        return
    
    existing = session.query(Donor).filter_by(email=email).first()

    if existing:
        print(f"Skipping: {first_name} {last_name}")

    donors_list.append((first_name, last_name, age, email))
    donor = Donor(first_name, last_name, age, email)
    session.add(donor)
    
    try:
        session.commit()
        print(f"Added {first_name} {last_name} to the table")
    except IntegrityError:
        session.rollback()
        print(f"{first_name} {last_name} is already in the table")