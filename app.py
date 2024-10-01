from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message

import os
secret_key = os.urandom(24)
print(secret_key)


app = Flask(__name__)
app.secret_key = b"\xf9k\xb92#\xe3\xcc\xce\x7f!\xf1\xa5'A\xae\xb0B\xe4Z\xe4\xb8\xc5f\xc8"

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'jaspreetnarang83@gmail.com'
app.config['MAIL_PASSWORD'] = 'bool zsyj bzou scqt'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    if name and email and message:
        # Create the email message
        msg = Message(subject=f"New message from {name}",
                      sender=email,
                      recipients=['jaspreetnarang83@gmail.com'])  # your email to receive the contact messages
        msg.body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        
        try:
            mail.send(msg)
            flash('Message sent successfully!', 'success')
            print('Email sent successfully!')
        except Exception as e:
            print(f"Error sending email: {e}")  # Log the error
            flash('Failed to send message. Please try again later.', 'danger')
    else:
        flash('All fields are required.', 'danger')

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)

