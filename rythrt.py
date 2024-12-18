from inspect import getmodule



def introspection_info(obj):
    result = {}
    result["type"] = type(obj).__name__
    result["attributes"] = obj.__dict__
    result  ['methods'] = dir(obj)
    result['module'] = getmodule(obj)
    return result
class Human:
    pass
a = Human()


number_info = introspection_info(a)
print(number_info)
