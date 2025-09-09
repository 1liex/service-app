const entry = document.getElementById("entry");
const btn = document.getElementById("btn");


btn.addEventListener("click", () => {
  fetch("http://127.0.0.1:5000/get/teacher", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ keyword: entry.value }),
  });
});
