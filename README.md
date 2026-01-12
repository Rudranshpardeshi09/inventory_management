# InventoryRobo 📦

> **A Modern, Production-Ready Inventory Management System Built with Django**

A comprehensive web-based inventory management solution designed for efficient tracking, management, and distribution of inventory items. InventoryRobo provides real-time stock monitoring, bulk import capabilities, transaction history, and component issuance tracking with role-based workflows.

---

## 🌟 Features

### Core Inventory Management
- **Real-time Dashboard**: Interactive overview of inventory status with summary cards and metrics
- **Item Management**: Create, edit, delete, and manage inventory items with auto-generated serial numbers
- **Stock Operations**: Add or remove stock with automatic transaction logging
- **Low-Stock Alerts**: Visual indicators for items at or below reorder levels
- **Inventory Search**: Live search functionality with fast filtering across all items

### Bulk Import System
- **Excel Import**: Support for `.xlsx`, `.xls`, and `.csv` file formats
- **Smart Column Mapping**: Dynamic field mapping UI for flexible data structure handling
- **Batch Processing**: Import up to 5,000 items with validation
- **Header Detection**: Automatic or manual header row recognition
- **Data Validation**: Real-time validation with descriptive error messages

### Transaction Tracking
- **Complete History**: Full audit trail of all stock operations (additions and removals)
- **Live Search**: Filter transactions by item name, type, or date range
- **Transaction Details**: Date, quantity, item reference, and remarks for each transaction
- **Pagination**: Efficient browsing of large transaction datasets

### Component Issuance System
- **Item Issuance**: Issue components to users with issuer/receiver tracking
- **Status Tracking**: Monitor component condition (OK, Faulty, Lost)
- **Condition Types**: Track returnable vs. non-returnable items
- **Item Autocomplete**: Smart search for quick item selection
- **Receive Workflow**: Receive components back with status updates
- **Role-Based Assignments**: Structured issuer and receiver assignments
- **Email Notifications**: Automated email alerts to department heads

### User Interface
- **Modern Design**: Responsive Bootstrap 5 interface with smooth animations
- **Professional Styling**: Gradient cards, icons, and intuitive navigation
- **Mobile-Friendly**: Fully responsive design for desktop and mobile devices
- **Interactive Tables**: Sortable tables with live search and filtering
- **Visual Feedback**: Status badges, color-coded alerts, and loading states

---

## 🛠️ Tech Stack

### Backend
| Technology | Version | Purpose |
|-----------|---------|---------|
| **Django** | 5.2.7 | Web framework |
| **Python** | 3.x | Programming language |
| **SQLite** | Latest | Database (development) |
| **Pandas** | Latest | Data import/export |

### Frontend
| Technology | Version | Purpose |
|-----------|---------|---------|
| **Bootstrap** | 5.3.3 | CSS framework |
| **HTML5** | - | Markup |
| **CSS3** | - | Styling & animations |
| **JavaScript (Vanilla)** | - | Client-side interactivity |
| **Font Awesome** | 6.5.0 | Icons |

### Additional Libraries
- **django-environ**: Environment variable management
- **openpyxl**: Excel file processing
- **python-dotenv**: Configuration management

---

## 📋 System Requirements

- **Python**: 3.8+
- **Operating System**: Windows/macOS/Linux
- **RAM**: 512MB minimum (1GB recommended)
- **Disk Space**: 500MB free space
- **Database**: SQLite (included)

---

## 🚀 Installation & Setup

### Prerequisites
Ensure you have Python 3.8+ installed:
```bash
python --version
```

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd inventory-mgn/inventory-robo
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Environment Configuration
Create a `.env` file in the project root directory:
```env
# Email Configuration
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
DEFAULT_FROM_EMAIL=your-email@gmail.com

# Email Recipient (Department Head)
HEAD_EMAIL=department-head@example.com

# Django Settings
DEBUG=True
SECRET_KEY=django-insecure-your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
```

### Step 5: Initialize Database
```bash
python manage.py migrate
```

### Step 6: Create Superuser (Admin)
```bash
python manage.py createsuperuser
```
Follow the prompts to set username, email, and password.

