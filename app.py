from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

SMTP_SERVER =  'smtp.gmail.com'  # Enter your SMTP server
SMTP_PORT = 587  # Common port for SMTP
SMTP_USERNAME = 'bacanidonnamae452@gmail.com'  # Your email
SMTP_PASSWORD = 'aiyk zgfe cauw qqln'  # Your email password


@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.json

    if 'message' not in data or 'email' not in data:
        return jsonify({'error': 'Missing message or email'}), 400

    message = data['message']
    recipient_email = data['email']

    try:
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = SMTP_USERNAME
        msg['To'] = recipient_email
        msg['Subject'] = 'this email is from Flask'

        # Add message body
        msg.attach(MIMEText(message, 'plain'))

        # Send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(SMTP_USERNAME, recipient_email, msg.as_string())

        return jsonify({'message': 'Email sent successfully'}), 200

    except Exception as e:
        return jsonify({'error': 'Failed to send email'}), 500

if __name__ == '__main__':
    app.run(debug=True)