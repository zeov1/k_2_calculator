from django.shortcuts import render


def index(request):
    try:
        a = request.GET['a']
        a = int(a)
        a_ok = True
    except ValueError:
        a = None
        a_ok = False

    try:
        b = request.GET['b']
        b = int(b)
        b_ok = True
    except ValueError:
        b = None
        b_ok = False

    try:
        op = request.GET['op']
        op_ok = True
    except ValueError:
        op = None
        op_ok = False

    if op == 'plus':
        op = '+'
        res = a + b
    elif op == 'minus':
        op = '-'
        res = a - b
    elif op == 'mult':
        op = '*'
        res = a * b
    elif op == 'divide':
        op = '/'
        res = a / b
    else:
        res = None
        op_ok = False

    return render(request, "calc.html", {
        'a_ok': a_ok,
        'b_ok': b_ok,
        'op_ok': op_ok,
        'a': a,
        'b': b,
        'op': op,
        'res': res,
    })
