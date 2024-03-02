## AssetGuardian

### General Information
AssetGuardian is a Django-powered application designed for exploration and management of IT assets.

Crafted by a trio of Python developers in just 42 hours, the project embraces the MVP (Minimum Viable Product) approach, enabling rapid development and iteration. Tasks included brainstorming business ideas, architectural design, logical implementation, and integrating front-end elements.

Practicing application development in a team setting, with a well-defined task allocation, the team brought the envisioned concepts to fruition, culminating in the creation of this application.

By adopting the MVP strategy, the team prioritized the development of critical features essential for delivering value to users.

### Technologies Used
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [SQLite](https://www.sqlite.org/)
- [HTML](https://en.wikipedia.org/wiki/HTML)
- [CSS](https://en.wikipedia.org/wiki/CSS)
- [Bootstrap](https://getbootstrap.com/)
- [PyTest](https://pypi.org/project/pytest/)

### Key Features
- *Centralized Asset Management:* AssetGuardian serves as a centralized platform for managing all types of assets. Users can easily view, add, update, and delete assets through the application.
- *Asset Information Storage:* The application stores comprehensive information about each asset, including its category, description, vendor, serial number, value, assigned employee, and purchase date. This information allows users to track and monitor assets effectively.
- *Employee Management:* In addition to assets, AssetGuardian enables the management of employees. Users can add, update, and delete employee records within the application.

### Functions

#### User
- *User Authentication:* Users can register, login, and logout. A unique username is required for registration.
- *Asset Exploration:* Logged-in users can view, filter and sort assets.
- *Asset Management:* Logged-in users with appropriate permissions can add, update, and remove assets.

#### Admin
- **Admin Dashboard:** After logging in, the admin is directed to a dashboard where comprehensive information is displayed, allowing efficient management of assets and employees.

### Screenshots

### Main page
![Example screenshot](./img/screen1.jpg)

### Setup
To clone this repository, refer to [this publication](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).

To download and install Python 3.12.2, visit [this link](https://www.python.org/).

Python version check:
```bash
$ python --version
```

Create and activate a virtual environment:

```bash
$ python -m venv .venv
$ .venv\Scripts\activate.bat
```

Install dependencies:

```bash
$ pip install -r requirements.txt
```
Set up the database:

```bash
$ python manage.py migrate
```
Create a superuser:

```bash
$ python manage.py createsuperuser
```

Run the server:

```bash
$ python manage.py runserver
```

Run the application:


```bash
# Run from Terminal
python main.py
# Access from browser or using curl
curl 127.0.0.1:8000/


```


This updated README.md file provides clear and concise information about the AssetGuardian application, its features, technologies used, setup process, and testing procedures. It also improves readability and organization for better user understanding.
