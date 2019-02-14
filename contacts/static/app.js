document.addEventListener('DOMContentLoaded', function () {
    var box = document.querySelectorAll('.link');

    for (var i = 0; i < box.length; i++) {
        box[i].addEventListener('mouseover', function () {
            this.style.backgroundImage = 'linear-gradient(to right top, #5d6f77, #6c7883, #7c808c, #8c8995, #9b939c)';

            this.firstElementChild.style.color = 'white';
        });
        box[i].addEventListener('mouseleave', function () {
            this.style.backgroundImage = '';
            this.firstElementChild.style.color = '';

        });
    }
})




