document.addEventListener("DOMContentLoaded",(e)=>{
    //console.log("Hola Mundo");
    serializarCategorias();
});

async function cargaCategorias(){
    let peticion = await fetch('/products/categories',{
        method: "GET",
        headers: {
            'Content-type': 'application/json'
        }
    });

    let datos = await peticion.json();
    console.log(datos);
    //alert(datos);
    return datos;
}

async function serializarCategorias(){
    let categorias = await cargaCategorias();
    let padre = document.getElementsByName("cmbCategoria")[0];
    //console.log(padre);
    if(categorias.errors!=[]){
        //console.log(categorias["data"]);
        Array.from(categorias["data"]).map((categoriaActual)=>{
            let nodo = document.createElement('option');
            nodo.setAttribute('value',categoriaActual["id"]);
            nodo.textContent = categoriaActual["name"];
            padre.appendChild(nodo);
        });
    }
}
