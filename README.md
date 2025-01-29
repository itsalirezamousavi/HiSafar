These two Python files, `Admin.py` and `User.py`, are part of a travel management system built using the PyQt5 library for the graphical user interface (GUI). The system allows administrators to manage travel information and users to search, book, and cancel travel tickets.

### **Admin.py**
- **Purpose**: This file handles the administrative side of the travel management system.
- **Key Features**:
  - **Add Travel**: Admins can add new travel details, including source, destination, date, time, capacity, travel number, and price.
  - **Remove Travel**: Admins can remove existing travel entries by searching for the travel number.
  - **Edit Travel**: Admins can edit existing travel details.
  - **Show Travels**: Admins can view all available travel options, filtered by source and destination.
  - **Login System**: Admins must log in with a username and password to access the admin panel.

### **User.py**
- **Purpose**: This file handles the user-facing side of the travel management system.
- **Key Features**:
  - **User Login/Signup**: Users can log in or sign up to access the system. User credentials are stored in a CSV file.
  - **Search Travels**: Users can search for available travels based on source, destination, and sorting criteria (price or date).
  - **Last-Minute Travels**: Displays last-minute travel options for the current date.
  - **Buy Tickets**: Logged-in users can purchase tickets for selected travels.
  - **Cancel Tickets**: Users can cancel their booked tickets.
  - **Logout**: Users can log out of the system.

### **Common Features**:
- Both files use CSV files (`trvl.db` for travel data and `up.db` for user data) to store and retrieve information.
- The GUI is built using PyQt5, providing a user-friendly interface for both admins and users.
- The system supports multiple locations and allows filtering and sorting of travel options.

These files together form a complete travel management system where admins can manage travel data, and users can search, book, and cancel travel tickets.
