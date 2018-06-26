## Descrição da Avaliação

### Parte 1

Neste exercício, tomando o código abaixo como ponto de partida, você vai desenvolver uma rede neural capaz de classificar diferentes artigos de vestuário. Para isso, você deverá implementar uma rede neural do tipo perceptron utilizando apenas NumPy (sem o auxílio de bibliotecas como TensorFlow, Theano, Torch, Caffe).

Para a realização deste exercício utilizaremos a base de dados [Fashion-MNIST](https://github.com/zalandoresearch/fashion-mnist). A base de dados consiste em imagens monocromáticas de tamanho 28x28 pixels, cada imagem acompanhada de uma etiqueta que identifica a classe à qual ela pertence -- a classe representa a categoria de artigo de vestuário mostrado na imagem.

Critérios de avaliação:
- Implementação da rede neural com pelo menos uma camada escondida e função ou método de *Forward propagation*
- Implementação do algoritmo de *back propagation*
- Definição adequada da função de erro e cálculo da derivada no algoritmo de *back propagation*
- Treinamento demonstrando redução gradual do erro nos dados de treinamento
- Treinamento demonstrando redução gradual do erro nos dados de validação
- Mostrar alcance de pelo menos 84% de exatidão nos dados de validação
- **Ponto Extra:** Alcance de 87% ou mais de exatidão nos dados de validação


### Parte 2

Neste exercício você irá preparar uma base de dados de imagens de expressões faciais e treinar uma regressão logística nesses dados. Para isso usaremos uma base de dados de um desafio [publicado no site Kaggle em 2013](https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge), e descrito [neste artigo do arXiv.org](http://arxiv.org/abs/1307.0414). Esta base consiste em um arquivo [em formato CSV](https://pt.wikipedia.org/wiki/Comma-separated_values), onde constam milhares de imagens monocromáticas de 48x48 pixels de rostos de diferentes pessoas. Para cada imagem é dado um número inteiro de 0 a 6 que representa uma expressão seguindo esta legenda: 0=Raiva, 1=Nojo, 2=Medo, 3=Felicidade, 4=Tristeza, 5=Surpresa, 6=Neutro.

Nesta base de dados há exatamente 28709 imagens destinadas para treinamento, 3589 destinadas para validação e 3589 para teste (respectivamente marcadas como 'Training', 'PublicTest' e 'PrivateTest').

A regressão logística deverá ser implementada utilizando a biblioteca TensorFlow, seguindo os mesmos moldes do exercício "Assignment 1: notMNIST" do [curso de Deep Learning da Udacity](https://classroom.udacity.com/courses/ud730).

Critérios de avaliação:
- Abrir o arquivo CSV fornecido e acessar os dados a partir do código em Python
- Separar adequadamente dados de treinamento, validação e teste
- Criar arrays do NumPy com as devidas dimensões e tipagem, e preenchê-las com os dados lidos do arquivo
- Armazenar as no formato one-hot e as normalizar as imagens
- Criar um arquivo binário do Pickle com todos os dados já formatados em arrays do NumPy
- Ler o arquivo binário do Pickle, restaurando todos os dados já formatados em arrays do NumPy
- Mostrar 10 exemplos aleatórios de imagens, imprimindo suas classes correspondentes
- Implementar o Grafo da Regressão Linear no TensorFlow com as constantes, os placeholders e as variáveis, realizando as dimensões e operações corretas, incluindo erro apropriado para *one-hot encoding*
- Implementar a Sessão no TensorFlow, fazendo o treinamento por lotes, e mostrando o erro de treinamento diminuindo
- Mostrar o erro nos dados de validação a cada época do treinamento
- Mostrar o erro nos dados de teste ao final de todo treinamento
- **Ponto Extra:** Implementar e treinar uma rede neural do tipo perceptron com duas camadas ou mais