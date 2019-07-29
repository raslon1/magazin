import json
import os
import urllib.parse
from .models import *



path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'fixtures')

def Categoryitems(modl):
    for item in modl:
        data = {}
        name = urllib.parse.unquote(item['name'])
        guid = item['guid']
        if not Model.objects.filter(guid=guid).exists():
            if (item.get('parent',None) == None):
                data.update(name = name, guid = guid)
                ObjectCreat(data)
            elif  not Model.objects.filter(guid = item['parent']).exists():
                parent = item['parent']
                searchitems(modl, parent)
                par = Model.objects.get(guid = parent)
                data.update(name = name, guid = guid, parent = par)
                ObjectCreat(data)
            else:
                parent = item['parent']
                par = Model.objects.get(guid = parent)
                data.update(name = name, guid = guid, parent = par)
                ObjectCreat(data)


def Coloritems(modl):
    for item in modl:
        data = {}
        name = urllib.parse.unquote(item['name'])
        guid = item['guid']
        hexcode = '#'+item['hexcode']
        if not Model.objects.filter(guid = item['guid']).exists():
            data.update(name = name, guid = guid, hexcode = hexcode)
            ObjectCreat(data)

def Productitems(modl):
    for item in modl:
        data = {}
        name = urllib.parse.unquote(item['name'])
        guid = item['guid']
        price = item['price']
        color = Color.objects.get(guid = item['color'])
        category = Category.objects.get(guid = item['category'])
        
        data.update(name = name, guid = guid, price = price, color = color, category = category)
        ObjectCreat(data)


def searchitems(items, parent):
    data = {}
    for item in items:
        if item['guid']==parent:
            name = urllib.parse.unquote(item['name'])
            guid = item['guid']
            print(parent, ' <<<Search')
            data.update(name = name, guid = guid)
            ObjectCreat(data)

def ObjectCreat(data):
    print(data, ' Save data')
    Model.objects.create(**data)

# class JsonToData():
#     def __init__()
#         try:
#             with open(path+'/data.json') as f:
#                 data = json.load(f)
#         except:
#             pass
        
#     def read(self):
#         category()
#     def category():
#         for category in data['']





with open(path+'/data.json') as f:
    data = json.load(f)   

for modl in data['models']:
    # try:
    model = modl['model'].title()
    Model = eval(model)
    if model == 'Category':
        Categoryitems(modl['items'])
    elif model == 'Color':
        Coloritems(modl['items'])
    elif model == 'Products':
        Productitems(modl['items'])
        





        # dat = {}
        # #print(item)
        
        # if modl['model'].title() == 'Category':
        #     name = urllib.parse.unquote(item['name'])
        #     gui = item['guid']
        #     dat = {'name':name,'guid':gui}
        #     if item.get('parent',None) != None:
        #         parent = Model.objects.get(guid = item['parent'])
        #         print(parent)
        #         dat.update({'parent':parent})
        #     print(dat)
        #     if not Model.objects.filter(name=name).exists():
        #         Model.objects.create(**dat)
        # except:
        #     print('Error: ', item['name'])
        
            
#     # except:
#     #     print('Ошибка ', modl['model'])


    