### Step 7: Run Development Server
```bash
python manage.py runserver
```

### Step 8: Access the Application
Open your browser and navigate to:
- **Application**: `http://127.0.0.1:8000/`
- **Admin Panel**: `http://127.0.0.1:8000/admin/`

---

## 📁 Project Architecture

### Directory Structure
```
inventory-robo/
├── backend/                          # Django project settings
│   ├── __init__.py
│   ├── settings.py                  # Project configuration
│   ├── urls.py                      # URL routing
│   ├── asgi.py                      # ASGI configuration
│   └── wsgi.py                      # WSGI configuration
│
├── inventory/                        # Main application
│   ├── migrations/                  # Database migrations
│   ├── templates/inventory/         # HTML templates
│   │   ├── base.html                # Base template
│   │   ├── dashboard.html           # Dashboard view
│   │   ├── inventory_list.html      # Items listing
│   │   ├── add_item.html            # Add new item
│   │   ├── edit_item.html           # Edit item
│   │   ├── add_stock.html           # Stock addition
│   │   ├── remove_stock.html        # Stock removal
│   │   ├── import_upload.html       # File upload
│   │   ├── import_mapping.html      # Column mapping
│   │   ├── transaction_history.html # Transaction log
│   │   ├── issuance_list.html       # Issuances listing
│   │   ├── issuance_form.html       # Issue form
│   │   └── partials/
│   │       ├── inventory_rows.html  # Table rows partial
│   │       └── transaction_rows.html # Transaction rows partial
│   │
│   ├── static/
│   │   └── js/                      # JavaScript files
│   │
│   ├── admin.py                     # Django admin configuration
│   ├── models.py                    # Database models
│   ├── views.py                     # View functions
│   ├── forms.py                     # Form definitions
│   ├── urls.py                      # App URL patterns
│   ├── utils.py                     # Utility functions
│   ├── email.py                     # Email utilities
│   └── constants.py                 # Application constants
│
├── db.sqlite3                        # SQLite database
├── manage.py                         # Django management script
├── requirements.txt                  # Python dependencies
└── .env                              # Environment variables (create)
```

### Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                     WEB BROWSER (Frontend)                  │
│                    (Bootstrap 5 + JavaScript)               │
└───────────────────────┬─────────────────────────────────────┘
                        │ HTTP Requests/Responses
                        ▼
┌─────────────────────────────────────────────────────────────┐
│                    Django Web Server                        │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  URL Router (urls.py)                                       │
│         │                                                    │
│         ▼                                                    │
│  Views (views.py)                                           │
│    ├─ Dashboard View                                        │
│    ├─ Inventory Management Views                            │
│    ├─ Stock Operations Views                                │
│    ├─ Import/Mapping Views                                  │
│    ├─ Transaction Views                                     │
│    └─ Issuance Views                                        │
│         │                                                    │
│         ▼                                                    │
│  Forms (forms.py) & Utilities (utils.py, email.py)         │
│         │                                                    │
│         ▼                                                    │
│  Models (models.py)                                         │
│    ├─ Item Model                                            │
│    ├─ Transaction Model                                     │
│    └─ Issuance Model                                        │
│         │                                                    │
└─────────────┼──────────────────────────────────────────────┘
              │ ORM (Object-Relational Mapping)
              ▼
┌─────────────────────────────────────────────────────────────┐
│              SQLite Database (db.sqlite3)                   │
│                                                              │
│  ├─ Items Table                                             │
│  ├─ Transactions Table                                      │
│  ├─ Issuances Table                                         │
│  └─ Auth Tables                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔄 Data Flow

### 1. **Adding a New Item**
```
User Input → Add Item Form → Validation → Model.save()
                                              ↓
                          Auto-generate Serial Number
                                              ↓
                          Store in Database → Redirect to Inventory
```

### 2. **Bulk Import Process**
```
Excel File Upload
       ↓
Parse File (Pandas)
       ↓
Preview Data
       ↓
User Maps Columns
       ↓
Validation & Processing
       ↓
Batch Insert to Database (atomic transaction)
       ↓
Create Transaction Records
       ↓
Success/Error Response
```

