document.getElementById("soilForm").addEventListener("submit", async function (e) {
  e.preventDefault();

  const formData = new FormData(this);

  try {
    const response = await fetch("/analyze", {
      method: "POST",
      body: formData
    });

    if (!response.ok) {
      throw new Error("Server error");
    }

    const data = await response.json();

    document.getElementById("prediction").textContent = data.prediction;
    document.getElementById("moisture").textContent = data.moisture.toFixed(2) + " %";

    const remediesList = document.getElementById("remedies");
    remediesList.innerHTML = "";
    data.remedies.forEach(r => {
      let li = document.createElement("li");
      li.textContent = r;
      remediesList.appendChild(li);
    });

  } catch (error) {
    alert("Error: " + error.message);
  }
});
