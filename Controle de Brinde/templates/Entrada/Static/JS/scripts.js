function toggleChaveAcesso() {
    const sim = document.getElementById('chave-sim').checked;
    const campoChave = document.getElementById('campo-chave-acesso');
    campoChave.style.display = sim ? 'block' : 'none';
}

// Inicializa o estado dos campos ao carregar a página
window.onload = function() {
    toggleChaveAcesso();
};

function cad_forne() {
    $('.modal').modal('hide');
    $('#cadastrarFornecedor').modal('show');
}
