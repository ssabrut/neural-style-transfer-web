(function () {
  'use strict';

  document.getElementsByTagName('label')[0].innerHTML = 'Select Content Image';
  document.getElementsByTagName('label')[1].innerHTML = 'Select Style Image';
  const contentImage = document.getElementById('content_image');
  const styleImage = document.getElementById('style_image');

  contentImage.addEventListener('change', previewContent, false);
  styleImage.addEventListener('change', previewStyle, false);

  function previewContent(e) {
    if (window.FileReader) {
      const contentPreview = document.getElementById('content-preview');
      const img = e.target.files[0];
      const ofReader = new FileReader();
      if (img && img.type.match('image.*')) {
        ofReader.readAsDataURL(img);
      }

      ofReader.onloadend = function (e) {
        contentPreview.src = ofReader.result;
      }
    }
  } 

  function previewStyle(e) {
    if (window.FileReader) {
      const stylePreview = document.getElementById('style-preview');
      const img = e.target.files[0];
      const ofReader = new FileReader();
      if (img && img.type.match('image.*')) {
        ofReader.readAsDataURL(img);
      }

      ofReader.onloadend = function (e) {
        stylePreview.src = ofReader.result;
      }
    }
  }
})();