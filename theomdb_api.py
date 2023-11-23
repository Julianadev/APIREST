import requests
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Certifique-se de ter a biblioteca Pillow instalada: pip install pillow

def obter_informacoes_pokemon():
    pokemon = entry_pokemon.get()
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}/'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if 'abilities' in data:
            habilidades = [ability['ability']['name'] for ability in data['abilities']]
            habilidades_str = ", ".join(habilidades)

            resultado_label.config(
                text=f"Nome do Pokémon: {data['name'].capitalize()}\n"
                     f"\nHabilidades: {habilidades_str}\n"
                     f"\nAltura: {data['height'] / 10} metros\n"
                     f"\nPeso: {data['weight'] / 10} quilogramas"
            )

            # Exibir a imagem
            if 'sprites' in data and 'front_default' in data['sprites']:
                url_imagem = data['sprites']['front_default']
                imagem = Image.open(requests.get(url_imagem, stream=True).raw)
                imagem.thumbnail((200, 200))
                foto = ImageTk.PhotoImage(imagem)

                imagem_label.config(image=foto)
                imagem_label.image = foto
            else:
                resultado_label.config(text='Imagem não encontrada para este Pokémon.')
        else:
            resultado_label.config(text='Informações de habilidades não encontradas para este Pokémon.')
    else:
        resultado_label.config(text=f'Erro de conexão: {response.status_code}')

# Configuração da interface gráfica
root = tk.Tk()
root.title("Informações do Pokémon")

frame = ttk.Frame(root, padding="20")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

label_pokemon = ttk.Label(frame, text="Nome do Pokémon:")
label_pokemon.grid(column=0, row=0, padx=10, pady=10, sticky=tk.W)

entry_pokemon = ttk.Entry(frame, width=20)
entry_pokemon.grid(column=1, row=0, padx=5, pady=5, sticky=tk.W)

btn_pesquisar = ttk.Button(frame, text="Pesquisar", command=obter_informacoes_pokemon)
btn_pesquisar.grid(column=2, row=0, padx=5, pady=5, sticky=tk.W)

resultado_label = ttk.Label(frame, text="")
resultado_label.grid(column=0, row=1, columnspan=3, pady=10)

imagem_label = ttk.Label(frame)
imagem_label.grid(column=0, row=2, columnspan=3, pady=10)

root.mainloop()
