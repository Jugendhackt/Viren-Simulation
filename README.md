# Viren-Simulation
[![CodeQL](https://github.com/Jugendhackt/Viren-Simulation/actions/workflows/codeql.yml/badge.svg)](https://github.com/Jugendhackt/Viren-Simulation/actions/workflows/codeql.yml)
[![Python application](https://github.com/Jugendhackt/Viren-Simulation/actions/workflows/python-app.yml/badge.svg)](https://github.com/Jugendhackt/Viren-Simulation/actions/workflows/python-app.yml)
#### [Finn](www.github.com/fingadumbledore), [Thomas](www.github.com/hyperbel), [Luca](www.github.com/erase01), [Arne](www.github.com/amxx1679), Alex, [Jakob](www.github.com/ferox123), [Marius](www.github.com/gnome79), [Stefan](www.github.com/stefan1293), [Halil](www.github.com/connordoesdev)
## Installation Virus-Simulator
#### `git clone https://github.com/Jugendhackt/Viren-Simulation.git`
#### `./setup.sh`
## API Endpoints
- `/api/results` - POSTing to this endpoint will create the user
- `/api/results/:id` - GETting this will return user data, PUTting will update the user, and DELETEing will _delete_ the user
- `/api/timer/fertig` - Frontend should POST to this endpoint once their 30 minute timer has expired, the request.form should include the session storage variables
- `/api/timer/started` - Frontend should POST to this endpoint once their 30 minute timer has started, backend will create a column in the database for the user with 0 values for `cookies`, `viren` and `phishing`
