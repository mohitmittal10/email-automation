# Email Automation Script

This project allows you to send personalized emails in bulk using a simple Python script. It reads the email body from an HTML template and the recipient list from a text file.

## Files

- [`send_emails.py`](send_emails.py): Main script to send emails.
- [`email_template.html`](email_template.html): The HTML template for your email body.
- [`recipients.txt`](recipients.txt): List of recipient email addresses (one per line).

## Prerequisites

- Python 3.x installed.
- Access to an SMTP server (e.g., Gmail).
- If using Gmail, you may need to generate an [App Password](https://support.google.com/accounts/answer/185833).

## Setup

1. **Edit `email_template.html`**  
   Customize the email body as needed.

2. **Edit `recipients.txt`**  
   Add the email addresses of your recipients, one per line.

3. **Install Required Libraries**  
   The script uses only Python's standard libraries, so no extra installation is needed.

## Usage

1. Open a terminal in the project directory.
2. Run the script:

   ```sh
   python send_emails.py
   ```

3. Follow the prompts:
   - Enter your full name.
   - Enter your email address.
   - Enter your email password or app password (input is hidden).
   - Enter the email subject.

4. The script will send the email to each recipient individually and display progress in the terminal.

## Notes

- Make sure [`email_template.html`](email_template.html) and [`recipients.txt`](recipients.txt) are in the same directory as [`send_emails.py`](send_emails.py).
- For Gmail, enable "Less secure app access" or use an App Password.
- The script sends emails one by one to avoid exposing recipient addresses.

## Troubleshooting

- **Authentication Error:**  
  Double-check your email and password. For Gmail, use an App Password.
- **File Not Found:**  
  Ensure all required files are present in the directory.

---

Feel free to modify the template and recipient list