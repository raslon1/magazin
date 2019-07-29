import json
import os
import urllib.parse
from .models import *



class JsonToData(object):
    data = {}
    
    def __init__(self):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'fixtures')
        with open(path+'/data.json') as f:
            self.data = json.load(f)
    def run(self):
        for model in self.data['models']:
            model_name = model['model'].title()
            if model_name == 'Category':
                self.Categoryitems(model['items'])
            elif model_name == 'Color':
                self.Coloritems(model['items'])
            elif model_name == 'Products':
                self.Productitems(model['items'])
            
    def Categoryitems(self, model):
        for item in model:
            data = {}
            name = urllib.parse.unquote(item['name'])
            guid = item['guid']
            if not Category.objects.filter(guid=guid).exists():
                if (item.get('parent',None) == None):
                    data.update(name = name, guid = guid)
                    self.ObjectCreat(Category,data)
                elif  not Category.objects.filter(guid = item['parent']).exists():
                    parent = item['parent']
                    self.Searchitems(model, parent)
                    par = Category.objects.get(guid = parent)
                    data.update(name = name, guid = guid, parent = par)
                    self.ObjectCreat(Category,data)
                else:
                    parent = item['parent']
                    par = Category.objects.get(guid = parent)
                    data.update(name = name, guid = guid, parent = par)
                    self.ObjectCreat(Category, data)
            
    
    def Coloritems(self, model):
        for item in model:
            data = {}
            name = urllib.parse.unquote(item['name'])
            guid = item['guid']
            hexcode = '#'+item['hexcode']
            if not Color.objects.filter(guid = item['guid']).exists():
                data.update(name = name, guid = guid, hexcode = hexcode)
                self.ObjectCreat(Color, data)
    def Productitems(self, model):
        for item in model:
            data = {}
            name = urllib.parse.unquote(item['name'])
            guid = item['guid']
            price = item['price']
            color = Color.objects.get(guid = item['color'])
            category = Category.objects.get(guid = item['category'])
            if not Products.objects.filter(guid = item['guid']).exists():
                data.update(name = name, guid = guid, price = price, color = color, category = category)
                self.ObjectCreat(Products,data)
    def Searchitems(self, items, parent):
        data = {}
        for item in items:
            if item['guid']==parent:
                name = urllib.parse.unquote(item['name'])
                guid = item['guid']
                data.update(name = name, guid = guid)
                self.ObjectCreat(Category,data)
    
    def ObjectCreat(self,mod, data):
        mod.objects.create(**data)
