Coisas da Le — Loja virtual
Projeto acadêmico de uma loja de roupas desenvolvido com Python e Django. O site possui páginas de início, coleções, novidades, detalhes dos produtos, contato, carrinho e finalização demonstrativa de pedido. O layout utiliza HTML e CSS e foi organizado para se adaptar a telas menores.
Importante: o checkout deste projeto é demonstrativo. Ele não processa pagamentos reais, não se conecta a bancos ou gateways de pagamento e, na implementação atual, os pedidos de demonstração são guardados na sessão do navegador. Não informe dados reais de cartão ou bancários.

1. Requisitos
- Python 3.10 ou superior (recomendado).
- pip, que normalmente já acompanha a instalação do Python.
- Visual Studio Code (opcional, mas recomendado).
- Navegador atualizado.
As dependências Python estão listadas em requirements.txt (Django e Pillow).
2. Como abrir e executar no Windows
1. Baixe e extraia o arquivo ZIP do projeto.
2. Abra o VS Code e selecione Arquivo > Abrir Pasta. Escolha a pasta coisas-da-le, aquela que contém manage.py.
3. Abra o terminal integrado do VS Code (Terminal > Novo Terminal).
4. Crie o ambiente virtual:
   python -m venv venv
5. Ative o ambiente virtual:
   .\venv\Scripts\Activate.ps1
   Se o PowerShell bloquear a ativação, abra o PowerShell nessa pasta e execute, somente para a sessão atual:
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   .\venv\Scripts\Activate.ps1
6. Instale as dependências:
   python -m pip install -r requirements.txt
7. Aplique as migrações do banco de dados:
   python manage.py migrate
8. Inicie o servidor:
   python manage.py runserver
9. Abra no navegador: http://127.0.0.1:8000/.
Para encerrar o servidor, pressione Ctrl + C no terminal. Para sair do ambiente virtual, execute deactivate.
3. Páginas do site
Página	Endereço local	Descrição
Início	/	Página inicial e destaques da loja.
Coleções	/colecoes/	Lista de roupas e filtro por categoria.
Novidades	/novidades/	Exibe os produtos destacados como novidades.
Contato	/contato/	Informações de atendimento e link de WhatsApp de exemplo.
Detalhe do produto	/produto/1/	Informações de uma peça; substitua 1 pelo identificador do produto.
Carrinho	/carrinho/	Lista os itens, permite atualizar quantidades e remover peças.
Pagamento	/pagamento/	Formulário demonstrativo de entrega e escolha da forma de pagamento.
Confirmação	/pedido/confirmado/	Resumo do pedido de demonstração.
Entrar	/conta/entrar/	Login de usuário.
Cadastrar	/conta/cadastrar/	Cadastro de usuário.
Administração	/admin/	Área administrativa do Django.


4. Estrutura principal de pastas
coisas-da-le/
├── config/                 # Configurações e URLs principais do Django
├── core/                   # Aplicativo principal: URLs, views, formulários e modelos
│   ├── migrations/         # Migrações do banco de dados
│   ├── catalogo.py         # Produtos de demonstração exibidos na loja
│   ├── forms.py            # Formulários de cadastro e checkout
│   ├── models.py           # Modelos de roupas e pedidos
│   ├── urls.py             # Endereços das páginas
│   └── views.py            # Lógica das páginas e do carrinho
├── static/
│   └── css/styles.css      # Estilos do site
├── templates/              # Páginas HTML
│   └── registration/       # Templates de login e cadastro
├── manage.py               # Utilitário de comandos do Django
├── requirements.txt        # Dependências Python
└── README.md               # Este guia
5. Como adicionar ou alterar roupas
Na versão demonstrativa atual, os produtos apresentados nas páginas da loja estão cadastrados na lista PRODUTOS, no arquivo core/catalogo.py.

Cada produto possui os campos id, nome, categoria, preco, tamanho, descricao, cor e imagem. Para adicionar uma peça:
1. Abra core/catalogo.py no VS Code.
2. Dentro da lista PRODUTOS, acrescente outro dicionário, usando um id que ainda não exista.
3. Preencha os dados da roupa e salve o arquivo.
4. Atualize a página no navegador.
Os endereços das imagens incluídos no catálogo são exemplos externos e dependem de conexão com a internet. Para usar fotos próprias, configure os arquivos de mídia do Django e atualize os caminhos das imagens.

Observação sobre o banco de dados: o projeto também contém modelos Django em core/models.py, incluindo Roupa, Pedido e ItemPedido. Entretanto, o catálogo exibido pelas páginas e o carrinho demonstrativo usam atualmente a lista de core/catalogo.py e a sessão do navegador. Cadastrar um registro no modelo Roupa pelo Admin, por si só, não adiciona esse produto à lista demonstrativa da loja.
6. Como criar um usuário administrador
Com o ambiente virtual ativado e as migrações aplicadas, execute:
python manage.py createsuperuser
Siga as perguntas do terminal para definir usuário, e-mail (se solicitado) e senha. Depois, inicie o servidor e acesse http://127.0.0.1:8000/admin/.
7. Comandos úteis
Verificar problemas de configuração:
python manage.py check
Criar arquivos de migração após alterações nos modelos:
python manage.py makemigrations
Aplicar migrações:
python manage.py migrate
Executar os testes do aplicativo:
python manage.py test core
8. Observações e próximos passos
- Atualize o e-mail, telefone, Instagram e número do WhatsApp de exemplo em templates/contato.html.
- Os valores e as peças são ilustrativos; confira preços, tamanhos, estoque e imagens antes de uma apresentação.
- O carrinho usa a sessão do Django. Ele é adequado para demonstração, mas não substitui um sistema de pedidos persistido no banco de dados.
- A página de pagamento apenas registra uma escolha demonstrativa. Para receber pagamentos reais, seria necessário implementar uma integração segura com um provedor de pagamentos, com credenciais protegidas e validação no servidor.
- Antes de publicar o site na internet, configure DEBUG, ALLOWED_HOSTS, HTTPS, arquivos estáticos e variáveis secretas de acordo com as recomendações do Django.
9. Tecnologias utilizadas
- Python
- Django
- HTML5
- CSS3
- SQLite (banco de dados padrão do projeto)
- JavaScript/links externos quando aplicável