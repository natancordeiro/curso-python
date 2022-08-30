# Função para MOSTRAR as oções cadastradas
def show_op(todo_list):
    print()
    print('Tarefas: ')
    print(todo_list)
    print()

# Função para DESFAZER
def do_undo(todo_list, redo_list):
    if not todo_list: 
        print('Nada a desfazer.')
        return
    last_todo = todo_list.pop()
    redo_list.append(last_todo)

# Função para REFAZER
def do_redo(todo_list, redo_list):
    if not redo_list:
        print('Nada a refazer.')
        return
    last_redo = redo_list.pop()
    todo_list.append(last_redo)

# Função para ADICIONAR objeto ao todo_list 
def do_add(todo, todo_list):
    todo_list.append(todo)

# Tratamento de Módulo
if __name__ == 'main':
    todo_list = []
    redo_list = []

    # Looping de input do usuário
    while True:
        todo = input('''
        Digite a tarefa que deseja fazer: 
        Outras opções:  
        [undo] para desfazer
        [redo] para refazer
        [ls] para listar ''')

        # Tratando a escolha do usuário
        if todo == 'ls':
            show_op(todo_list)
            continue
        elif todo == 'undo':
            do_undo(todo_list, redo_list)
            continue
        elif todo == 'redo':
            do_redo(todo_list, redo_list)
            continue
        do_add(todo, todo_list)
