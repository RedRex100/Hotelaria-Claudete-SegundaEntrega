async function enviar(event) {
    event.preventDefault();

    const nome = document.getElementById("nome").value.trim();
    const endereco = document.getElementById("endereco").value.trim();
    const cpf = document.getElementById("cpf").value.trim();
    const telefone = document.getElementById("telefone").value.trim();
    const email = document.getElementById("email").value.trim();
    const senha = document.getElementById("senha").value.trim();
    const confirmar = document.getElementById("confirmar-senha").value.trim();

    // Regex para validações
    const nomeRegex = /^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$/; // Apenas letras e espaços
    const numeroRegex = /^\d+$/; // Apenas números
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Formato válido de email

    // Validação do nome
    if (!nomeRegex.test(nome)) {
        alert("O nome deve conter apenas letras.");
        return;
    }

    // Validação do CPF (apenas números e com 11 dígitos)
    if (!numeroRegex.test(cpf) || cpf.length !== 11) {
        alert("O CPF deve conter exatamente 11 dígitos numéricos.");
        return;
    }

    // Validação do telefone (apenas números)
    if (!numeroRegex.test(telefone)) {
        alert("O telefone deve conter apenas números.");
        return;
    }

    // Validação do e-mail
    if (!emailRegex.test(email)) {
        alert("O e-mail deve ser válido e conter um '@'.");
        return;
    }

    // Verificação de senhas
    if (senha !== confirmar) {
        alert("As senhas não coincidem.");
        return;
    }

    var senhaCriptografada = CryptoJS.SHA256(senha).toString(CryptoJS.enc.Base64);
    
    try {
        const response = await fetch('/cadastro', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ nome, endereco, cpf, telefone, email, senha: senhaCriptografada }),
        });

        const result = await response.json();
        const mensagem = document.getElementById("mensagem");

        if (response.ok) {
            window.location.href = result.redirect; // Redirecionar em caso de sucesso
        } else {
            mensagem.textContent = "Erro ao cadastrar: " + result.message;
        }
    } catch (error) {
        console.error("Erro ao enviar os dados:", error);
        alert("Ocorreu um erro inesperado. Tente novamente.");
    }
}
