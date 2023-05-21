function validarFormulario() {
    let nombre = document.getElementById("user_first").value.trim();
    let apellido = document.getElementById("user_last").value.trim();
    let correo = document.getElementById("email_1").value;
    let cumple = document.getElementById("birth").value;
    let foto = document.getElementById("photo");


    if (nombre === "" || apellido === "" || correo === "" || cumple === "") {
        alert("Por favor, complete todos los campos del formulario.");
        return false;
     }

     if (foto.value === "") {
        alert("Por favor, seleccione un archivo para su foto de perfil.");
        return false;
     }
     
     const array = [nombre , apellido]
     console.log(array[0])
     console.log(array[1])
     for (let x = 0; x < 2; x++){
         for (let i = 0; i < array[x].length; i++) {
            let charCode = array[x].charCodeAt(i);
            if (!((charCode >= 65 && charCode <= 90) || (charCode >= 97 && charCode <= 122) || charCode === 32)) {
               alert("Los campos 'Nombres' y 'Apellidos' solo puede contener caracteres alfabéticos y espacios.");
               return false;
            } 
         }
      }

     let imagen = foto.value;
     let extenciones = /(.jpg|.jpeg|.png|.gif)$/i;
     if (!extenciones.exec(imagen)){
        alert("Extención no admitida, por favor utilice extenciones .jpg/.jpeg/.png/.gif");
        return false;
     }
     
}