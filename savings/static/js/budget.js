// register timeouts and execute actions
if ($('.alert').length >= 1) {
  window.setTimeout(() => {
    $('.alert').alert('close')
  }, 2000)
}
let isLogoutPage = $('#logout-page')
let logoutRedirectTarget = $('#logout-page').attr('data-login-target')
let logoutRedirectURL = window.location.protocol + '//' + window.location.host + logoutRedirectTarget
if (isLogoutPage) {
  window.setTimeout(() => {
    window.location = logoutRedirectURL
  }, 2500)
}
