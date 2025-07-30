def div(a, b):
    print(a/b)

def super_div(func):
    def actual_func(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return actual_func

div = super_div(div)
div(4,8)