# Viren-Simulation
#### Finn, Thomas, Luca, Arne, Alex, Jakob, Marius, Stefan, Halil
## API Endpoints
- `/api/results` - POSTing to this endpoint will create the user
- `/api/results/:id` - GETting this will return user data, PUTting will update the user, and DELETEing will _delete_ the user
- `/api/timer/fertig` - Frontend should POST to this endpoint once their 30 minute timer has expired, the request.form should include the session storage variables
- `/api/timer/started` - Frontend should POST to this endpoint once their 30 minute timer has started, backend will create a column in the database for the user with 0 values for `cookies`, `viren` and `phishing`

## Installation Guide
- Clone the repository. `git clone https://github.com/Jugendhackt/Viren-Simulation.git`
- Install the dependencies. `pip install -r requirements.txt`
- Run the server. `python3 flask/app.py`
- Open the website. `http://localhost:5000/`