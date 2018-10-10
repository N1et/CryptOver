# CryptOver
**[Esse script é feito apenas para estudos, não me resposabilizo pela suas merdas.]**

O ransomware usará como criptografia principal, o algoritmo de chave simétrica **AES**. E como criptografia secundária, usaremos o algoritmo de criptografia assimétrica **RSA**, gerada apartir de uma chave pré-compartilhada. <br>
A criptografia secundária, algoritmo assimétrico RSA, terá o propósito de criptografar o arquivo *data.enc*, que é onde será despejado a chave pré-compartilhada(shared key) e a IV correspondente ao primeiro algoritmo gerado, AES em modo CBC.
# Genkey .py
Como dito anteriormente, o algoritmo RSA irá ser gerado apartir de uma chave pré-compartilhada. Para isso, o script *genkey.py* irá pedir uma senha, e, através dela, será gerada, o par de chaves. Porém, se não for especificado, por padrão, apenas a chave pública será impressa. <br>
*./genkey.py  <br>* 
*./genkey.py Private_key* <br>
Por padrão, o script *ransom.py* procurará a chave pública em um arquivo chamado *key.pub*. Por conta disso, é um bom costume que, quando for gerar, adicionar o redirecionamento da saido para tal arquivo.<br>
*./genkey.py > key.pub*

# Ransom .py
Aqui, é onde contém os comandos necessários para executar as funções ditas anteriormente. Funções como *encrypt_file* entre outras funções, será armazenada neste arquivo. A função *decrypt_file* não foi criada, pois, na minha visão, não achei necessário um *ransomware* ter uma função de descriptografar.
