agenda = []

print("Agenda")
print("Opciones")
print("1- Agregar contacto (deberá agregar 5 contactos como mínimo)")
print("2- Buscar número")
print("0- Salir")

cant_contac = 0

opcion_seleccionada = int(input("Eliga opción: "))
while opcion_seleccionada != 0:
    if opcion_seleccionada == 1:
        while cant_contac < 2:
            nuevo_nombre = input("Ingrese nombre completo: ")
            nuevo_telefono = int(input("Ingrese numero de telefono: "))
            nuevo_contacto = {"nombre": nuevo_nombre, "telefono": nuevo_telefono}
            agenda.append(nuevo_contacto)
            cant_contac += 1
        opcion_seleccionada = int(input("Si desea seguir agregando presione 1, si ya no desea agregar presione 0: "))
        print(agenda)
    
    else:
        nombrecontacto = input("Ingrese nombre del contacto que desea buscar: ")
        def buscar_contacto():
            for x in agenda:
                if nombrecontacto == x["nombre"]:
                    print(int(x["telefono"]))
        
        buscar_contacto()
    opcion_seleccionada = int(input("Si desea seguir agregando presione 1, si desea buscar un número presione 2, si ya no desea agregar presione 0: "))
        