<<<<<<< HEAD
# Django Daily Sales App


Welcome to the Django Daily Sales App, a sleek and efficient web application built to manage and display daily sales records from a Firebird database. 
Designed with a modern, user-friendly interface, this app allows you to filter sales data by date and showcases a beautifully styled native datepicker. 
Perfect for small businesses or developers looking to explore Django with Firebird integration!

🌟 ## Features

Dynamic Date Filtering: Use a custom-styled native <input type="date"> to view sales records for any date.
Firebird Integration: Connects to a Firebird database (POWERFO.GDB) to retrieve sales data.
Filtered Data: Displays records for specific DSR_ID values [8, 42, 59, 67, 69, 70, 71, 74, 81, 91, 97, 99], showing FODATE, TEXT, and AMOUNT.
Beautiful Design: Features gradients, shadows, and hover effects for a polished look, built with custom CSS.
Responsive Layout: Optimized for desktop and mobile viewing.
Error Handling: Provides clear feedback for database errors or missing data.


🛠️ ## Technologies Used

Django 4.2.16: The Python web framework powering the app.
Firebird 2.0.2: Database driver for Firebird integration.
HTML/CSS: Custom styling with native datepicker enhancements.
Bootstrap 5.3.3: For responsive and consistent UI components.

📋 ## Prerequisites

Python 3.12+
Firebird Client (with fbclient.dll in PATH or project directory)
Access to the POWERFO.GDB database file

📦 ## Installation

Clone the Repository
		git clone https://github.com/your-username/django-daily-sales-app.git
		cd django-daily-sales-app


Set Up a Virtual Environment
		python -m venv venv
		.\venv\Scripts\activate  # On Windows
		source venv/bin/activate  # On macOS/Linux


Install Dependencies
		pip install -r requirements.txt


Configure the Database

Place POWERFO.GDB in the database/ directory.
Ensure Firebird Client is installed and fbclient.dll is accessible.


Apply Migrations
	python manage.py migrate


Collect Static Files
	python manage.py collectstatic


Run the Application
	python manage.py runserver


Access the AppOpen your browser and go to http://127.0.0.1:8000/.


🎨 ## Customization

Database Path: Update the path in sales/views.py if POWERFO.GDB is located elsewhere.
DSR_IDs: Modify the DSR_ID list in sales/views.py to filter different records.
Styling: Adjust colors and styles in static/css/styles.css to match your brand.

.

🤝 ## Contributing
Feel free to fork this repository, submit issues, or send pull requests. Contributions to enhance functionality or design are welcome!
📄 ##License
This project is licensed under the MIT License - see the LICENSE.md file for details.
🙏 Acknowledgments

Inspired by the need for a simple yet elegant sales tracking solution.
I will update this project if i'm not lazy AF :)


=======
# power-sales
Interface of Firebird database from the infamous PMS PowerPro
>>>>>>> 1f00182557aaeccec940b06a33ebd100bd859229
