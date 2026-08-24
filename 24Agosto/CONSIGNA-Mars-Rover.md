# Kata Mars Rover — clase de TDD en mob programming

**Cuándo:** clase del 18:45 a 20:30. La kata arranca ~18:55 → **95 minutos de trabajo.**
**Modalidad:** virtual, en grupos, **mob programming**.
**Lenguaje y framework de test:** los elige el grupo.

> ### Lo primero: 15 minutos de setup, todos a la vez
>
> Apenas se dividan en grupos, **antes de escribir una línea de código**:
>
> - [ ] **Uno** crea el repo (público) y agrega a los demás como colaboradores.
> - [ ] **Todos** clonan y hacen la prueba de traspaso: `git commit --allow-empty -m "hola"`
>       + `git push`. Si eso te funciona, podés manejar.
> - [ ] **Todos** verifican `git config user.name` y `user.email` con su **nombre real**.
> - [ ] **Todos** corren un test de ejemplo en verde en su máquina.
> - [ ] Acuerdan el **orden de rotación**.
>
> **Elijan el lenguaje que más integrantes ya tengan andando.** Esa decisión, en el primer
> minuto, es la que más tiempo les ahorra: no instalen nada nuevo hoy.
>
> Háganlo **en paralelo**, no de a uno mirando al que configura. El que se traba, que lo
> diga en voz alta: el resto sigue y alguien lo ayuda. Van a rotar el teclado entre todos,
> así que el que no completa esta lista no puede manejar (ver §3.1.1).
>
> **A las 19:10 se arranca la kata**, con los que estén listos. El que quede afuera entra
> como navigator y se pone al día en paralelo — el grupo no espera.

---

## 1. Objetivo

Practicar el ciclo completo de TDD —**rojo → verde → refactor**— sobre un problema
con **estado y comportamiento**, no sobre una función pura.

Esta kata es el paso intermedio entre el String Calculator y el TP del Ahorcado.
Acá aparecen por primera vez tres cosas que el TP va a necesitar:

- un **objeto con estado** que evoluciona según los comandos que recibe,
- **decisiones de diseño reales** (cómo modelar la orientación no es obvio),
- un **dominio separado de cualquier interfaz** — el rover se prueba sin pantalla.

> No se evalúa cuánto avanzaron. Se evalúa **cómo**: el historial de git es la
> entrega principal.

## 2. El problema

Un rover se mueve por una grilla. En todo momento tiene una **posición** `(x, y)` y
una **orientación** (`N`, `E`, `S`, `O`).

Recibe una **cadena de comandos** y los ejecuta en orden:

| Comando | Efecto |
|---------|--------|
| `F` | avanza una celda en la dirección a la que mira |
| `B` | retrocede una celda (sin cambiar de orientación) |
| `L` | gira 90° a la izquierda |
| `R` | gira 90° a la derecha |

**Ejemplo:** un rover en `(0, 0)` mirando al `N` que recibe `"FFRFF"` termina en
`(2, 2)` mirando al `E`.

### 2.1 Pasos

Háganlos **en este orden**, uno por vez, cada uno con su ciclo rojo → verde → refactor.
No pasen al siguiente hasta tener el anterior en verde.

1. El rover informa su posición y orientación iniciales.
2. Gira a la izquierda. Gira a la derecha.
3. Avanza una celda.
4. Retrocede una celda.
5. Ejecuta una **cadena** de comandos (`"FFRFF"`).
6. La grilla es **esférica**: al pasarse de un borde, el rover aparece por el opuesto.
7. Hay **obstáculos**. Al encontrar uno, el rover se detiene en la última celda libre,
   **descarta el resto de la cadena** e informa el obstáculo encontrado.

> **Los pasos 6 y 7 son de yapa.** El objetivo de la clase son los pasos 1 a 5 bien
> hechos, con su refactor. Nadie va a ser evaluado por no haber llegado al 7; sí por
> haber llegado salteándose el ciclo.
>
> Si terminan el paso 7 antes de tiempo, **no agreguen features por su cuenta**: avisen.

## 3. Cómo trabajar: mob programming remoto

Todo el grupo trabaja sobre **un solo problema a la vez**, en una sola llamada.

