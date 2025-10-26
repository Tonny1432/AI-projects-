document.addEventListener("DOMContentLoaded", () => {

  // --------------------------
  // Login / Signup
  // --------------------------
  const loginForm = document.getElementById("loginForm");
  const signupForm = document.getElementById("signupForm");

  if (loginForm) {
    loginForm.addEventListener("submit", (e) => {
      e.preventDefault();
      localStorage.setItem("user", document.getElementById("email").value);
      window.location.href = "dashboard.html";
    });
  }

  if (signupForm) {
    signupForm.addEventListener("submit", (e) => {
      e.preventDefault();
      localStorage.setItem("user", document.getElementById("email").value);
      window.location.href = "dashboard.html";
    });
  }

  // --------------------------
  // Sidebar Toggle
  // --------------------------
  const openNavBtn = document.getElementById("toggleArrow");
  let isOpen = false;

  if (openNavBtn) {
    openNavBtn.addEventListener("click", () => {
      const sidebar = document.getElementById("sidebar");
      const main = document.getElementById("main");

      if (isOpen) {
        sidebar.style.width = "0";
        main.style.marginLeft = "0";
        openNavBtn.textContent = "⬅";
        isOpen = false;
      } else {
        sidebar.style.width = "250px";
        main.style.marginLeft = "250px";
        openNavBtn.textContent = "➔";
        isOpen = true;
      }
    });
  }

  // --------------------------
  // Manual Soil Form
  // --------------------------
  const soilForm = document.getElementById("soilForm");
  if (soilForm) {
    soilForm.addEventListener("submit", async (e) => {
      e.preventDefault();

      const formData = new FormData();
      formData.append("pH", document.getElementById("ph").value);
      formData.append("temperature", document.getElementById("temperature").value);
      formData.append("moisture", document.getElementById("moisture").value);
      formData.append("salinity", document.getElementById("EC").value); // default value
      formData.append("N", document.getElementById("N").value);
      formData.append("P", document.getElementById("P").value);
      formData.append("K", document.getElementById("K").value);

      try {
        const response = await fetch("http://127.0.0.1:5000/analyze", {
          method: "POST",
          body: formData
        });

        if (!response.ok) throw new Error("Server error");

        const data = await response.json();
        let history = JSON.parse(localStorage.getItem("soilHistory")) || [];
        history.push({
          date: new Date().toLocaleDateString(),
          parameters: {
            pH: data.parameters.pH,
            salinity: data.parameters.salinity, // added
            temperature: data.parameters.temperature,
            moisture: data.parameters.moisture,
            N: data.parameters.N,
            P: data.parameters.P,
            K: data.parameters.K
          },
          prediction: data.prediction
        });
        localStorage.setItem("soilHistory", JSON.stringify(history));

        localStorage.setItem("analysisResult", JSON.stringify(data));
        window.location.href = "result.html";

      } catch (err) {
        console.error(err);
        alert("❌ Error analyzing soil data. Make sure backend is running.");
      }
    });
  }

  // --------------------------
  // File Upload
  // --------------------------
  const soilFile = document.getElementById("soilFile");
  if (soilFile) {
    soilFile.addEventListener("change", async (e) => {
      const file = e.target.files[0];
      if (!file) return;

      const formData = new FormData();
      formData.append("file", file);

      try {
        const response = await fetch("http://127.0.0.1:5000/analyze", {
          method: "POST",
          body: formData
        });

        if (!response.ok) throw new Error("Server error");

        const data = await response.json();
        let history = JSON.parse(localStorage.getItem("soilHistory")) || [];
        history.push({
          date: new Date().toLocaleDateString(),
          parameters: {
            pH: data.parameters.pH,
            salinity: data.parameters.salinity, // added
            temperature: data.parameters.temperature,
            moisture: data.parameters.moisture,
            N: data.parameters.N,
            P: data.parameters.P,
            K: data.parameters.K
          },
          prediction: data.prediction
        });
        localStorage.setItem("soilHistory", JSON.stringify(history));

        localStorage.setItem("analysisResult", JSON.stringify(data));
        window.location.href = "result.html";

      } catch (err) {
        console.error(err);
        alert("❌ Error analyzing file. Make sure backend is running.");
      }
    });
  }

  // --------------------------
  // History (dummy)
  // --------------------------
  const historyList = document.getElementById("historyList");
  const history = JSON.parse(localStorage.getItem("soilHistory")) || [];

  if (history.length > 0) {
    history.forEach(item => {
      const li = document.createElement("li");
      li.textContent = `${item.date} → pH: ${item.parameters.pH.toFixed(2)},EC: ${item.parameters.salinity !== undefined ? item.parameters.salinity.toFixed(2) : "N/A"}
,Temperature: ${item.parameters.temperature.toFixed(2)}, Moisture: ${item.parameters.moisture.toFixed(2)},N: ${item.parameters.N}, P: ${item.parameters.P}, K: ${item.parameters.K}`;
      historyList.appendChild(li);
    });
  } else {
    historyList.innerHTML = "<p>No history yet.</p>";
  }
});
