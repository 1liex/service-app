const cont = document.getElementById("container"); // المكان اللي بنعرض فيه الفيديوهات

(async () => {
  // سحب البيانات من السيرفر
  const res = await fetch("http://127.0.0.1:5000/get/student");
  const data = await res.json();
  console.log(data); // تتأكد من شكل البيانات

  // نمر على كل كلمة مفتاحية
  Object.entries(data).forEach(([keyword, videos]) => {
    
    // نعرض اسم الكلمة المفتاحية
    const kwTitle = document.createElement("h2");
    kwTitle.textContent = keyword;
    cont.appendChild(kwTitle);

    // نمر على الفيديوهات الخاصة بها
    videos.forEach(video => {
      const link = document.createElement("a");
      link.href = video.url;       // رابط الفيديو
      link.target = "_blank";      // يفتح في تاب جديد
      link.textContent = video.title;

      const div = document.createElement("div");
      div.appendChild(link);

      cont.appendChild(div);
    });
  });
})();
