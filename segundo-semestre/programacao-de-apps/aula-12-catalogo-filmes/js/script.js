const form = document.querySelector('form');
const search = document.querySelector('#pesquisa');
const searchBtn = document.querySelector(".btn-pesquisa");

const divPages = document.querySelector(".pages");
const currentPage = document.querySelector(".current-page");
const totalPages = document.querySelector(".total-pages");

let page = 1;

const apiKey = "774ef98b";

const searchMovies = async (page) => {
   const search = document.querySelector("#pesquisa").value;

   if (!search) {
      alert("Preencha o campo de pesquisa");
      return;
   }

   try {
      const response = await fetch(`http://www.omdbapi.com/?apiKey=${apiKey}&s=${search}&page=${page}`)
      const movies = await response.json()
      loadList(movies)
   } catch (error) {
      console.log(error)
   }
};

const loadList = json => {
   const list = document.querySelector(".lista");
   list.innerHTML = "";

   const totalResults = Number(json.totalResults)
   totalPages.textContent = `${Math.round(totalResults / 10)}`

   const errorMsg = document.createElement("h2");
   errorMsg.classList.add("error");

   if (json.Response === "False") {
      divPages.classList.remove('active')
      
      errorMsg.textContent = "Nenhum filme encontrado, tente novamente!";
      list.appendChild(errorMsg);

      setInterval(() => {
         errorMsg.remove();
      }, 3 * 1000);

      return;
   }

   json.Search.forEach(movie => {
      const div = document.createElement("div");
      const poster = movie.Poster === "N/A" ? "./imgs/image-not-found.jpg" : movie.Poster

      div.classList.add("item");
      div.innerHTML = `
         <img src="${poster}" alt="${movie.Title}" />
         <h2 class="film-title">${movie.Title}<h2/>
      `;

      list.insertAdjacentElement("beforeend", div);
   });

   divPages.classList.add("active");
};

const changePages = (e) => {
   const buttonClicked = e.srcElement.parentElement;

   if(buttonClicked.classList.contains('last-page')) {
      if(page <= 1) return;

      page -= 1;
      currentPage.textContent = page
      searchMovies(page)
   }

   if(buttonClicked.classList.contains('next-page')) {
      if(page >= totalPages.textContent) return

      page += 1;
      currentPage.textContent = page
      searchMovies(page)
   }
}

searchBtn.addEventListener("click", searchMovies);
divPages.addEventListener("click", changePages);

form.addEventListener('submit', (e) => e.preventDefault())

search.addEventListener('change', () => {
   page = 1
   currentPage.textContent = page;
})