# Biblioteca-pessoal-digital
A Biblioteca Pessoal é um projeto que permite gerenciar  livros e revistas digitais, autoriza o cadastro de publicações, o registro de leituras, o controle de status e a geração de relatórios sobre o acervo. O projeto foi desenvolvido na como parte da disciplina de Programação Orientada à Objetos. 

# UML Textual

| Classe | Atributos | Métodos | Relacionamentos|
|---- | ---- | ---- | ----|
| Publicacao | id_publicacao, titulo, autor, ano, tipo, genero, numero_de_paginas, nota_avaliacao, status_leitura, avaliacao | @property título, @titulo.setter, @property ano, @ano.setter, @property nota_avaliacao, @nota_avaliacao.setter, CRUD | Colecao, Relatorio, Leitura |
| Anotacao | texto, trecho, data | adicionar_anotacao, listar_anotacaoes | - |
| Leitura | NÃO_LIDO, LENDO, LIDO | status_leitura, iniciar_leitura, concluir_leitura | Colecao, Relatorio |
| Colecao | publicacoes | adicionar_publicacao, buscar_por_titulo, buscar_por_autor, buscar_por_genero, filtrar_por_status, filtrar_por_periodo, total_publicacoes, publicacoes_lidas, media_avaliacoes | Publicacao, Usuario |
| Configuracao | genero_favorito, limite_paginas_leitura_simultanea, meta_leitura_anual | carregar_json, salvar_em_json | Publicacao |
| Usuario | nome, colecao, configuracao | carregar_configuracoes, salvar_configuracoes | Colecao, Configuracao |
| Relatorio | - | total_publicacoes, publicacoes_lidas, media_avaliacoes, percentual_por_status, top5_avaliacoes | Publicacao, Colecao

# Estrutura de Diretórios

/BibliotecaPessoal
├── /CLI
│   ├─── init.py
│   ├─── anotacao_cli.py
│   ├─── colecao_cli.py
│   ├─── configuracao_cli.py
│   ├─── leitura_cli.py
│   ├─── livro_cli.py
│   ├─── obra_cli.py
│   ├─── relatorio_cli.py
│   ├─── revista_cli.py
│   ├─── status_cli.py
│   └─── utils_cli.py
├── /graphics
│    ├─── Media de avaliacaoes de Obras Lidas.png
│    ├─── Número Total de Obras.png
│    └─── Porcentagem de Livros por Status de Leitura.png
├── /models
│   ├─── init.py
│   ├─── anotacao.py
│   ├─── colecao.py
│   ├─── conexao.py
│   ├─── configuracao.py
│   ├─── leitura.py
│   ├─── livro.py
│   ├─── obra.py
│   ├─── relatorio.py
│   ├─── revista.py
│   └─── status.py
├── .gitignore
├── biblioteca.db
├── main.py
├── README.md
├── requirements.txt
└── settings.json
