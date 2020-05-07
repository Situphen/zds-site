/* ===== Zeste de Savoir ====================================================
   Accordeon for sidebar
   ---------------------------------
   Author: Alex-D
   ========================================================================== */

(function() {
  'use strict'

  function accordeon($elem) {
    $('h4 + ul, h4 + ol').children($elem).each(function() {
      if (!$(this).hasClass('unfolded')) {
        if ($('.current', $(this)).length === 0) { $(this).hide() }
      }
    })

    $('h4').children($elem).click(function(e) {
      $('+ ul, + ol', $(this)).slideToggle(100)

      e.preventDefault()
      e.stopPropagation()
    })
  }

  document.addEventListener("DOMContentLoaded", function() {
    $('.main .sidebar.accordeon, .main .sidebar .accordeon')
      .each(function() {
        accordeon($(this))
      })
      .on('DOMNodeInserted', function(e) {
        accordeon($(e.target))
      })
  })
})()
