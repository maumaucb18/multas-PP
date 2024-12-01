
// Função para alternar a visibilidade do conteúdo
function toggleAccordion(event) {
    const content = event.target.nextElementSibling;  // O conteúdo está logo após o cabeçalho
    if (content.style.display === "block") {
        content.style.display = "none";
    } else {
        content.style.display = "block";
    }
}

// Adicionar eventos de clique a cada cabeçalho
window.onload = function() {
    const accordionHeaders = document.querySelectorAll(".accordion-header");
    accordionHeaders.forEach(header => {
        header.addEventListener("click", toggleAccordion);
    });
}
