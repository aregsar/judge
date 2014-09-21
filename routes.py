from views import home
from views import account


#optionally use this function to add  application routing rules in a single location
#all the application routes can be specified here instead of using attribute routeing
#or you can use a combination of both specifying some route rules here
def add_url_rules():
    pass
    #examples:
    #view_func is the actual view function prefixed by the blueprint
    #endpoint can be any unique name per bluepring. Generally the view function name is used.
    #home.mod.add_url_rule('/', endpoint='index',view_func=home.index)
    #post.mod.add_url_rule('/posts/<id>', endpoint='index',view_func=post.index, defaults={'id': None}, methods=['GET','POST'])


    #
    #list all bluprint mapped routes
    #home.mod.url_map
