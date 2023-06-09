import { useContext } from 'react';
import { Navigate, Outlet } from 'react-router-dom';
import { AppContext } from '../Context/AuthContext';

export const PrivateRoute = ({children, ...rest}) => {
    let {user} = useContext(AppContext);
    
    return user ? <Outlet /> : <Navigate to="/login" />;
}