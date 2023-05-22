new Vue({
    el: '#app',
    data: {
      name: '',
      email: '',
      subject: '',
      message: '',
      showConfirmation: false
    },
    methods: {
      submitForm() {
        if (this.validateForm()) {
          // Hey guys! We have update this part when we begin with the backend part in class for part two of TPO.
          // Example using JavaScript fetch API:
          fetch('/send-email', {
            method: 'POST',
            body: JSON.stringify({
              name: this.name,
              email: this.email,
              subject: this.subject,
              message: this.message
            }),
            headers: {
              'Content-Type': 'application/json'
            }
          })
          .then(response => {
            if (response.ok) {
              this.showConfirmation = true;
            }
          })
          .catch(error => {
            console.error('Error:', error);
          });
        }
      },
      validateForm() {
        const form = document.querySelector('.needs-validation');
        if (form.checkValidity() === false) {
          form.classList.add('was-validated');
          return false;
        }
        return true;
      },
      resetForm() {
        this.name = '';
        this.email = '';
        this.subject = '';
        this.message = '';
        this.showConfirmation = false;
        const form = document.querySelector('.needs-validation');
        form.classList.remove('was-validated');
      }
    }
  });
  