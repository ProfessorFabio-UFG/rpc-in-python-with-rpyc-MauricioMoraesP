# 🧠 Sistema de Lista Compartilhada com RPyC

Este projeto implementa um sistema cliente-servidor usando **RPC com a biblioteca RPyC (Remote Python Call)**. O servidor mantém uma **lista compartilhada** que pode ser manipulada por múltiplos clientes de forma interativa via prompt.

---

## ⚙️ Funcionalidades

O cliente interage com o sistema por meio de um menu interativo. As operações disponíveis são:

1. Ver a lista atual
2. Adicionar item à lista
3. Remover item da lista
4. Limpar toda a lista
5. Ver o tamanho da lista
6. Buscar item por índice
7. Verificar se um valor está na lista
8. Ver histórico de operações
9. Salvar a lista em arquivo (`data.json`)
10. Carregar lista salva de arquivo
0. Sair do programa

---

## 📁 Estrutura de Arquivos

```bash
rpc-in-python/
├── client.py           # Cliente com menu interativo
├── server.py           # Servidor RPyC com lógica da lista
├── constRPYC.py        # Constantes de IP e porta
└── data.json           # (gerado automaticamente ao salvar a lista)
