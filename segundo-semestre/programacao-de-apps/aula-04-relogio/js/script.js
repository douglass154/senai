

const formatarTempo = (tempo) => {
   let tempoFormatado;
   
   tempo < 10
   ? tempoFormatado = `0${tempo}`
   : tempoFormatado = tempo;
   
   return tempoFormatado;
}

const mudarData = () => {
   const data = new Date()

   let diaAtual = data.getDate()
   let mesAtual = data.getMonth() + 1;
   const anoAtual = data.getFullYear();

   if (diaAtual < 10) diaAtual = `0${diaAtual}`;
   if (mesAtual < 10) mesAtual = `0${mesAtual}` 
   
   const dataSpan = document.querySelector('#data');
   dataSpan.innerHTML = `${diaAtual}/${mesAtual}/${anoAtual}`
}

mudarData()

const mudarCumprimento = (hora) => {
   const cumprimentar = document.querySelector('#cumprimentar')
   
   if (hora > 1 && hora < 12) {
      cumprimentar.innerHTML = 'BOM DIA';
   } else if (hora > 12 && hora < 18) {
      cumprimentar.innerHTML = 'BOA TARDE';
   } else {
      cumprimentar.innerHTML = 'BOA NOITE';   
   }
}

mudarCumprimento();

const atualizarTempo = () => {
   const data = new Date();
   
   const hora = formatarTempo(data.getHours());
   const min = formatarTempo(data.getMinutes());
   const seg = formatarTempo(data.getSeconds());
   
   document.querySelector('.hora').textContent = hora;
   document.querySelector('.min').textContent = min;
   document.querySelector('.seg').textContent = seg;

   mudarCumprimento(hora);
}

setInterval(atualizarTempo, 1000);