
import React, { useState, useContext } from 'react';
import { Container, Card, Button, Table, Form, Row, Col, Spinner } from 'react-bootstrap';
import { AuthContext } from '../context/AuthContext';
import { signOut } from 'firebase/auth';
import { auth } from '../lib/firebase';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';
import { format } from 'date-fns';
import { ptBR } from 'date-fns/locale';
import { getFirestore, collection, addDoc, Timestamp } from 'firebase/firestore';
import { app } from '../lib/firebase';

const Dashboard = () => {
  const { user } = useContext(AuthContext);
  const [file, setFile] = useState<File | null>(null);
  const [previsao, setPrevisao] = useState<any[]>([]);
  const [loading, setLoading] = useState(false);
  const db = getFirestore(app);

  const handleUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    const selectedFile = e.target.files?.[0];
    if (!selectedFile) return;
    setFile(selectedFile);
  };

  const enviarArquivo = async () => {
    if (!file) return;
    setLoading(true);
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await fetch('http://localhost:8000/prever', {
        method: 'POST',
        body: formData,
      });
      const data = await response.json();

      if (data.previsao) {
        const now = new Date();
        const meses = Array.from({ length: data.previsao.length }, (_, i) => {
          const dataMes = new Date(now.getFullYear(), now.getMonth() + i + 1, 1);
          return format(dataMes, 'MMMM yyyy', { locale: ptBR });
        });

        const dadosGrafico = data.previsao.map((valor: number, idx: number) => ({
          mes: meses[idx],
          unidades: valor,
        }));

        setPrevisao(dadosGrafico);

        // Persistência no Firestore
        await addDoc(collection(db, 'previsoes'), {
          previsao: dadosGrafico,
          criado_em: Timestamp.now(),
          usuario: user?.email || null,
        });
      }
    } catch (err) {
      console.error('Erro ao enviar para backend:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <Container className="py-5">
      <div className="d-flex justify-content-between align-items-center mb-4">
        <h4>Olá, {user?.displayName || user?.email}</h4>
        <Button variant="outline-danger" onClick={() => signOut(auth)}>
          Sair
        </Button>
      </div>

      <Card className="p-4 mb-4">
        <Row className="align-items-center">
          <Col md={8}>
            <Form.Group controlId="formFile">
              <Form.Label>Escolha o arquivo Excel (.xlsx)</Form.Label>
              <Form.Control type="file" accept=".xlsx" onChange={handleUpload} />
            </Form.Group>
          </Col>
          <Col md={4}>
            <Button
              variant="primary"
              className="w-100 mt-4 mt-md-0"
              onClick={enviarArquivo}
              disabled={!file || loading}
            >
              {loading ? <Spinner animation="border" size="sm" /> : 'Enviar'}
            </Button>
          </Col>
        </Row>
      </Card>

      {previsao.length > 0 && (
        <>
      <Card className="p-4 mb-4">
      <h5 className="mb-3">📈 Previsão de Vendas</h5>
      <ResponsiveContainer width="100%" height={350}>
        <LineChart
          data={previsao}
          margin={{ top: 20, right: 30, left: 0, bottom: 5 }}
        >
          <CartesianGrid stroke="#e0e0e0" strokeDasharray="4 4" />
          <XAxis dataKey="mes" tick={{ fontSize: 12 }} />
          <YAxis tick={{ fontSize: 12 }} />
          <Tooltip
            contentStyle={{ backgroundColor: '#f8f9fa', borderColor: '#ccc' }}
            formatter={(value: any) => [`${value} unidades`, 'Previsão']}
            labelStyle={{ fontWeight: 'bold' }}
          />
          <Line
            type="monotone"
            dataKey="unidades"
            stroke="#0d6efd"
            strokeWidth={3}
            dot={{ r: 5, stroke: '#0d6efd', strokeWidth: 2, fill: 'white' }}
            activeDot={{ r: 7 }}
          />
        </LineChart>
      </ResponsiveContainer>
    </Card>

    <Card className="p-4">
      <h5 className="mb-3">📊 Tabela de Previsão</h5>
      <table className="table table-bordered">
        <thead className="table-light">
          <tr>
            <th>Mês</th>
            <th>Unidades Previstas</th>
          </tr>
        </thead>
        <tbody>
          {previsao.map((item, index) => (
            <tr key={index}>
              <td>{item.mes}</td>
              <td>{item.unidades}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </Card>
        </>
      )}
    </Container>
  );
};

export default Dashboard;
