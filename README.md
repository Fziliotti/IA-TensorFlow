# IA-TensorFlow
Esse é o repositório dos arquivos utilizados em minha [apresentação](https://slides.com/fziliotti/deck-d6777cd9-e72f-4234-b4c9-5ba2ae4ed8ab/fullscreen) sobre o framework tensorflow na disciplina de Inteligência-Artificial.

Para não ter que instalar todas as dependencias do python, jupyter e instalação de bibliotecas, utilizei o [Docker](https://www.docker.com/).

Para criar o container utilizando a imagem com as configurações necessárias para rodar o tensorflow com jupyter, basta rodar o seguinte comando:
`docker run -it -p 8888:8888 tensorflow/tensorflow:nightly-py3-jupyter`

Com o comando acima, basicamente o container irá "conversar" com o seu sistema operacional (host) apartir da porta 888, porta padrão do jupyter.
Dessa forma o que você modificar no seu SO, vai refletir no container do docker ao executar os comandos no browser.
