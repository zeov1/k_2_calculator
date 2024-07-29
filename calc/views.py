from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from .forms import CalcForm


@csrf_protect
def calc(request):
    if request.method == 'POST':
        data = CalcForm(request.POST)
        ok = True
        msg = []
        if data.is_valid():
            a_str = data.cleaned_data['a']
            try:
                a = float(a_str)
            except ValueError:
                ok = False
                msg.append('Value a must be float')
            b_str = data.cleaned_data['b']
            try:
                b = float(b_str)
            except ValueError:
                ok = False
                msg.append('Value b must be float')
            op = data.cleaned_data['op']
            if op == '+':
                res = a + b if ok else None
            elif op == '-':
                res = a - b if ok else None
            elif op == '*':
                res = a * b if ok else None
            elif op == '/':
                if b != 0:
                    res = a / b if ok else None
                else:
                    res = float('inf') * a if ok else None
            else:
                ok = False
                res = None
                msg.append(f'Unknown operation: {op}')
        else:
            a = b = res = None

        print(res)

        return render(request, 'calc.html', {
            'ok': ok,
            'msg': msg,
            'a': a,
            'b': b,
            'res': res,
        })

    return render(request, 'calc.html')


def about(request):
    return render(request, 'about.html')
