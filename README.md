# To run the minimal example using Flask and Python

1. Run the following commands:
```
python3 -m venv .venv
. .venv/bin/activate
cd from_scratch_minimal
pip3 install -r requirements.txt
npm install
npm run build
make serve
```

2. Point your browser to `localhost:3000`


# Configuring a minimal react app from scratch

1. Run the following commands:

```
npx create-react-app from_scratch
cd from_scratch
npm install react-bootstrap-typeahead
npm install bootstrap@v5.3.3
npm install
```

2. Edit `src/App.js` so that it has the following contents:
```
import 'bootstrap/dist/css/bootstrap.css';
import { Typeahead } from 'react-bootstrap-typeahead';
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <Typeahead
           onChange={(selected) => {
             // Handle selections...
           }}
           options={[ /* Array of objects or strings */ ]}
        />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
```

3. To build and deploy, see the above section on how to do this for the minimal example.
