#265
def bisec(f,a,b,N):
    if f(a)*f(b)>=0:return None
    for m in map(lambda n:(a+b)/2,range(1,N+1)):
        y=f(m)
        if f(a)*y<0:b=m
        elif f(b)*y<0:a=m
        elif y==0:return m
        else:return None
    return (a+b)/2