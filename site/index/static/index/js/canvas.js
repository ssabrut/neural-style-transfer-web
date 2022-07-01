(function () {
  var width = 1;
  var row = 0;
  var col = 0;
  const progress = document.querySelector(".progress");
  const percentage = document.querySelector(".percentage");
  const caption = document.querySelector(".caption");
  const captions = [
    ["Picking up canvas.", "Picking up canvas..", "Picking up canvas..."],
    ["Picking the right color.", "Picking the right color..", "Picking the right color..."],
    ["Scratching all over the canvas.", "Scratching all over the canvas..", "Scratching all over the canvas..."],
    ["Finishing up.", "Finishing up..", "Finishing up..."],
  ];

  var identity = setInterval(function () {
    if (width >= 100) {
      clearInterval(identity);
    } else {
      percentage.innerHTML = width + "%";
      if (width % 25 == 0 && width < 75) {
        row++;
      }

      if (width == 90) {
        row++;
      }

      if (width % 1 == 0) {
        if (col == 3) {
          col = 0;
        }
        caption.innerHTML = captions[row][col];
        col++;
      }
      width++;
      progress.style.width = width + "%";
    }
  }, 100);
})();