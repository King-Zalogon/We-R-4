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
            main: document.querySelector(".perfiles")
        }
    },
    mounted(){
        this.imagen = "imagen1.png",
        this.altura = 50
        this.main = document.querySelector(".perfiles")
    },

    methods:{
        verMas(){
            for(let i = 0; i <= 2; i++){
                this.generarPerfil()
            }

            
        },

        generarPerfil(){
            fetch("https://randomuser.me/api/")
            .then(data => data.json())
            .then(data => data)
            .then(data =>{
                console.log(data)
                this.main.innerHTML += `<div class="perfil">
            <img src="${data["results"][0]["picture"]["large"]}" alt="" class="perfil-img">
            <div class="datos">
                <h4>${data["results"][0]["name"]["first"]} ${data["results"][0]["name"]["last"]}</h4>
                <p class="descripcion">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Consectetur alias quas ea aperiam, soluta sint officiis ut? Eum aut nihil minima, suscipit, facere pariatur consequatur dolorum sequi ipsam neque sapiente illum sit aliquam deserunt veniam non, alias voluptate laboriosam ipsa odit quidem est? Laudantium adipisci, cum vero assumenda tempora placeat.</p>
                <p class="modalidad"><b>Modalidad:</b> A distancia</p>
                <p class="zona"><b>Zona:</b> No especifica</p>
                <p class="telefono"><b>Telefono:</b> 11 56369556</p>
            </div>
            
        </div>`
            })
            
        }
    }

})
miApp.mount("#main__app")