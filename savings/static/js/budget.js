$(document).ready(function () {
  // gets the nth class of any DOM element specified in the order given in DOM
  // INPUT:
  // targetElement[string] - DOM element from which the classses are pulled
  // nthClass[int]         - Number of the array position where the wanted class is
  // ---
  // OUTPUT:
  // targetClass[string]   - The nth class from the given element
  function getClass(targetElement, nthClass) {
    var targetClasses = $(targetElement).classes()
    var targetClass = JSON.stringify(targetClasses[nthClass]).replace(/"/g, '')
    return targetClass
  }

  // popuplate an object with references to specific DOM elements for easier manipulation
  function populateCategoryRow(editButton) {
    let categoryId = $(editButton).attr('data-category-id')
    let categoryRow = {}
    let container = $('.category[data-category-id=' + categoryId + ']')
    categoryRow.id = categoryId
    categoryRow.saveButton = container.find('button.save')
    categoryRow.editButton = container.find('button.edit')
    categoryRow.closeButton = container.find('button.stop-edit')
    categoryRow.deleteButton = container.find('button.delete')
    categoryRow.inputName = container.find('.name input')
    categoryRow.name = container.find('.name p')
    categoryRow.selectIcon = container.find('.icon select')
    categoryRow.icon = container.find('.icon p')
    return categoryRow
  }

  // Alert auto-closed after timeout
  if ($('.alert').length >= 1) {
    window.setTimeout(() => {
      $('.alert').alert('close')
    }, 2000)
  }

  // Redirect from logout to login page after timeout
  var isLogoutPage = $('#logout-page').length > 0
  if (isLogoutPage) {
    var logoutRedirectTarget = $('#logout-page').attr('data-login-target')
    var logoutRedirectURL = window.location.protocol + '//' + window.location.host + logoutRedirectTarget
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

  // Show edit form elements for category
  $('.category button.edit').on('click', function () {
    let allCategoryRows = $('.categories .category')
    allCategoryRows.find('input, select').fadeOut()
    allCategoryRows.find('.name>p, .icon>p').fadeIn()
    allCategoryRows.find('.btn.save').fadeOut()
    allCategoryRows.find('.btn.edit').fadeIn()
    let categoryRow = populateCategoryRow(this)
    // hide elements
    categoryRow.editButton.fadeOut()
    categoryRow.deleteButton.fadeOut()
    categoryRow.name.fadeOut()
    categoryRow.icon.fadeOut()
    // show elements
    categoryRow.saveButton.fadeIn()
    categoryRow.closeButton.fadeIn()
    categoryRow.inputName.fadeIn()
    categoryRow.selectIcon.fadeIn()
  })
  $('.category button.save').on('click', function () {
    let categoryRow = populateCategoryRow(this)
    // fill form and trigger submit to update category
    let form = $('.update-category')
    let formName = form.find('input[name="name"]')
    let formIcon = form.find('select[name="icon_id"]')
    let newSelectValue = categoryRow.selectIcon.val().replace('icon-', '')
    formName.val(categoryRow.inputName.val())
    formIcon.val(newSelectValue).change()
    form.prop('action', ((form.attr('action').replace('0', '')) + categoryRow.id))
    $(form).submit()
    // hide elements
    categoryRow.saveButton.fadeOut()
    categoryRow.closeButton.fadeOut()
    categoryRow.inputName.fadeOut()
    categoryRow.selectIcon.fadeOut()
    // show elements
    categoryRow.editButton.fadeIn()
    categoryRow.deleteButton.fadeIn()
    categoryRow.name.fadeIn()
    categoryRow.icon.fadeIn()
  })
  $('.category button.stop-edit').on('click', function () {
    let categoryRow = populateCategoryRow(this)
    // hide elements
    categoryRow.saveButton.fadeOut()
    categoryRow.closeButton.fadeOut()
    categoryRow.inputName.fadeOut()
    categoryRow.selectIcon.fadeOut()
    // show elements
    categoryRow.editButton.fadeIn()
    categoryRow.deleteButton.fadeIn()
    categoryRow.name.fadeIn()
    categoryRow.icon.fadeIn()
  })
  
  // Fill add-category-form from in-row inputs
  $('.new-category .btn.save').on('click', function () {
    let categoryRow = $(this).parents('tr.add-category')
    let form = $('form.add-category')
    let formName = form.find('input[name="name"]')
    let formIcon = form.find('select[name="icon_id"]')
    let newName = categoryRow.find('.new-name>input').val()
    let newIcon = categoryRow.find('.new-icon>select').val()
    formName.val(newName)
    formIcon.val(newIcon)
    form.submit()
  })

  // Fill delete-category form hidden input with in-row delete-button category-id attribute
  $('.category button.delete').on('click', function () {
    let categoryRow = populateCategoryRow(this)
    let form = $('form.delete_category')
    form.find('input[name="category_id"]').val(categoryRow.id)
  })

})

