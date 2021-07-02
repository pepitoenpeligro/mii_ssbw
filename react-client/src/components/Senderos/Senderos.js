
import './Senderos.css'
import React, { useState, useEffect } from "react";
import Sendero from '../Sendero/Sendero';


const Senderos = () => {

    const [sendero, setSendero] = React.useState([]);
    const [searchTerm, setSearchTerm] = useState('');

    React.useEffect(() => {
        async function fetchSenderos() {
            const fullResponse = await fetch('http://157.90.224.208:3008/api/senderos');
            const data = await fullResponse.json();
            console.log("Los datos son");
            console.log(data);
            setSendero(data);
        }

        fetchSenderos();

    }, []);

    return (
        <>
            <div className="container-fluid mb-4">
                <input className="busqueda text-center mt-4" type="text" placeholder="Buscar sendero..."
                    onChange={event => { setSearchTerm(event.target.value) }}
                ></input>

            </div>

            {/*         
        {JSON.stringify(sendero.senderos)} */}
            {/* {sendero.senderos.map(sendero => <p>{sendero.nombre}</p>)} */}
            {!sendero.some && sendero.senderos.filter((val) => {
                if (searchTerm == "") {
                    return val
                } else if (val.nombre.toLowerCase().includes(searchTerm.toLocaleLowerCase())) {
                    return val
                }

            }

            ).map(sendero =>
                <Sendero
                    key={sendero.id}
                    data={sendero}
                >
                </Sendero>)
            }
        </>
    );

}

export default Senderos;