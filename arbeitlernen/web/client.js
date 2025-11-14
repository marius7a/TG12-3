
document.getElementById("meinFormular").addEventListener("submit", async function(event) {
    event.preventDefault();
 
    const daten = {
        name: document.getElementById("name").value,
        alter: parseInt(document.getElementById("alter").value)
    };
 
    const response = await fetch("http://127.0.0.1:5000/daten", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(daten)
    });
 
    const antwort = await response.json();
    document.getElementById("serverAntwort").textContent = JSON.stringify(antwort, null, 2);
});
 
 