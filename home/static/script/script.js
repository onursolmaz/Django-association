$(document).ready(function () {
    // jQuery code for inside dropdonws
    $(document).on('click', '.dropdown-menu', function (e) {
        e.stopPropagation();
    });

    // make it as accordion for smaller screens
    if ($(window).width() < 992) {
        $('.dropdown-menu a').click(function (e) {
            e.preventDefault();
            if ($(this).next('.submenu').length) {
                $(this).next('.submenu').toggle();
            }
            $('.dropdown').on('hide.bs.dropdown', function () {
                $(this).find('.submenu').hide();
            })
        });
    }
})


$(function () {
    $("#query").autocomplete({
        source: "/search_auto/",
        select: function (event, ui) { //item selected
            AutoCompleteSelectHandler(event, ui)
        },
        minLength: 2,
    });
});

function AutoCompleteSelectHandler(event, ui) {
    var selectedObj = ui.item;
}

