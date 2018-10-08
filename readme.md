# CryptOver
Esse script é feito apenas para estudos, não me resposabilizo pela suas merdas.
## GenKey.py
Ele gera a chave publica e privada apartir de uma determinada senha, que seria a chave pra descriptografar.
Com essa senha vc consegue descriptografar a shared key e IV do algoritmo AES.
## Ransom.py
Possui os comandos, em uma classe, para criptografar e etc...

Assim que acionado, o script cria um diretorio de configuração chamado "ransomware".
Dentro deste diretorio será criado 3 arquivos: <br>
data.enc - Aqui é onde estara a IV e a shared key para montar a chave AES <br>
key.pub -  É onde estará a public key da chave RSA que foi usada pra criptografar data.enc <br>
file_hash.json - Hash's dos arquivos criptografados.  <br>
 
 # Instruções 
 Através do script "genkey.py" gere um par de chaves apartir da senha que o script irá pedir, salve-a a chave publica em "key.pub". Recomendo guarde também a privada, por segurança<br>
Depois é só fazer um simples script importanto o modulo ransom.py
 
