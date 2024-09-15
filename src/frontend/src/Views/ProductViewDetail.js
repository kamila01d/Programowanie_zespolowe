import NavBar from "../Components/NavBar";
import ProductSummary from "../Components/ProductSummary";

import { useParams } from 'react-router-dom'

function ProductView(){

    const {productQuery} = useParams();

    return(
        <>
        <ProductSummary productQuery={productQuery}></ProductSummary>
        </>
    );

}

export default ProductView;