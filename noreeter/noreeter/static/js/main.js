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

    function participateActivity () {
        var $activityID = $('#activityID').data('activityid');

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
            url: '/api/participate/', 
            data: {
                activityID: $activityID,
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
