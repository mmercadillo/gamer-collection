# PCGA-LAB-01 — Laboratorio de compatibilidad

**Proyecto:** PC Game Archive  
**Identificador público del entorno:** PCGA-LAB-01  
**Última caracterización:** 18/10/2026

## Función

PCGA-LAB-01 es el entorno principal utilizado por PC Game Archive para:

- montar copias de trabajo verificadas;
- instalar juegos;
- ejecutar software antiguo;
- probar compatibilidad;
- aplicar, cuando la evidencia lo exige, capas de compatibilidad, wrappers o parches;
- completar matrices funcionales;
- generar guías reproducibles de ejecución.

Nunca se realizan estas pruebas directamente sobre un máster de preservación. Las copias de trabajo parten del máster conservado y verificado en [PCGA-MASTER-01](/documentacion/laboratorio/pcga-master-01/).

## Metodología asociada

Este entorno aplica el [Estándar de guías de ejecución y compatibilidad](/documentacion/guias/estandar-guias-ejecucion-compatibilidad/).

Cada guía conserva la configuración realmente utilizada y cualquier diferencia relevante respecto a esta referencia.

## Hardware de referencia

- **Equipo:** Lenovo 20UHS0JF00.
- **Sistema operativo:** Windows 10 Pro 22H2 x64.
- **Build:** 19045.6466.
- **CPU:** AMD Ryzen 5 PRO 4650U.
- **Núcleos / hilos:** 6 / 12.
- **Memoria:** 16 GB.
- **GPU principal:** AMD Radeon(TM) Graphics.
- **Driver GPU:** 31.0.21921.11005.
- **Fecha del driver:** 30/05/2025.
- **Resolución de referencia:** 1920 × 1080.
- **Frecuencia:** 60 Hz.
- **Escalado de Windows:** 150 %.

## Adaptadores gráficos auxiliares

El entorno dispone también de adaptadores **DisplayLink USB Device** con driver `11.5.6380.0`.

Cuando una prueba pueda verse afectada por la ruta de salida de vídeo utilizada, se documentará expresamente qué adaptador o pantalla intervino.

## Monitores detectados

Durante la caracterización del entorno se detectaron:

- panel Lenovo;
- Acer G247HL;
- pantallas LG Full HD.

La guía de cada juego documentará únicamente la resolución y configuración realmente utilizadas durante la prueba.

## Audio

Dispositivos disponibles en el entorno:

- Realtek High Definition Audio;
- AMD High Definition Audio Device;
- AMD Audio Device;
- AMD Streaming Audio Device;
- DisplayLink USB Audio Adapter.

La matriz funcional de cada juego indicará el resultado real de sonido y música.

## Software de montaje

Software de referencia actual:

- **WinCDEmu 4.1**.

Su presencia no implica que todas las piezas deban utilizarlo. Cada guía documentará la herramienta de montaje realmente empleada.

## Capas y herramientas de compatibilidad

PCGA-LAB-01 sigue el principio de **mínima intervención**:

1. probar primero ejecución nativa;
2. registrar el resultado;
3. introducir un único cambio cada vez;
4. documentar qué problema resuelve;
5. conservar visibles las limitaciones y elementos no probados.

No se aplican automáticamente:

- modo de compatibilidad;
- ejecución como administrador;
- parches no oficiales;
- wrappers gráficos;
- emulación;
- virtualización;
- capas Win16;
- componentes legacy de Windows.

Si una pieza necesita alguna de estas técnicas, la herramienta y versión utilizadas quedan registradas en su guía específica.

## Flujo operativo

```text
PCGA-MASTER-01
      ↓
MÁSTER DE PRESERVACIÓN
      ↓
COPIA DE TRABAJO
      ↓
VERIFICACIÓN SHA-256
      ↓
PCGA-LAB-01
      ↓
MONTAJE
      ↓
INSTALACIÓN
      ↓
EJECUCIÓN NATIVA
      ↓
AJUSTES SOLO SI SON NECESARIOS
      ↓
MATRIZ FUNCIONAL
      ↓
GUÍA REPRODUCIBLE
```

## Criterios de evaluación

Los resultados funcionales se expresan mediante:

- `Correcto`;
- `Correcto con limitaciones`;
- `No funcional`;
- `No probado`;
- `No aplicable`.

No se declara compatibilidad completa mientras queden subsistemas relevantes sin comprobar.

## Información no publicada

Por seguridad operativa, esta ficha pública no expone:

- nombres de host;
- rutas locales;
- números de serie;
- identificadores PNP/USB completos;
- estructura interna de almacenamiento;
- rutas de copias de trabajo.

Estos datos no son necesarios para interpretar los resultados de compatibilidad publicados por PC Game Archive.

---

Esta ficha identifica el entorno de referencia. Cada guía de compatibilidad registra además cualquier cambio específico aplicado durante la prueba.
