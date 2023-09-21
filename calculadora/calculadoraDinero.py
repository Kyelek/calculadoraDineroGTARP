import math

def imprimir_linea(repeticiones):
    for _ in range(repeticiones):
        print('═', end='')
    print()  # para el salto de línea

while True:

    """ Comisiones """

    comision_normal_ganancias = 0.25
    comision_premium_ganancias = 0.20
    comision_deluxe_ganancias = 0.10

    comision_obligatoria = 0.75  # --> perdemos 25% (75% --> para nosotros)
    comision_obligatoria_perdida = 0.25  # dinero perdido de la comisión obligatoria
    comision_normal = 0.50  # -50% (25% --> para nosotros)
    comision_premium = 0.55  # -45% (20% --> para nosotros)
    comision_deluxe = 0.65  # -35% (10% --> para nosotros)
    
    """ Fuciones """
    
    dinero_Ingresado = float(input("¿Cuánto dinero quieres ingresar?"))
    porcentaje_manual = input("¿Ingresa Manualmente el porcentaje? (S/N): ").strip().lower()
    
    if porcentaje_manual == 's':
        while True:
        
            comision_manual = (float(input("Introduce la comision manual: ")))
            comision_manual_completa = (((comision_manual + 25 ) * 100 ) // 100)
            if comision_manual_completa > 100 :
                print("La comision añadida no puede ser mayor a 75")
            else:
                break
        
        
        dinero_menos_comision_manual = dinero_Ingresado * comision_manual_completa # total dinero con la comision aplicada
        ganancias_comision_manual_pibe = dinero_Ingresado * comision_manual_completa # porcentaje de ganancias para el pibe
        
        dinero_perdido_menos_maquina = dinero_Ingresado * comision_obligatoria
        dinero_perdido_maquina = comision_obligatoria_perdida * dinero_Ingresado
        
        dinero_total_pibe_maquina = (ganancias_comision_manual_pibe //100) + (dinero_perdido_maquina)
        dinero_total_mafia_manual = dinero_Ingresado - dinero_total_pibe_maquina
        
        imprimir_linea(50)
        print("Total porcentaje aplicado + 25% = ", comision_manual_completa, "%" )
        print("Total dinero que se queda la maquina = ", dinero_perdido_maquina )
        print("Total dinero para el pibe =", ganancias_comision_manual_pibe // 100)
        print("Total dinero que se queda la mafia = ", dinero_total_mafia_manual)
        imprimir_linea(50)
                
    else:

        """Calculos"""

        """                     Ingreso directo de mafia                        """

        dinero_menos_comision_obligatoria = dinero_Ingresado * comision_obligatoria
        dinero_perdido_comision_obligatoria = dinero_Ingresado * comision_obligatoria_perdida  # dinero perdido que se come la máquina siempre

        """                     Ingreso comisión normal                         """

        dinero_menos_comision_normal = dinero_Ingresado * comision_normal  # 50% del 100% --> esto es lo que se lleva el pibe
        dinero_ganado_comision_normal = dinero_Ingresado * comision_normal_ganancias  # 25% del 100% -- ganancias --> esto nos llevamos nosotros

        """                     Ingreso comisión premium                        """

        dinero_menos_comision_premium = dinero_Ingresado * comision_premium  # 55% del 100% --> esto es lo que se lleva el pibe
        dinero_ganado_comision_premium = dinero_Ingresado * comision_premium_ganancias  # 20% del 100% --> ganancias --> esto nos lo llevamos nosotros

        """                     Ingreso comisión deluxe                         """

        dinero_menos_comision_deluxe = dinero_Ingresado * comision_deluxe  # 65% del 100% --> esto se lleva el pibe
        dinero_ganado_comision_deluxe = dinero_Ingresado * comision_deluxe_ganancias  # 10% del 100% --> esto nos lo llevamos nosotros
        
        
        
        """Salida por consola"""

        imprimir_linea(50)
        print("-- BLANQUEO DINERO MAFIA --")
        print("Total dinero ganado 75% = {:,.2f}".format(dinero_menos_comision_obligatoria))
        print("Total perdido la maquina - 25% = {:,.2f}".format(dinero_perdido_comision_obligatoria))
        imprimir_linea(50)
        print("-- BLANQUEO DE DINERO COMISION NORMAL 50% --")
        print("Dinero para el Pibe = {:,.2f}".format(dinero_menos_comision_normal))
        print("Dinero para la mafia = {:,.2f}".format(dinero_ganado_comision_normal))
        imprimir_linea(50)
        print("-- BLANQUEO DE DINERO COMISION PREMIUM 55% -- ")
        print("Dinero para el pibe = {:,.2f}".format(dinero_menos_comision_premium))
        print("Dinero para la mafia = {:,.2f}".format(dinero_ganado_comision_premium))
        imprimir_linea(50)
        print("-- BLANQUEO DE DINERO COMISION DELUXE 65% -- ")
        print("Dinero para el pibe = {:,.2f}".format(dinero_menos_comision_deluxe))
        print("Dinero para la mafia = {:,.2f}".format(dinero_ganado_comision_deluxe))
        imprimir_linea(50)

        # Pedir al usuario si quiere realizar otra operación
    respuesta = input("¿Quieres ingresar otra cantidad? (S/N): ").strip().lower()
    if respuesta != 's':
        break  # Salir del bucle si la respuesta no es 's'





