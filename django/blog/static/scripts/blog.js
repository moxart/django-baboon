$(function(){var o=$(".start-style");function s(){768<$(window).width()&&$(".navbar .dropdown").on("mouseover",function(){$(".dropdown-toggle",this).trigger("click")}).on("mouseout",function(){$(".dropdown-toggle",this).trigger("click").blur()})}$(window).scroll(function(){10<=$(window).scrollTop()?o.removeClass("start-style").addClass("scroll-on"):o.removeClass("scroll-on").addClass("start-style")}),s(),$(window).resize(s)});