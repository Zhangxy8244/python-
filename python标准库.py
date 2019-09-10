from collections import OrderedDict

favorite_language = OrderedDict()
favorite_language['Zhang'] = 'C'
favorite_language['Wang'] = 'python'
favorite_language['Li'] = 'C++'
favorite_language['Zhao'] = 'C#'
for name, language in favorite_language.items():
    print(name.title()+"'s favorite language is "+language.title()+".")