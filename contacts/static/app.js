document.addEventListener('DOMContentLoaded', function () {
    var box = document.querySelectorAll('.link');

    for (var i = 0; i < box.length; i++) {
        box[i].addEventListener('mouseover', function () {
            this.style.backgroundImage = 'linear-gradient(to left top, #d5cad6, #c6bcc7, #b8aeb9, #a9a0aa, #9b939c)';

            this.firstElementChild.style.color = 'white';
        });
        box[i].addEventListener('mouseleave', function () {
            this.style.backgroundImage = '';
            this.firstElementChild.style.color = '';

        });
    }
})




