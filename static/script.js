let dados = [];

fetch("/api/financeiro")
  .then(res => res.json())
  .then(json => {
      dados = json;
      renderTabela();
  });

function renderTabela() {
    let html = `<table border="1">
        <tr><th>Moeda</th><th>Valor</th></tr>`;

    dados.forEach(m => {
        html += `<tr>
            <td>${m.nome}</td>
            <td>${m.valor}</td>
        </tr>`;
    });

    html += `</table>`;
    document.getElementById("content").innerHTML = html;
}

function renderCards() {
    let html = "";
    dados.forEach(m => {
        html += `
          <div class="card">
            <h3>${m.nome}</h3>
            <p>${m.valor}</p>
          </div>
        `;
    });
    document.getElementById("content").innerHTML = html;
}

function renderGrafico() {
    document.getElementById("content").innerHTML = `<canvas id="chart"></canvas>`;

    new Chart(document.getElementById("chart"), {
        type: "bar",
        data: {
            labels: dados.map(m => m.nome),
            datasets: [{
                data: dados.map(m => parseFloat(m.valor.replace(",", ".")))
            }]
        }
    });
}
