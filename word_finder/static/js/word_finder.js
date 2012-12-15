$('.letter').click(function() {
    var element = $(this);
    if (element.hasClass('other')) {
        element.removeClass('other');
    } else if (element.hasClass('own')) {
        element.removeClass('own');
        element.addClass('other');
    } else {
        element.addClass('own');
    }
});

function get_letter_strings() {
    var letters = new Array();
    letters['own'] = '';
    letters['other'] = '';
    letters['neutral'] = '';
    $('.letter.own').each(function(index) {
        letters['own'] += $(this).html();
    });
    $('.letter.other').each(function(index) {
        letters['other'] += $(this).html();
    });
    $('.letter:not(.own):not(.other)').each(function(index) {
        letters['neutral'] += $(this).html();
    });
    return letters
}

$('#find').click(function () {
    var letters = get_letter_strings();
    $.ajax({
        type: 'POST',
        data: {
            own:     letters['own'],
            other:   letters['other'],
            neutral: letters['neutral'],
        },
        dataType: 'json',
        success: function(data) {
            $('#words ol li').remove();
            $.each(data, function(i) {
                $('#words ol').append('<li>' + data[i] + '</li>');
            });
        },
    });
});
