import customtkinter as ctk;

ctk.set_appearance_mode("dark");

def calcularConsumo():
    distancia = float(campoDistancia.get());
    consumo = float(campoConsumo.get());
    preco = float(campoPreco.get());
    
    gastoTotal = distancia / consumo * preco;
    
    resultado.configure(
        text = f"O gasto será de R${gastoTotal:.2f}",
        font=("Arial", 20)
    );

window = ctk.CTk();
window.geometry("900x600");
window.title("Consumo de Viagem");
window.iconbitmap("fuel-pump.ico");

ctk.CTkLabel(
    window,
    text="APP Consumo de Viagem",
    font=("Arial", 30, "bold")             
).pack(pady=(40, 0));

ctk.CTkLabel(
    window,
    text="03/2025 - Senai Bahia",
    font=("Arial", 20, "bold")
).pack();

ctk.CTkLabel(
    window,
    text="Distância:",
    font=("Arial", 20)  
).place(x=150, y=120);

campoDistancia = ctk.CTkEntry(
    window,
    height=40,
    width=600,
    placeholder_text="Digite a distância",
    font=("Arial", 18)
);

campoDistancia.pack(pady=(50, 0));

ctk.CTkLabel(
    window,
    text="Consumo:",
    font=("Arial", 20)  
).place(x=150, y=210)

campoConsumo = ctk.CTkEntry(
    window,
    height=40,
    width=600,
    placeholder_text="Digite o consumo",
    font=("Arial", 18)
);

campoConsumo.pack(pady=50);

ctk.CTkLabel(
    window,
    text="Preço:",
    font=("Arial", 20)  
).place(x=150, y=300)

campoPreco = ctk.CTkEntry(
    window,
    height=40,
    width=600,
    placeholder_text="Digite o preco",
    font=("Arial", 18)
);

campoPreco.pack();

botao = ctk.CTkButton(
    window,
    width=150,
    height=40,
    fg_color="green",
    hover_color="darkgreen",
    corner_radius=7,
    text="Calcular",
    command=calcularConsumo
);

botao.pack(pady=30);

resultado = ctk.CTkLabel(window, text="");
resultado.pack(pady=10);

window.mainloop();