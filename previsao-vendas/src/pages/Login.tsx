// src/pages/Login.tsx
import React, { useState } from 'react';
import { Container, Card, Button, Form, Alert } from 'react-bootstrap';
import { signInWithPopup, signInWithEmailAndPassword } from 'firebase/auth';
import { auth, provider } from '../lib/firebase';
import { useNavigate } from 'react-router-dom';

const Login = () => {
  const [email, setEmail] = useState('');
  const [senha, setSenha] = useState('');
  const [erro, setErro] = useState('');
  const navigate = useNavigate();

  const loginGoogle = async () => {
    try {
      await signInWithPopup(auth, provider);
      navigate('/dashboard');
    } catch (err) {
      setErro('Erro ao entrar com Google');
    }
  };

  const loginEmailSenha = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await signInWithEmailAndPassword(auth, email, senha);
      navigate('/dashboard');
    } catch (err) {
      setErro('Email ou senha inválidos');
    }
  };

  return (
    <Container className="d-flex justify-content-center align-items-center vh-100">
      <Card className="p-4 shadow" style={{ width: '24rem' }}>
        <Card.Body>
          <Card.Title className="text-center mb-4">Login</Card.Title>

          {erro && <Alert variant="danger">{erro}</Alert>}

          <Form onSubmit={loginEmailSenha}>
            <Form.Group className="mb-3">
              <Form.Label>Email</Form.Label>
              <Form.Control type="email" value={email} onChange={(e) => setEmail(e.target.value)} required />
            </Form.Group>

            <Form.Group className="mb-3">
              <Form.Label>Senha</Form.Label>
              <Form.Control type="password" value={senha} onChange={(e) => setSenha(e.target.value)} required />
            </Form.Group>

            <Button variant="primary" type="submit" className="w-100 mb-2">
              Entrar com Email/Senha
            </Button>
          </Form>

          <hr />

          <Button variant="danger" className="w-100" onClick={loginGoogle}>
            Entrar com Google
          </Button>
        </Card.Body>
      </Card>
    </Container>
  );
};

export default Login;
