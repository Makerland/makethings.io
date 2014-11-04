(function ($) {
  'use strict';

  var MakeThings = (function () {
    var $navToggler = $('#toggle-nav'),
        $nav = $('#nav'),

        enableJS = function enableJS() {
          var $body = $('body');

          $body.removeClass('no-js')
               .addClass('js');
        },

        toggleNavigation = function toggleNavigation() {
          $([$nav, $navToggler]).toggleClass('is-active');
        },

        handleNavToggler = function handleNavToggler() {
          $navToggler.on('click', function (e) {
            e.preventDefault();
            toggleNavigation()
          });
        },

        handleNav = function handleNav() {
          var $navLinks = $nav.find('a[data-scroll]');

          $navLinks.on('click', function () {
            toggleNavigation();
          });
        },

        handleSmoothScroll = function handleSmoothScroll() {
          smoothScroll.init({
            updateURL: true,
            offset: '50px'
          });
        };

    return {
      now: function () {
        enableJS();
        handleNavToggler();
        handleNav();
        handleSmoothScroll();
      }
    }
  }());

  MakeThings.now();
}(Zepto))