### 3. **Stock Transaction Flow**
```
User Request (Add/Remove Stock)
       ↓
Fetch Item → Validate Quantity
       ↓
Update Item.quantity
       ↓
Create Transaction Record (atomic)
       ↓
Update Dashboard Metrics
       ↓
Real-time Sync to Frontend
```

### 4. **Component Issuance Workflow**
```
Issue Request
       ↓
Search & Select Item → Autocomplete
       ↓
Validate: Issuer ≠ Receiver, Stock Available
       ↓
Create Issuance Record
       ↓
Deduct Stock from Item
       ↓
Create Transaction Record
       ↓
Send Email Notification to Head
       ↓
Display in Issuance List
       ↓
       (Later) Receive Item
              ↓
       Update Component Status
              ↓
       Optional: Return to Stock
              ↓
       Mark as Received
```

### 5. **Live Search Implementation**
```
User Typing in Search Box
       ↓
Trigger AJAX Request (debounced)
       ↓
Backend Query Database (Q objects)
       ↓
Return Filtered Results (JSON)
       ↓
JavaScript Updates DOM
       ↓
Real-time Results Display
```

---

## 📊 Database Models

### Item Model
```python
Item
├── serial_no (PositiveInteger, Auto-generated, Unique)
├── name (CharField)
├── category (CharField)
├── quantity (PositiveInteger)
├── reorder_level (PositiveInteger)
├── unit_price (DecimalField)
├── location (CharField)
├── created_at (DateTimeField, Auto)
└── is_imported (Boolean)
```

### Transaction Model
```python
Transaction
├── item (ForeignKey → Item)
├── transaction_type (Choice: IN/OUT)
├── quantity (PositiveInteger)
├── date (DateTimeField, Auto)
└── remarks (TextField, Optional)
```

### Issuance Model
```python
Issuance
├── item (ForeignKey → Item)
├── quantity (PositiveInteger)
├── issue_date (DateTimeField, Auto)
├── receive_date (DateTimeField, Optional)
├── user (CharField)
├── receiver (CharField)
├── issuer (Choice: Harsh/Gaurav)
├── component_status (Choice: OK/Faulty/Lost)
├── issue_condition (Choice: Returnable/Non-Returnable)
├── remark (TextField)
└── received (Boolean)
```

---

## 🔑 Key Features Deep Dive

### Dashboard
- **Summary Cards**: Total items, in-stock items, low-stock items, out-of-stock items
- **Recent Inventory**: Table showing latest items with pagination
- **Visual Indicators**: Color-coded status (Red = Out, Yellow = Low, Green = In Stock)
- **Animations**: Smooth fade-in and slide effects

### Inventory Management
- **CRUD Operations**: Full create, read, update, delete functionality
- **Auto Serial Numbers**: Atomic, concurrency-safe sequential numbering
- **Category System**: Predefined categories with custom category support
- **Search & Filter**: Live search with multiple filter options
- **Pagination**: 10 items per page (configurable)

### Import System
- **Multi-Format Support**: Excel (.xlsx, .xls) and CSV files
- **Smart Mapping**: Drag-and-drop or select column mapping
- **Batch Validation**: Row-level validation with error reporting
- **Progress Tracking**: Visual feedback during import
- **Atomic Transactions**: All-or-nothing import guarantee

### Issuance Tracking
- **Role-Based Workflow**: Structured issuer/receiver assignments
- **Status Monitoring**: Track component condition throughout lifecycle
- **Email Integration**: Automatic notifications to department head
- **Return Processing**: Receive items with status update
- **Audit Trail**: Complete history of all issuances

---

