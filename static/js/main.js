if (window.location.pathname != '/') {
    jQuery('nav').addClass('bg-white').find('.nav-link').css('color', '#6c757d');
} 
if (window.location.pathname == '/match/') {
    jQuery('.potential-match:first-child').show();
}
jQuery('.yes').on('click', function() {
    jQuery(this).parents('.potential-match').remove();
    jQuery('.potential-match:first-child').fadeIn(1000);
});