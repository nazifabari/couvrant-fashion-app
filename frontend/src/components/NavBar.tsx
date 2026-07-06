import { HiMiniMagnifyingGlass } from "react-icons/hi2";

function NavBar(){

return (

<nav className= "flex w-full fixed justify-between px-3 lg:px-20 md:px-20 py-4 border bg-[#F5F0E8] border-[#F5F0E8] items-center z-50 ">

    <span className= "uppercase tracking-[0.5em] zen-antique-soft-regular text-[13px] md:text-[20px] text-[#2C2A28]" >
        Couvrant
    </span>


    <label className="rounded-full bg-[#FFFFFF] border border-gray-300 w-full  max-w-[200px]  md:max-w-[400px]  lg:max-w-[400px]   py-2 px-3 flex items-center" >

        <HiMiniMagnifyingGlass className = "text-gray-500 mr-2.5" />
        <input className="lg:text-sm md:text-sm text-[10px] w-full outline-none"
         placeholder= "what are we looking for today?" type="text" />




    </label>





























</nav>









)







}

export default NavBar