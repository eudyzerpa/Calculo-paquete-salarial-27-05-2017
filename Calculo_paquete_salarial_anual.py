#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys

#Programa en Python para calcular el Paquete Salarial Anual

# DeclaraciÃ³n de variables 

salario_base=int(9)
salario_base_diario=int(9)
salario_integral=float(2)
monto_mensual_cesta_ticket=int(9)
cesta_ticket_diario=int(9)
dias_bono_vacacional=float(2)
factor_bono_vacacional_diario=float(2) 
monto_bono_vacacional_diario=float(2)
factor_utilidad_diaria=float(2)
monto_utilidad_diaria=float(2)
meses=int(2)
dias_meses_utilidades=float(2)
dias_mes =30
meses_ano =12
porcentaje_aporte_empresarial_caja_ahorros=int(2)
monto_caja_ahorros=int(9)
porcentaje_comisiones=int(2)
monto_comisiones=float(2)
bonificacion_BCR=float(2)
mi_paquete_anual=float(2)
monto_anual_prestaciones=float(2)
mi_salario_mensual_comisiones=float(2)
mi_salario_mensual_BCR=float(2)
salario_integral=float(2)
salario_integral_mensual=float(2)



def calculo_salario_mensual(item1, item2):
	salario_base = item1
	monto_comisiones = item2

	paquete_mensual = salario_base + monto_comisiones
	return paquete_mensual 

# Funciones para calculo de paquete anual

def calculo_paquete_anual_con_RxP(item1, item2, item3, item4, item5, item6, item7, item8):
	salario_anual = item1
	monto_anual_cesta_ticket = item2
	monto_total_bono_vacacional = item3
	monto_total_utilidades = item4
	monto_anual_prestaciones = item5
	monto_anual_caja_ahorros = item6
	monto_anual_ayuda_escolar = item7
	monto_anual_comisiones = item8
	

	paquete_anual = salario_anual + monto_anual_cesta_ticket + monto_total_bono_vacacional + monto_total_utilidades + monto_anual_prestaciones + monto_anual_caja_ahorros + monto_anual_ayuda_escolar + monto_anual_comisiones
	return paquete_anual


def calculo_paquete_anual_con_BCR(item1, item2, item3, item4, item5, item6, item7, item8):
	salario_anual = item1
	monto_anual_cesta_ticket = item2
	monto_total_bono_vacacional = item3
	monto_total_utilidades = item4
	monto_anual_prestaciones = item5
	monto_anual_caja_ahorros = item6
	monto_anual_ayuda_escolar = item7
	bonificacion_BCR = item8

	paquete_anual = salario_anual + monto_anual_cesta_ticket + monto_total_bono_vacacional + monto_total_utilidades + monto_anual_prestaciones + monto_anual_caja_ahorros + monto_anual_ayuda_escolar + bonificacion_BCR
	return paquete_anual               	

# Captura de informaciÃ³n de ingresos

print("Por favor indique si su cargo es Supervisorio o Ingeniero/Arquitecto")
cargo = int(input("Si su cargo es Supervisorio (Gerente, Lider) presione 1 , si su cargo es Arquitecto o Ingeniero presione 2 : "))


if cargo == 2:

	salario_base = input("Introduzca el monto de su salario basico: ")
	salario_base_diario = salario_base / dias_mes

	monto_mensual_cesta_ticket = input("Introduzca el monto mensual que percibe por concepto de Cesta Ticket: ")
	cesta_ticket_diario = monto_mensual_cesta_ticket / dias_mes

	dias_bono_vacacional = input("Introduzca el numero de dias considerados para el pago de su bono vacacional: ")

	meses = input("Introduzca el numero de meses de utilidades que prevee pagara CANTV este año: ")
	dias_meses_utilidades = meses * dias_mes       	

	porcentaje_aporte_empresarial_caja_ahorros = input("Introduzca el porcentaje que aporta CANTV por concepto de Caja de Ahorros: ")
	monto_caja_ahorros = (salario_base * porcentaje_aporte_empresarial_caja_ahorros)/100

	porcentaje_comisiones = input("Indique el promedio porcentaje mensual (20%-30%) que percibe por concepto de comisiones: ")
	monto_comisiones = (salario_base * porcentaje_comisiones)/100

	monto_mensual_ayuda_escolar = input("(Pago parcial Guardería/Preescolar): Si recibe este beneficio social indique el monto mensual que percibe por este concepto, en caso contrario introduzca 0 : ")

