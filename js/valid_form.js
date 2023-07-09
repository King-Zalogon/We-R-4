let provincias = ["Buenos Aires",
"Catamarca",
"Chaco",
"Chubut",
"Córdoba",
"Corrientes",
"Entre Ríos",
"Formosa",
"Jujuy",
"La Pampa",
"La Rioja",
"Mendoza",
"Misiones",
"Neuquén",
"Río Negro",
"Salta",
"San Juan",
"San Luis",
"Santa Cruz",
"Santa Fe",
"Santiago del Estero",
"Tierra del Fuego",
"Tucumán"]


let selectorDeProvincias = document.getElementById("provincias")

console.log(selectorDeProvincias)
for (let i of provincias){
   selectorDeProvincias.innerHTML += `<option>${i}</option>`
}

const { createApp } = Vue;
const miApp = createApp({
   data() {
      return {
         perfil: "",
         materia: document.querySelector("#div_materia"),
         modalidad : "",
         provincia : document.getElementById("provincias")

      };
   },
   mounted() {
      this.materia = document.querySelector("#div_materia");
      this.perfil = document.querySelector("#user_choice").value;
      this.modalidad = document.querySelector("#modalidad").value;
      this.provincia = document.getElementById("provincias");
   },
   methods: {
      mostrar_materia() {
         if (this.perfil == "profesor" || this.perfil == "ambas") {
            this.materia.style.display = "block";
         } else {
            this.materia.style.display = "none";
         }
      },
      mostrar_provincias(){
         if (this.modalidad == "presencial" || this.modalidad == "ambas") {
            this.provincia.style.display = "block";
         } else {
            this.provincia.style.display = "none";
         }
      },
      validarFormulario(event) {
         event.preventDefault()
         let nombre = document.getElementById("user_first").value.trim();
         let apellido = document.getElementById("user_last").value.trim();
         let correo = document.getElementById("email_1").value.trim();
         let numero = document.getElementById("numero").value.trim();
         let cumple = document.getElementById("birth").value;
         let descripcion = document.getElementById("descripcion").value;
         let perfil = document.getElementById("user_perfil");
         let modalidad = document.getElementById("modalidad");
         let provincia = document.getElementById("provincias").value;
         let foto = document.getElementById("photo");
         if (nombre === "" || apellido === "" || correo === "" || numero === "" || cumple === ""|| descripcion === "" || perfil === "" || modalidad === "") {
            alert("Por favor, complete todos los campos del formulario.");
            return false;
         }

         try{
            numero = parseInt(numero)
            if (numero.length != 12){
               alert("Numero de telofono invalido")
               return False
            }
         }
         catch{
            alert("Numero de telofono invalido")
         }

         if (foto.value === "") {
            alert("Por favor, ingrese una url con una imagen");
            return false;
         }
         const array = [nombre, apellido];
         console.log(array[0]);
         console.log(array[1]);
         for (let x = 0; x < 2; x++) {
            for (let i = 0; i < array[x].length; i++) {
               let charCode = array[x].charCodeAt(i);
               if (
                  !(
                     (charCode >= 65 && charCode <= 90) ||
                     (charCode >= 97 && charCode <= 122) ||
                     charCode === 32
                  )
               ) {
                  alert(
                     "Los campos 'Nombres' y 'Apellidos' solo pueden contener caracteres alfabéticos y espacios."
                  );
                  return false;
               }
            
            }

         }

         if (descripcion.length < 80){
            alert("Ingresa una descripcion mas larga")
            return false
         }
         else if(descripcion.length > 360){
            alert("Ingresa una descripcion mas larga")
            return false
         }

         let imagen = foto.value;
         let extensiones = /(.jpg|.jpeg|.png|.gif)$/i;
         if (!extensiones.exec(imagen)) {
            alert(
               "Extensión no admitida, por favor utilice extensiones .jpg/.jpeg/.png/.gif"
            );
            return false;
         }
      }
   }
});

miApp.mount("#app");
