# Contact Manager CLI

A simple command-line interface for managing contacts with SQLAlchemy ORM and SQLite database.

## Features

- Add contacts with name, phone, email, and group
- Organize contacts into groups (Family, Friends, Work, etc.)
- Add addresses to contacts
- List all contacts
- Search contacts by group
- Update contact information
- Delete contacts

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
# Add a new contact (interactive prompts)
python cli.py add-contact
# Prompts: name, phone, email, group

# List all contacts with details
python cli.py list-contacts
# Shows: ID, name, phone, email, group, address

# List contacts in specific group
python cli.py list-by-group --group Work
# Filters contacts by group name

# Add address to existing contact
python cli.py add-address --contact-id 1
# Prompts: street, city, zip code

# Update contact information
python cli.py update-contact --contact-id 1
# Shows current info, prompts for new values

# Delete contact with confirmation
python cli.py delete-contact --contact-id 1
# Asks for confirmation before deletion

# View all groups and contact counts
python cli.py list-groups
# Shows group names with contact counts
```

## Function Workflow

### add-contact
1. Prompts user for contact details (name, phone, email, group)
2. Validates input using lists, dicts, tuples
3. Creates or finds group in database
4. Creates new contact record
5. Confirms successful creation

### add-address
1. Prompts for contact ID and address details
2. Validates contact exists
3. Checks if address already exists
4. Creates address record linked to contact
5. Confirms successful addition

### list-contacts
1. Queries all contacts from database
2. Formats data for display
3. Shows contact details with group and address info
4. Handles empty database gracefully

### update-contact
1. Validates contact ID input
2. Retrieves existing contact data
3. Shows current information
4. Prompts for new values with defaults
5. Validates email format
6. Updates database and confirms changes

### delete-contact
1. Validates contact exists
2. Shows contact details
3. Requests user confirmation
4. Deletes contact and related address
5. Confirms successful deletion

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