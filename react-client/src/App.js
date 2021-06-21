import logo from './logo.svg';
import {BrowserRouter as Router, Route, Switch} from 'react-router-dom';
import './App.css';

import Dashboard from './components/Dashboard/Dashboard';


function App() {
  return (

    <Router>
      <div className="App">
        <Route exact path="/" component={Dashboard}></Route>
      </div>

    </Router>

    
  );
}

export default App;