else:

	salario_base = input("Introduzca el monto de su salario basico: ")
	salario_base_diario = salario_base / dias_mes

	monto_mensual_cesta_ticket = input("Introduzca el monto mensual que percibe por concepto de Cesta Ticket: ")
	cesta_ticket_diario = monto_mensual_cesta_ticket / dias_mes

	dias_bono_vacacional = input("Introduzca el numero de dias considerados para el pago de su bono vacacional: ")

	meses = input("Introduzca el numero de meses de utilidades que prevee pagara CANTV este año: ")
	dias_meses_utilidades = meses * dias_mes       	

	porcentaje_aporte_empresarial_caja_ahorros = input("Introduzca el porcentaje que aporta CANTV por concepto de Caja de Ahorros: ")
	monto_caja_ahorros = (salario_base * porcentaje_aporte_empresarial_caja_ahorros)/100

	monto_mensual_ayuda_escolar = input("(Pago parcial Guardería/Preescolar): Si recibe este beneficio social indique el monto mensual que percibe por este concepto, en caso contrario introduzca 0 : ")



# Calculo de Salario Integral 

factor_bono_vacacional_diario = ((float(dias_bono_vacacional) / meses_ano) / dias_mes)
monto_bono_vacacional_diario = factor_bono_vacacional_diario*salario_base_diario

factor_utilidad_diaria = ((float(dias_meses_utilidades) / meses_ano) / dias_mes)
monto_utilidad_diaria = factor_utilidad_diaria*salario_base_diario


salario_integral = salario_base_diario + monto_utilidad_diaria + monto_bono_vacacional_diario
salario_integral_mensual = salario_integral * 30

# Calculo de Salario anual

salario_anual = salario_base * meses_ano 

# Calculo de utilidades

monto_total_utilidades = dias_meses_utilidades * salario_base_diario 

# Calculo de prestaciones 

monto_mensual_prestaciones = salario_integral * 5
monto_anual_prestaciones = monto_mensual_prestaciones * meses_ano


# Calculo de pagos anuales: Bono vacacional, utilidades,  montos anuales por concepto de prestaciones sociales, aporte empresa Caja de Ahorros, ayuda escolar y comisiones de ventas 

monto_total_bono_vacacional = salario_base_diario * dias_bono_vacacional
monto_anual_cesta_ticket = (monto_mensual_cesta_ticket * meses_ano)
monto_anual_caja_ahorros = (monto_caja_ahorros * meses_ano)
monto_anual_comisiones = (monto_comisiones * meses_ano)
monto_anual_prestaciones = (monto_mensual_prestaciones * meses_ano)
monto_anual_ayuda_escolar = (monto_mensual_ayuda_escolar * meses_ano)
bonificacion_BCR = salario_base * 2.5

mi_salario_mensual_comisiones = calculo_salario_mensual(salario_base, monto_comisiones)
mi_salario_mensual_BCR = salario_base + (bonificacion_BCR/meses_ano)



# TOTALES
mi_paquete_anual = calculo_paquete_anual_con_BCR(salario_anual, monto_anual_cesta_ticket, monto_total_bono_vacacional, monto_total_utilidades, monto_anual_prestaciones, monto_anual_caja_ahorros, monto_anual_ayuda_escolar, bonificacion_BCR)
mi_paquete_anual = calculo_paquete_anual_con_RxP(salario_anual, monto_anual_cesta_ticket, monto_total_bono_vacacional, monto_total_utilidades, monto_anual_prestaciones, monto_anual_caja_ahorros, monto_anual_ayuda_escolar, monto_anual_comisiones)


#paquete_anual = salario_anual + monto_anual_cesta_ticket + monto_total_bono_vacacional + monto_total_utilidades + monto_anual_prestaciones + monto_anual_caja_ahorros + monto_anual_ayuda_escolar + monto_anual_comisiones


 # Reporte
