# Registro de compatibilidad — A Sangre Fría / Windows 10

**Estado:** Funcional en el entorno probado  
**Ficha PCGA:** #000216  
**URL:** `juegos/a-sangre-fria-bigbox/`  
**Fecha de última prueba:** 07/10/2026  
**Responsable:** PC Game Archive

## 1. Identificación

- Título: A Sangre Fría
- Edición: española Big Box
- Mercado / idioma: España / Español
- Soportes: 3 CD-ROM
- Registro de preservación: `registros_preservacion/a-sangre-fria-bigbox.md`

## 2. Punto de partida

Copia de trabajo derivada de los tres másteres BIN/CUE verificados. Los seis SHA-256 fueron comprobados en la máquina de pruebas antes del montaje y coincidieron con los másteres.

| Fichero | SHA-256 |
|---|---|
| `ICB_CD1.bin` | `A2E6389E84A0DB8987436313474CD63FBB7BD6840B846696B6168B61C3B75F3F` |
| `ICB_CD1.cue` | `DD098198B8E26D1BA33916A29CEBB8750920C8A25DCC51E15A703D3532FD187E` |
| `ICB_CD2.bin` | `D7885BE96FBF94A1CBFDC45497FDBAD62E74F8944E0B82470ED7F23B6646C2BA` |
| `ICB_CD2.cue` | `DDA6BAE46D3B7B182A67AEFB376848146302B4C338A8CA176AAE3D2E95FF90BF` |
| `ICB_CD3.bin` | `14CCBC39339FDF2290AA07FFF4F7FBC3A8C08911D0D263288237B450DF062512` |
| `ICB_CD3.cue` | `FF63F8D352C5D22041254E9A5153761A2021A1E3F7930AA87B07681F67B98A12` |

## 3. Entorno anfitrión

- Sistema operativo: Windows 10 Pro
- Build: 19045
- Arquitectura: 64 bits
- CPU: Intel Core i5-3470 @ 3.20 GHz
- RAM física informada: 17.057.873.920 bytes (~15,9 GiB)
- GPU: Intel HD Graphics
- Driver GPU: 10.18.10.4358
- Resolución: 1360 × 768
- Audio: Sonido Intel(R) para pantallas — OK
- Audio: Dispositivo de High Definition Audio — OK

## 4. Herramientas y ajustes

- WinCDEmu 4.1: montaje de BIN/CUE.
- PowerShell: verificación SHA-256 y comprobación del volumen.
- Parches: ninguno.
- Wrappers: ninguno.
- Modo de compatibilidad: no utilizado.
- Ejecución como administrador: no utilizada.
- DirectX 7 incluido en el CD: no fue necesario instalarlo durante la prueba.

## 5. Instalación base

1. Se montó `ICB_CD1.cue` con WinCDEmu 4.1.
2. Windows expuso la unidad `E:` con etiqueta `ICB_CD1`, CDFS y tamaño lógico 676.773.888 bytes.
3. Se ejecutó `E:\setup.exe` sin ajustes especiales.
4. El instalador arrancó correctamente.
5. Durante la instalación solicitó el CD2; se desmontó CD1 y se montó `ICB_CD2.cue`.
6. La instalación continuó correctamente y posteriormente solicitó CD3.
7. Se desmontó CD2 y se montó `ICB_CD3.cue`.
8. La instalación finalizó correctamente.

## 6. Ejecución

Al intentar arrancar tras finalizar la instalación con CD3 montado, el juego solicitó el **CD1**. Tras montar `ICB_CD1.cue`, el juego arrancó correctamente sin ajustes adicionales.

Se inició una partida, se jugó una secuencia representativa, se guardó, se cerró el juego, se realizó un segundo arranque y se cargó correctamente la partida guardada.

## 7. Procedimiento final reproducible

1. Verificar los SHA-256 de los seis ficheros de la copia de trabajo contra los másteres.
2. Montar `ICB_CD1.cue` con WinCDEmu 4.1.
3. Ejecutar `setup.exe` de forma normal.
4. Cuando el instalador solicite el segundo disco, desmontar CD1 y montar `ICB_CD2.cue` en la misma unidad virtual.
5. Cuando solicite el tercero, desmontar CD2 y montar `ICB_CD3.cue`.
6. Completar la instalación.
7. Para ejecutar el juego, montar `ICB_CD1.cue`.
8. Ejecutar el juego normalmente, sin modo de compatibilidad ni elevación administrativa.

## 8. Matriz funcional

| Subsistema | Estado | Observaciones |
|---|---|---|
| Instalación | Correcto | Instalación completa desde 3 CD |
| Arranque | Correcto | Requiere CD1 montado |
| Menús | Correcto | Verificado |
| Vídeos/cinemáticas | Correcto | Verificado durante la prueba |
| Gráficos 2D | Correcto | Verificado |
| Gráficos 3D | Correcto | Verificado |
| Sonido | Correcto | Verificado |
| Música | Correcto | Verificado |
| Teclado/ratón | Correcto | Verificado |
| Gamepad/joystick | No probado | — |
| Inicio de partida | Correcto | Verificado |
| Juego representativo | Correcto | Secuencia inicial jugada sin incidencias |
| Guardado | Correcto | Verificado |
| Carga | Correcto | Verificado tras segundo arranque |
| Cambio de nivel/escena | Correcto | Verificado durante la prueba representativa |
| Cambios de disco | Correcto | CD1→CD2→CD3 durante instalación |
| Multijugador | No probado | — |
| Cierre | Correcto | Verificado |
| Segundo arranque | Correcto | Verificado con CD1 montado |

## 9. Limitaciones conocidas

- La validación corresponde exclusivamente a esta edición española Big Box y al entorno descrito.
- No se ha verificado Windows 11 ni otros sistemas operativos.
- No se han probado otras GPU/controladores.

## 10. Elementos no probados

- Gamepad / joystick.
- Multijugador.

## 11. Problemas descartados / intentos fallidos

- El primer arranque con CD3 montado no continúa y solicita CD1. No es un fallo de compatibilidad: forma parte del requisito de disco de esta edición.
- No fue necesario instalar DirectX 7 desde el CD.

## 12. Fuentes externas utilizadas

Ninguna necesaria para determinar el procedimiento final. El resultado se basa en la prueba directa de la pieza conservada.

## 13. Evidencias internas

- hashes SHA-256 de másteres y copia de trabajo;
- logs de adquisición de los tres soportes;
- capturas del instalador;
- salidas PowerShell del sistema de pruebas;
- resultados observados durante instalación, cambios de disco, arranque, guardado y carga.

## 14. Repetición final

- [x] Partida desde copia de trabajo conocida.
- [x] Entorno identificado.
- [x] Procedimiento ejecutado desde copia verificada.
- [x] No han sido necesarios pasos fuera de la guía.
- [x] Resultado coincide con la matriz funcional.
- [x] Limitaciones documentadas.
- [x] Fecha de última prueba actualizada.

## 15. Estado final

- **Estado:** Funcional
- **Fecha de última prueba:** 07/10/2026
- **Observaciones finales:** instalación y ejecución nativas en Windows 10 Pro build 19045, sin parches, wrappers, modo de compatibilidad ni privilegios de administrador. CD1 requerido para jugar.
