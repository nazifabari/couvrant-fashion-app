import NavBar from './NavBar'
import Hero from './Hero'
import ProductGrid from './ProductGrid'
import Footer from './Footer'
import { useState, useEffect } from "react"






function HomePage() {
  
  const [search, setSearch] = useState("")






  return (

 
    <div className = "bg-[#F5F0E8]">


    <NavBar search= {search} setSearch = {setSearch}  ></NavBar>
    <Hero></Hero>
    <ProductGrid search= {search} ></ProductGrid>
    <Footer></Footer>














  </div>

  )
}

export default HomePage
