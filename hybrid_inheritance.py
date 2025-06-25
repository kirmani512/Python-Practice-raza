# when we use more than one inheritance that is hybrid inheritance e.g

class BaseClass():
    pass

class Derived1(BaseClass):
    pass

class Derived2(BaseClass):
    pass

class Derived3(Derived1,Derived2):
    pass

# Hierarchical inheritanace is when multiple subclasees inherits from a single base class

class Bclass():
    pass

class d1(Bclass):
    pass

class d2(Bclass):
    pass

class d3(d1):
    pass

#image reference for better understanding
#https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.naukri.com%2Fcode360%2Flibrary%2Ftypes-of-inheritance-in-python&psig=AOvVaw1ClnaS-gNvPnksXeEh3pHc&ust=1750946175355000&source=images&cd=vfe&opi=89978449&ved=2ahUKEwi91dj33IyOAxXiXKQEHYbCHgEQjRx6BAgAEBk