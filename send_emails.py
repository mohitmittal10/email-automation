# Import the necessary libraries for sending emails
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr # To format the 'From' field with a name
import getpass # To securely ask for the password
import os # To check if the required files exist

def send_bulk_emails():
    """
    This function sends an email to multiple recipients individually.
    It reads the recipient list and email body from separate files,
    making the process clean and reusable.
    """
    # --- Debugging line to confirm the script is running ---
    print("--- Email Automation Script Initializing ---") 
    try:
        # --- Define file paths ---
        email_template_path = "email_template.html"
        recipients_path = "recipients.txt"

        # --- Check for required files before starting ---
        if not os.path.exists(email_template_path):
            print(f"\n[ERROR] The email template file '{email_template_path}' was not found.")
            print("Please ensure it is in the same directory as the script.")
            return # Exit if the file is missing
        if not os.path.exists(recipients_path):
            print(f"\n[ERROR] The recipients file '{recipients_path}' was not found.")
            print("Please ensure it is in the same directory as the script.")
            return # Exit if the file is missing

        # --- Get User Input ---
        sender_name = input("Enter your full name (e.g., Mohit Mittal): ")
        sender_email = input("Enter your email address: ")
        password = getpass.getpass("Enter your email password or app password: ")
        subject = input("Enter the email subject: ")
        
        # --- Read Email Body from HTML file ---
        with open(email_template_path, 'r', encoding='utf-8') as file:
            body = file.read()
        print("\n[INFO] Successfully loaded email body from 'email_template.html'.")

        # --- Read Recipients from text file ---
        with open(recipients_path, 'r', encoding='utf-8') as file:
            # Read all lines, strip whitespace, and filter out any empty lines
            recipients = [line.strip() for line in file if line.strip()]
        print(f"[INFO] Successfully loaded {len(recipients)} recipient(s) from 'recipients.txt'.")

        # --- SMTP Server Configuration (for Gmail) ---
        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        # --- Connect to the SMTP server ---
        print("\n[INFO] Connecting to the email server...")
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls() # Secure the connection
        server.login(sender_email, password)
        print("[SUCCESS] Connected and logged in successfully.")

        # --- Loop through recipients and send individual emails ---
        total_emails = len(recipients)
        for i, recipient_email in enumerate(recipients, 1):
            print(f"--> Sending email {i}/{total_emails} to {recipient_email}...")

            # Create the email message object for each recipient
            msg = MIMEMultipart()
            msg['From'] = formataddr((sender_name, sender_email))
            msg['To'] = recipient_email
            msg['Subject'] = subject
            
            # Attach the HTML body
            msg.attach(MIMEText(body, 'html'))

            # Send the email
            server.sendmail(sender_email, recipient_email, msg.as_string())
            print(f"    Email sent to {recipient_email}")

        print("\n[COMPLETE] All emails have been sent successfully!")

    except smtplib.SMTPAuthenticationError:
        print("\n[ERROR] Authentication failed. Please double-check your email and password.")
        print("         If you're using Gmail, you might need to generate an 'App Password'.")
    except Exception as e:
        print(f"\n[ERROR] An unexpected error occurred: {e}")
    finally:
        # Ensure the server connection is closed
        if 'server' in locals() and server.sock:
            server.quit()
            print("[INFO] Disconnected from the server.")

# --- Run the main function when the script is executed ---
if __name__ == "__main__":
    send_bulk_emails()
