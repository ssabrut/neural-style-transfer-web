(function () {
  'use strict';

  const progress = document.querySelector('.progress');
  const percentage = document.querySelector('.percentage');
  const captions = ['Picking up canvas...', 'Picking the right color...', 'Scratching all over the canvas...', 'Finishing up...'];
  const caption = document.querySelector('.caption');

  var width = 0;
  var counter = 0;
  var identity = setInterval(function () {
    if (width >= 100) {
      clearInterval(identity);
    } else {
      percentage.innerHTML = width + '%';
      if (width % 25 == 0 && width < 70) {
        caption.innerHTML = captions[counter];
        counter++;
      } else if (width == 90) {
        caption.innerHTML = captions[counter];
      }
      width++;
      progress.style.width = width + '%';
    }
  }, 200);
})();