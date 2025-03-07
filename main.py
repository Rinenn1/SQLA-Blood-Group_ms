from models import Donor
from functions import add_donor

donor1 = Donor("Benson", "Alucard", 24, "benson.alu@gmail.com")
donor2 = Donor("Jane", "Woodroffe", 21, "jane.woodroffe@gmail.com")
donor3 = Donor("Alex", "John", 29, "alex.john22@gmail.com")
donor4 = Donor("George", "Austin", 32, "georgeau@gmail.com")


add_donor(donor4)