 $(document).ready(function () {
            $('#datatable').dataTable();
        });


$(function() {
  // Initialize form validation on the registration form.
  // It has the name attribute "registration"
  $("form[name='registration']").validate({
    // Specify validation rules
    rules: {
      // The key name on the left side is the name attribute
      // of an input field. Validation rules are defined
      // on the right side
      username: "required",
      password: {
        required: true,
        minlength: 5
      },
      email: {
        required: true,
        // Specify that email should be validated
        // by the built-in "email" rule
        email: true
      },
      fornavn: "required",
      etternavn: "required",
      addresse: "required"

    },
    // Specify validation error messages
    messages: {
        username: "Please enter a username/username already taken",
        password: {
            required: "Please provide a password",
            minlength: "Your password must be at least 5 characters long"
        },
        email: "Please enter a valid email address",
        fornavn: "Please enter your firstname",
        etternavn: "Please enter your lastname",
        addresse: "Please enter your address"

    },
    // Make sure the form is submitted to the destination defined
    // in the "action" attribute of the form when valid
    submitHandler: function(form) {
      form.submit();
    }
  });
});

$(function() {
  // Initialize form validation on the registration form.
  // It has the name attribute "registration"
  $("form[name='login']").validate({
    // Specify validation rules
    rules: {
      // The key name on the left side is the name attribute
      // of an input field. Validation rules are defined
      // on the right side
      username: "required",
      password: {
        required: true,
        minlength: 5
      }

    },
    // Specify validation error messages
    messages: {
        username: "Enter your username /Wrong username",
        password: {
            required: "Enter a password / Wrong password",
            minlength: "Your password must be at least 5 characters long"
        }
    },
    // Make sure the form is submitted to the destination defined
    // in the "action" attribute of the form when valid
    submitHandler: function(form) {
      form.submit();
    }
  });
});

$(function() {
  // Initialize form validation on the registration form.
  // It has the name attribute "registration"
  $("form[name='addnewproduct']").validate({
    // Specify validation rules
    rules: {
      // The key name on the left side is the name attribute
      // of an input field. Validation rules are defined
      // on the right side
      name: "required",
      description: "required",
      price: {
        required: true,
        min: 1,
        max: 10000
      },
      percentage: {
        required: true,
        min: 0,
        max: 100
      },
      type: "required",
      file: "required"

    },
    // Specify validation error messages
    messages: {
        name: "Enter product name!",
        description: "Enter product description!",
        price: {
            required: "Enter a price!",
            min: "Price cannot be bellow 1$",
            max: "Price cannot be higher than 10000$"
        },
        percentage: {
            required: "Set price level",
            min: "Range cannot go bellow 0%",
            max: "Range cannot go over 100%"
        },
        type: "Enter product console/plattform name",
        file: "Choose an image for the product"
    },
    // Make sure the form is submitted to the destination defined
    // in the "action" attribute of the form when valid
    submitHandler: function(form) {
      form.submit();
    }
  });
});

$(function() {
  // Initialize form validation on the registration form.
  // It has the name attribute "registration"
  $("form[name='editproduct']").validate({
    // Specify validation rules
    rules: {
      // The key name on the left side is the name attribute
      // of an input field. Validation rules are defined
      // on the right side
      name: "required",
      description: "required",
      price: {
        required: true,
        min: 1,
        max: 10000
      },
      percentage: {
        required: true,
        min: 0,
        max: 100
      },
      type: "required",
      file: "required"

    },
    // Specify validation error messages
    messages: {
        name: "Enter product name!",
        description: "Enter product description!",
        price: {
            required: "Enter a price!",
            min: "Price cannot be bellow 1$",
            max: "Price cannot be higher than 10000$"
        },
        percentage: {
            required: "Set price level",
            min: "Range cannot go bellow 0%",
            max: "Range cannot go over 100%"
        },
        type: "Enter product console/plattform name",
        file: "Choose an image for the product"
    },
    // Make sure the form is submitted to the destination defined
    // in the "action" attribute of the form when valid
    submitHandler: function(form) {
      form.submit();
    }
  });
});
