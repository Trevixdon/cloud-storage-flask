from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory list to simulate file storage (each item is just a filename)
files = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Simulate file upload by capturing a filename from the form (text input)
        filename = request.form.get('filename')
        if filename:
            files.append(filename)
    return render_template('index.html', files=files)

@app.route('/update/<int:index>', methods=['GET', 'POST'])
def update(index):
    if index < len(files):
        if request.method == 'POST':
            # Simulate update by modifying the filename
            new_name = request.form.get('filename')
            if new_name:
                files[index] = new_name
                return redirect(url_for('index'))
        # Render update form with the current filename
        return render_template('update.html', filename=files[index], index=index)
    return redirect(url_for('index'))

@app.route('/delete/<int:index>', methods=['POST'])
def delete(index):
    if index < len(files):
        files.pop(index)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
