# Stock Control Database System

## Overview

This project is a command-line Stock Control Database System developed in Python using SQLite. 
The system demonstrates the use of relational database design, foreign key constraints, and SQL querying techniques.
It allows users to manage inventory data through a structured and user-friendly interface.

The system supports full CRUD operations (Create, Read, Update, Delete) across multiple related tables, including:

- Products  
- Categories  
- Suppliers  
- Clothing Types  

Additionally, the system includes reporting functionality that provides insights into stock levels and product distribution.

The application is designed with a modular architecture, separating concerns into different components such as:
- Controller (menu navigation)
- CRUD operations
- Data viewing
- Utility functions
- Reporting module

## Technologies Used

- Python 3
- SQLite
- Colorama (for enhanced terminal user experience)

## Features

### Core Functionality

- **Full CRUD Operations**
  - Create, view, update, and delete records across all tables:
    - Products
    - Categories
    - Suppliers
    - Clothing Types

- **Relational Database Structure**
  - Tables are linked using foreign keys to maintain data integrity
  - Ensures valid relationships between products, categories, suppliers, and clothing types

- **User-Friendly Menu System**
  - Interactive command-line interface with clear navigation
  - Consistent menu structure across all modules
  - Option to return to previous menus or cancel operations

---

### Data Validation

- Input validation is implemented to:
  - Prevent invalid data types (e.g. text instead of numbers)
  - Ensure required fields are not left empty
  - Validate names using appropriate formatting rules

- Error handling prevents programme crashes and guides the user with clear messages

---

### Reporting System

The application includes basic reporting features using SQL queries:

- **Total Stock Value**
  - Calculates the total value of all products in inventory

- **Products per Category**
  - Displays the number of products within each category

- **Low Stock Items**
  - Identifies products with low quantity levels

---

### User Experience Enhancements

- **Colour-coded feedback**
  - Success messages (green)
  - Errors (red)
  - Warnings (yellow)

- Improves readability and usability of the terminal interface

---

### Modular Design

The system is structured into separate modules for maintainability:

- `controller.py` → Handles menu navigation and program flow  
- `crud.py` → Contains all database operations  
- `view.py` → Handles data display  
- `reports.py` → Generates reports using SQL queries  
- `utility.py` → Reusable helper functions  
- `database.py` → Database connection and setup  

---

### Data Storage

- Uses **SQLite** for lightweight, file-based database storage
- Automatically creates tables if they do not exist

## How to Run the Programme

Follow the steps below to set up and run the application.

### 1. Clone the Repository

```bash
git clone https://github.com/rameenjamil/stock_control_database_system.git
cd stock_control_database_system
```

### 2. Ensure Python is Installed

Make sure Python 3 is installed on your system.

Check using `python --version` or on Windows `py --version`.

### 3. Install Dependencies

```bash
py -m pip install colorama
```

### 4. Run the Application
```bash
py main.py
```
### 5. Using the Programme

- Select a table from the main menu  
- Choose an action (Add, View, Update, Delete)  
- Follow the on-screen prompts  
- Use `0` or menu options to go back or exit  

### Notes

- The database (`stock.db`) is created automatically if it does not exist  
- All data is stored locally using SQLite  
- The application runs entirely in the terminal  
## Database Structure

The application uses a relational database implemented with SQLite.  
It consists of four main tables that are linked using foreign key relationships.

---

### Tables Overview

#### 1. Product

Stores information about each product in the inventory.

| Column Name   | Data Type | Description                     |
|--------------|----------|---------------------------------|
| product_id   | INTEGER  | Primary key                     |
| name         | TEXT     | Product name                    |
| size         | TEXT     | Product size                    |
| quantity     | INTEGER  | Quantity in stock               |
| price        | REAL     | Price per unit                  |
| category_id  | INTEGER  | Foreign key → Category          |
| supplier_id  | INTEGER  | Foreign key → Supplier          |
| type_id      | INTEGER  | Foreign key → Clothing Type     |

---

#### 2. Category

Stores product categories.

| Column Name     | Data Type | Description         |
|-----------------|----------|---------------------|
| category_id     | INTEGER  | Primary key         |
| category_name   | TEXT     | Category name       |

---

#### 3. Supplier

Stores supplier details.

| Column Name            | Data Type | Description        |
|------------------------|----------|--------------------|
| supplier_id           | INTEGER  | Primary key        |
| supplier_name         | TEXT     | Supplier name      |
| supplier_contact_info | TEXT     | Contact details    |

---

#### 4. Clothing Type

Stores types of clothing.

| Column Name | Data Type | Description       |
|------------|----------|-------------------|
| type_id    | INTEGER  | Primary key       |
| type_name  | TEXT     | Clothing type     |

---

### Relationships

- A **Product** belongs to one **Category**
- A **Product** is supplied by one **Supplier**
- A **Product** has one **Clothing Type**

These relationships are enforced using foreign key constraints:

- `product.category_id → category.category_id`
- `product.supplier_id → supplier.supplier_id`
- `product.type_id → clothing_type.type_id`

---

### Data Integrity

- Primary keys ensure each record is uniquely identifiable
- Foreign keys enforce valid relationships between tables
- Constraints prevent invalid or orphaned records

## Future Improvements

While the current system provides full CRUD functionality and basic reporting, several enhancements could be implemented to improve usability, scalability, and functionality.

### User Interface Enhancements

- Develop a graphical user interface (GUI) to replace the command-line interface, improving accessibility for non-technical users  
- Improve layout and formatting of tables for better readability with larger datasets  

---

### Advanced Reporting

- Add more detailed reports, such as:
  - Total quantity of products per category  
  - Most frequently supplied products  
  - Stock value per category  
- Export reports to external formats such as CSV or Excel  

---

### Search and Filtering

- Implement search functionality to quickly find products by name, category, or supplier  
- Add filtering options (e.g. low stock, price range, category-specific views)  

---

### Data Validation and Constraints

- Strengthen validation rules (e.g. minimum and maximum values for quantity and price)  
- Add database-level constraints such as UNIQUE and NOT NULL where appropriate  

---

### Database Scalability

- Migrate from SQLite to a more scalable database system (e.g. MySQL or PostgreSQL) for handling larger datasets and multi-user access  

---

### User Management

- Introduce user authentication (login system)  
- Implement role-based access control (e.g. admin vs standard user)  

---

### Logging and Error Handling

- Add logging functionality to track system usage and errors  
- Improve error handling to provide more detailed feedback  

---

### Code Improvements

- Refactor repeated logic into reusable functions where appropriate  
- Improve code documentation and inline comments for maintainability  
