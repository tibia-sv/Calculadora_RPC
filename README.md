# Calculadora_RPC

## Atividade proposta
Implemente uma calculadora distribuída que permita um cliente consultar serviços de operações aritméticas básicas tais como: somar, subtrair, multiplicar ou dividir. A quantidade de números a serem somados, subtraídos ou multiplicados está limitado a 20 números. Os números de entrada estão na mesma linha separador por um espaço. Ao teclar ENTER, o serviço correspondente da calculadora deve ser invocado.

O servidor da calculadora distribuída deve atender requisições na porta 15000 usando o protocolo RPC. O cliente deve oferecer um menu para o usuário escolher qual operação deseja executar. Após escolher uma operação aritmética, o usuário deve informar os números desejados, conectar no servidor, aguardar resposta e imprimir o resultado na tela.

O menu de operações aritméticas deverá ser apresentado novamente para o usuário escolher outra operação ou encerrar o programa.

## Realização
Foram abertas duas máquinas virtuais no sistema da AWS Academy, uma para o ```Servidor``` e uma para o ```Cliente```

 Para o vínculo do ```Cliente``` e ```Servidor``` foi usado o IP de coneção do Servidor

### Rodando o Código
Ao executar o ```Cliente``` no terminal da maquina da AWS, aparece o menu de interação para a solicitação dos valores e da operação a ser realizada.

Para a manipulação dos valores é realizada a chamada da função ```ADD```, ```SUB```, ```DIV``` ou ```MULT``` pelo ```Cliente``` para o ```Servidor```, assim, a realização da operação com o retorno do resultado.
