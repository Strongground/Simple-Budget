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
var conditionalFieldParent = conditionalField.parent()
var triggerField = $('#id_recurring')
conditionalFieldParent.hide()
triggerField.change(function () {
  if ($(this).prop('checked') === true) {
    console.log('I come til here')
    conditionalFieldParent.fadeIn()
  } else {
    conditionalFieldParent.fadeOut()
  }
})