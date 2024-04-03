function validateForm() {
  var name = document.getElementById("name").value;
  var username = document.getElementById("username").value;
  var email = document.getElementById("email").value;
  var password = document.getElementById("password").value;
  var confirmPassword = document.getElementById("confirmPassword").value;
  var phone = document.getElementById("phone").value;
  var gender = document.getElementById("gender").value;
  var website = document.getElementById("website").value;

  var nameError = document.getElementById("nameError");
  var usernameError = document.getElementById("usernameError");
  var emailError = document.getElementById("emailError");
  var passwordError = document.getElementById("passwordError");
  var confirmPasswordError = document.getElementById("confirmPasswordError");
  var phoneError = document.getElementById("phoneError");
  var genderError = document.getElementById("genderError");
  var websiteError = document.getElementById("websiteError");

  var valid = true;

  nameError.textContent = "";
  usernameError.textContent = "";
  emailError.textContent = "";
  passwordError.textContent = "";
  confirmPasswordError.textContent = "";
  phoneError.textContent = "";
  genderError.textContent = "";
  websiteError.textContent = "";

  // Validasi nama
  if (name === "") {
    nameError.textContent = " *Wajib diisi";
    valid = false;
  }

  // Validasi username
  if (username === "") {
    usernameError.textContent = " *Wajib diisi";
    valid = false;
  }

  // Validasi email
  if (email === "") {
    emailError.textContent = " *Email harus diisi";
    valid = false;
  } else if (!/\S+@\S+\.\S+/.test(email)) {
    emailError.textContent = " *Email tidak valid";
    valid = false;
  } else if (email.indexOf("@") === -1) {
    emailError.textContent = ' *Email harus mengandung karakter "@"';
    valid = false;
  }

  // Validasi password
  if (password === "") {
    passwordError.textContent = " *Kata sandi harus diisi";
    valid = false;
  } else if (
    !/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,12}$/.test(password)
  ) {
    passwordError.textContent =
      " *Kata sandi harus terdiri dari 8-12 karakter, kombinasi huruf besar, huruf kecil, dan angka tanpa karakter spesial";
    valid = false;
  }

  // Validasi ulangi password
  if (confirmPassword === "") {
    confirmPasswordError.textContent = " *Wajib diisi";
    valid = false;
  } else if (confirmPassword !== password) {
    confirmPasswordError.textContent = " *Kata sandi tidak cocok";
    valid = false;
  }

  // Validasi phone number
  if (phone === "") {
    phoneError.textContent = " *Nomor telepon harus diisi";
    valid = false;
  } else if (!/^\d+$/.test(phone)) {
    phoneError.textContent = " *Nomor telepon hanya boleh berisi angka";
    valid = false;
  }

  // Validasi gender
  if (gender === "") {
    genderError.textContent = " *Wajib dipilih";
    valid = false;
  }

  // Validasi alamat website
  if (website === "") {
    websiteError.textContent = " *Alamat Website harus diisi";
    valid = false;
  } else if (!/^(ftp|http|https):\/\/[^ "]+$/.test(website)) {
    websiteError.textContent = "Alamat Website tidak valid";
    valid = false;
  }

  return valid;
}

function primaryPassword() {
  var x = document.getElementById("password");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}

function repeatPassword() {
  var x = document.getElementById("confirmPassword");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}