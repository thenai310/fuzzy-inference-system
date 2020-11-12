from fuzzy_system import *

system = FuzzySystem()

quality = FuzzyVariable('Quality', 0, 10)
quality.add_gaussian('Bad', 2,0)
quality.add_gaussian('Good', 2, 5)
quality.add_gaussian('Excellent', 2,10)

position = FuzzyVariable('Position', 0, 20)
position.add_trapezoidal('Close', 0, 0, 4, 8)
position.add_trapezoidal('Mid', 6, 9, 12, 15)
position.add_trapezoidal('Far', 14, 18, 20, 20)

attendance = FuzzyVariable('Attendance', 20, 100)
attendance.add_triangular('Low', 20, 20 ,40)
attendance.add_triangular('Moderate', 30, 50, 70)
attendance.add_triangular('High', 60, 100, 100)


system.add_rule([(position,'Far'),(quality,'Bad')],(attendance,'Low',False), 'or')

system.add_rule([(position,'Mid'),(quality,'Good')],(attendance,'Moderate',False))

system.add_rule([(position,'Close'),(quality,'Excellent')],(attendance,'High',False),'or')


print("Ingrese la calidad en base a 10 y la distancia hasta 20km")
q,p = int (input("Calidad: ")),int (input("Distancia: "))
input_values = [(quality,q),(position,p)]

#############################
#   calls to run the system, use 'centroid','bisector','lom','som' or 'mom' for desired defuzzify method
#   and use 'Mamdani' or 'Larsen' for agregation method
#############################

ouput_mam = system.run_sid_mamdani(input_values,'centroid')
ouput_lars = system.run_sid_larsen(input_values, 'centroid')

print(f'La asistencia esperada es de {ouput_mam}% en Mamdani')
print(f'La asistencia esperada es de {ouput_lars}% en Larsen')

#########################----------show the variables in a graphic---------#################################
# fig, axs = plt.subplots(3,1)
# position.plot_variable(axs[0],False)
# quality.plot_variable(axs[1],False)
# attendance.plot_variable(axs[2],False)
# plt.show()
