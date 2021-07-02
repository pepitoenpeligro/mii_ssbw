
import './Sendero.css'

import React, { Component, useState , useEffect} from "react";


const Sendero = (props, dispatch) => {

    const [data, setData] = useState();

    useEffect(() => {
        setData(props);
    }, props);

    const handleSubirLikes =  (event) => {
        console.log(event.target.id)

        const res = fetch(`http://157.90.224.208:3008/addlike/${event.target.id}`,{
            method: 'GET',
            headers: {
                'Content-Type': "application/json; charset=utf-8",
            }
        })
        .then(response => {
            console.log(response);
            let datos = response.json();
            datos.then(val => {
                console.log('Likes: ');
                console.log(val.likes);
                //props.data.likes = val.likes;
                setData({... props.data.likes = val.likes})
                console.log("Lo que hay: ", props.data);
                

                //setData(props)
                console.log("ahora tiene:" , props.data.likes )
            })
            
        })
        .catch(error =>{
                console.log(error)
        })
    }

    const handleBajarLikes =  (event) => {
        console.log(event.target.id)

        const res = fetch(`http://157.90.224.208:3008/substractlike/${event.target.id}`,{
            method: 'GET',
            headers: {
                'Content-Type': "application/json; charset=utf-8",
            }
        })
        .then(response => {
            console.log(response);
            let datos = response.json();
            datos.then(val => {
                console.log('Likes: ' , val);
                setData({... props.data.likes = val.likes})
                //props.data.likes = val;
            })
        })
        .catch(error =>{
                console.log(error)
            })

    }

    



    return (
        <main className="container py-2">
            <div className="mt-4 mb-2" ></div>     

            
    
            <article className="postcard light blue">
                <a className="postcard__img_link" href="#">
                    <img className="postcard__img" src={props.data.fotos[0].url} alt="Image Title" />
                </a>
                <div className="postcard__text t-dark">
                    <h1 className="postcard__title t-dark"><a href="#">{props.data.nombre}</a></h1>
                    <div className="postcard__subtitle small">

                            <i className="fas fa-calendar-alt mr-2">

                            </i> {props.data.duracion} minutos , <span className="plikes" id={props.data.id} >{props.data.likes} </span> me gustas

                    </div>
                    <div className="postcard__bar"></div>
                    <div className="mt-4 mb-4">
                        <a >
                            <span className="likes" id={props.data.id} onClick={handleSubirLikes}  >👍</span>
                         </a>
                         <a >
                            <span className="dislikes" id={props.data.id} onClick={handleBajarLikes}>👎</span>
                         </a>
                          
                    </div>
                    <div className="postcard__preview-txt">{props.data.descripcion}</div>
                    <ul className="postcard__tagbox">
                        {/* {% for tag in sendero.tags %}
                        <li className="tag__item"><i className="fas fa-tag mr-2"></i>{{ tag }}</li>
                        {% endfor %} */}
                    </ul>
                    {/* {% if user.is_authenticated %}  */}
                
                    {/* <div className="row mt-4">
                        <div className="col col-lg-2">
                            <a  href="{% url 'editar' id=sendero.id %}" className="mt-2 mb-2 btn btn-info">Editar</a>

                        </div>
                        <div className="col col-lg-2">

                            <a  href="{% url 'eliminar' id=sendero.id %}" className="mt-2 mb-2  btn btn-danger eliminar" id={props.data.id}>Eliminar</a>
                        </div>

                        
                        
                    </div> */}

                    {/* {% endif %} */}
                </div>
            </article>
    
        </main>


    );

}


export default Sendero;