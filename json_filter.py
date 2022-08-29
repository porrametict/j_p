import json 
from jsonpath_ng import parse

def excute(path,data):
    jsonpath_expr = parse(path)
    return [match.value for match in jsonpath_expr.find(data)]

