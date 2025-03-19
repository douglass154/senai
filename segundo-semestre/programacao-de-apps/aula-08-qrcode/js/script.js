
const btnGerarQR = document.querySelector(".gerar-qr");
const inputURL = document.querySelector("#url");
const QRContainer = document.querySelector(".qr-code");
const container = document.querySelector('.container')

const gerarQRCode = () => {
    if(!inputURL.value) return
    QRContainer.innerHTML = '';

    new QRCode(QRContainer, {
        text: inputURL.value,
        width: 350,
        height: 350,
        colorLight: 'transparent',
        colorDark: 'purple'
    });

    container.classList.toggle('active')
};

btnGerarQR.addEventListener("click", gerarQRCode);
inputURL.addEventListener("keypress", (event) => {
	if (!inputURL.value) return;

	const key = event.key;
	if (key === "Enter") gerarQRCode();
});
