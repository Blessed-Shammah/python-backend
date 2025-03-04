# Email Finder using Hunter API

## Check it out here https://python-backend-nv3v.onrender.com/
---

## Overview

The **Email Finder Web App** is a Flask-based web application that leverages the [Hunter.io API](https://hunter.io/api) to scrape email addresses, names, and job titles associated with a given domain and company name. Users can input a domain (e.g., `x.com`) and a company name (e.g., `X`), and the app fetches relevant contact data, displays it in a table, and generates a downloadable CSV file with the results. This tool is ideal for lead generation, recruitment, or market research.

The app is designed to be lightweight, secure (with API keys stored in environment variables), and deployable online (e.g., on Render) or run locally.

---

## Features

- **Web Interface**: Simple HTML form for entering domain and company name, with results displayed in a styled table.
- **Hunter.io Integration**: Uses the Hunter.io Domain Search API to fetch email data.
- **CSV Export**: Saves results to a company-specific folder and provides a download link.
- **Secure Configuration**: API key is managed via a `.env` file locally and environment variables in production.
- **Error Handling**: Displays user-friendly error messages for API failures or invalid inputs.

---

## Prerequisites

To run this app locally, ensure you have the following installed:
- **Python 3.8+**: The app is written in Python.
- **Git**: For cloning the repository (optional if you’re setting up manually).
- **Hunter.io API Key**: Sign up at [Hunter.io](https://hunter.io) to get a free API key (50 requests/month on the free tier).

---

## Project Structure

```
email-finder/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── templates/          # HTML templates
│   └── index.html      # Frontend template
├── .env                # Environment variables (not in Git)
└── .gitignore          # Git ignore file
```

---

## Setup Instructions (Local)

Follow these steps to set up and run the app on your local machine:

### 1. Clone the Repository (Optional)
If you’re using a Git repository:
```bash
git clone [https://github.com/Blessed-Shammah/python-backend.git](https://github.com/Blessed-Shammah/python-backend.git)
cd email-finder
```
Alternatively, manually download and extract the project files.

### 2. Create a Virtual Environment
Set up a Python virtual environment to isolate dependencies:
```bash
python -m venv venv
```
Activate it:
- **Windows**: `venv\Scripts\activate`
- **Mac/Linux**: `source venv/bin/activate`

### 3. Install Dependencies
Install the required Python packages:
```bash
pip install -r requirements.txt
```
This installs:
- `flask`: Web framework
- `requests`: For API calls
- `gunicorn`: WSGI server (optional for local, required for hosting)
- `python-dotenv`: For loading `.env` variables

### 4. Configure the API Key
Create a `.env` file in the project root:
```bash
touch .env
```
Add your Hunter.io API key:
```
HUNTER_API_KEY=your-api-key-here
```
Replace `your-api-key-here` with your actual Hunter.io API key.

### 5. Run the Application
Start the Flask development server:
```bash
python app.py
```
The app will run on `http://localhost:5000`.

### 6. Access the App
Open your browser and go to `http://localhost:5000`. Enter a domain (e.g., `x.com`) and company name (e.g., `X`), then click "Find Emails" to see results.

---

## How It Works

1. **User Input**: The `index()` route handles GET (display form) and POST (process input) requests.
2. **API Call**: The `find_emails()` function queries the Hunter.io API with the provided domain and API key.
3. **Data Processing**: Results are parsed into a list of dictionaries (name, email, job title, etc.).
4. **Display & Export**: Results are rendered in an HTML table, and a CSV file is generated in a company-specific folder (e.g., `X/X_contacts.csv`).
5. **Download**: The `/download/<path:csv_path>` route serves the CSV file to the user.

---

## Example Usage

- **Input**: 
  - Domain: `x.com`
  - Company Name: `X`
- **Output**: A table with columns like:
  ```
  First Name | Last Name | Email          | Job Title      | Company
  John       | Doe       | john@x.com     | Engineer       | X
  Jane       | Smith     | jane@x.com     | Manager        | X
  ```
- **CSV**: Downloadable file `X/X_contacts.csv` with the same data.

---

## Troubleshooting

- **"API key not found"**: Ensure the `.env` file exists and contains `HUNTER_API_KEY`.
- **No results**: Check the domain format (e.g., use `x.com`, not `https://x.com`) and your Hunter.io API quota.
- **Port in use**: Change the port in `app.run(port=5001)` if `5000` is occupied.

---

## Deployment (Optional)

To host online (e.g., on Render):
1. Push the code to a GitHub repository (ensure `.env` is in `.gitignore`).
2. Set up a Render Web Service with:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
   - Environment Variable: `HUNTER_API_KEY=your-api-key-here`
3. Deploy and access the live URL.

---

## Limitations

- **Hunter.io Free Tier**: Limited to 50 requests/month.
- **Local Storage**: CSV files are stored locally; deployed versions may need adjustments for persistent storage.
- **Input Validation**: Basic validation; enhance for production use.

---

## Contributing

Feel free to fork this repository, submit pull requests, or suggest improvements via issues!

---

## License

This project is unlicensed—use it freely, but keep your API keys secure!
