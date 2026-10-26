//  comentário curto

/* comentário longo */

/* 
    anotações adicionais:
    - o js exige o uso de ponto e virgula ao fim de cada linha, pra que ele saiba onde uma instrução termina e onde começa uma nova
    - declarações d evariaveis utilizam: let, const e var
        - dos 3, apenas o const não permite a mudança de valor após a atribuição
    - typeof mostra o tipo do valor dentro da variavel
    - aspas simples e duplas são aceitas

    - uso de operadores matematicos e aritmeticos:
    + - * / % //

    - operadores relacionais:
    < > <= >= === !==

    - operadores lógicos:
    and -> &&, or -> ||, not -> !
*/


// imprime a msg na tela, equivale ao print do python. Pra ver essa mensagem, precisamos abrir o console do navegador (F12 -> console)
console.log("hello world"); 

// declaração de variaveis no JS
var nome = "junin";
const cpf = '00000000000';
let idade = 23;

// impressão de valores (igual ao python)
// separado:
console.log(nome);
console.log(cpf);
console.log(typeof idade);

// junto:
console.log(nome, cpf, idade); // vai aparecer um do lado do outro

// concatenação dentro do c.log
console.log(`hello, ${nome}`); // requer o uso de crase ``

// usando if - else com apenas um parametro:
let media = 9;
if(media >= 6){
    console.log('aprovado');
}
else if(media >= 4){
    console.log("de recuperação");
}
else{
    console.log("reprovado");
};

// usando if - else com mais de um parametro:
let faltas = 15;

if(media >= 6 && faltas <= 20){
    console.log('aprovado por nota e frequencia');
};