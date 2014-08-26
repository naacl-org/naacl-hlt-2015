
var menu_timeout = 3000;

$(function() {
    init_toggleable_menus();
});

function init_toggleable_menus() {
    $(".page-container").on("click", hide_toggleable_menus);
    $(".toggleable_menu").parent()
        .on("click mouseenter mouseleave", toggle_submenu);
    hide_toggleable_menus();
}

function hide_toggleable_menus() {
    $(".toggleable_menu").hide();
}

var current_menu_timer = null;

function toggle_submenu(event) {
    event.stopImmediatePropagation();
    var menu = $(this).children(".toggleable_menu");
    if (event.type == "mouseleave") {
        menu.hide();
    } else {
        if (current_menu_timer) {
            clearTimeout(current_menu_timer);
            current_menu_timer = null;
        }
        hide_toggleable_menus();
        current_menu_timer = setTimeout(hide_toggleable_menus, menu_timeout);
        menu.show();
    }
}
