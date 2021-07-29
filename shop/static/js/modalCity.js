$(function () {

    $('#callback-button').click(function (e) {
        e.preventDefault();
        $('.modal').addClass('modal_active');
        $('body').addClass('hidden');
    });

    $('.modal__close-button').click(function (e) {
        e.preventDefault();
        $('.modal').removeClass('modal_active');
        $('body').removeClass('hidden');
    });

    if ($.cookie('city') == "!") {
        $('.modal').addClass('modal_active');
        $('body').addClass('hidden');
    };
});