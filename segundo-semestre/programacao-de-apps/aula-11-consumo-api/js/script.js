const inputCidade = document.querySelector(".input-cidade");
const buttonSearch = document.querySelector(".botao-busca");

const cidade = document.querySelector(".cidade");
const tempo = document.querySelector(".temp");
const previsao = document.querySelector(".texto-previsao");

const key = "3da3fe101d49d97f7be33c2da5b83153";

inputCidade.addEventListener('keypress', (e) => {
    const keyEnter = e.key
    if(keyEnter !== "Enter") return

    showWeather();
})

const showWeather = async() => {
    const cidadeEscolhida = inputCidade.value;

    const response = await fetch(`https://api.openweathermap.org/data/2.5/weather?q=${cidadeEscolhida}&appid=${key}&units=metric&lang=br`)
        .then(res => res.json())
        .catch(err => console.log(err));
    
    console.log(response)

    cidade.textContent = `Tempo em ${response.name}`
    tempo.textContent = `${response.main.temp} Cº`
    // previsao.textContent = `${}`
}

buttonSearch.addEventListener("click", showWeather);
