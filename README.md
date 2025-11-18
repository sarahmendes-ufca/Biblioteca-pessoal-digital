# Biblioteca-pessoal-digital
A Biblioteca Pessoal é um projeto que permite gerenciar  livros e revistas digitais, autoriza o cadastro de publicações, o registro de leituras, o controle de status e a geração de relatórios sobre o acervo. O projeto foi desenvolvido na como parte da disciplina de Programação Orientada à Objetos. 

# UML Textual

| Classe | Atributos | Métodos | Relacionamentos|
|---- | ---- | ---- | ----|
| Publicacao | id_publicacao, titulo, autor, ano, tipo, genero, numero_de_paginas, nota_avaliacao, status_leitura, avaliacao | @property título, @titulo.setter, @property ano, @ano.setter, @property nota_avaliacao, @nota_avaliacao.setter, CRUD | 
| Anotacao | texto, trecho, data | adicionar_anotacao, listar_anotacaoes | - |
