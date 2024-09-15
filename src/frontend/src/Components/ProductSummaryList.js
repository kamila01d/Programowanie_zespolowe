import './ProductSummaryList.css'
import { useAuth } from "../AuthProvider";

import { useEffect, useState } from 'react';

function ProductSummaryList(props){

    const [currentGalleryScroll, setCurrentGalleryScroll] = useState(0);
    const [isFavourite, setIsFavourite] = useState("");
    const [productArray, setProductArray] = useState("");
    const authContext = useAuth();

    /*res = {
        name: "Samsung Galaxy S24",
        description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc eleifend mattis purus sit amet volutpat. Cras vitae sem leo. Duis sagittis tristique magna, sit amet cursus diam lobortis non. Fusce pretium suscipit eros. Sed nulla urna, egestas eu arcu eget.",
        imageURLArr: [
            "https://f00.esfr.pl/foto/6/135247539345/94c58bc2be7b4e0fb8a6fad627397cc5/samsung-smartfon-s24-8-128-black-samsung,135247539345_5.jpg",
            "https://f00.esfr.pl/foto/6/135247539345/fb4e7c408cbe4f0a040775ad293c6b40/samsung-smartfon-s24-8-128-black-samsung,135247539345_5.jpg",
            "https://f00.esfr.pl/foto/6/135247539345/859294722dffe9bd20820cf39e7713e4/samsung-smartfon-s24-8-128-black-samsung,135247539345_5.jpg"
        ],
        pricingArr: [
            {
                shopName: "MediaExpert" ,
                shopLogoURL: "https://glogovia-galeria.pl/wp-content/uploads/2022/07/Media-Expert_Logo.png",
                shopPrice: "2499,99 PLN",
                shopURL: ""
            },
            {
                shopName: "RTVEuroAGD" ,
                shopLogoURL: "https://sokolpark.pl/wp-content/uploads/018b7cd5-d8b5-4e81-8f67-26c049e5cc63-1024x277.png",
                shopPrice: "2199,99 PLN",
                shopURL: ""
            }
        ]
    });*/

    //let productName = res.name;
    //let description = res.description;
    //let imageURLArr = res.imageURLArr;
    //let pricingArr = res.pricingArr;

    async function checkFavourite(){

        try{

            if(authContext.isLogged())
            {
                let userInfo = authContext.getUserInfo();
                let favouritesArray = userInfo.favourites;
                setIsFavourite(JSON.stringify(favouritesArray));
            }
            else
            {
                let favouritesArrayStr = localStorage.getItem('favourites');
                if(favouritesArrayStr != null)
                {
                    setIsFavourite(favouritesArrayStr);
                }
            }

        }
        catch(e)
        {
            console.log(e);
        }

    }

    async function addFavourite(productName){

        console.log("fav")

        try{

            if(authContext.isLogged())
            {
                await authContext.addFavourite(productName);
            }
            else
            {
                let favouritesArray = [];

                let favouritesArrayStr = localStorage.getItem('favourites');
                if(favouritesArrayStr != null)
                {
                    favouritesArray = JSON.parse(favouritesArrayStr);
                }
                else
                {
                    favouritesArray = [];
                }

                if(!favouritesArray.includes(productName))
                {
                    favouritesArray.push(productName);
                } 
                console.log(favouritesArray);
                localStorage.setItem('favourites', JSON.stringify(favouritesArray));
            }

            

        }
        catch(e)
        {
            console.log(e);
        }

        checkFavourite();
    }

    async function getScrapperData(query) {

        try{

            console.log(query);
            let response = await fetch(`/compare-products/?product=${query}`);
            let res = await response.json();
            res = JSON.parse(res);

            setProductArray(JSON.stringify(res));

            /*setProductName(res.name);
            setDescription(res.description);
            setImageURLArr(res.imageURLArr);
            setPricingArr(res.pricingArr);*/

        }
        catch(err)
        {

            let res = {
                name: "Samsung Galaxy S24",
                description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc eleifend mattis purus sit amet volutpat. Cras vitae sem leo. Duis sagittis tristique magna, sit amet cursus diam lobortis non. Fusce pretium suscipit eros. Sed nulla urna, egestas eu arcu eget.",
                imageURLArr: [
                    "https://f00.esfr.pl/foto/6/135247539345/94c58bc2be7b4e0fb8a6fad627397cc5/samsung-smartfon-s24-8-128-black-samsung,135247539345_5.jpg",
                    "https://f00.esfr.pl/foto/6/135247539345/fb4e7c408cbe4f0a040775ad293c6b40/samsung-smartfon-s24-8-128-black-samsung,135247539345_5.jpg",
                    "https://f00.esfr.pl/foto/6/135247539345/859294722dffe9bd20820cf39e7713e4/samsung-smartfon-s24-8-128-black-samsung,135247539345_5.jpg"
                ],
                pricingArr: [
                    {
                        shopName: "MediaExpert" ,
                        shopLogoURL: "https://glogovia-galeria.pl/wp-content/uploads/2022/07/Media-Expert_Logo.png",
                        shopPrice: "2499,99 PLN",
                        shopURL: ""
                    },
                    {
                        shopName: "RTVEuroAGD" ,
                        shopLogoURL: "https://sokolpark.pl/wp-content/uploads/018b7cd5-d8b5-4e81-8f67-26c049e5cc63-1024x277.png",
                        shopPrice: "2199,99 PLN",
                        shopURL: ""
                    }
                ]
            };
            /*setProductName(res.name);
            setDescription(res.description);
            setImageURLArr(res.imageURLArr);
            setPricingArr(res.pricingArr);*/

        }

    }

    useEffect(() => {
        checkFavourite();
        getScrapperData(props.productQuery);
    },[]);


    let productArray_ = [];
    try
    {
        productArray_ = JSON.parse(productArray);
        console.log(productArray_);
        console.log(productArray_[0]);
        console.log(typeof productArray_);
        
    }
    catch(err)
    {

    }
    

    return(
        <div className='productPageScrollWrapper'>
        <div className='productPage'>
        <div className='productContainer'>

            {productArray_.map((product) => {

                let favClass = 'productListFavFalse';
                console.log(isFavourite);
                try
                {
                    let favouriteArray = JSON.parse(isFavourite);
                    console.log(favouriteArray);
                    if(favouriteArray.includes(product.name))
                    {
                        favClass = 'productListFavTrue';
                    }
                }
                catch(err)
                {

                }
                

                

                return( 
                <div className='productListContainer'>
                    <img src={`${product.src}`} className='productListThumbnail' ></img>
                    <a className='productListLinkSection' href={`${product.link}`}>
                        <div className='productListName'>{product.name}</div>
                        <div className='productListLink'></div>
                    </a>
                    <div className='productListPrice'>{`${product.price} PLN`}</div>
                    <div className={`${favClass}`} onClick={() => {addFavourite(`${product.name}`)}}></div>
                </div>
                );

            })}

        </div>
        </div>
        </div>
    );

}

export default ProductSummaryList;

/**/