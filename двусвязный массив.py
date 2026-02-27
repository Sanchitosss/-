# Узел
class Node:
    def __init__(self, name):
        self.name = name
        self.next = None

# Список
class ListNode:
    def __init__(self):
        # Голова списка
        self.head = None

    # Добавление нового элемента в конец
    def add(self):
        name = input('Введите имя: ')
        current = self.head

        # Если список пустой
        if not current:
            self.head = Node(name)
            return

        # Перебираем список до последнего узла
        while current.next:
            current = current.next
        current.next = Node(name)

    # Просмотр всех элементов
    def view(self):
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
            return

        # Перебираем до предпоследнего
        while current.next.next:
            current = current.next
        current.next = None



def menu():
    List = ListNode()
    while True:
        print('\n---------- Меню ----------')
        print('1. Добавить пользователя')
        print('2. Посмотреть всех пользователей')
        print('3. Удалить последнего пользователя')

        choice = int(input('\nВыберите пункт: '))

        if choice == 1:
            List.add()
        elif choice == 2:
            List.view()
        elif choice == 3:
            List.delete()


menu()

