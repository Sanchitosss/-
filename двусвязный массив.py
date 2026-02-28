# Узел
class Node:
    def __init__(self, name):
        self.name = name
        self.next = None

# Список
class ListNode:
    def __init__(self):
        self.head = None   # Голова списка
        self.len_list = 0  # длинна списка

    # Добавление нового элемента в конец
    def add(self):
        name = input('Введите имя: ')
        current = self.head

        # Если список пустой
        if not current:
            self.head = Node(name)
            self.len_list += 1
            return

        # Перебираем список до последнего узла
        while current.next:
            current = current.next
        current.next = Node(name)
        self.len_list += 1

    # Просмотр всех элементов
    def view(self):
        print(f'Всего {self.len_list} пользователей: ')
        current = self.head

        # Если список пустой
        if not current:
            print('Список пуст!')
            return

        # выводим все узлы
        while current:
            print(current.name)
            current = current.next

    # Удаление последнего элемента
    def delete(self):
        current = self.head

        # Если список пустой
        if not current:
            print('Список пуст!')
            return

        # Если только один элемент
        elif not current.next:
            self.head = None
            self.len_list -= 1
            return

        # Перебираем до предпоследнего
        while current.next.next:
            current = current.next
        current.next = None
        self.len_list -= 1

    # Добавление пользователя по индексу
    def add_to_index(self):
        index = int(input('Введите индекс нового пользователя: '))
        name = input('Введите имя пользователя: ')
        current = self.head

        # Если недопустимый индекс
        if index > self.len_list:
            print(f'Ошибка: максимальный разрешённый индекс - {self.len_list}!')
            return

        # Если вставляем на индекс 0
        elif index == 0:
            new_node = Node(name)
            new_node.next = self.head
            self.head = new_node
            self.len_list += 1
            return

        # Ищем индекс перед новым узлом
        for i in range(index - 1):
            current = current.next

        # Вставляем новый узел и присваиваем указатели ему и на него
        next_Node = current.next
        current.next = Node(name)
        current.next.next = next_Node
        self.len_list += 1


def menu():
    List = ListNode()
    while True:
        print('\n---------- Меню ----------')
        print('1. Добавить пользователя')
        print('2. Посмотреть всех пользователей')
        print('3. Удалить последнего пользователя')
        print('4. Вставить пользователя по индексу')

        choice = int(input('\nВыберите пункт: '))

        if choice == 1:
            List.add()
        elif choice == 2:
            List.view()
        elif choice == 3:
            List.delete()
        elif choice == 4:
            List.add_to_index()


menu()
