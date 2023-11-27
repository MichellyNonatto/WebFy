const btn = document.querySelectorAll('[data-filter]');
const btnArray = Array.from(btn);

const container = document.querySelectorAll('[data-container]');
const containerArray = Array.from(container)

console.log(btn)
const Filtrate = (evento) => {
    evento.preventDefault();

    const btn_click = evento.target;
    console.log(btn_click)
    const indexDoBotaoClicado = btnArray.indexOf(btn_click);

    btnArray.forEach((btn) => {
        btn.classList.remove("active");
    });

    btn_click.classList.add("active");

    containerArray.forEach((container, index) => {
        if (index === indexDoBotaoClicado) {
            container.classList.add("inline-block");
            container.classList.remove("hidden");
        } else {
            container.classList.remove("inline-block");
            container.classList.add("hidden");
        }
    });
}

btnArray.forEach((btn) => {
    btn.addEventListener('click', Filtrate);
});

var date = new Date();
var hora = date.getHours();
var mensagem = document.getElementById('mensagem');

function mensagemHora(elemento) {
    if ((hora > 11) && (hora < 19)) {
        elemento.innerHTML = "Boa Tarde";

    } else if ((hora > 18) && (hora < 24)) {
        elemento.innerHTML = "Boa Noite";

    } else if ((hora > 4) && (hora < 12)) {
        elemento.innerHTML = "Bom Dia";
    } else {
        elemento.innerHTML = "Boa Madrugada";
    }
}

mensagemHora(mensagem);

var swiper = new Swiper('.swiper-container', {
            loop: true,
            speed: 1500,
            autoplay: {
                delay: 10000,
                disableOnInteraction: false,
            },
        });
        var myswiper = new Swiper("#swiper", {
            slidesPerView: 1,
            spaceBetween: 30,
        });