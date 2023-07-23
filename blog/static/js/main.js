$(document).ready(function () {
    $(".sub-btn").click(function () {
        $(this).next(".sub-menu").slideToggle();
    });

    $(".more-btn").click(function () {
        $(this).next(".more-menu").slideToggle();
    });
});

var menu = document.querySelector(".menu");
var menuBtn = document.querySelector(".menu-btn");
var closeBtn = document.querySelector(".close-btn");

menuBtn.addEventListener("click", () => {
    menu.classList.add("active")

});

closeBtn.addEventListener("click", () => {
    menu.classList.remove("active")

});









/*----------------------------------------------------------------
let copyText = document.querySelector(".copy-text");
copyText.querySelector("button").addEventListener("click", function () {
    let input = copyText.querySelector("input.text");
    input.select();
    document.execCommand("copy");
    copyText.classList.add("active");
    window.getSelection().removeAllRanges();
    setTimeout(function () {
        copyText.classList.remove("active");
    }, 2500);
});
*/