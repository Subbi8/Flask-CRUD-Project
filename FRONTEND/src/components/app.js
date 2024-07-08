document.addEventListener('DOMContentLoaded', function() {
    const titleInput = document.getElementById('title');
    const descInput = document.getElementById('desc');
  
    const titleMaxLength = 5; 
    const descMaxLength = 20; 
  
    function limitInputLength(element, maxLength) {
      element.addEventListener('input', function() {
        if (this.value.length > maxLength) {
          this.value = this.value.slice(0, maxLength);
        }
      });
    }
  
    if (titleInput) {
      limitInputLength(titleInput, titleMaxLength);
    }
  
    if (descInput) {
      limitInputLength(descInput, descMaxLength);
    }
  });
  