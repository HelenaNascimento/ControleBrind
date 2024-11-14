function toggleFields() {
    // Pega os botões de rádio e os campos de entrada
    const possuiChave = document.querySelector('input[name="chave_acesso"]:checked').value;
    const chaveAcessoField = document.querySelector('input[name="in_chav_acesso"]');
    const numeroNotaField = document.querySelector('input[name="NF_ENT"]');
    const dataEmissaoField = document.querySelector('input[name="Dat_Entrada"]');
    const cnpjFornecedorField = document.querySelector('input[name="CNPJ_FORN"]');
    
    if (possuiChave === 'sim') {
        // Se tiver chave de acesso
        chaveAcessoField.disabled = false;
        numeroNotaField.disabled = true;
        dataEmissaoField.disabled = true;
        cnpjFornecedorField.disabled = true;
        
        // Exibir como rótulos se quiser exibir o valor atual como label (opcional)
        numeroNotaField.classList.add('label-like');
        dataEmissaoField.classList.add('label-like');
        cnpjFornecedorField.classList.add('label-like');
    } else {
        // Se não tiver chave de acesso
        chaveAcessoField.disabled = true;
        numeroNotaField.disabled = false;
        dataEmissaoField.disabled = false;
        cnpjFornecedorField.disabled = false;

        numeroNotaField.classList.remove('label-like');
        dataEmissaoField.classList.remove('label-like');
        cnpjFornecedorField.classList.remove('label-like');
    }


}

function toggleFields_cad() {
    const compraWeb = document.querySelector('input[name="compra"][value="Web"]').checked;
    const webField = document.getElementById("webField");
    const addressFields = document.getElementById("addressFields");

    if (compraWeb) {
        webField.style.display = "block";
        addressFields.style.display = "none";
    } else {
        webField.style.display = "none";
        addressFields.style.display = "block";
    }
}
// Chama a função de ativação ao carregar a página
document.addEventListener("DOMContentLoaded", function() {
    toggleFields();
    document.querySelectorAll('input[name="in_chav_acesso"]').forEach((radio) => {
        radio.addEventListener("change", toggleFields);
    });
});
document.addEventListener("DOMContentLoaded", toggleFields_cad);