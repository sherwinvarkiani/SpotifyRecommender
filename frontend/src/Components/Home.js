import React, { useEffect } from 'react';

function Home() {
    useEffect(() => {
        console.log('here');
    }, []);

    return <div> Home </div>;
}

export default Home;
