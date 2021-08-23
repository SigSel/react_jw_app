import React, { useState, useEffect }  from 'react'
import { csv } from 'd3'
import csvPath from './JW_vinmon.csv'
import Products from './components/Products/Products'


const App = () => {
    const [products, setProducts] = useState([]);

    useEffect(() => {
        csv(csvPath).then(products => {
            setProducts(products);
        });
    }, []);
    
    return (
        <div>
             <Products products={products} />
        </div>
    )
}

export default App
