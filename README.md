# Contact Manager CLI

A simple command-line interface for managing contacts with SQLAlchemy ORM and SQLite database.

## Features

- ✅ Add contacts with name, phone, email, and group
- ✅ Organize contacts into groups (Family, Friends, Work, etc.)
- ✅ Add addresses to contacts
- ✅ List all contacts
- ✅ Search contacts by group
- ✅ Update contact information
- ✅ Delete contacts

## Setup

1. Install dependencies:
```bash
pipenv install
```

2. Activate virtual environment:
```bash
pipenv shell
```

## Usage

Run the CLI:
```bash
python cli.py --help
```

### Available Commands

- `add-contact` - Add a new contact
- `add-address` - Add address to a contact
- `list-contacts` - List all contacts
- `list-by-group` - List contacts by group
- `update-contact` - Update contact information
- `delete-contact` - Delete a contact
- `list-groups` - List all groups

### Examples

```bash
# Add a new contact
python cli.py add-contact

# List all contacts
python cli.py list-contacts

# List contacts in Work group
python cli.py list-by-group --group Work

# Add address to contact ID 1
python cli.py add-address --contact-id 1

# Update contact ID 1
python cli.py update-contact --contact-id 1

# Delete contact ID 1
python cli.py delete-contact --contact-id 1
```

## Database Schema

- **Groups**: id, name
- **Contacts**: id, name, phone, email, group_id
- **Addresses**: id, street, city, zip_code, contact_id

## Project Structure

```
contact-manager-project/
├── lib/
│   ├── __init__.py
│   ├── models.py      # SQLAlchemy models
│   └── cli.py         # CLI commands
├── cli.py             # Main entry point
├── Pipfile            # Dependencies
└── README.md
```