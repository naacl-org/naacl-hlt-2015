
var menu_timeout = 3000;

$(function() {
    init_toggleable_menus();
});

function init_toggleable_menus() {
    $("body").on("click touchstart", hide_toggleable_menus);
    $(".toggleable_menu").parent()
        .on("click mouseenter mouseleave", toggle_submenu);
    hide_toggleable_menus();
}

function hide_toggleable_menus() {
    $(".toggleable_menu").hide();
}

var menu_timer = null;

function toggle_submenu(event) {
    event.stopImmediatePropagation();
    // if (!event.handled) {
    var show = (event.type !== "mouseleave");
    var menu = $(this).children(".toggleable_menu");
    if (show) {
        if (menu_timer) clearTimeout(menu_timer);
        hide_toggleable_menus();
        menu_timer = setTimeout(hide_toggleable_menus, menu_timeout);
        menu.show();
    } else {
        menu.hide();
    }
    event.handled = true;
    // }
}
