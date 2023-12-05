# Django_Portfolio_Site
Portfolio Site in Django, Python

Desenvolvi minha pagina na Web, onde eu queria:
- Uma pagina única contendo uma parte com minha foto e minha especialização, os portfolios, um texto sobre mim, um formulário para contactos, minha localização e links paras as principais redes sociais.
- Uma página para cada projeto do portfolio detalhando como foi executado, e incluindo as tecnologias usadas e os problemas e soluções encontrados durante seu desenvolvimento.

Resolvi desenvolver em Django para poder usar, inclusive, a criação dessa página como portfolio.

Desenvolvi uma Home Page, com todo conteúdo que gostaria, com o portfolio e a pagina para cada projeto, iterando sobre meu banco de dados criado, que possui os seguintes campos: nome do projeto, subtitulo, imagem do projeto, descrição, tecnologias usadas, problemas e soluções encontrados durante o desenvolvimento do projeto.

![site_django_portfolio](https://github.com/JulioDEVReis/Django_Portfolio_Site/assets/142347463/db32a55b-9f28-4c84-bb38-4de755b70bd7)

## Dificuldades e Soluções:

- Ao iterar sobre os projetos de meu portfolio, e inclui-los com Jinja em meus arquivos HTML, percebi que os conteúdos vinham sem quebras de linha. Para solucionar, pesquisei na documentação e encontrei a solução incluindo |linebreaks em cada código Jinja que eu importasse do banco de dados campos que possuiam conteúdos com quebras de linha.

- A iteração sobre os projetos na criação das páginas de detalhamento do portfolio piorou o desempenho da página, a identificação por SEO, e a localização pelos motores de busca. Para solucionar isso, uma página para cada projeto foi criada, com seu respectivo SEO.

## Tecnologias usadas:

- Django (Framework para desenvolvimento da minha página Portfolio em Python)
- Bootstrap (Estilização da página Web)
