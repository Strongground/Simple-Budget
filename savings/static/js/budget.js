$(document).ready(function () {
  // Alert auto-closed after timeout
  if ($('.alert').length >= 1) {
    window.setTimeout(() => {
      $('.alert').alert('close')
    }, 2000)
  }

  // Redirect from logout to login page after timeout
  let isLogoutPage = $('#logout-page')
  let logoutRedirectTarget = $('#logout-page').attr('data-login-target')
  let logoutRedirectURL = window.location.protocol + '//' + window.location.host + logoutRedirectTarget
  if (isLogoutPage) {
    window.setTimeout(() => {
      window.location = logoutRedirectURL
    }, 2500)
  }

  // Make form field visible and editable only after its depedency form element has been checked
  var conditionalField = $('#id_repeat_time')
  var triggerField = $('#id_recurring')
  if (triggerField.prop('checked') !== true) {
    conditionalField.parent().hide()
  }
  triggerField.change(function () {
    if ($(this).prop('checked') === true) {
      conditionalField.parent().fadeIn()
    } else {
      conditionalField.parent().fadeOut()
    }
  })

  // Set quick menu to active
  var quickMenuContainer = $('.quick_menu_container')
  var quickMenuTrigger = quickMenuContainer.find('.menu_trigger')
  var quickMenuEntries = quickMenuContainer.find('.menu_entry')
  quickMenuEntries.hide()
  quickMenuTrigger.on('click', function () {
    window.setTimeout(() => {
      quickMenuContainer.toggleClass('active')
    }, 10)
    quickMenuEntries.fadeToggle(150)
  })
})
