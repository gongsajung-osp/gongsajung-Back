const boxes = document.querySelectorAll('.deli-type');
const deliPrice = document.getElementById('deli-price');

    boxes.forEach(box => {
        box.addEventListener('click', function() {
            const checkbox = box.querySelector('.deli-btn');
            checkbox.checked = !checkbox.checked;
            box.classList.toggle('checkbox-active', checkbox.checked);

            const checkboxValue = Array.from(boxes).map(box=>box.querySelector('.deli-btn')).filter(checkbox=>checkbox.checked).map(checkbox=>checkbox.value);

            if(checkboxValue.includes('택배') || checkboxValue.includes('우편')) {
                deliPrice.style.visibility = 'visible';
            } else {
                deliPrice.style.visibility = 'hidden';
            }
        });
    });

