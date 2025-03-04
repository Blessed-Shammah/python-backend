# app.py
from flask import Flask, request, render_template, send_file
import requests
import os
import csv
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Access the API key from environment variables
API_KEY = os.getenv('HUNTER_API_KEY')

def find_emails(domain, company_name):
    """
    Fetch emails using Hunter.io API and return data for display or CSV.
    """
    if not API_KEY:
        return "API key not found. Please set HUNTER_API_KEY in your environment."
    
    url = f'https://api.hunter.io/v2/domain-search?domain={domain}&api_key={API_KEY}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if data.get('data', {}).get('emails'):
            results = []
            for email_info in data['data']['emails']:
                first_name = email_info.get('first_name', 'N/A')
                last_name = email_info.get('last_name', 'N/A')
                email = email_info.get('value', 'N/A')
                job_title = email_info.get('position', 'N/A')
                results.append({
                    'first_name': first_name,
                    'last_name': last_name,
                    'email': email,
                    'job_title': job_title,
                    'company': company_name
                })
            return results
        return None
    except requests.exceptions.RequestException as e:
        return str(e)

@app.route('/', methods=['GET', 'POST'])
def index():
    results = None
    csv_path = None
    error = None

    if request.method == 'POST':
        domain = request.form.get('domain')
        company_name = request.form.get('company_name')

        if domain and company_name:
            results = find_emails(domain, company_name)
            if isinstance(results, str):  # Error case
                error = results
                results = None
            elif results:
                # Generate CSV in memory
                folder_name = company_name.replace(" ", "_")
                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)
                csv_path = os.path.join(folder_name, f"{folder_name}_contacts.csv")
                with open(csv_path, mode='w', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow(["First Name", "Last Name", "Email", "Job Title", "Company"])
                    for result in results:
                        writer.writerow([
                            result['first_name'], result['last_name'],
                            result['email'], result['job_title'], result['company']
                        ])
            else:
                error = f"No emails found for {company_name} ({domain})."
        else:
            error = "Please provide both domain and company name."

    return render_template('index.html', results=results, csv_path=csv_path, error=error)

@app.route('/download/<path:csv_path>')
def download_csv(csv_path):
    return send_file(csv_path, as_attachment=True)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)