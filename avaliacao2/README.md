## Descrição da avaliação

Criar uma rede neural para realizar a análise de sentimentos de textos em *português*;

- :heavy_check_mark: Realizar a extração de uma grande quantidade de textos;
  - Os textos foram coletados do Twitter através da Twitter Streaming API e armazenados em um arquivo Pickle. Quebras de linha foram removidas;
- :heavy_check_mark: Pré-processar os textos para remoção de conteúdos indesejáveis;
  - O pré-processamento considerou a transformação de caracteres maiúsculos para minúsculos, lematização das palavras e remoção de URLs, hashtags, menções, emojis, pontuação, acentuação e espaços em branco extras.
- :heavy_check_mark: Treinar Word2Vec;
  - Para treinar o word2vec foi utilizado o gensim
- :heavy_check_mark: Realizar extração de textos contendo a classificação das mensagens;
  - Os textos com classificação também foram coletados do Twitter, porém, através de IDs de tweets classificados como posivitos e negativos, disponibilizados no repositório [pauloemmilio/dataset](https://github.com/pauloemmilio/dataset)
- :heavy_check_mark: Pré-processar os textos com classificação;
  - Foram realizados os mesmos passos que no pré-processamento dos textos não classificados;
- :heavy_check_mark: Treinar LSTM;
  - Para treinar a LSTM foi utilizado o keras

OBS.: O conteúdo dos textos não foram disponibilizados aqui para não ferir as políticas de privacidade do Twitter.
