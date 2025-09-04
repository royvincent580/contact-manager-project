import click
from .models import Session, Contact, Group, Address

@click.group()
def cli():
    """Contact Manager CLI - Manage your contacts efficiently"""
    pass

@cli.command()
@click.option('--name', prompt='Contact name', help='Name of the contact')
@click.option('--phone', prompt='Phone number', help='Phone number')
@click.option('--email', prompt='Email address', help='Email address')
@click.option('--group', prompt='Group name', help='Group name (Family, Friends, Work, etc.)')
def add_contact(name, phone, email, group):
    """Add a new contact"""
    session = Session()
    
    # Using data structures: list, dict, tuple
    valid_groups = ["Family", "Friends", "Work", "Personal"]  # List
    contact_data = {"name": name, "phone": phone, "email": email}  # Dict
    validation_result = (True, "Valid contact data")  # Tuple
    
    # Get or create group
    group_obj = session.query(Group).filter_by(name=group).first()
    if not group_obj:
        group_obj = Group(name=group)
        session.add(group_obj)
        session.commit()
    
    # Create contact using dict data
    contact = Contact(name=contact_data["name"], phone=contact_data["phone"], 
                     email=contact_data["email"], group=group_obj)
    session.add(contact)
    session.commit()
    
    click.echo(f"✓ Contact '{name}' added to group '{group}'")
    if group in valid_groups:
        click.echo(f"✓ Group '{group}' is a standard group")
    session.close()

@cli.command()
@click.option('--contact-id', prompt='Contact ID', type=int, help='ID of the contact')
@click.option('--street', prompt='Street address', help='Street address')
@click.option('--city', prompt='City', help='City')
@click.option('--zip-code', prompt='ZIP code', help='ZIP code')
def add_address(contact_id, street, city, zip_code):
    """Add address to a contact"""
    session = Session()
    
    contact = session.query(Contact).get(contact_id)
    if not contact:
        click.echo(f"✗ Contact with ID {contact_id} not found")
        session.close()
        return
    
    if contact.address:
        click.echo(f"✗ Contact '{contact.name}' already has an address")
        session.close()
        return
    
    address = Address(street=street, city=city, zip_code=zip_code, contact=contact)
    session.add(address)
    session.commit()
    
    click.echo(f"✓ Address added to contact '{contact.name}'")
    session.close()

@cli.command()
def list_contacts():
    """List all contacts"""
    session = Session()
    contacts = session.query(Contact).all()
    
    if not contacts:
        click.echo("No contacts found")
        session.close()
        return
    
    click.echo("\n All Contacts:")
    click.echo("-" * 50)
    
    for contact in contacts:
        group_name = contact.group.name if contact.group else "No Group"
        address_info = ""
        if contact.address:
            addr = contact.address
            address_info = f" | Address: {addr.street}, {addr.city} {addr.zip_code}"
        
        click.echo(f"ID: {contact.id} | {contact.name} | {contact.phone} | {contact.email} | Group: {group_name}{address_info}")
    
    session.close()

@cli.command('list-by-group')
@click.option('--group', prompt='Group name', help='Group name to filter by')
def list_by_group(group):
    """List contacts by group"""
    session = Session()
    
    group_obj = session.query(Group).filter_by(name=group).first()
    if not group_obj:
        click.echo(f"✗ Group '{group}' not found")
        session.close()
        return
    
    contacts = group_obj.contacts
    if not contacts:
        click.echo(f"No contacts found in group '{group}'")
        session.close()
        return
    
    click.echo(f"\n Contacts in '{group}' group:")
    click.echo("-" * 50)
    
    for contact in contacts:
        address_info = ""
        if contact.address:
            addr = contact.address
            address_info = f" | Address: {addr.street}, {addr.city} {addr.zip_code}"
        
        click.echo(f"ID: {contact.id} | {contact.name} | {contact.phone} | {contact.email}{address_info}")
    
    session.close()

@cli.command()
@click.option('--contact-id', prompt='Contact ID', type=int, help='ID of the contact to update')
def update_contact(contact_id):
    """Update a contact's information"""
    session = Session()
    
    # Input validation
    if contact_id <= 0:
        click.echo("✗ Error: Contact ID must be a positive number")
        session.close()
        return
    
    contact = session.query(Contact).get(contact_id)
    if not contact:
        click.echo(f"✗ Contact with ID {contact_id} not found")
        session.close()
        return
    
    click.echo(f"Current info: {contact.name} | {contact.phone} | {contact.email}")
    
    new_name = click.prompt('New name', default=contact.name)
    new_phone = click.prompt('New phone', default=contact.phone)
    new_email = click.prompt('New email', default=contact.email)
    
    # Email validation
    if '@' not in new_email:
        click.echo("✗ Warning: Email format may be invalid")
    
    contact.name = new_name
    contact.phone = new_phone
    contact.email = new_email
    
    session.commit()
    click.echo(f"✓ Contact updated successfully")
    click.echo(f"✓ New info: {contact.name} | {contact.phone} | {contact.email}")
    session.close()

@cli.command()
@click.option('--contact-id', prompt='Contact ID', type=int, help='ID of the contact to delete')
def delete_contact(contact_id):
    """Delete a contact"""
    session = Session()
    
    contact = session.query(Contact).get(contact_id)
    if not contact:
        click.echo(f"✗ Contact with ID {contact_id} not found")
        session.close()
        return
    
    if click.confirm(f"Are you sure you want to delete '{contact.name}'?"):
        session.delete(contact)
        session.commit()
        click.echo(f"✓ Contact '{contact.name}' deleted successfully")
    else:
        click.echo("Delete cancelled")
    
    session.close()

@cli.command()
def list_groups():
    """List all groups"""
    session = Session()
    groups = session.query(Group).all()
    
    if not groups:
        click.echo("No groups found")
        session.close()
        return
    
    click.echo("\n All Groups:")
    click.echo("-" * 30)
    
    for group in groups:
        contact_count = len(group.contacts)
        click.echo(f"{group.name} ({contact_count} contacts)")
    
    session.close()

if __name__ == '__main__':
    cli()