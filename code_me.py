import json
from jsonpath_ng import jsonpath, parse



def covid_provinces(data):
    jsonpath_expr = parse('$.[*]')
    return [match.value for match in jsonpath_expr.find(data)]

def json_users(data):
    jsonpath_expr = parse('$.[*]')
    jsonpath_expr  = parse(f"{jsonpath_expr}.address.geo") 
    return [match.value for match in jsonpath_expr.find(data)]

def multipage(data) :
    jsonpath_expr = parse('$.result.records.[*]')
    return [match.value for match in jsonpath_expr.find(data)]


def sam_san(data) :
    jsonpath_expr = parse('$.[*].data')
    return [match.value for match in jsonpath_expr.find(data)]

def weekly_covid(data):
    jsonpath_expr = parse('$.[*]')
    return [match.value for match in jsonpath_expr.find(data)]


if __name__ == '__main__':
    # ============ load file
    my_json = None 
    f= open('example_source/weekly_covid.json')
    my_json = json.load(f)
    f.close()

    # ==========
    
    results = covid_provinces(my_json)
    results = json_users(my_json)
    results = multipage(my_json)
    results = sam_san(my_json)
    results = weekly_covid(my_json)

    print(results)