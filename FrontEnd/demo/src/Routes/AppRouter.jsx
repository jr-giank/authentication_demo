import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { LoginPage } from '../Pages/LoginPage';
import { Home } from '../Pages/Home';
import { AppContext } from '../Context/AuthContext';
import { InitialState } from '../Context/InitialState';
import { PrivateRoute } from './PrivatesRoutes';

export const AppRouter = () => {
    return(
        <AppContext.Provider value={InitialState()}>
            <Router>
                <Routes>
                    <Route exact path='login/' element={<LoginPage/>}/>
                    <Route exact path='/' element={<PrivateRoute/>}>
                        <Route exact path='/' element={<Home/>}/>
                    </Route>
                </Routes>
            </Router>
        </AppContext.Provider>
    )
}