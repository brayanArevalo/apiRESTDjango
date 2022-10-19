<template>
    <nav class="navbar navbar-expand-lg bg-primary ">
        <div class="container-fluid ">
            <router-link to="/" class="navbar-brand text-light">Schooltool</router-link>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup"
                aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
                <div class="navbar-nav">
                    <router-link to="/" class="nav-link active text-light" aria-current="page">Home</router-link>
                    <router-link to="/about" class="nav-link text-light">About</router-link>
                    <router-link to="/post" class="nav-link text-light">Post</router-link>
                </div>
            </div>
        </div>
    </nav>
    <div class="container mt-3">
        <h2>Estudiantes</h2>
        <div class="table-responsive">
            <table class="table table-striped">
                <thead>
                    <tr>
                        <th>id</th>
                        <th>Nombre</th>
                        <th>Apellido</th>
                        <th>Grupo</th>                    
                        <th>Opciones</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="todo in todos" :key="todo.id">
                        <td>{{todo.id}}</td>
                        <td>{{todo.nombre}}</td>
                        <td>{{todo.apellido}}</td>
                        <td>{{todo.grupo}}</td>
                      <td>
                            <a class="btn btn-success btn-sm" href="editarEstudiante/{{e.id}}"> Actualizar</a>
                            <!-- ESTO ES PARA EL MODAL DEL BOTON ACTUALIZAR
                            data-bs-toggle="modal" data-bs-target="#contenedor-modal-modificar" -->
                            <a class="btn btn-danger btn-sm" href="eliminarEstudiante/{{e.id}}">Eliminar</a>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>

</template>

<script>
import axios from 'axios'
import { onMounted } from 'vue';
export default {
    data() {
        return {
            todos: null
        }


    },
    mounted() {
        this.getTodos()
    },
    methods: {
        getTodos() {
            console.log("aqui va el codigo de getTodos")
            axios
                .get('http://127.0.0.1:8000/api/estudiantes/')
                .then(response => {
                    this.todos = response.data
                    console.log(response)
                })
                .catch(e => console.log(e))

        }
    }

}

</script>


