(function ($) {
   var defaults = {
       interval: 1000,
       duration: 1000,
       autoStart: true
   };

   $.fn.carousel = function (options) {
       //default + option setting
       options = $.extend({}, defaults, options);
       var $carousel = this, index = 0, interval = options.interval;
       var $next = $carousel.find('.next');
       var $first = $carousel.find('ul li:first-child');
       var $second = $carousel.find('ul li:nth-child(2)');
       var $third = $carousel.find('ul li:nth-child(3)');
       var $fourth = $carousel.find('ul li:nth-child(4)');

       $carousel.find('ul').append($carousel.find('li'));
       $carousel.find('ul').append($first.clone());
       $carousel.find('ul').append($carousel.find('li'));
       $carousel.find('ul').append($second.clone());
       $carousel.find('ul').append($carousel.find('li'));
       $carousel.find('ul').append($third.clone());
       $carousel.find('ul').append($carousel.find('li'));
       $carousel.find('ul').append($fourth.clone());

       $next.on('click', function (event) {
           event.preventDefault();
           if ($first.is(':animated')) return;
           var len = $carousel.find('li').length;
           index = (index + 1) % len;
           $first.animate({ 'margin-left': (-25 * index) + '%' }, function () {
               if (index == len - 1) {
                   index = 0;
                   $first.css('margin-left', 0);
               }
           });
       });

       //avoid reduplication
       var intervalID;
       $carousel
           .on('mouseenter', function (event) {
               $(this).addClass('hover');
               clearInterval(intervalID);
           })
           .on('mouseleave', function (event) {
               $(this).removeClass('hover');
               intervalID = setInterval(function () {
                   $next.triggerHandler('click');
               }, interval + options.duration);
           })
           .on('focusin', function (event) {
               if ($(this).has(event.relatedTarget).length === 0) {
                   $(this).trigger('mouseenter');
               }
           })
           .on('focusout', function (event) {
               if ($(this).has(event.relatedTarget).length === 0) {
                   $(this).trigger('mouseleave');
               }
           });
       if (options.autoStart) {
           $carousel.trigger('mouseleave');
       }
       //enable chaining
       return this;
   };
})(window.jQuery);
