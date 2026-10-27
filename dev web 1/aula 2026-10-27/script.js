/*
    - o number faz o msm que o int no python, porém ele apenas garante q seja um numero, e dps de receber ele escolhe o tipo de numero mais adequado
    - estruturas de controle:
        - condição (if - else)
        - seleção (switch - case)
        - repetição (while, for e Do-while)

    - um lista.length serve para obter o tamanho da lista q está sendo usada
*/

// Estrutura de seleção - switch case (equivalente ao match case do python) - [ NEED FIX ]
let mes = Number(prompt("Informe o mês a ser verificado (apenas numero): ")); // o prompt pega o texto digitado pelo usuario (equivalente ao input())

switch(mes){
    case 1:
    case 3:
    case 5:
    case 7:
    case 8:
    case 10:
    case 12:
        console.log("Mes de 31 dias");
        break;
    case 2:
        console.log('Mes de 28 dias');
        break;
    case 4:
    case 6:
    case 9:
    case 11:
        console.log("Mes de 30 dias");
        break;
    default:
        console.log('mes inválido, só é aceito um número no intervalo de 1 a 12');

};

// estrutura de repetição - for
let soma = 0;

// for (inicio, fim, incremento){
for (let i = 0; i <= 100; i++){
    soma += 1;
};
    console.log(`A soma de 1 a 100 é: ${soma}`);

// for usando listas
let carros = ["volkswagen", "fiat", "honda", "chevrolet"];

for(let i = 0; i < carros.length; i++){
    console.log(carros[i]);
};

// outro jeito de utilizar o for (meio exclusivo do JS)
for(let carro of carros){       // para cada carro em carros...
    console.log(carro);         // ...imprime o carro
};

// while - não há limitador de repetições (pode rodar infinitamente, se vc quiser)
let i , soma2 = 0 // dá pra declarar mais de uma variavel de uma vez, desde que ambas possuam o msm valor inicial e tipo

while(i <= 100){
    soma2 +=1;
    i++;
};
console.log(`A soma de 1 a 100 é: ${soma2}`);

// do - while - ele faz primeiro, e só dps confere a condição
let j , soma3 = 0 // dá pra declarar mais de u

do{
    soma3 +=1;
    j++;
}
while(j <= 100);

console.log(`A soma de 1 a 100 é: ${soma2}`);
