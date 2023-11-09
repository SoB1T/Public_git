class Node:  # класс ну грубо говоря точки с напрваленым графом
    '''Класс точки с графом, где name это имя точки, а access это словарь с графами оформленый по принципу
    название точки: стоимость графа, а так же методом __repr__ для улудшения отображения'''
    def __init__(self, name, access):
        self.name = name
        self.access = access

    def __repr__(self):
        return f'Node with name:{self.name}, and access: {self.access}'


# идея попробуй реализовать граф где все как в связном списке

class MapGraff:
    """
    Карта графов и точек хранит в себе экземпляры Node после создания, сам их собственно создает, по необходимости
    обновляет доступы графов
    """
    def __init__(self):
        """data это список всех точек и графов, names пространство имен точек"""
        self.data = []
        self.names = []

    # def is_empty(self):
    #     if len(self.data) == 0:
    #         return True
    #     else:
    #         return False

    def append(self, name, access={}):
        """метод добавления графов, в случае создания графа с направлением в еще не существующую точку создает ее, по
        моей глупости делает двухнаправленные графы
        """
        new_node = Node(name, access)
        self.data.append(new_node)
        self.names.append(name)
        for i in access.keys():
            if i in self.names:
                self.update(i, {name: access.get(i)})
            else:
                new_node = Node(i, {name: access.get(i)})
                self.data.append(new_node)

    # def grup_append(self, name):
    #     for k in name.keys():
    #         new_node = Node(k, name.get(k))
    #         self.data.append(new_node)
    #         self.names.append(k)
    #         for i in name.values():
    #
    #             for j in i.keys():
    #                 if j in self.names:
    #                     self.update(j, {k: i.get(j)})
    #                 else:
    #                     new_node = Node(j, {k: i.get(j)})
    #                     self.data.append(new_node)
    # #            self.names.append(j)
    #  #           new_node = Node(j, {i:name.get(j)})
    #  #           self.data = new_node
    #   #  for i in name.keys():
    #  #       self.names.append(i)
    #  #       new_node = Node(i, name.get(i))
    #   #      self.data = new_node
    #   #      for i in name.values():
    #  #           for j in i.keys():
    # #               new_node = Node(j,name.get(j))
    # #                self.data = new_node

    def get_node(self, name):
        """метод получения экземпляра нода с именем и доступами"""
        for i in self.data:
            if i.name == name:
                print(i)

    def update(self, name, access):
        """метод для добавления в существующие точки доступов"""
        for i in self.data:
            if i.name == name:
                if len(i.access) == 0:
                    i.access = access
                else:
                    i.access.update(access)

    def check(self, a, b):
        """проверка на наличие доступа из точки A в точку B """
        for i in self.data:
            if i.name == a:
                if b in i.access.keys():
                    return True
                else:
                    return False


gr = MapGraff()
gr.append("first", )
print(gr.data)
gr.append("second", {"first": 1})
print(gr.data)
gr.get_node("first")
print(gr.data)
print(gr.check("first", "second"))
# grf = Graff()
# grf.grup_append({"a":{"b":2,"c":3}})
# a={"b":2,"c":3}
# print(grf.data)
