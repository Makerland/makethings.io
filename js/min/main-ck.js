!function(n){"use strict";var o=function(){var o=n("#toggle-nav"),t=n("#nav"),c=function u(){var o=n("body");o.removeClass("no-js").addClass("js")},i=function e(){n([t,o]).toggleClass("is-active")},a=function l(){o.on("click",function(n){n.preventDefault(),i()})},f=function r(){var n=t.find("a[data-scroll]");n.on("click",function(){i()})},s=function v(){smoothScroll.init({updateURL:!0,offset:"50px"})};return{now:function(){c(),a(),f(),s()}}}();o.now()}(Zepto);