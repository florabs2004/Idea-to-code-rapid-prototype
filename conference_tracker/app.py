from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# In-memory storage for events
# Each event is a dictionary:
# {
#     'id': int,
#     'title': str,
#     'presenter': str,
#     'event_date': str (YYYY-MM-DD),
#     'start_time': str (HH:MM),
#     'location': str,
#     'description': str
# }
events = []
next_id = 1

@app.route('/')
def dashboard():
    """Display the list of upcoming events sorted by date and time."""
    # Sort events by date then time
    sorted_events = sorted(events, key=lambda x: (x['event_date'], x['start_time']))
    return render_template('dashboard.html', events=sorted_events)

@app.route('/add', methods=['GET', 'POST'])
def add_event():
    """Handle adding a new conference event."""
    global next_id
    if request.method == 'POST':
        new_event = {
            'id': next_id,
            'title': request.form.get('title'),
            'presenter': request.form.get('presenter'),
            'event_date': request.form.get('event_date'),
            'start_time': request.form.get('start_time'),
            'location': request.form.get('location'),
            'description': request.form.get('description')
        }
        events.append(new_event)
        next_id += 1
        return redirect(url_for('dashboard'))
    
    return render_template('add_event.html')

@app.route('/event/<int:event_id>')
def event_details(event_id):
    """View details for a specific event."""
    event = next((e for e in events if e['id'] == event_id), None)
    if event is None:
        return "Event not found", 404
    return render_template('event_details.html', event=event)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
