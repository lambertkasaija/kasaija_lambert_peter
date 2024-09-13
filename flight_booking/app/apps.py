from flask import Flask, render_template, request, redirect, url_for, flash # type: ignore

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messages

# Home route with booking form
@app.route('/')
def booking_form():
    return render_template('booking.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit_booking():
    # Fetch form data
    name = request.form['name']
    gender = request.form['gender']
    dob = request.form['dob']
    nationality = request.form['nationality']
    phone = request.form['phone']
    email = request.form['email']
    emergency_contact = request.form['emergency_contact']
    passport_number = request.form['passport']
    visa = request.files['visa']
    departure_city = request.form['departure_city']
    destination = request.form['destination']
    
    # Form validation
    if not (name and gender and dob and nationality and phone and email and emergency_contact and passport_number and departure_city and destination):
        flash("All required fields must be filled out.", "error")
        return redirect(url_for('booking_form'))
    
    # Simulate form submission success
    flash("Your booking request has been submitted successfully!", "success")
    
    # Reset form after submission
    return redirect(url_for('booking_form'))

if __name__ == '__main__':
    app.run(debug=True)
