jQuery(function ($) {
    var $search_town = $('#id_search'),
        $towns = $('#id_result');
    
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
        console.log('keyup!!');
        getTownList();
    });

    $('.carousel').carousel({
        interval: 2000,
        duration: 0,
        autoStart: true
    });

});
