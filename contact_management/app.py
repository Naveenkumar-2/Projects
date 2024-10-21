from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database setup
def init_db():
    conn = sqlite3.connect('contact.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    conn = sqlite3.connect('contact.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts")
    contacts = cursor.fetchall()
    conn.close()
    return render_template('index.html', contacts=contacts)

@app.route('/add', methods=['GET', 'POST'])
def add_contact():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']

        conn = sqlite3.connect('contact.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)", (name, phone, email))
        conn.commit()
        conn.close()

        flash('Contact added successfully!')
        return redirect(url_for('index'))

    return render_template('add_contact.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_contact(id):
    conn = sqlite3.connect('contact.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts WHERE id=?", (id,))
    contact = cursor.fetchone()

    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        
        cursor.execute("UPDATE contacts SET name=?, phone=?, email=? WHERE id=?", (name, phone, email, id))
        conn.commit()
        conn.close()

        flash('Contact updated successfully!')
        return redirect(url_for('index'))

    return render_template('edit_contact.html', contact=contact)

@app.route('/delete/<int:id>')
def delete_contact(id):
    conn = sqlite3.connect('contact.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM contacts WHERE id=?", (id,))
    conn.commit()
    conn.close()

    flash('Contact deleted successfully!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
