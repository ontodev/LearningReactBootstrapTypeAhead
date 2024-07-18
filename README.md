1. Run the following commands:

```
npx create-react-app from_scratch
cd from_scratch
npm install --save react-bootstrap-typeahead
```

2. Edit `src/App.js` so that it has the following contents:
```
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

3. Run `npm start` and then in your browser navigate to localhost:3000 (in fact npm should open your page automatically but you can navigate there manually in case it does not).