print("                                                     ")
print("                                                     ")
print("########################## PAQUETE ANUAL ####################")
print("                                                     ")
print "Su Paquete Anual antes de impuestos (bruto) es: Bs", round(mi_paquete_anual,2)
print("                                                     ")
print "NOTA: El Paquete Anual esta compuesto por los ingresos relacionados a salario base anual, cesta ticket anual, bono vacacional, utilidades, prestaciones sociales, aporte de Cantv a la caja de ahorros mas comisiones o bonificaciones(BCR) según sea el caso, tambien son considerados otros ingresos unitarios y/o recurrentes"
print("                                                     ")
print("                                                     ")
print("########################## DESGLOSE INGRESO ANUAL ####################")
print("                                                     ")
print "El monto anual que percibe por concepto de salario basico es: Bs", salario_anual
print "El monto anual que percibe por concepto de Cesta Ticket es: Bs", monto_anual_cesta_ticket
print "El monto anual que percibe por concepto de Bono vacacional es: Bs", monto_total_bono_vacacional
print "El monto anual que percibe por concepto de utilidades es: Bs", monto_total_utilidades
print "El monto anual que percibe por concepto de Prestaciones sociales es: Bs", round(monto_anual_prestaciones,2)
print "El monto anual que percibe por concepto de aporte empresa a Caja de Ahorros es: Bs", monto_anual_caja_ahorros
print "El monto anual que percibe por concepto de ayuda pago preescolar es: Bs", monto_anual_ayuda_escolar
print "                                                     "
print "########################## BASES DE CALCULO ####################"
print "                                                     "
print "El monto diario del Salario integral devengado en 2017 es: Bs", round(salario_integral,2)
print "El monto mensual del Salario integral devengado en 2017 es: Bs", round(salario_integral_mensual,2)
print "                                                     "
print "                                                     "
print "########################## COMPARATIVA INGRESOS X MODELO DE COMPENSACIÓN (RXP vs BCR) ####################"
print "                                                     "
print "-Aplica Ing/Arq- El monto mensual que percibe por concepto de salario basico y comisiones es: Bs", round(mi_salario_mensual_comisiones,2)
print "-Aplica Supervisor- El monto mensual que percibe por concepto de salario basico y BCR es: Bs", round(mi_salario_mensual_BCR,2)
print "                                                     "




    

		
	











#			 printf("Los dÃ­as de utilidades a considerar para el calculo son: %d\n",dias_meses_utilidades);
#			 printf("El salario integral diario es: %d\n",salario_integral);
#			 printf("                                                     \n");
#			 printf("##########################INGRESO DIARIO####################\n");
#			 printf("                                                     \n");
#			 printf("Su salario base diario es: Bs %d\n",salario_base_diario);
#			 printf("Su pago diario por concepto de Cesta Ticket es: Bs %d\n",cesta_ticket_diario);
#			 printf("La utilidad diarÃ­a considerada para el calculo de salario integral es Bs: %.2f\n",monto_utilidad_diaria);
#			 printf("El pago unitario por dÃ­a de vacaciÃ³n considerado para el calculo de salario integral es Bs: %.2f\n",monto_bono_vacacional_diario);
#			 printf("Usted acumula mensualmente por concepto de prestaciones sociales: Bs %d\n",monto_mensual_prestaciones);
#			 printf("                                                     \n");
#			 printf("##########################DESGLOSE DE INGRESOS ANUALES|####################\n");
#			 printf("                                                     \n");
#			 printf("El monto anual que percibe por concepto de salario bÃ¡sico es: Bs %d\n",salario_anual);
#			 printf("El monto anual que percibe por concepto de Cesta Tickets es: Bs %d\n",monto_anual_cesta_ticket);
#			 printf("El monto de su bono vacacional es: Bs %d\n",monto_total_bono_vacacional);
#			 printf("Usted percibe anualmente por concepto de utilidades: Bs %d\n",monto_total_utilidades);
#			 printf("Usted acumula anualmente por concepto de prestaciones sociales: Bs %d\n",monto_anual_prestaciones);
#			 printf("                                                     \n");
#			 printf("##########################INGRESO ANUAL####################\n");
#			 printf("El paquete anual es: %d\n", paquete_anual);



#print paquete_anual

