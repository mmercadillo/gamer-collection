# Fase 15 — Procedencia y trazabilidad pública del ejemplar

## Objetivo

Documentar el origen del ejemplar físico concreto conservado por PC Game Archive y permitir reconocer públicamente a quien lo aportó sin exigir nombre real.

## Modelo de datos

Se añade `procedencia` como objeto obligatorio:

```json
{
  "tipo": "Donación",
  "nombre_publico": "",
  "redes": {
    "instagram": "https://www.instagram.com/usuario/",
    "facebook": "",
    "x": "https://x.com/usuario"
  }
}
```

El nombre y cada red son independientes. Una persona puede aparecer solo mediante una RRSS.

## Tipos permitidos

- vacío (no documentado)
- Compra
- Donación
- Cesión
- Intercambio
- Colección fundacional
- Otro

## Presentación

La ficha individual incorpora una fila `Procedencia` únicamente cuando existe información real. Se reutiliza el sistema visual de etiquetas existente para las RRSS. No se crean hubs, taxonomías ni páginas por donante.

## Privacidad

`juegos.json` forma parte del contenido público del proyecto. No se almacena información privada con flags de ocultación: `nombre_publico` y las RRSS solo deben contener datos autorizados para publicación.

## Migración

Las fichas anteriores se migran con una estructura vacía para evitar inventar información histórica. Se incluye `migrar_fase15_procedencia.py` para otras copias del catálogo.

## Validación

El schema valida estructura, tipos y dominios de las RRSS. `validar_catalogo.py` añade comprobaciones semánticas y avisa si existe identidad pública sin tipo de procedencia.
