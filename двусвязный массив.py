class Node:
    def __init__(self, name):
        self.name = name
        self.next = None


class ListNode:
    def __init__(self):
        self.head = None

    def add(self):
        name = input('Введите имя: ')
        current = self.head

        if not current:
            self.head = Node(name)
            return

        while current.next:
            current = current.next
        current.next = Node(name)

    def view(self):
        current = self.head

        if not current:
            print('Список пуст!')
            return

        while current:
            print(current.name)
            current = current.next

    def delete(self):

        current = self.head

        if not current:
            print('Список пуст!')
            return

        elif not current.next:
            self.head = None
            return

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
