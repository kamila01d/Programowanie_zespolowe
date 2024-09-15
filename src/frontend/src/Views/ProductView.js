import NavBar from "../Components/NavBar";
import ProductSummaryList from "../Components/ProductSummaryList";

import { useParams } from 'react-router-dom'

function ProductView(){

    const {productQuery} = useParams();

    return(
        <>
        <ProductSummaryList productQuery={productQuery}></ProductSummaryList>
        </>
    );

}

export default ProductView;