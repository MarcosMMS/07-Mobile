function exibir(produto){
    return `Produto: ${produto.nome}, Preco: R$${produto.preco.toFixed(2)},
    Estoque: ${produto.estoque} unidades.`
}

const carro = {
    nome: "bmw",
    preco: 10000000,
    estoque: 2
}

console.log(exibir(carro))