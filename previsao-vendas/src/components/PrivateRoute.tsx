import { JSX, useContext } from 'react';
import { Navigate } from 'react-router-dom';
import { AuthContext } from '../context/AuthContext';

const PrivateRoute = ({ children }: { children: JSX.Element }) => {
  const { user, loading } = useContext(AuthContext);

  if (loading) return <p>Carregando...</p>;

  return user ? children : <Navigate to="/" />;
};

export default PrivateRoute;
