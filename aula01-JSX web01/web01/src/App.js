import React from 'react';

const nome = "Marcos Moreira";

const elemento = (
  <div>
    <h1>Olá, {nome}</h1>
    <p>Bem vindo ao ultimo ano do seu curso!!</p>
  </div>
);

function App(){
  return elemento;
}

export default App;