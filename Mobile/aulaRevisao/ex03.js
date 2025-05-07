const pessoa = {
    nome: "marcos",
    idade: 21,
    usuario: "aluno",
    saudar: function(){
        return "oi, meu nome é "+this.nome+" e eu sou um "+this.usuario+"."
    }
}

console.log(pessoa.nome)
console.log(pessoa.saudar())

class Animal{
    constructor(nome, tipo){
    this.nome = nome
    this.tipo = tipo   
    }

exibirInfo(){
    return `Este é o, ${this.tipo} chamado ${this.nome}`
}
}

const cachorro = new Animal("Duck", "cachorro")
const gato = new Animal("Tom", "gato")
console.log(cachorro.exibirInfo())
console.log(gato.exibirInfo())