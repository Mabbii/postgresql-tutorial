"""imports"""

from sqlalchemy import(
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db = create_engine("postgresql://postgres:Arif1234@localhost:5432/chinook")
base = declarative_base()

# create a class-based model for the "programmer" table
class Programmer(base):
    """Programmer Class"""
    __tablename__ = "Programmer"
    Id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    nationality = Column(String)
    gender = Column(String)
    famous_for = Column(String)

# create a new instance of sessionmaker, the point to our engine  (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

# creating record on our Programmer table
ada_lovelace = Programmer(
    first_name = "ada",
    last_name = "lovelace",
    nationality = "British",
    gender = "F",
    famous_for = "First Programmer"
)

allan_turing = Programmer(
    first_name = "Allan",
    last_name = "Turing",
    nationality = "British",
    gender = "M",
    famous_for = "Modern Computing"
)

grace_hopper = Programmer(
    first_name = "Grace",
    last_name = "Hopper",
    nationality = "American",
    gender = "F",
    famous_for = "COBOL Language"
)

margaret_hamiltion = Programmer(
    first_name = "Margaret",
    last_name = "Hamiltion",
    nationality = "American",
    gender = "F",
    famous_for = "Apollo 11"
)

bill_gates = Programmer(
    first_name = "Bill",
    last_name = "Gates",
    nationality = "American",
    gender = "M",
    famous_for = "Microsoft"
)

tim_bernerslee = Programmer(
    first_name = "Tim",
    last_name = "Berners-lee",
    nationality = "American",
    gender = "M",
    famous_for = "World Wide Web"
)

noreen_butt = Programmer(
    first_name = "Noreen",
    last_name = "Butt",
    nationality = "British/Pakistani",
    gender = "F",
    famous_for = "Noreen's Cafe"
)

# add each instance of our programmer to session
# session.add(ada_lovelace)
# session.add(allan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamiltion)
# session.add(bill_gates)
# session.add(tim_bernerslee)
# session.add(noreen_butt)

# commit our session to database
# session.commit()

# programmer = session.query(Programmer).filter_by(Id = 17).first()
# programmer.famous_for = "Pakistan's Prime Minister"

# commit our session to database
# session.commit()

# Update
# peoples = session.query(Programmer)
# for people in peoples:
#     if people.gender == "F":
#         people.gender = "Female"
#     if people.gender == "M":
#         people.gender = "Male"
#     else:
#         print("Gender not defined!")
#     session.commit()


# Delete
fname = input("Enter first name: ")
lname = input("Enter last name: ")
programmer = session.query(Programmer).filter_by(first_name = fname, last_name=lname).first()
if programmer is not None:
    print("Programmer found! " + programmer.first_name + " " + programmer.last_name)
    confirmation = input("Are you sure you want to delete the programmer?")
    if confirmation.lower() == "y":
        session.delete(programmer)
        session.commit()
        print("Programmer has been Deleted")
    else:
        print("No Programmer Deleted!")
else:
    print("No record found")
# query the database to find all programmers
programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.Id,
        programmer.first_name + " " + programmer.last_name,
        programmer.nationality,
        programmer.gender,
        programmer.famous_for,
        sep=" | "
    )
