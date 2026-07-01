# Full-Stack Product Inventory Catalog (Task API) 📦

A full-stack web application featuring a Python **FastAPI** backend connected to a Neon PostgreSQL database and a responsive **React + Vite** frontend catalog manager.

> [!NOTE]
> Although the directory and FastAPI service titles are named `task_api`, the application implements a product inventory management system (CRUD) handling catalog items.

---

## 📁 Project Structure

```
task_api/
├── database.py         # SQLAlchemy engine & session configurations
├── database_model.py   # SQLAlchemy database tables and ORM classes
├── model.py            # Pydantic schemas for request validation
├── main.py             # FastAPI backend server definition & endpoints
├── pyproject.toml      # Backend dependencies and configurations
├── uv.lock             # uv package manager lockfile
├── frontend/           # React + Vite client application
│   ├── src/
│   │   ├── App.jsx     # Main React component (CRUD form, search, table)
│   │   ├── App.css     # CSS styling sheet
│   │   ├── index.css   # Global styles
│   │   └── main.jsx    # React entry point
│   ├── package.json    # Frontend dependency manifest
│   ├── vite.config.js  # Vite dev server configurations
│   └── README.md       # Vite default template documentation
└── README.md           # Master project documentation (this file)
```

---

## 🛠️ Technical Stack

### **Backend**
- **Framework**: [FastAPI](https://fastapi.tiangolo.com/) (Python 3.12+)
- **ORM**: [SQLAlchemy](https://www.sqlalchemy.org/)
- **Database**: [Neon PostgreSQL](https://neon.tech/) (Serverless Postgres)
- **Data Validation**: [Pydantic v2](https://docs.pydantic.dev/)
- **Package Manager**: [uv](https://github.com/astral-sh/uv)

### **Frontend**
- **Core Library**: [React](https://react.dev/)
- **Build Tool**: [Vite](https://vite.dev/)
- **Styling**: Vanilla CSS

---

## 🔌 Backend API Endpoints

The API operates locally on port `8000`. CORS is enabled for all origins by default in development mode.

| Method | Endpoint | Description | Request Body |
|--------|----------|-------------|--------------|
| **GET** | `/API` | Verify service status | None |
| **GET** | `/products` | Retrieve all products | None |
| **GET** | `/product/{id}` | Retrieve a product by ID | None |
| **POST** | `/product` | Create a new product | `Product` Pydantic model |
| **PUT** | `/product/{id}` | Update product details | `Product` Pydantic model |
| **DELETE** | `/product/{id}` | Delete a product from the database | None |

### **Product Schema**
- `id` (int): Unique database key
- `name` (str): Product name
- `description` (str): Details / specifications
- `price` (float): Cost in USD
- `quantity` (int): Available stock units

---

## 💻 Frontend Client Features

The React interface integrates directly with the backend endpoints to deliver:
- **Real-Time Search**: Filter list by ID, Name, or Description dynamically.
- **Dynamic Sorting**: Click table headers to toggle ascending/descending sorting for any column.
- **Add / Edit Form**: Interactive forms to create new items or edit existing properties.
- **Interactive Deletions**: Prompts users for confirmation before purging a record.

---

## 🚀 Running the Project

### **1. Set up Environment Variables**
In the root of the `task_api` directory, create a `.env` file containing your Neon database connection URL:
```env
neon_db=postgresql://<username>:<password>@<neon-host>/<db-name>?sslmode=require
```

### **2. Launch Backend Server**
Ensure you have `uv` installed, then run:
```bash
# Navigate to project directory
cd task_api

# Install backend dependencies
uv sync

# Run backend development server
uv run uvicorn main:app --reload
```
The backend API documentation will be available at `http://localhost:8000/docs`.

### **3. Launch Frontend Client**
In a new terminal window:
```bash
# Navigate to the frontend directory
cd task_api/frontend

# Install node dependencies
npm install

# Start Vite development server
npm run dev
```
The React catalog interface will open in your browser at `http://localhost:5173`.
