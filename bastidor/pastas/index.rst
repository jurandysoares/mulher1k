Bastidores do exercício sobre pastas
======================================

As pastas do exercício foram criadas utilizando o recurso de expansão das chaves do `bash <https://pt.wikipedia.org/wiki/Bash>`_, o interpretador de comandos padrão do Linux e que também pode ser executado no Windows.

* Dia e seus turnos::

    mkdir -p Dia/{Manhã,Tarde,Noite}

* Refeições do dia::

    mkdir -p Refeição/{Café,Almoço,Jantar}

* Ocupação de um ser humano, segundo a terapia ocupacional::

    mkdir -p Ocupação/{Trabalho,Autocuidado,Lazer}

* Dinâmica de apresentação::

    mkdir -p Apresentação/{'Quem sou','Que gosto de fazer','Que sei fazer bem'}

* Dias da semana::

    mkdir -p Semana/{Seg,Ter,Qua,Qui,Sex,Sáb,Dom}

* Meses do ano::

    mkdir -p Ano/{Janeiro,Fevereiro,Março,Abril,Maio,Junho,Julho,Agosto,Setembro,Outubro,Novembro,Dezembro}


* Meses do ano, em ordem::

    mkdir -p Ano+organizado/{1-Janeiro,2-Fevereiro,3-Março,4-Abril,5-Maio,6-Junho,7-Julho,8-Agosto,9-Setembro,10-Outubro,11-Novembro,12-Dezembro}

* Dias da semana, em ordem::

    mkdir -p Semana+organizada/{2-Seg,3-Ter,4-Qua,5-Qui,6-Sex,7-Sáb,1-Dom}

* Turnos do dia, em ordem::

    mkdir -p Dia+organizado/{1-Manhã,2-Tarde,3-Noite}

* Refeições do dia, em ordem::

    mkdir -p Refeição+organizada/{1-Café,2-Almoço,3-Jantar}
