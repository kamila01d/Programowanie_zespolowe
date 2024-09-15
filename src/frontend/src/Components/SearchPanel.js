import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './SearchPanel.css'

function SearchPanel(){

    const [searchterm, setSearchterm] = useState("");
    const navigate = useNavigate();

    async function attemptSearch()
    {
        try{
            console.log(searchterm);

            navigate(`/product/${searchterm}`);

        }
        catch(err)
        {
            console.log(err);
        }
    }

    async function handleEnter(e){

        if(e.key === "Enter")
        {
            attemptSearch();
        }

    }

    return(
        <div className='searchpanelContainer'>
            <input className='searchpanelInput' placeholder='Product name' value={searchterm} onChange={(e) => {setSearchterm(e.target.value)}} onKeyDown={(e) => {handleEnter(e)}}></input>
            <button className='searchpanelButton' onClick={attemptSearch}>Search</button>
        </div>
    );

}

export default SearchPanel;