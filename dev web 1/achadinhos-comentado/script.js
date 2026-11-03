// =====================================================
// script.js - JavaScript da página "Sobre nós"
// Usa só o que foi visto em aula: variáveis, if/else,
// DOM e eventos.
// =====================================================


// PASSO 1: SELECIONAR os elementos que vamos usar.
// querySelector usa o mesmo seletor do CSS (#id).
const saudacao   = document.querySelector("#saudacao");     // ele procura no HTML a tag que possua o parametro id="saudacao"
const botaoTema  = document.querySelector("#btn-tema");     // procura a tag que possua o id="btn-tema"
const formulario = document.querySelector("#formulario");   // procura a tag que possua o id="formulario"
const campoNome  = document.querySelector("#nome");         // procura a tag que possua o id="nome"
const campoRecado = document.querySelector("#recado");      // procura a tag que possua o id="recado"
const mensagem   = document.querySelector("#mensagem");     // procura a tag que possua o id="mensagem"


// -----------------------------------------------------
// RECURSO 1: SAUDAÇÃO POR HORÁRIO (variável + if/else)
// -----------------------------------------------------
const hora = new Date().getHours(); // hora de agora (0 a 23) - obtem a hora atual do computador
let texto;                          // "let" porque o valor muda

if (hora < 12) {                    // confere a hora obtida e define qual saudacao mostrar
  texto = "Bom dia!";
} else if (hora < 18) {
  texto = "Boa tarde!";
} else {
  texto = "Boa noite!";
}

// textContent troca o texto do elemento: isso é mexer no DOM.
// Este mesmo script roda em TODAS as páginas. Como nem toda página
// tem #saudacao, primeiro conferimos se o elemento existe (senão dá erro).
if (saudacao) {
  saudacao.textContent = texto + " Que bom ter você por aqui."; // concatena a saudacao como uma mensagem extra
}


// -----------------------------------------------------
// RECURSO 2: MODO ESCURO (evento de clique)
// -----------------------------------------------------
if (botaoTema) botaoTema.addEventListener("click", function () { // confere se o botão existe, se sim, adiciona uma função ao clicar nele

  // toggle: se a classe existe, tira; se não existe, coloca.
  // O CSS (body.escuro) cuida do visual.
  document.body.classList.toggle("escuro");           // adiciona ou remove a class="escuro" da tag <body>

  // O texto do botão acompanha o estado atual.
  if (document.body.classList.contains("escuro")) {   // confere se o <body> possui a class="escuro"
    botaoTema.textContent = "☀️ Modo claro";          // troca o texto e icone do botão para claro
  } else {
    botaoTema.textContent = "🌙 Modo escuro";         // troca o texto e icone do botão para escuro
  }
});


// -----------------------------------------------------
// RECURSO 3: VALIDAÇÃO DO FORMULÁRIO (evento submit)
// -----------------------------------------------------
// Só existe na página Sobre nós; as outras usam a validação do HTML.
if (formulario) formulario.addEventListener("submit", function (evento) {

  // Impede o envio padrão: quem decide agora é o nosso código.
  evento.preventDefault();

  // trim() tira espaços das pontas ("   " conta como vazio).
  const nome   = campoNome.value.trim();
  const recado = campoRecado.value.trim();

  // Começa limpando marcas de erro de tentativas anteriores.
  campoNome.classList.remove("campo-invalido");
  campoRecado.classList.remove("campo-invalido");

  if (nome === "") {
    mensagem.textContent = "Por favor, digite seu nome.";     // o campo mensagem inicia vazio, e só mostra a mensagem caso o usuario não digite o nome
    mensagem.className = "erro";                              // coloca a class="erro" na tag que possui o id="mensagem"
    campoNome.classList.add("campo-invalido");                // coloca a class="campo-invalido" na tag que possui o id="nome"

  } else if (recado === "") {
    mensagem.textContent = "Escreva um recado para a gente.";
    mensagem.className = "erro";
    campoRecado.classList.add("campo-invalido");

  } else { // se não houver erros, ele gera uma confirmação de envio
    mensagem.textContent = "Obrigado, " + nome + "! Recebemos seu recado.";
    mensagem.className = "sucesso";
    formulario.reset(); // limpa os campos
  }
});
/*
      Observação: nenhum dos valores inseridos no formulário estão sendo armazenado nesse exemplo, 
      as informações só existem enquanto a página estiver rodando, logo os dados são volateis
*/


// Dica de debug: aparece no Console do DevTools (F12).
console.log("script.js carregado! Hora atual:", hora);
