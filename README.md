# ⌨️ Python Key Event Logger (Educational Project)

Este es un script de Python diseñado para registrar las pulsaciones de teclas en tiempo real y guardarlas en un archivo de texto local. El objetivo de este proyecto es entender la interacción entre el software y los eventos de hardware, así como el manejo de estados de teclado (Caps Lock, Shift) mediante programación.

---

## 🚀 Características

* **Detección Inteligente de Mayúsculas:** Utiliza lógica XOR para alternar correctamente entre mayúsculas y minúsculas basándose en el estado de `Caps Lock` y `Shift`.
* **Prevención de Duplicados:** Gestiona el estado de las teclas para evitar que el archivo se llene de caracteres repetidos cuando se mantiene presionada una tecla.
* **Limpieza de Log:** Filtra teclas de control (como Ctrl o Alt) y traduce teclas como `Space` o `Enter` a sus caracteres naturales para una lectura fluida.
* **Multi-evento:** Registra caracteres especiales y símbolos.

---

## 🛠️ Requisitos

Para ejecutar este script, necesitarás tener instalado **Python 3.x** y la librería `pynput`.

* **Instalar dependencias:**

   ```
   pip install pynput
   ```

* Compatibilidad:

La detección del estado de Caps Lock mediante ctypes está optimizada para Windows.

En otros sistemas operativos, el registro de teclas funcionará, pero la lógica de estado del LED de bloqueo puede variar.

---

## 📂 Uso
Clona este repositorio o descarga el archivo .py.

Abre una terminal en la carpeta del proyecto.

Ejecuta el script:

```
python logger.py
```

El archivo registro_teclas.txt se creará automáticamente en el mismo directorio.

Para detener el registro, presiona la tecla Esc.

---

## 🧠 Conceptos Aprendidos
- Manejo de Eventos (Listeners): Uso de hilos en segundo plano para escuchar entradas del sistema.
- Lógica Booleana: Implementación de la puerta lógica XOR para determinar el "Case" (Upper/Lower) de las letras.
- Gestión de Archivos: Escritura persistente en modo "append" (a) con codificación UTF-8.

---

## ⚠️ Aviso Legal (Disclaimer)
Este proyecto tiene fines exclusivamente educativos y de investigación. El uso de esta herramienta para monitorizar dispositivos sin el consentimiento explícito del propietario es ilegal y poco ético. El autor no se hace responsable del mal uso que se le pueda dar a este código. ¡Sé un desarrollador responsable!
