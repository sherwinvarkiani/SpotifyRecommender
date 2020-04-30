import React, { useEffect } from 'react';
import axios from 'axios';

function Login() {
    useEffect(() => {
        window.location.href = 'http://127.0.0.1:5000/getUserInfo';
    }, []);

    return <div> </div>;
}

export default Login;
