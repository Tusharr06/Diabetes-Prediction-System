document
  .getElementById("predictionForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    const pregnancies = parseFloat(
      document.getElementById("pregnancies").value
    );
    const glucose = parseFloat(document.getElementById("glucose").value);
    const bloodPressure = parseFloat(
      document.getElementById("bloodPressure").value
    );
    const skinThickness = parseFloat(
      document.getElementById("skinThickness").value
    );
    const insulin = parseFloat(document.getElementById("insulin").value);
    const bmi = parseFloat(document.getElementById("bmi").value);
    const dpf = parseFloat(document.getElementById("dpf").value);
    const age = parseFloat(document.getElementById("age").value);

    const predictData = {
      pregnancies: pregnancies,
      glucose: glucose,
      bloodPressure: bloodPressure,
      skinThickness: skinThickness,
      insulin: insulin,
      bmi: bmi,
      dpf: dpf,
      age: age,
    };

    console.log("Sending data:", predictData); 

    fetch("/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(predictData),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("Received response:", data); 
        document.getElementById("result").innerText = data.result;
      })
      .catch((error) => {
        console.error("Error:", error);
        document.getElementById("result").innerText = "An error occurred";
      });
  });
