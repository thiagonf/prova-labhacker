[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

# prova-labhacker
Para acessar o deploy do projeto realizado na Digital Ocean [cliqui aqui](http://157.245.7.255/)

# Requisitos
Para executar o projeto é necessário a instalação do [Docker](https://docs.docker.com/install/) e [docker-compose](https://docs.docker.com/compose/install/). Após a instalação destes requisitos é possível executar o projeto.

# Executando o projeto
```
git clone https://github.com/thiagonf/prova-labhacker.git
cd projeto_labhacker
sudo docker-compose up
```
**OBS:** O projeto está configurado pra sessão ter tempo de duração de 10 minutos.

# Executando os testes
Com o projeto 
```
sudo docker-compose run web bash
./manage.py test
```

# Visualizando o projeto local
Para acessar a página do projeto é através do link: http://0.0.0.0:8000


# Licença
Este projeto está sobre a licença MIT

