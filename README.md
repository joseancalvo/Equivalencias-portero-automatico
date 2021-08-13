# Equivalencias-portero-automatico
Pequeña aplicación para facilitar la sustitución de los telefonillos de portero automático convencional. Solo es valida para sistemas convencionales 4 + n.
Seleccionamos la marca del telefonillo que está instalado y la del telefonillo universal que vamos a instalar. La aplicación nos devolverá el orden de los cables en las diferentes marcas.

Es un pequeño programa escrito en python para ejecutar en una terminal. Se puede utilizar en smartphones Iphone y Android desde las aplicaciones de terminal iSH y Termux respectivamente.

iSH lo podéis descargar desde la app store de Apple y Termux lo tenéis que descargar desde la web de [F-Droid](https://f-droid.org/es/)

Una vez instalada la app, necesitais instalar git y python.
  
  # En Termux
  
  Primero actualizamos:
  >pkg update
  
  Luego instalamos Git y Python:
  >pkg install git python3
  
  Descargamos el repositorio de Github:
  >git clone https://github.com/joseancalvo/equivalencias-portero-automatico.git
  
  Entramos en la carpeta donde hemos clonado el repositorio:
  >cd equivalencias-portero-automatico
  
  Y finalmente ejecutamos la aplicación:
  >python3 equivalenciasportero.py
  
  ![WhatsApp Image 2021-08-13 at 17 51 49](https://user-images.githubusercontent.com/64921162/129386706-2cefc224-3736-4661-87dc-61fcb7a6a349.jpeg)


  # En iSH
  
  Primero actualizamos:
  >apk update
  >apk upgrade
  
  Luego instalamos Git y Python:
  >apk add git python3
  
  Descargamos el repositorio de Github:
  >git clone https://github.com/joseancalvo/equivalencias-portero-automatico.git
  
  Entramos en la carpeta donde hemos clonado el repositorio:
  >cd equivalencias-portero-automatico
  
  Y finalmente ejecutamos la aplicación:
  >python3 equivalenciasportero.py
