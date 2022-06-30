(function () {
  const contentImage = document.getElementById('content-image');

  contentImage.addEventListener('change', previewImage, false);

  function previewImage(e) {
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
})();