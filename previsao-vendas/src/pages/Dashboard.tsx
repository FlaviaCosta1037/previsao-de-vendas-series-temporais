// src/pages/Dashboard.tsx
import React, { useState } from 'react';

const Dashboard = () => {
  const [previsao, setPrevisao] = useState<number[]>([]); // ← define o estado

  const handleUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await fetch('http://localhost:8000/prever', {
        method: 'POST',
        body: formData,
      });

      const data = await response.json();

      if (data.previsao) {
        setPrevisao(data.previsao);
      } else {
        alert("Erro: " + data.erro);
      }
    } catch (error) {
      console.error('Erro ao enviar arquivo:', error);
    }
  };

  return (
    <div style={{ padding: '2rem' }}>
      <h1>Previsão de Vendas</h1>

      <input type="file" accept=".xlsx" onChange={handleUpload} />

      {previsao.length > 0 && (
        <div style={{ marginTop: '2rem' }}>
          <h3>Previsão dos próximos 3 meses:</h3>
          <ul>
            {previsao.map((valor, index) => (
              <li key={index}>Mês {index + 1}: {valor}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default Dashboard;
