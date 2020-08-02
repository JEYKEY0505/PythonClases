from bokeh.plotting import figure, output_file, show
if __name__=='__main__':
    output_file('grafico_simple.html')
    fig= figure()
    valores=int(input('Cuantos valores va a graficar: '))
    x_valores=[i for i in range(valores)]
    y_valores=[]
    for j in x_valores:
        val=int(input(f'Valor y para {j}: '))
        y_valores.append(val)

    fig.line(x_valores, y_valores, line_width=2)
    show(fig)
