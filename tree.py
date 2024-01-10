class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children: list[TreeNode] = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self, *args, **kwargs):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def print_tree_by_level(self, level):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children and self.get_level() < level:
            for child in self.children:
                child.print_tree_by_level(level)

    def __repr__(self):
        return f"{self.data}"


class ManagementTree(TreeNode):
    def __init__(self, name, designation, data="", ):
        super().__init__(data)
        self.name = name
        self.designation = designation

    def print_mng_tree(self, typ, *args, **kwargs):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        txt = prefix
        # print(typ)
        if typ == 'name':
            txt += self.name
        elif typ == 'designation':
            txt += self.designation
        elif typ == 'both':
            txt += f"{self.name} ({self.designation})"
        print(txt)
        if self.children:
            for child in self.children:
                child.print_mng_tree(typ)


def build_management_tree():
    # CTO Hierarchy
    infra_head = ManagementTree("Vishwa", "Infrastructure Head")
    infra_head.add_child(ManagementTree("Dhaval", "Cloud Manager"))
    infra_head.add_child(ManagementTree("Abhijit", "App Manager"))

    cto = ManagementTree("Chinmay", "CTO")
    cto.add_child(infra_head)
    cto.add_child(ManagementTree("Aamir", "Application Head"))

    # HR hierarchy
    hr_head = ManagementTree("Gels", "HR Head")

    hr_head.add_child(ManagementTree("Peter", "Recruitment Manager"))
    hr_head.add_child(ManagementTree("Waqas", "Policy Manager"))

    ceo = ManagementTree("Nilupul", "CEO")
    ceo.add_child(cto)
    ceo.add_child(hr_head)

    return ceo


def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    root.print_tree()


def build_location_tree():
    root = TreeNode("Global")

    india = TreeNode("India")

    gujarat = TreeNode("Gujarat")
    gujarat.add_child(TreeNode("Ahmedabad"))
    gujarat.add_child(TreeNode("Baroda"))

    karnataka = TreeNode("Karnataka")
    karnataka.add_child(TreeNode("Bangluru"))
    karnataka.add_child(TreeNode("Mysore"))

    india.add_child(gujarat)
    india.add_child(karnataka)

    usa = TreeNode("USA")

    nj = TreeNode("New Jersey")
    nj.add_child(TreeNode("Princeton"))
    nj.add_child(TreeNode("Trenton"))

    california = TreeNode("California")
    california.add_child(TreeNode("San Francisco"))
    california.add_child(TreeNode("Mountain View"))
    california.add_child(TreeNode("Palo Alto"))

    usa.add_child(nj)
    usa.add_child(california)

    root.add_child(india)
    root.add_child(usa)

    return root


if __name__ == '__main__':
    # build_product_tree()
    # root_node = build_management_tree()
    # root_node.print_mng_tree("name")
    # root_node.print_mng_tree("designation")
    # root_node.print_mng_tree("both")

    root_node = build_location_tree()
    root_node.print_tree_by_level(2)