## 🌐 API Endpoints / URL Patterns

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/` | GET | Dashboard home page |
| `/inventory/` | GET | List all inventory items |
| `/add/` | GET, POST | Add new item |
| `/edit/<id>/` | GET, POST | Edit existing item |
| `/delete/<id>/` | GET | Delete item |
| `/inventory/live-search/` | GET | Live search for items |
| `/add_stock/<id>/` | GET, POST | Add stock to item |
| `/remove_stock/<id>/` | GET, POST | Remove stock from item |
| `/transactions/` | GET | View transaction history |
| `/transactions/live-search/` | GET | Search transactions |
| `/issuances/` | GET | List issuances |
| `/issuances/issue/` | GET, POST | Issue new component |
| `/issuances/receive/` | GET, POST | Receive issued component |
| `/items/autocomplete/` | GET | Autocomplete for items |
| `/import-items/` | GET, POST | Upload import file |
| `/import-items/mapping/` | GET, POST | Map file columns |
| `/delete-imported/` | POST | Delete imported items |

---

## 🔒 Security Features

- **CSRF Protection**: Django's built-in CSRF middleware
- **SQL Injection Prevention**: Django ORM parameterized queries
- **XSS Protection**: Template auto-escaping
- **Atomic Transactions**: Concurrency-safe database operations
- **Input Validation**: Form-level and model-level validation
- **Environment Variables**: Sensitive credentials in `.env` file (not committed)

---

## 🎯 Usage Guide

### Adding Items Manually
1. Navigate to **Add Item** from navbar
2. Fill in item details (Name, Category, Quantity, etc.)
3. Click **Add Item** → Auto-generated serial number assigned
4. Item appears in inventory dashboard

### Importing Items in Bulk
1. Prepare Excel/CSV file with item data
2. Go to **Import Items** → Upload file
3. Preview data and confirm
4. Select **Column Mapping** for each field
5. Confirm import → Items batch processed
6. Check **Transaction History** for import records

### Managing Stock
1. **Add Stock**: Click item → Add Stock → Enter quantity → Confirm
2. **Remove Stock**: Click item → Remove Stock → Enter quantity → Confirm
3. **Automatic Transactions**: Every operation creates audit record

### Issuing Components
1. Go to **Issuances** → Click **Issue New Component**
2. Search and select item (uses autocomplete)
3. Enter quantity and select issuer/receiver
4. Set condition (returnable/non-returnable)
5. Add remarks if needed
6. Submit → Email notification sent
7. Item appears in **Issuance List** → Can be marked received later

### Viewing Reports
1. **Dashboard**: Quick overview of inventory status
2. **Transaction History**: Complete audit trail with search/filter
3. **Issuance List**: Track all issued items and their status

---

## 🚀 Deployment Considerations

### For Production:
1. **Database**: Migrate to PostgreSQL or MySQL
2. **Environment**: Set `DEBUG=False` in `.env`
3. **Security**: 
   - Update `SECRET_KEY` to a secure random value
   - Set proper `ALLOWED_HOSTS`
   - Use HTTPS only
4. **Email**: Configure production SMTP settings
5. **Static Files**: Collect static files: `python manage.py collectstatic`
6. **Logging**: Configure proper logging
7. **Backups**: Implement regular database backups
8. **Web Server**: Use Gunicorn/uWSGI + Nginx

### Docker Support:
Create `Dockerfile`:
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "backend.wsgi:application"]
```

---

## 🐛 Troubleshooting

### Issue: Database Migration Errors
```bash
# Reset migrations (development only!)
python manage.py migrate inventory zero
python manage.py migrate
```

### Issue: Import File Not Processing
- Check file format (.xlsx, .xls, .csv only)
- Verify file size < session limit
- Check encoding (UTF-8 or Latin-1)

### Issue: Emails Not Sending
- Verify `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD` in `.env`
- Check if Gmail 2-factor authentication is enabled (use App Password)
- Verify `HEAD_EMAIL` is correctly configured

### Issue: Static Files Not Loading
```bash
python manage.py collectstatic --noinput
```

---

## 📞 Contact & Support

For issues, feature requests, or contributions, please contact the development team.

---

## 📄 License

This project is proprietary software. All rights reserved.

---

## 🎓 Learning Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [SQLite Documentation](https://www.sqlite.org/docs.html)

---

## 📝 Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | Jan 2026 | Initial release |

---

**Built with ❤️ using Django**
