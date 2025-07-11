// src/pages/Login.tsx
import React from 'react';
import { useNavigate } from 'react-router-dom';

const Login = () => {
  const navigate = useNavigate();

  const handleLogin = () => {
    // Simulação de login
    navigate('/dashboard');
  };

  return (
    <div>
      <h2>Login</h2>
      <button onClick={handleLogin}>Entrar</button>
    </div>
  );
};

export default Login;
