import React, { useState, useEffect }  from 'react';
import { csv } from 'd3';
import csvPath from './JW_vinmon.csv';
import { Products, Navbar } from './components';



const App = () => {
    const [products, setProducts] = useState([]);

    useEffect(() => {
        csv(csvPath).then(products => {
            setProducts(products);
        });
    }, []);
    
    return (
        <div>
            <Navbar />
            <Products products={products} />
        </div>
    )
}

export default App
