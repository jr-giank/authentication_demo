import { useEffect, useState } from "react";
import jwt_decode from "jwt-decode";

export const InitialState = () => {
    const [autorizacionToken, setAutorizacionToken] = useState(() => localStorage.getItem('autorizacionToken') ? JSON.parse(localStorage.getItem('autorizacionToken')) : null)
    const [user, setUser] = useState(() => localStorage.getItem('autorizacionToken') ? jwt_decode(localStorage.getItem('autorizacionToken')) : null);     
    const [loading, setLoading] = useState(true);

    const loginService = async (values) => {
        let response = await fetch("http://127.0.0.1:8000/api/token/", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(values)
        })
    
        let info = await response.json();
    
        if (response.status === 200){
            let user = jwt_decode(info.data.access)
            if (user.company_is_active === true){
                setAutorizacionToken(info.data);
                setUser(jwt_decode(info.data.access));
                localStorage.setItem('autorizacionToken', JSON.stringify(info.data));
            }else{
                alert('Su empresa no tiene autorización a la plataforma');
            }

        }else{
            alert('Usuario o contraseña incorrectos');
        }
    }

    const updateToken = async () => {
        let response = await fetch("http://127.0.0.1:8000/api/token/refresh/", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({'refresh':autorizacionToken.refresh})
        })

        let info = await response.json();

        if(response.status === 200){
            setAutorizacionToken(info.data);
            setUser(jwt_decode(info.data.access));
            localStorage.setItem('autorizacionToken', JSON.stringify(info.data));
        }
    }

    useEffect(() => {
        let time = 1000 * 60 * 4

        let interval = setInterval(() => {
            if(autorizacionToken){
                updateToken();
            }
        }, time)

        return () => clearInterval(interval)

    }, [autorizacionToken, loading])

    return{
        user,
        autorizacionToken,
        loginService,
        updateToken,
    }
}