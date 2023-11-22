from xmlrpc.client import ServerProxy

# Função para se conectar ao servidor e realizar operações
def perform_operation():
    print("Operações disponíveis: add, subtract, multiply, divide")
    operation = input("Escolha uma operação: ").strip().lower()

    if operation not in ('add', 'subtract', 'multiply', 'divide'):
        print("Operação inválida.")
        return

    numbers = input("Digite os números separados por espaço: ")

    try:
        # Conectar ao servidor RPC
        with ServerProxy(f'http://{SERVER_HOST}:{SERVER_PORT}') as proxy:
            # Chamar a função remota no servidor RPC
            result = getattr(proxy, operation)(*map(float, numbers.split()))
            print(f"Resultado: {result}")

    except Exception as e:
        print(f"Erro ao conectar ao servidor: {e}")

# Configuração do cliente
SERVER_HOST = '54.172.57.13'
SERVER_PORT = 15000

while True:
    perform_operation()
    another = input("Deseja realizar outra operação? (S/N): ").strip().lower()
    if another != 's':
        break
