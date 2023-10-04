const btn = document.querySelectorAll('[data-filter]');
const btnArray = Array.from(btn);

const container = document.querySelectorAll('[data-container]');
const containerArray = Array.from(container)

console.log(btn)
const Filtrate = (evento) => {
    evento.preventDefault();

    const btn_click = evento.target;
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