- **Un driver** comparte pantalla y escribe **en su propia máquina**. **El driver no
  decide**: escribe lo que el resto del grupo (los *navigators*) le indica.
- **Se rota el driver en cada verde**, o cada 10 minutos como máximo, lo que pase primero.
- Todos participan: si alguien estuvo 20 minutos sin hablar, el mob no está funcionando.

### 3.1 El traspaso entre máquinas

Como cada uno trabaja en su propia máquina, rotar de driver implica **pasar el código**.
El protocolo es simple y siempre el mismo:

```sh
# el driver que termina su turno:
git commit -m "GREEN: gira a la derecha"
git push

# el que toma el teclado, antes de escribir una línea:
git pull
```

Tres reglas para que no se pisen:

1. **Todos trabajan sobre la misma rama.** Nada de ramas por persona en esta kata.
2. **Sólo el driver del turno pushea.** Los demás miran la pantalla compartida, no
   tocan su copia local.
3. **El que toma el teclado hace `pull` primero**, siempre. Si arranca sin actualizar,
   el traspaso siguiente se convierte en un conflicto.

Al principio el traspaso les va a costar un minuto; después sale solo. Y tiene un
efecto lateral bueno: como no pueden rotar sin commitear, **los commits salen chicos y
frecuentes**, que es justo lo que se busca.

> **Ventaja del formato remoto:** cada uno commitea desde su propia máquina, así que el
> historial refleja la rotación sin que tengan que hacer nada especial. Verifiquen una
> sola vez, al empezar, que su `git config user.name` y `user.email` tengan su nombre
> real — no un alias.

### 3.1.1 Si alguien no puede manejar

Se espera que **todos los integrantes aparezcan como autores** en el historial.

Puede pasar que alguien no llegue con el entorno listo (sin el lenguaje instalado, sin
git configurado, problemas de conexión). En ese caso:

- **Participa igual como navigator.** El mob se sostiene con la voz, no con el teclado:
  puede dictar el próximo test, revisar el refactor, o llevar la cuenta de qué caso
  sigue. Un navigator activo aporta más que un driver mudo.
- **Aprovechen la clase para destrabarlo.** Si a los 20 minutos sigue sin entorno,
  paren cinco minutos y resuélvanlo entre todos: es tiempo mejor invertido que dos
  horas de una persona mirando.
- **Anótenlo en el `README.md`**: quién no pudo manejar y por qué. No es una falta —
  es la única forma de que no se lea como que no participó.

**Lo que se verifica:** un grupo que mobeó bien muestra los nombres alternándose cada
8–10 minutos en `git log`. Un solo autor en dos horas, sin explicación en el README,
se lee como que no hubo mob.

### 3.2 Mensajes de commit

Prefijo obligatorio, igual que en el TP:

```
RED: el rover gira a la derecha
GREEN: el rover gira a la derecha
REFACTOR: la orientación pasa a ser un objeto
```

- El commit **`RED:`** contiene **sólo el test**, y ese test tiene que fallar
  (ver §3.3).
- El commit **`GREEN:`** contiene el **mínimo código** que lo hace pasar. Hardcodear
  está permitido y es esperable en los primeros pasos.
- El commit **`REFACTOR:`** **no cambia comportamiento**: los mismos tests que estaban
  en verde antes siguen en verde después.

### 3.3 Qué cuenta como rojo

No todo test que "no anda" es un rojo. La pregunta es **si la falla les está diciendo
algo que querían saber**.

- ✅ **El primer test de una clase o método que todavía no existe.** No compila —o tira
  `ImportError` / `NameError`, según el lenguaje— y está perfecto: el compilador les
  está dando la primera información de diseño, les dice qué API les falta.
- ✅ **Un assert que falla** porque el comportamiento todavía no está implementado.
- ❌ **Un test roto**: un typo en el nombre de la aserción, un import que falta, el
  nombre de la función mal escrito. Ahí no aprenden nada del diseño, sólo tienen el
  test mal escrito.

**Y un paso más, que vale la pena hacer siempre:** aunque el primer rojo sea de
compilación, antes de implementar conviene **llegar a que falle el assert**. Creen el
stub vacío —`pass`, `return null`, `return 0`— corran, y vean fallar la aserción.

