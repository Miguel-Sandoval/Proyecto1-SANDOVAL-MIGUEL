from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches
from quick_sort import quick_sort

import sys

numero_produtos = len(lifestore_products)

year_dictionary = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}


def ventas_por_producto(reembolso=False):

    ventar_por_producto_lista = [[i + 1, 0] for i in range(numero_produtos)]
    for sale in lifestore_sales:
        if reembolso:
            if sale[4] == 0:
                ventar_por_producto_lista[sale[1] - 1][1] += 1
        else:

            ventar_por_producto_lista[sale[1] - 1][1] += 1
    return ventar_por_producto_lista


def calcular_busquedas_por_producto():

    busqueda_por_lista_productos = [[i + 1, 0] for i in range(numero_produtos)]
    for search in lifestore_searches:

        busqueda_por_lista_productos[search[1] - 1][1] += 1
    return busqueda_por_lista_productos


def ordenar_productos_por_ventas():


    ventar_por_producto_lista = ventas_por_producto()

    quick_sort(ventar_por_producto_lista, lambda x: x[1])

    return ventar_por_producto_lista


def organizar_productos_por_busquedas():


    busqueda_por_lista_productos = calcular_busquedas_por_producto()

    quick_sort(busqueda_por_lista_productos, lambda x: x[1])

    return busqueda_por_lista_productos


def calculadora_por_categorias(array):

    for element in array:
        product_id = element[0]
        categoria_producto = lifestore_products[product_id - 1][3]
        element.append(categoria_producto)
    por_categoria_lista = []
    categoria_anterior = array[0][2]
    acumulacion_categoria = 0
    productos_por_categoria = 0
    # Append a dummy element to the array to consider the last category
    array.append([0, 0, 'dummy'])
    for product in array:
        category = product[2]
        if category != categoria_anterior:
            por_categoria_lista.append([categoria_anterior, acumulacion_categoria, productos_por_categoria])
            acumulacion_categoria = 0
            productos_por_categoria = 0

        categoria_anterior = category
        acumulacion_categoria += product[1]
        productos_por_categoria += 1
    # Delete the dummy element
    del array[-1]

    return por_categoria_lista


def ordenar_categorias_por_ventas():
    ventas_por_producto = ventas_por_producto()
    ventas_por_lista_categoria = calculadora_por_categorias(ventas_por_producto)
    quick_sort(ventas_por_lista_categoria, lambda x: x[1])

    return ventas_por_lista_categoria


def ordenar_categorias_por_busquedas():
    busquedas_por_producto = calcular_busquedas_por_producto()
    busqueda_por_categoria_lista = calculadora_por_categorias(busquedas_por_producto)
    quick_sort(busqueda_por_categoria_lista, lambda x: x[1])

    return busqueda_por_categoria_lista


def mejor_y_peor_productos_reviews():

    puntuacion_promedio_por_producto = []
    suma_promedio_por_producto = [[i + 1, 0] for i in range(numero_produtos)]
    # Copying the list of lists is not working due to python binding, the element lists are bound
    ventar_por_producto_lista = ventas_por_producto()

    for sale in lifestore_sales:
        product_id = sale[1]
        suma_promedio_por_producto[product_id - 1][1] += sale[2]

    for puntaje_acumulativo in suma_promedio_por_producto:
        product_id = puntaje_acumulativo[0]
        sales = ventar_por_producto_lista[product_id - 1][1]
        # Only count them if they have been sold
        if sales > 0:
            puntaje_promedio = puntaje_acumulativo[1] / sales
            puntuacion_promedio_por_producto.append([product_id, puntaje_promedio])

    # Sort the list from minimum to maximum
    quick_sort(puntuacion_promedio_por_producto, lambda x: x[1])

    return puntuacion_promedio_por_producto


def calculo_total_ingresos():
    # declare total_revenue equal to zero
    total_revenue = 0
    ventas_por_producto = ventas_por_producto(reembolso=True)
    for sales in ventas_por_producto:
        product_id = sales[0]
        total_revenue += lifestore_products[product_id - 1][2] * sales[1]
    return total_revenue


def calculo_mensual_ventas():
    # Create a list of lists with elements [month, sales_per_month]
    monthly_sales_list = [[month, 0] for month in range(1, 13)]
    total_concreted_sales = 0
    for sale in lifestore_sales:
        month = int(sale[3].split('/')[1])
        if sale[4] == 0:
            # Increment the sales per month if the in the monthly_sales_list
            monthly_sales_list[month - 1][1] += 1
            total_concreted_sales += 1

    #quick_sort(monthly_sales_list, lambda x: x[1])
    return monthly_sales_list, total_concreted_sales


def option_1():

    show_worst = 60;
    ventar_por_producto_lista = ordenar_productos_por_ventas()

    print('Los 10 productos mas vendidos son: ')
    for index in range(1, 11):
        print(
            f'{index}.- {ventar_por_producto_lista[-index][1]} ventas para'
            f' {lifestore_products[ventar_por_producto_lista[-index][0] - 1][1]}')
    print('\n')


    busqueda_por_lista_productos = organizar_productos_por_busquedas()
    print('El top 10 productos buscados: ')
    for index in range(1, 11):
        print(
            f'{index}.- {busqueda_por_lista_productos[-index][1]} busquedas para'
            f' {lifestore_products[busqueda_por_lista_productos[-index][0] - 1][1]}')
    print('\n')


    sales_per_categories_list = ordenar_categorias_por_ventas()
    sales_per_categories_list.reverse()
    print(f'ventas por categoria son:')
    for index in range(len(sales_per_categories_list)):
        print(
            f'{index + 1}.- {sales_per_categories_list[index][1]} para {sales_per_categories_list[index][0]} with '
            f'{sales_per_categories_list[index][2]} productos'
        )
    print('\n')

    searches_per_categories_list = ordenar_categorias_por_busquedas()
    searches_per_categories_list.reverse()
    print(f'Busquedas por categoria son:')
    for index in range(len(searches_per_categories_list)):
        print(
            f'{index + 1}.- {searches_per_categories_list[index][1]} para {searches_per_categories_list[index][0]} '
            f'con {searches_per_categories_list[index][2]} productos'
        )


def option_2():

    puntuacion_promedio_por_producto = mejor_y_peor_productos_reviews()
    print('El top 10 de los productos puntuados es: ')

    for index in range(1, 21):
        print(
            f'{index}.- {puntuacion_promedio_por_producto[-index][1]:.2f}/5 estrellas para'
            f' {lifestore_products[puntuacion_promedio_por_producto[-index][0] - 1][1]}')
    print('\n')
    print('los 10 peores rateados son: ')
    for index in range(10):
        print(
            f'{index + 1}.- {puntuacion_promedio_por_producto[index][1]:.2f}/5 estrellas para'
            f' {lifestore_products[puntuacion_promedio_por_producto[index][0] - 1][1]}')


def option_3():

    total_revenue = calculo_total_ingresos()
    monthly_sales_list, total_concreted_sales = calculo_mensual_ventas()
    print(f'los reembolsos mensuales son: {total_revenue}')
    print(f'Ingresos promedio: {total_revenue / 8:.2f}')
    print(f'las ventas del 2021: {total_concreted_sales} \n')
    print(f'Las ventas mensuales son:')
    for index, month in enumerate(monthly_sales_list):
        print(f'{index + 1} .- {month[1]}  ventas concretadas en {year_dictionary[month[0]]}')
