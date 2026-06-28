import { HiMiniMagnifyingGlass } from "react-icons/hi2";

function NavBar(){

return (

<nav className= "flex w-full fixed justify-between px-20 py-4 border bg-[#FAF8F5] border-[#FAF8F5] items-center ">

    <span className= "uppercase tracking-[0.5em] zen-antique-soft-regular text-lg text-[]#2C2A28]" >
        Couvrant
    </span>


    <label className="rounded-full border border-gray-300 w-full max-w-[400px] py-2 px-3 flex items-center" >

        <HiMiniMagnifyingGlass className = "text-gray-400 mr-2.5" />
        <input className="text-sm w-full outline-none"
         placeholder= "what are we looking for today?" type="text" />




    </label>





























</nav>









)







}

export default NavBar