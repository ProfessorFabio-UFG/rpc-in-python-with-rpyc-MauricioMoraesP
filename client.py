import rpyc
from constRPYC import *

def print_menu():
    print("\n--- MENU ---")
    print("1. Ver lista")
    print("2. Adicionar item")
    print("3. Remover item")
    print("4. Limpar lista")
    print("5. Ver tamanho da lista")
    print("6. Buscar por índice")
    print("7. Verificar se valor está na lista")
    print("8. Ver histórico")
    print("9. Salvar lista em arquivo")
    print("10. Carregar lista de arquivo")
    print("0. Sair")

def main():
    conn = rpyc.connect(SERVER, PORT)
    print("Conectado ao servidor.")

    while True:
        print_menu()
        choice = input("Escolha uma opção: ")

        match choice:
            case "1":
                print("Lista atual:", conn.root.exposed_value())
            case "2":
                item = input("Digite o valor a adicionar: ")
                conn.root.exposed_append(item)
            case "3":
                item = input("Digite o valor a remover: ")
                success = conn.root.exposed_remove(item)
                print("Removido." if success else "Item não encontrado.")
            case "4":
                conn.root.exposed_clear()
                print("Lista limpa.")
            case "5":
                print("Tamanho da lista:", conn.root.exposed_size())
            case "6":
                idx = int(input("Digite o índice: "))
                item = conn.root.exposed_get(idx)
                print("Item:", item if item is not None else "Índice inválido.")
            case "7":
                item = input("Digite o valor: ")
                print("Está na lista:", conn.root.exposed_contains(item))
            case "8":
                history = conn.root.exposed_history()
                print("--- Histórico ---")
                for h in history:
                    print(h)
            case "9":
                conn.root.exposed_save()
                print("Lista salva.")
            case "10":
                conn.root.exposed_load()
                print("Lista carregada.")
            case "0":
                print("Saindo...")
                break
            case _:
                print("Opção inválida.")

if __name__ == "__main__":
    main()
