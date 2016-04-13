jQuery(function ($) {
    var $search_town = $('#id_search'),
        $towns = $('#id_result'),
        $participants_list = $('#participants_list'),
        $participants = $('#participants'),
        $participate_modal_text = $('#participate-modal-text'),
        $participate_button = $('#participate-button');

    var $due_datetime_next_btn = $('.datetimepicker .table-condensed .next i'),
        $due_datetime_prev_btn = $('.datetimepicker .table-condensed .prev i');
    
    $participants_list.on('click', function(event){
        event.preventDefault();
    });

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
    
    $search_town.on('keyup', function(event) {
        getTownList();
    });

    function checkParticipationState () {
        var $current_page_pathname = $(location).attr('pathname');
        $.ajax({
            type: 'GET',
            url: '/api' + $current_page_pathname + 'participate/',
            success: function (data) {
                var participants_list = $.parseJSON(data.participants);

                if (data.participation_state) {
                    $participate_button.html('취소').addClass('cancel').prop('disabled', false);
                    $participants.children('li').remove();
                    for ( var i = 0; i < participants_list.length; i++) {
                        var participant = participants_list[i];
                        $participants.append('<li>' + participant + '</li>')
                    }
                    console.log(data);
                } else if ( data.is_full ) {
                    $participate_button.html('마감').addClass('closed').prop('disabled', true);
                    $participants.children('li').remove();
                    for ( var i = 0; i < participants_list.length; i++) {
                        var participant = participants_list[i];
                        $participants.append('<li>' + participant + '</li>')
                    }
                    console.log(data);
                } else if ( !data.is_full ) {
                    $participate_button.html('참여').addClass('join').prop('disabled', false);
                    $participants.children('li').remove();
                    for ( var i = 0; i < participants_list.length; i++) {
                        var participant = participants_list[i];
                        $participants.append('<li>' + participant + '</li>')
                    }
                    console.log(data);
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
            success: function (data) {
                var participants_list = $.parseJSON(data.participants);
                $participate_button.html('취소').removeClass('join').addClass('cancel').prop('disabled', false);
                $participate_modal_text.html('참여가 완료 됐습니다!');
                $participants.children('li').remove();
                for ( var i = 0; i < participants_list.length; i++) {
                    var participant = participants_list[i];
                    $participants.append('<li>' + participant + '</li>')
                }
                console.log(data);
            },
            error: function (data,e) {
                //var participants_list = $.parseJSON(data.participants);
                $participate_button.html('인원이 가득 찼습니다').prop('disabled', true);
                $participate_modal_text.html('아쉽게도 방금 모집인원이 가득 찼습니다.');
                $participants.children('li').remove();
                for ( var i = 0; i < participants_list.length; i++) {
                    var participant = participants_list[i];
                    $participants.append('<li>' + participant + '</li>')
                }
          }
        });
    }

    function cancelActivity () {
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
            type: 'DELETE',
            url: '/api' + $current_page_pathname + 'participate/', 
            data: {
                activityID: $current_page_pathname.split('/')[2],
            },
            success: function (data) {
                var participants_list = $.parseJSON(data.participants);
                $participate_button.html('참여').addClass('join').removeClass('cancel').removeClass('closed');
                $participate_modal_text.html('참여가 취소 됐습니다.');
                $participants.children('li').remove();
                for ( var i = 0; i < participants_list.length; i++) {
                    var participant = participants_list[i];
                    $participants.append('<li>' + participant + '</li>')
                }
                console.log(data);
            },
        });
    }

    $participate_button.on('click', function(event) {
        if ($participate_button.hasClass('cancel')) {
            cancelActivity();
        } else if ($participate_button.hasClass('join')) {
            participateActivity();
        }
    });

    $('.carousel').carousel({
        interval: 2000,
        duration: 0,
        autoStart: true
    });

    $due_datetime_next_btn.removeClass('icon-arrow-right').addClass('fa fa-arrow-right');
    $due_datetime_prev_btn.removeClass('icon-arrow-left').addClass('fa fa-arrow-left');

});
