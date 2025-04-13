#Este projeto implementa um sistema simples de detecção de faces que processa um arquivo de vídeo para identificar faces humanas em cada frame, utilizando o classificador Haar Cascade pré-treinado do OpenCV. As faces detectadas são destacadas com retângulos azuis e exibidas em tempo real.

#Visão Geral do Projeto
O script utiliza a biblioteca OpenCV para:

Carregar um arquivo de vídeo.
Converter cada frame para escala de cinza para melhorar a eficiência da detecção de faces.
Detectar faces utilizando o classificador Haar Cascade.
Desenhar retângulos azuis ao redor das faces detectadas.
Exibir os frames processados em uma janela.
Repetir o vídeo continuamente até que o usuário pressione 'q' para sair.


#Pré-requisitos
Para executar este projeto, você precisará de:

Python 3
OpenCV: A biblioteca opencv-python é necessária para o processamento de imagens e detecção de faces.
Arquivo de Vídeo: Um arquivo de vídeo (ex.: video.mp4) para processar. Coloque-o no mesmo diretório do script ou forneça o caminho completo.

#Instalar :
Python ,
pip install opencv-python

#Executar o Script:
Abra um terminal no diretório do projeto e execute:

python deteccao.py


Integrantes :

Gustavo Nascimento 93292
Gabriel Jun 93540
Enrico Thomas 94371
Luigi Macedo 93989