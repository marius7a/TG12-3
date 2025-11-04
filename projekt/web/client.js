document.getElementById("spielerForm").addEventListener("submit", async function(event) {
    event.preventDefault();

    const spieler = {
        name: document.getElementById("name").value,
        jahrgang: parseInt(document.getElementById("jahrgang").value),
        staerke: parseInt(document.getElementById("staerke").value),
        torschuss: parseInt(document.getElementById("torschuss").value),
        motivation: parseInt(document.getElementById("motivation").value),
        position: document.getElementById("position").value,
    };

    try {
        const response = await fetch("/spieler", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(spieler)
        });

        const data = await response.json();
        document.getElementById("serverAntwort").textContent = JSON.stringify(data, null, 2);
    } catch (error) {
        document.getElementById("serverAntwort").textContent = "Fehler: " + error;
    }
});
