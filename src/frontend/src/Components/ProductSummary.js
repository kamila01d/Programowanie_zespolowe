import './ProductSummary.css'
import { useAuth } from "../AuthProvider";

import { useEffect, useState } from 'react';

function ProductSummary(props){

    const [currentGalleryScroll, setCurrentGalleryScroll] = useState(0);
    const [isFavourite, setIsFavourite] = useState(false);
    const [productName, setProductName] = useState("");
    const [description, setDescription] = useState("");
    const [imageURLArr, setImageURLArr] = useState([]);
    const [pricingArr,  setPricingArr] = useState([]);
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

    let maxGalleryScroll = imageURLArr.length;

    function scrollTo(index)
    {
        if(index < maxGalleryScroll && index >= 0)
        {
            setCurrentGalleryScroll(index);
            console.log("here")
        }

        console.log(index)
    }

    async function checkFavourite(){

        try{

            if(authContext.isLogged())
            {
                let userInfo = authContext.getUserInfo();
                let favouritesArray = userInfo.favourites;
                if(favouritesArray.includes(productName)){
                    setIsFavourite('favFilled');
                }
                else
                {
                    setIsFavourite('');
                }
               
            }
            else
            {
                let favouritesArrayStr = localStorage.getItem('favourites');
                if(favouritesArrayStr != null)
                {
                    let favouritesArray = JSON.parse(favouritesArrayStr);
                    if(favouritesArray.includes(productName)){
                        setIsFavourite('favFilled');
                    }
                    else
                    {
                        setIsFavourite('');
                    }
                }
            }

        }
        catch(e)
        {
            console.log(e);
        }

    }

    async function addFavourite(){

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
            console.log("new res");
            let response = await fetch(`/compare-products/?product=${query}`);
            let res = await response.json();

            console.log(res);

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
            setProductName(res.name);
            setDescription(res.description);
            setImageURLArr(res.imageURLArr);
            setPricingArr(res.pricingArr);

        }

    }

    useEffect(() => {
        checkFavourite();
        getScrapperData(props.productQuery);
    },[]);


    return(
        <div className='productPageScrollWrapper'>
        <div className='productPage'>
        <div className='productContainer'>

            <div className='productNameContainer'>
                <div className='productName'>{productName}</div>
                <div className={`productFavourite ${isFavourite}`} onClick={() => {addFavourite()}}></div>
            </div>
            

            <div className='productOverviewContainer'>
                
                    <div className='productGalleryContainer'>

                        <div className='productGalleryMainContainer'>
                            <div className='productGalleryMainArrow leftArrow' onClick={() => {scrollTo(currentGalleryScroll-1)}}></div>
                            <div className='productGalleryMainPhotosContainer'>
                                <div className='productGalleryMainPhotosContainerInner'>
                                <div className='producGalleryMainPhotosWrapper' style={{right: `${currentGalleryScroll*100}%` }}>
                                    {imageURLArr.map(imageURL => 
                                        <img src={`${imageURL}`} className='producGalleryMainPhoto' ></img>
                                    )}
                                </div>
                                </div>
                            </div>
                            <div className='productGalleryMainArrow rightArrow'  onClick={() => {scrollTo(currentGalleryScroll+1)}}></div>
                        </div>

                        <div className='productGalleryThumb'>
                            <div className='productGalleryThumbWrapper'>
                                {imageURLArr.map((imageURL, index) => 
                                    <img src={`${imageURL}`} className='producGalleryThumbPhoto' onClick={() => {scrollTo(index)}}></img>
                                )}
                            </div>
                        </div>
                        
                    </div>
                
                    <div className='productDescriptionContainer'>
                        <div className='productDescriptionTitle'>
                            Description:
                        </div>
                        <div className='productDescriptionContent'>
                            {description}
                        </div>
                    </div>
                
            </div>

            <div className='productPricingList'>
                <div className='productPricingListTitle'>Offers found:</div>
                <div className='productPricingListWrapper'>
                {pricingArr.map(pricing => 
                    <a className='productPricingLink' href={pricing.shopURL}>
                        <div className='productPricingRow'>
                            <div className='productPricingName'>{pricing.shopName}</div>
                            <div className='productPricingPrice'>{pricing.shopPrice}</div>
                            <div className='productPricingLinkLogo'></div>
                        </div>
                    </a>
                )}
                </div>
            </div>

        </div>
        </div>
        </div>
    );

}

export default ProductSummary;

/**/