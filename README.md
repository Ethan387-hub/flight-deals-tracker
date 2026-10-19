#  Flight Deals Tracker

A Python application that searches for affordable flights, compares prices against target prices stored in Google Sheets, updates the spreadsheet when a cheaper flight is found, and sends email notifications about flight deals.

This project was built to practise Python, object-oriented programming, API integration, data processing, and working with external services.

##  Features

* **Flight Search:** Searches for available flights using SerpApi and Google Flights.
* **Price Comparison:** Compares the cheapest returned flight option against the target price for each destination.
* **Google Sheets Integration:** Retrieves destination information and updates target prices using Sheety.
* **Email Notifications:** Sends email alerts containing flight details when a cheaper deal is found.
* **Modular Design:** Separates flight searching, data management, flight information, and email notifications into different Python modules.
* **Environment Variables:** Keeps API keys and credentials outside the Python source code.

##  Technologies Used

* Python
* Requests
* SerpApi
* Sheety
* Google Sheets
* SMTP and Gmail
* python-dotenv
* Git and GitHub

##  Project Structure

```text
flight-tracker/
│
├── main.py
├── flight_search.py
├── data_manager.py
├── flight_data.py
├── notification_manager.py
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

### Python Modules

| File                      | Responsibility                                                                           |
| ------------------------- | ---------------------------------------------------------------------------------------- |
| `main.py`                 | Coordinates the flight search, price comparison, spreadsheet updates, and notifications. |
| `flight_search.py`        | Searches for flights through the SerpApi API.                                            |
| `data_manager.py`         | Retrieves destination data and updates prices using Sheety.                              |
| `flight_data.py`          | Stores information about a flight deal using a Python class.                             |
| `notification_manager.py` | Sends email notifications about cheaper flights.                                         |

##  Getting Started

### Prerequisites

Before running the application, you will need:

* Python installed on your computer.
* A SerpApi API key.
* A Sheety account and an accessible Google Sheets integration.
* A Gmail account configured to send email through an app password.

### 1. Clone the Repository

```bash
git clone https://github.com/Ethan387-hub/flight-deals-tracker.git
```

Navigate into the project directory:

```bash
cd flight-deals-tracker
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create your local `.env` file by copying the example template.

On Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

Open `.env` and replace the placeholder values with your own credentials:

```dotenv
SERPAPI_KEY=your_serpapi_key

SHEETY_USERNAME=your_sheety_username
SHEETY_PASSWORD=your_sheety_password
SHEETY_URL=your_sheety_endpoint

GMAIL_ADDRESS=your_gmail_address
GMAIL_APP_PASSWORD=your_gmail_app_password
RECIPIENT_EMAIL=your_recipient_email
```

Use the exact variable names expected by the application.

**Never commit your `.env` file or publish your real API keys, passwords, or other secrets.**

### 5. Configure Your Destination Spreadsheet

Set up your Google Sheet and Sheety integration so the application can retrieve destination information and update prices.

Ensure the spreadsheet contains the destination fields expected by the application, including the city, IATA airport code, and target price.

Configure the Sheety endpoint and credentials in your `.env` file.

### 6. Run the Application

```bash
python main.py
```

The application will search for flights for the configured destinations, compare the returned prices against the target prices, update the spreadsheet when a cheaper deal is found, and send email notifications for the deals collected.

##  Security

* API keys and credentials are stored in a local `.env` file.
* `.gitignore` prevents local secrets and unnecessary development files from being tracked.
* `.env.example` documents the required configuration without containing actual credentials.

Always keep your credentials private.

## Current Limitations

* Flight search dates and the departure airport are configured in the application code.
* Flight results depend on the availability and coverage of the external flight-search API.
* Email delivery depends on the Gmail SMTP configuration and valid credentials.
* The application compares the returned flight options; it does not guarantee that every available flight has been searched.

##  Learning Objectives

This project provided practical experience with:

* Python classes and objects.
* Modular programming and separation of responsibilities.
* HTTP requests and JSON responses.
* Third-party API integration.
* Finding and comparing data.
* Sending emails with SMTP.
* Environment variables and credential management.
* Git version control and GitHub.

##Author

**Ethan Kim**

GitHub: [@Ethan387-hub](https://github.com/Ethan387-hub)
