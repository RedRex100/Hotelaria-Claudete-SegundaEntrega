async function checkout(nomeUsuario, event) {
    event.preventDefault();
    const response = await fetch('/checkoutar', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ nome: nomeUsuario })
    });

    const result = await response.json();
    const mensagem = document.getElementById("mensagem");

    if (response.ok) {
        mensagem.textContent = "Checkout realizado com sucesso.";
        window.location.href = result.redirect;
    } else {
        mensagem.textContent = "Erro ao realizar o checkout: " + result.error;
    }
}
