(function ($) {
  $.fn.initGUI = function () {
    // init dom
    let quickAddContainer = $('div.quick_add_container')
    quickAddContainer['menuEntries'] = quickAddContainer.children('.entry')
    let quickAddButton = []
    quickAddButton['button'] = $('a.quick_add_transaction')

    quickAddButton.addEventListener('hover', function () {
      console.log('test')
      quickAddContainer.addClass('active')
    })
  }
}(jQuery))
console.log('gui module initialized')
