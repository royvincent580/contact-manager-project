#!/usr/bin/env python3

from lib.models import Session, Contact, Group, Address

def create_sample_data():
    """Create sample contacts for demonstration"""
    session = Session()
    
    # Sample data using lists, dicts, and tuples
    groups_data = ["Family", "Friends", "Work"]
    
    contacts_data = [
        {"name": "John Doe", "phone": "0712345678", "email": "john@email.com", "group": "Family"},
        {"name": "Jane Smith", "phone": "0156234528", "email": "jane@email.com", "group": "Work"},
        {"name": "Bob Wilson", "phone": "555-0103", "email": "bob@email.com", "group": "Friends"},
        {"name": "Alice Brown", "phone": "555-0104", "email": "alice@email.com", "group": "Work"},
    ]
    
    addresses_data = [
        ("123 Main St", "New York", "10001"),
        ("456 Oak Ave", "Los Angeles", "90210"),
        ("789 Pine Rd", "Chicago", "60601"),
    ]
    
    # Create groups
    group_objects = {}
    for group_name in groups_data:
        group = Group(name=group_name)
        session.add(group)
        group_objects[group_name] = group
    
    session.commit()
    
    # Create contacts
    contact_objects = []
    for contact_data in contacts_data:
        contact = Contact(
            name=contact_data["name"],
            phone=contact_data["phone"],
            email=contact_data["email"],
            group=group_objects[contact_data["group"]]
        )
        session.add(contact)
        contact_objects.append(contact)
    
    session.commit()
    
    # Add addresses to first 3 contacts
    for i, (street, city, zip_code) in enumerate(addresses_data):
        if i < len(contact_objects):
            address = Address(
                street=street,
                city=city,
                zip_code=zip_code,
                contact=contact_objects[i]
            )
            session.add(address)
    
    session.commit()
    print("✓ Sample data created successfully!")
    session.close()

if __name__ == '__main__':
    create_sample_data()