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

const {createApp} = Vue 
const miApp = createApp({
    
    data(){
        return{
            main: document.querySelector(".perfiles"),
            contador : 0
        }
    },
    mounted(){
        this.imagen = "imagen1.png",
        this.altura = 50
        this.main = document.querySelector(".perfiles")
        this.contador = 0
    },

    methods:{
        verMas(){
            for(let i = 0; i <= 2; i++){
                this.generarPerfil()
            }

            
        },

        generarPerfil(){
            fetch("http://127.0.0.1:5000/profesores")
            .then(data => data.json())
            .then(data => data)
            .then(data =>{
                this.main.innerHTML += `<div class="perfil">
            <img src="${data[this.contador]["foto"]}" alt="" class="perfil-img">
            <div class="datos">
                <h4>${data[this.contador]["nombre"]} ${data[this.contador]["apellido"]}</h4>
                <p class="descripcion">${data[this.contador]["descripcion"]}</p>
                <p class="modalidad"><b>Modalidad: </b>${data[this.contador]["modalidad"]}</p>
                <p class="modalidad"><b>Materia: </b>${data[this.contador]["materia"]}</p>
                <p class="zona"><b>Provincia: </b>${data[this.contador]["provincia"]}</p>
                <p class="telefono"><b>Telefono: </b>${data[this.contador]["telefono"]}</p>
            </div>
            
        </div>`
                this.contador += 1
            })
            
        }
    }

})
miApp.mount("#main__app")