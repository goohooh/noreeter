jQuery(function ($) {
    var $search_town = $('#id_search'),
        $towns = $('#id_result'),
        $participate_button = $('#participate-button');

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');


    function getTownList() {
        $.ajax({
            type: 'GET',
            url: '/api/towns/?search=' + $search_town.val(),
            success: function (towns) {
                $towns.empty()
                for (var i = 0; i < towns.length; i++) {
                    var town = towns[i];
                    $towns.append(
                        '<option>' + town.full_address + '</option>'    
                    );
                }
            }
        });
    }

    function checkParticipationState () {
        var $current_page_pathname = $(location).attr('pathname');
        $.ajax({
            type: 'GET',
            url: '/api' + $current_page_pathname + 'participate/',
            success: function (data) {
                if (data.participation_state) {
                    console.log("I'm already in!!");
                } else if ( data.is_full ) {
                    console.log('sorry, already full...');
                } else if ( !data.is_full ) {
                    console.log('you can join us!!');
                }
            }
        });
    }

    checkParticipationState();

    function participateActivity () {
        var $current_page_pathname = $(location).attr('pathname');

        function csrfSafeMethod(method) {
            // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader('X-CSRFToken', csrftoken);
                }
            }
        });

        $.ajax({
            type: 'POST',
            url: '/api' + $current_page_pathname + 'participate/', 
            data: {
                activityID: $current_page_pathname.split('/')[2],
            },
            success: function (some) {
                console.log('join!!');
            },
        });
    }

    $search_town.on('keyup', function(event) {
        getTownList();
    });

    $participate_button.on('click', function(event) {
        participateActivity();
    });

    $('.carousel').carousel({
        interval: 2000,
        duration: 0,
        autoStart: true
    });

});
