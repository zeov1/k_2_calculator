from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from .forms import CalcForm


@csrf_protect
def calc(request):
    if request.method == 'POST':
        data = CalcForm(request.POST)
        ok = True
        msg = []
        if not data.is_valid():
            return render(request, 'calc.html')
        a_str = data.cleaned_data['a']
        try:
            a = float(a_str)
        except ValueError:
            ok = False
            msg.append('Value a must be float\n')
        b_str = data.cleaned_data['b']
        try:
            b = float(b_str)
        except ValueError:
            ok = False
            msg.append('Value b must be float\n')
        op = data.cleaned_data['op']
        if op == '+':
            res = a + b if ok else None
        elif op == '-':
            res = a - b if ok else None
        elif op == '*':
            res = a * b if ok else None
        elif op == '/':
            if ok:
                if b != 0:
                    res = a / b
                    if int(res) == res:
                        res = int(res)
                else:
                    res = float('inf') * a if ok else None
            else:
                res = None
        else:
            ok = False
            res = None
            msg.append(f'Unknown operation: {op}\n')

        return render(request, 'calc.html', {
            'ok': ok,
            'msg': msg,
            'a': a_str,
            'b': b_str,
            'res': res,
        })

    return render(request, 'calc.html')


def about(request):
    return render(request, 'about.html')
