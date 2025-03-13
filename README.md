**Blood Donation Management System**

***Overview***
The Blood Donation Management System is a CLI-based application designed to streamline the process of donor registration, blood donation tracking, and blood stock management. It allows users to:

- Register new donors.
- Record blood donations.
- Track available blood stock by type.
- Search for donors by blood type or last donation date.

This project demonstrates the use of SQLAlchemy ORM for database management, Alembic for database migrations, and Python for building the CLI interface.

***Features***

**Donor Management:**
- Add new donors with details such as name, age, contact info, blood type, and last donation date.
- Search for donors by blood type or last donation date.

**Donation Tracking:**
- Record blood donations with donor ID, donation date, and quantity donated.
- Automatically update the donor's last donation date and blood stock levels.

**Blood Stock Management:**
- View current blood stock levels by blood type.
- Automatically update stock levels when donations are recorded.

**Database Migrations:**
- Uses Alembic to manage database schema changes (e.g., adding/updating columns, creating tables).

***Technologies Used***
- **Python:** Core programming language.
- **SQLAlchemy ORM:** Object-relational mapping for database interactions.
- **Alembic:** Database migration tool.
- **SQLite:** Lightweight database for storing donor, donation, and blood stock data.
- **CLI:** Command-line interface for user interaction.

***Installation***

**Prerequisites**
- Python 3.x
- Pipenv (for virtual environment and dependency management)

***Steps***

**Clone the Repository:**
```bash
git clone git@github.com:Rinenn1/blood-donation-management-system.git
```

**Set Up Virtual Environment:**
```bash
pip install pipenv
pipenv install
```

**Install Dependencies:**
```bash
pipenv install -r requirements.txt
```

**Initialize the Database:**
```bash
alembic init migrations
```

**Run the Application:**
```bash
python main.py
```

***Usage***

**Main Menu**
To run the application, you will need to use the following commands:
```
Commands:
  add-donor (to add a donor)
  record-donation (to record the donations)
  search-donor (to search for a donor)
  search-donor-by-last-donation (to search for donors by donation dates)
  view-blood-stock (to view the blood stock)
```

**Options**

- **Add a New Donor:** Enter the donor's name, age, contact info, blood type, and last donation date (optional).
- **Record a Blood Donation:** Enter the donor's ID, donation quantity (in ml), and the donation date will be automatically set to the current date.
- **View Blood Stock Levels:** Displays the current blood stock levels for all blood types.
- **Search for Donors by Blood Type:** Enter a blood type (e.g., A+, O-) to find all donors with that blood type.
- **Search for Donors by Last Donation Date:** Enter a date (YYYY-MM-DD) to find all donors who last donated on that date.
- **Exit:** Exits the application.

***Database Schema***
The application uses the following tables:

**donors**
- `id`: Primary key (auto-incrementing integer).
- `name`: Donor's name (string).
- `age`: Donor's age (integer).
- `contact_info`: Donor's contact information (string).
- `email`: Donor's email (string).
- `blood_type`: Donor's blood type (string, e.g., A+, O-).
- `last_donation_date`: Date of the donor's last donation (date, nullable).

**donations**
- `id`: Primary key (auto-incrementing integer).
- `donor_id`: Foreign key referencing the donors table.
- `donation_date`: Date of the donation (date).
- `quantity_ml`: Quantity of blood donated (in ml, integer).

**blood_stock**
- `blood_type`: Primary key (string, e.g., A+, O-).
- `quantity_ml`: Total quantity of blood available for this type (integer).
- `last_updated`: Date when the stock was last updated (date).

***Running Migrations***
To update the database schema (e.g., add/remove columns, change data types), use Alembic:

**Generate a Migration:**
```bash
alembic revision --autogenerate -m "Description of changes"
```

**Apply the Migration:**
```bash
alembic upgrade head
```

**Roll Back a Migration:**
```bash
alembic downgrade -1
```

***Contributing***
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push to your branch.
4. Submit a pull request with a detailed description of your changes.


Enjoy using the Blood Donation Management System! 🩸

