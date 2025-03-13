from sqlalchemy.orm import Session
from models import Donor, Donation, BloodStock, session
from datetime import datetime
import click


@click.group()
def cli():
    """Command Line Interface for Blood Donation Management"""
    pass



@cli.command()
@click.option('--name', prompt='Donor Name')
@click.option('--age', prompt='Donor Age', type=int)
@click.option('--contact_info', prompt='Donor Contact Info')
def add_donor(name, age, contact_info):
    valid_blood_types = ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]
    blood_type = input("Enter blood type (A+, A-, B+, B-, O+, O-, AB+, AB-): ").upper()
    if blood_type not in valid_blood_types:
        click.echo("Invalid blood type. Please enter a valid blood type.")
        return
    
    last_donation_str = input("Enter last donation date (YYYY/MM/DD): ")
    last_donation_date=None
    if last_donation_str:
        try:
            last_donation_date = datetime.strptime(last_donation_str, "%Y/%m/%d").date()
        except ValueError:
            click.echo("❌ Invalid date format. Please use YYYY/MM/DD.")
            return

    

    donor = Donor(
            name=name, 
            age=age, 
            contact_info=contact_info, 
            blood_type=blood_type, 
            last_donation_date=last_donation_date
        )
    session.add(donor)
    session.commit()
    print(f"Donor {name} added successfully!")
    session.close()


@cli.command()
@click.option('--donor_id', prompt='Donor ID', type=int)
@click.option('--quantity_ml', prompt='Blood Quantity(ml)', type=int)
def record_donation(donor_id, quantity_ml):
    donor = session.get(Donor, donor_id)
    if donor:
        donation = Donation(donor_id=donor.id, donation_date=datetime.now().date(), quantity_ml=quantity_ml)
        session.add(donation)

        # to Update donor's last donation date
        donor.last_donation_date = datetime.now().date()

        # to Update blood stock
        stock = session.get(BloodStock, donor.blood_type)
        if stock:
            stock.quantity_ml += quantity_ml
            stock.last_updated = datetime.now().date()
        else:
            stock = BloodStock(blood_type=donor.blood_type, quantity_ml=quantity_ml, last_updated=datetime.now().date())
            session.add(stock)

        session.commit()
        print("Donation recorded successfully!")
    else:
        print("Donor not found!")
    session.close()


@cli.command()
def view_blood_stock():
    try:
        stocks = session.query(BloodStock).all()
        
        if not stocks:
            click.echo("\nNo blood stock available.")
            return
        
        click.echo("\nBlood Stock Levels:")
        click.echo("-" * 40)
        for stock in stocks:
            click.echo(f"Blood Type: {stock.blood_type}, Quantity: {stock.quantity_ml}ml, Last Updated: {stock.last_updated}")
        click.echo("-" * 40)

    except Exception as e:
        click.echo(f"Error fetching blood stock: {e}")
    
    finally:
        session.close()



@cli.command()
@click.option('--blood_type', prompt='Donor Blood Type')
def search_donor(blood_type):
    donors = session.query(Donor).filter(Donor.blood_type == blood_type).all()

    if donors:
        click.echo(f"\nDonors with blood type {blood_type}:")
        click.echo("-" * 40)
        for donor in donors:
            click.echo(f"ID: {donor.id}, Name: {donor.name}, contact_info: {donor.contact_info}, Last Donation: {donor.last_donation_date}")
        click.echo("-" * 40)
    else:
        click.echo(f"No donors found with blood type {blood_type}.")
    
    session.close()


@cli.command()
@click.option('--donation_date', prompt='Donation Date')
def search_donor_by_last_donation(donation_date):
    try:
        date = datetime.strptime(donation_date, "%Y/%m/%d").date()
        donors = session.query(Donor).filter(Donor.last_donation_date == date).all()
        if donors:
            click.echo(f"\nDonors who last donated on {date}:")
            click.echo("-" * 40)
            for donor in donors:
                click.echo(f"ID: {donor.id}, Name: {donor.name}, contact_info: {donor.contact_info}")
            click.echo("-" * 40)
        else:
            click.echo(f"No donors found who last donated on {date}.")
    except ValueError:
        click.echo("Invalid date format. Please use YYYY/MM/DD.")

    session.close()


if __name__ == "__main__":
    cli()