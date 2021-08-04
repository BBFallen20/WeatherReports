import {BrowserRouter as Router, Switch, Route} from 'react-router-dom';
import {MainPage} from "./pages/MainPage";

function App() {
  return (
    <div className="App">
        <Router>
            <Switch>
                <Route exact path='/' forceRefresh={true} component={MainPage}/>
            </Switch>
        </Router>
    </div>
  );
}

export default App;