Eso confirma que el test está **enchufado a su código**. Un test que nunca falla puede
estar probando otra cosa, o nada: es exactamente lo que pasa cuando se llama sin querer
a una función de la biblioteca estándar en vez de a la propia.

## 4. Uso de IA

La IA es un **par**, no un oráculo. Se puede y se debe usar, con una regla:

- ✅ *"¿cómo escribo un test parametrizado en pytest?"*, *"no entiendo este error"*,
  *"¿cuál sería el próximo caso más chico?"*, *"revisá este refactor"*
- ❌ *"resolvé la kata Mars Rover"*, *"escribí todos los tests"*, *"dame la implementación
  completa"*

Pegar una solución completa se nota en el historial —un commit gigante sin rojos
previos— y **invalida la entrega**. Además, a mitad de clase van a recibir un cambio
de requerimiento que ninguna IA tiene precocinado: si no entienden su propio código,
no lo van a poder absorber.

## 5. Cronograma

| Horario | Qué pasa |
|---------|----------|
| 18:45 – 18:55 | Explicación de la consigna |
| 18:55 – 19:10 | **Setup**: repo, accesos, prueba del traspaso, orden de rotación |
| 19:10 – 19:50 | **Pasos 1 a 4** — el grueso de la kata. Si llegan, el 5. |
| **~19:50** | **Cambio de requerimiento** — la cátedra entrega uno distinto a cada grupo |
| 19:50 – 20:15 | Absorber el cambio |
| 20:15 – 20:30 | Cierre: push final, README, y cada grupo abre su `git log` y cuenta qué ve |

El momento del cambio lo define la cátedra según cómo venga cada grupo; **no llega a
todos a la misma hora**. A un grupo que va rápido le puede llegar a las 19:30.

**Sobre los pasos 6 y 7:** en 95 minutos, la mayoría no va a llegar. Está bien. Cuando
reciban el cambio de requerimiento, **eso pasa a ser la prioridad** — los pasos 6 y 7
quedan para los grupos que ya los hayan hecho. Vale más un cambio absorbido con el ciclo
completo que dos pasos más apurados sin refactor.

El cambio **no se anuncia antes**. Es parte del ejercicio: en un
proyecto real los requerimientos cambian a mitad de camino, y un buen diseño se nota
justamente ahí. Un rover que modela la orientación como un objeto absorbe el cambio en
minutos; uno con una cadena de `if`s, no.

## 6. Entrega

Al terminar la clase:

1. **Push de todo** a un repositorio público (uno por grupo).
2. Link del repo en el canal de Discord del grupo.
3. En el `README.md`: **quiénes son**, **qué cambio de requerimiento les tocó**, y
   —si aplica— **quién no pudo manejar y por qué** (§3.1.1).

No hace falta que la kata esté terminada. Hace falta que el historial sea honesto.

## 7. Qué se evalúa

Todo se mira sobre el historial de git.

| | Qué se busca |
|---|---|
| **Ciclo** | Commits `RED:` / `GREEN:` alternados. Cada rojo es ancestro de su verde. |
| **Rojo legítimo** | El test del commit rojo falla **por el motivo correcto** (§3.3): porque la clase/método todavía no existe, o porque el assert no se cumple. No porque el test esté mal escrito. |
| **Pasos chicos** | Muchos commits chicos. Un commit que agrega 40 líneas de producción de una es señal de que el ciclo no se siguió. |
| **Refactor** | Al menos **dos** commits `REFACTOR:` con mensaje propio, que no cambien comportamiento. Es el paso que más se saltea. |
| **Rotación** | Los autores se alternan cada 8–10 minutos, y **aparecen todos** los integrantes. Las excepciones valen si están explicadas en el README (§3.1.1). |
| **El cambio** | Cuántos archivos y cuántas líneas hubo que tocar para absorber el requerimiento del minuto 60. |

### Señales de alarma

- Un solo autor en todo el historial.
- Verdes sin rojo previo.
- Un commit inicial gigante con la solución casi completa.
- Cero commits `REFACTOR:` y una función llena de casos hardcodeados al final.
