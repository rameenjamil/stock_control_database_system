# Stock Control Database System

A console-based inventory management application developed in Python using SQLite. The system allows users to manage products, suppliers, categories, and clothing types through a professional menu-driven interface.

---

## Features

### Inventory Management
- Add new products
- Update existing products
- Delete products safely
- View all inventory records

### Category Management
- Create categories
- Update category names
- Remove unused categories

### Supplier Management
- Add supplier details
- Update supplier information
- Delete supplier records

### Clothing Type Management
- Manage clothing type records
- Organize products efficiently

### Reporting System
- Total stock value report
- Low stock report
- Products per category report

### User Experience Enhancements
- Colorized console interface using Colorama
- Structured table formatting
- Improved validation and feedback messages
- Menu-driven navigation system
- ---

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| SQLite | Database management |
| Colorama | Colored console output |
| SQL | Database queries |

---

## Project Structure

```text
stock-control-database/
│
├── controller.py      # Application workflow controller
├── crud.py            # CRUD operations
├── database.py        # Database setup and connection
├── main.py            # Application entry point
├── reports.py         # Reporting functions
├── utility.py         # Validation and helper functions
├── view.py            # Display and viewing functions
├── stock.db           # SQLite database file
├── .gitignore         # Ignored Git files
└── README.md          # Project documentation
```
---

## Database Tables

### Product
Stores inventory product information.

**Fields:**
- Product ID
- Product Name
- Quantity
- Price
- Category ID
- Supplier ID
- Clothing Type ID

### Category
Stores product categories.

**Fields:**
- Category ID
- Category Name

### Supplier
Stores supplier details.

**Fields:**
- Supplier ID
- Supplier Name
- Contact Information

### Clothing Type
Stores clothing classifications.

**Fields:**
- Clothing Type ID
- Clothing Type Name

---

## Installation Guide

Follow the steps below to install and run the Stock Control Database System on your local machine.

### 1. Install Python

This project requires Python 3.10 or later.

Download Python from the official website:

https://www.python.org/downloads/

During installation:
- Enable **Add Python to PATH**
- Complete the installation wizard

Verify installation in the terminal:

```bash
python --version
```

Expected output example:

```text
Python 3.13.3
```

---

### 2. Install Git

Download Git from:

https://git-scm.com/downloads

Verify installation:

```bash
git --version
```

Expected output example:

```text
git version 2.49.0
```

---

### 3. Clone the Repository

Open a terminal or command prompt and run:

```bash
git clone https://github.com/your-username/stock_control_database_system.git
```

This downloads the project to your computer.

---

### 4. Open the Project Folder

Navigate into the project directory:

```bash
cd stock_control_database_system
```

---

### 5. Install Required Dependencies

Install the Colorama package used for colored console output:

```bash
pip install colorama
```

Verify installation:

```bash
pip show colorama
```

---

### 6. Run the Application

Start the system by running:

```bash
python main.py
```

---

### 7. Application Startup

When the application starts, the SQLite database file (`stock.db`) is automatically created if it does not already exist.

The main menu will then appear, allowing users to:
- Manage products
- Manage suppliers
- Manage categories
- Manage clothing types
- Generate reports

---

## Application Workflow

The Stock Control Database System uses a menu-driven console interface that allows users to navigate through different management sections of the application.

### Main Menu

When the application starts, users are presented with the main menu containing the following options:

1. Product Management  
2. Category Management  
3. Supplier Management  
4. Clothing Type Management  
5. Reporting System  
6. Exit Application  

---

## Product Management

The Product Management section allows users to perform CRUD operations on inventory products.

### Available Operations

- Add new products
- View all products
- Update existing product information
- Delete products safely

### Product Information Includes

- Product name
- Quantity
- Price
- Category
- Supplier
- Clothing type

---

## Category Management

The Category Management section allows users to organize products into categories.

### Available Operations

- Add categories
- View categories
- Update category names
- Delete categories

---

## Supplier Management

The Supplier Management section manages supplier records and contact details.

### Available Operations

- Add suppliers
- View supplier information
- Update supplier details
- Delete supplier records

---

## Clothing Type Management

The Clothing Type Management section allows products to be grouped by clothing classification.

### Available Operations

- Add clothing types
- View clothing types
- Update clothing type records
- Delete clothing types

---

## Reporting System

The Reporting System provides analytical information about inventory and stock management.

### Available Reports

#### Total Stock Value Report
Calculates the total monetary value of all inventory items.

#### Products Per Category Report
Displays the number of products stored in each category.

#### Low Stock Report
Identifies products with inventory quantities below the defined threshold.

---

## Navigation System

The application uses validated menu selections to ensure users can only choose valid options.

### Navigation Features

- Menu-driven workflow
- User-friendly prompts
- Input validation
- Error handling
- Colored feedback messages using Colorama

---

## Database Integration

The application uses SQLite to store and manage all inventory data.

### Database Features

- Automatic database creation
- Foreign key relationships
- Data integrity enforcement
- Persistent data storage
- Structured relational design
---

## Validation and Error Handling

The application includes multiple validation and error-handling mechanisms to improve reliability and user experience.

### Validation Features

- Numeric input validation
- Empty field prevention
- Duplicate record checking
- Menu selection validation
- Foreign key constraint protection
- Safe deletion confirmation

### Error Handling Features

- Invalid input detection
- Database integrity protection
- Graceful handling of runtime exceptions
- Clear user feedback messages
- Prevention of application crashes caused by incorrect input

---

## User Interface Enhancements

The application uses the Colorama library to provide a more professional and user-friendly console interface.

### Colorized Output

- Red text for errors
- Green text for success messages
- Yellow text for warnings and section headings

### Interface Improvements

- Structured table formatting
- Improved readability
- Consistent menu layout
- Enhanced navigation experience

---

## Future Improvements

Potential future enhancements for the project include:

- Search functionality
- User authentication system
- Export reports to CSV or PDF
- Graphical User Interface (GUI)
- Barcode integration
- Advanced inventory analytics
- Sales tracking system
- Multi-user support

---

## Learning Outcomes

This project demonstrates practical understanding of:

- Python programming
- SQLite database integration
- CRUD operations
- Relational database design
- Modular software development
- Input validation
- Error handling
- Git and GitHub version control
- Software documentation standards

---

## Author

Developed as part of a software development and database management project.

---

## License

This project is intended for educational purposes.
