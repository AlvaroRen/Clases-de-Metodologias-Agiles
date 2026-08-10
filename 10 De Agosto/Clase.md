En rdd primero escribo el test, y codifico a partir de este.

Metodo RED, GREEN, REFACTOR

Siempre debo escribir la menor cantidad de tiempo posible

El primer paso, escribo un test y lo ejecuto, y me tiene que dar rojo porque estoy testeando algo que no existe.

🔴1. Red (Rojo)
El primer paso siempre es escribir una prueba automatizada antes de escribir el código de producción.

Como la funcionalidad o la lógica que estás probando aún no existe, al ejecutar la prueba, esta inevitablemente va a fallar.

En la mayoría de los entornos de desarrollo, los tests fallidos se resaltan en color rojo, de ahí el nombre de esta fase.

Objetivo: Definir exactamente qué comportamiento se espera del sistema y asegurar que la prueba realmente es capaz de detectar cuándo falta esa funcionalidad.

🟢 2. Green (Verde)
El segundo paso es escribir la cantidad mínima de código indispensable para que la prueba pase.

En esta etapa no importa la elegancia, la eficiencia, ni las buenas prácticas arquitectónicas. Si el código es "feo" o si resolvés el problema de la forma más rudimentaria posible, está bien.

Al ejecutar la suite de pruebas nuevamente, esta debería ser exitosa y mostrarse en color verde.

Objetivo: Lograr que el sistema cumpla con el requerimiento exacto que definió el test.

🔵 3. Refactor (Refactorizar)
El último paso es limpiar, optimizar y mejorar el código que acabas de escribir en la fase Green.

Ahora tenés una red de seguridad: tu test en verde. Podés cambiar la estructura del código, eliminar duplicaciones, aplicar patrones de diseño o mejorar la legibilidad sin miedo a romper nada.

Después de cada pequeña modificación, volvés a ejecutar el test. Si sigue en verde, tu refactorización fue exitosa y no alteraste el comportamiento esperado.

Objetivo: Mantener el código limpio, mantenible y escalable, evitando que se acumule deuda técnica.

Trabajo: Cata de TDD, hacer un string calculator, codear haciendo tdd para ralizar bien el ciclo,
