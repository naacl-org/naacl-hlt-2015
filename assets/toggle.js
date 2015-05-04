
$(function() {
    init_toggleable_schedule();
});

function init_toggleable_schedule() {
    $('.session').on('click', toggle_session);
    $('.talkinfo').on('click', toggle_abstract);
    hide_sessions();
}

function hide_sessions() {
    $('.sessiontalk').hide();
    hide_abstracts();
}

function hide_abstracts() {
    $('.talkabstract').hide();
}

function toggle_session(event) {
    event.stopImmediatePropagation();
    var selector = '.session-' + $(this).children('.time').text().replace(/:/g, '');
    var talks = $(this).siblings(selector);
    var visible = talks.is(':visible');
    console.log("Toggle sessions", "Visible:", visible, "No. talks:", talks.length);
    hide_sessions();
    if (!visible) talks.show();
}

function toggle_abstract(event) {
    event.stopImmediatePropagation();
    var abstracts = $(this).children('.talkabstract');
    var visible = abstracts.is(':visible');
    console.log("Toggle abstracts", "Visible:", visible, "No. abstracts:", abstracts.length);
    hide_abstracts();
    if (!visible) abstracts.show();
}
