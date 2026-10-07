Esta guía documenta el procedimiento probado por PC Game Archive para instalar y ejecutar **la edición española Big Box de A Sangre Fría, compuesta por tres CD-ROM y conservada en la ficha #000216**, sobre Windows 10 Pro.

Los resultados corresponden a esta edición concreta y al entorno descrito. No deben extrapolarse automáticamente a otras ediciones o configuraciones.

## Punto de partida

La prueba se realizó exclusivamente desde una **copia de trabajo derivada de los tres másteres de preservación verificados**. Antes de utilizarla, los seis ficheros BIN/CUE se comprobaron mediante SHA-256 y coincidieron con los másteres.

## Equipo utilizado

- Sistema operativo: Windows 10 Pro
- Build: 19045
- Arquitectura: 64 bits
- Procesador: Intel Core i5-3470 @ 3.20 GHz
- Memoria: ~15,9 GiB de RAM física
- Gráficos: Intel HD Graphics
- Driver gráfico: 10.18.10.4358
- Resolución: 1360 × 768
- Audio: Intel Display Audio y High Definition Audio, ambos operativos durante la prueba

## Software utilizado

### WinCDEmu

- Versión: **4.1**
- Finalidad: montaje de los BIN/CUE de la copia de trabajo como unidad óptica virtual.

No fue necesario utilizar parches, wrappers, modo de compatibilidad, máquina virtual ni ejecución como administrador.

## Preparar la copia de trabajo

La copia de trabajo debe contener los BIN/CUE verificados de los tres soportes y mantenerse separada de los másteres de preservación.

Hashes de referencia:

```text
CD1 BIN  A2E6389E84A0DB8987436313474CD63FBB7BD6840B846696B6168B61C3B75F3F
CD1 CUE  DD098198B8E26D1BA33916A29CEBB8750920C8A25DCC51E15A703D3532FD187E
CD2 BIN  D7885BE96FBF94A1CBFDC45497FDBAD62E74F8944E0B82470ED7F23B6646C2BA
CD2 CUE  DDA6BAE46D3B7B182A67AEFB376848146302B4C338A8CA176AAE3D2E95FF90BF
CD3 BIN  14CCBC39339FDF2290AA07FFF4F7FBC3A8C08911D0D263288237B450DF062512
CD3 CUE  FF63F8D352C5D22041254E9A5153761A2021A1E3F7930AA87B07681F67B98A12
```

## Instalación

1. Montar `ICB_CD1.cue` con WinCDEmu 4.1.
2. Comprobar que Windows reconoce el volumen `ICB_CD1`.
3. Ejecutar `setup.exe` de forma normal.
4. Cuando el instalador solicite **A Sangre Fría 2**, desmontar CD1 y montar `ICB_CD2.cue` en la misma unidad virtual.
5. Continuar la instalación.
6. Cuando solicite el tercer disco, desmontar CD2 y montar `ICB_CD3.cue`.
7. Completar la instalación.

En la prueba realizada, los dos cambios de disco fueron reconocidos correctamente y la instalación finalizó sin incidencias.

No fue necesario instalar el DirectX 7 incluido en el CD.

## Ejecución

Después de la instalación, el juego requiere que esté montado **CD1**.

1. Desmontar cualquier otro disco que permanezca montado.
2. Montar `ICB_CD1.cue` con WinCDEmu 4.1.
3. Ejecutar A Sangre Fría normalmente.

En el entorno probado el juego arrancó correctamente sin aplicar ningún ajuste adicional.

## Resultado de las pruebas

- **Instalación:** Correcto.
- **Cambios CD1 → CD2 → CD3:** Correcto.
- **Arranque con CD1 montado:** Correcto.
- **Menús:** Correcto.
- **Vídeos/cinemáticas:** Correcto.
- **Gráficos 2D:** Correcto.
- **Gráficos 3D:** Correcto.
- **Sonido:** Correcto.
- **Música:** Correcto.
- **Teclado/ratón:** Correcto.
- **Inicio de partida:** Correcto.
- **Juego representativo:** Correcto.
- **Guardado:** Correcto.
- **Carga:** Correcto.
- **Cambio de escena/nivel:** Correcto durante la prueba realizada.
- **Cierre:** Correcto.
- **Segundo arranque:** Correcto.
- **Gamepad/joystick:** No probado.
- **Multijugador:** No probado.

## Estado de compatibilidad

**Funcional en el entorno probado, sin ajustes adicionales.**

La edición española Big Box de tres CD-ROM conservada por PC Game Archive pudo instalarse y ejecutarse directamente en Windows 10 Pro build 19045. No fueron necesarios parches, wrappers, modos de compatibilidad ni privilegios de administrador.

## Limitaciones

Esta guía no valida otras ediciones, Windows 11, otros controladores gráficos, gamepad/joystick ni multijugador.

## Relación con la preservación

El procedimiento parte de una copia de trabajo derivada de los tres másteres verificados. El detalle de adquisición y verificación puede consultarse en el [registro de preservación de A Sangre Fría](../../preservacion/a-sangre-fria-bigbox/).

**Última prueba:** 07/10/2026.
