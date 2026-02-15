function buscar() {
    const params = {
        url: $("#url").val(),
        container: $("#container").val(),
        administradora: $("#administradora").val(),
        valor_credito: $("#valor_credito").val(),
        entrada: $("#entrada").val(),
        parcelas: $("#parcelas").val(),
        valor_parcelas: $("#valor_parcelas").val(),
        proximo_vencimento: $("#proximo_vencimento").val()
    };

    $("#resultado").html(`
        <div class="text-center my-4">
            <div class="spinner-border" role="status"></div>
            <p class="mt-2">Buscando dados...</p>
        </div>
    `);

    $.get("/api/scrape", params, function (data) {
        renderTabela(data);
    });
}
function renderTabela(dados) {
    if (!dados || dados.length === 0) {
        $("#resultado").html(`
            <div class="alert alert-warning">
                Nenhum dado encontrado.
            </div>
        `);
        return;
    }

    const colunas = Object.keys(dados[0]);

    let html = `
        <div class="table-responsive">
            <table class="table table-striped table-hover table-bordered align-middle">
                <thead class="table-dark">
                    <tr>
    `;

    colunas.forEach(col => {
        html += `<th>${formatarTitulo(col)}</th>`;
    });

    html += `</tr></thead><tbody>`;

    dados.forEach(item => {
        html += "<tr>";
        colunas.forEach(col => {
            html += `<td>${item[col] ?? "-"}</td>`;
        });
        html += "</tr>";
    });

    html += `
                </tbody>
            </table>
        </div>
    `;

    $("#resultado").html(html);
}
function formatarTitulo(texto) {
    return texto
        .replace(/_/g, " ")
        .replace(/\b\w/g, l => l.toUpperCase());
}
