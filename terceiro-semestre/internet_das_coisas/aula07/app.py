import customtkinter as ctk;

ctk.set_appearance_mode("dark");

def converterMoeda():
    real_value = float(real_field.get());
    usd_price = 5.67;
    eur_price = 6.21;
    
    usd_value = real_value / usd_price;
    eur_value = real_value / eur_price;
    
    result.configure(
        text=f"Valor em Dolar: {usd_value:.2f} - Valor em Euro: {eur_value:.2f}",
        font=("Arial", 20)
    );

window = ctk.CTk();
window.geometry("900x600");
window.title("Conversão de Moedas");

ctk.CTkLabel(
    window,
    text="Conversão de Moedas",
    font=("Arial", 35, "bold")
).pack(pady=(35, 60));

ctk.CTkLabel(
    window,
    text="Valor em Real",
    font=("Arial", 20)
).place(x=250, y=100);

real_field = ctk.CTkEntry(
    window,
    placeholder_text="Insira o valor",
    font=("Arial", 18),
    width=400,
    height=40
);
real_field.pack()

button = ctk.CTkButton(
    window,
    text="Converter",
    fg_color="green",
    border_width=1,
    border_color="black",
    hover_color="darkgreen",
    font=("Arial", 20),
    width=200,
    height=50,
    corner_radius=12,
    command=converterMoeda
);

button.pack(pady=35);

result = ctk.CTkLabel(
    window,
    text=""
)

result.pack();

window.mainloop();