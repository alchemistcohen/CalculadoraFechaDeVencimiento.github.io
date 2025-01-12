calcular_vencimiento: Esta función toma la "Fecha de Elaboración" y los "Días de Vida Útil", calcula la "Fecha de Vencimiento" y el "Lote Juliano". La fecha de vencimiento se obtiene sumando los días de vida útil a la fecha de elaboración, y el lote juliano se calcula como el día del año en que ocurrió la fecha de elaboración.

calcular_fecha_elaboracion: Esta función toma el "Lote Juliano" y los "Días de Vida Útil", y calcula la "Fecha de Elaboración" y la "Fecha de Vencimiento". La fecha de elaboración se obtiene sumando los días del lote juliano al primer día del año y, luego, calculando la fecha de vencimiento sumando los días de vida útil.

Interfaz con Gradio: Usamos gr.Blocks para crear una interfaz gráfica. La interfaz tiene dos pestañas:

En la primera pestaña, puedes ingresar la fecha de elaboración y los días de vida útil para calcular la fecha de vencimiento y el lote juliano.
En la segunda pestaña, puedes ingresar el lote juliano y los días de vida útil para calcular la fecha de elaboración y la fecha de vencimiento.

![image](https://github.com/user-attachments/assets/f64767e8-fbeb-484c-a03c-7039835bdcbf)
