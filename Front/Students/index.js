const tag = document.getElementById('tag');

let data = [];

(async () => {
  const res = await fetch('http://127.0.0.1:5000/student');
  data = await res.json();

  print();
})();

function print() {
  data.forEach(element => {
    console.log(element.title)
  });
}
