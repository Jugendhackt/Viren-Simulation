# Viren-Simulation
[![CodeQL](https://github.com/Jugendhackt/Viren-Simulation/actions/workflows/codeql.yml/badge.svg)](https://github.com/Jugendhackt/Viren-Simulation/actions/workflows/codeql.yml)
#### Finn, Thomas, Luca, Arne, Alex, Jakob, Marius, Stefan, Halil
## Installation Virus-Simulator
#### `git clone https://github.com/Jugendhackt/Viren-Simulation.git`
#### `./setup.sh`
## API Endpoints
- `/api/results` - POSTing to this endpoint will create the user
- `/api/results/:id` - GETting this will return user data, PUTting will update the user, and DELETEing will _delete_ the user
- `/api/timer/fertig` - Frontend should POST to this endpoint once their 30 minute timer has expired, the request.form should include the session storage variables
- `/api/timer/started` - Frontend should POST to this endpoint once their 30 minute timer has started, backend will create a column in the database for the user with 0 values for `cookies`, `viren` and `phishing`
