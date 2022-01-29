// a classe é um molde que vamos usar várias vezes
// é uma boa prática deixar o nome das classes começando com maiúsculo

export class Cliente {
    // atributos (ou propriedades) para TODOS os clientes
    nome;
    _cpf;

    get cpf(){
        // precisamos botar return pq, caso contrário, ele retornará indefinido
        return this._cpf;
    }

    // construtor, passar as informações sem que outra pessoa
    // possa alterar esses dados
    constructor(nome, cpf){
        this.nome = nome;
        this._cpf = cpf;
    }
}