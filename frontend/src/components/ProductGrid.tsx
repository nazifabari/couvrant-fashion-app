
import { useState, useEffect } from "react"

function ProductGrid(){
    
    const [products, setProducts] = useState([])
    const [pageNumber, setPageNumber] = useState(1)
    const [total, setTotal] = useState(0)


    async function fetchProducts() {
        const result = await fetch(`${import.meta.env.VITE_API_URL}/items?page=${pageNumber}&limit=6`)
        const data = await result.json()
        setProducts(data.items)
        setTotal(data.total)
    }
    useEffect( ()=> {fetchProducts()}, [pageNumber])

    return(

        <section className = "max-w-[1440px] mx-auto px-6 md:px-16 pb-25">
            
            <p className="uppercase text-[#A07830] text-[12px] pt-15 tracking-[0.3em] open-sans-main" >Featured Pieces</p>

            <div className="grid pt-8 grid-cols-1 md:grid-cols-3 lg:grid-cols-3  w-full gap-6">

               { products.map(product => {
                    return (
                        <div key= {product.id} >
                            <div className= "bg-[#A07830] opacity-80 aspect-[3/4] md:h-[500px] rounded-2xl "></div>

                            <div className= "pt-4  " >

                                <p className="uppercase text-[11px]  tracking-[0.2em] text-[#A07830] "   >{product.brand_name}</p>
                                <p className="pt-1 text-[15px] "                                         >{product.name}</p>
                                <p className="pt-1 text-[14px] "                                         >${product.price}</p>
                                <p className="pt-3 text-[12px] text-gray-500"                            ><a href={product.product_url}>View Link → </a>  </p>

                            </div>
                        </div>
                    )
                 })
                }

            </div>

            <div className= "flex justify-between pt-20">
                <button className="bg-[#EBE1D0] rounded-full  px-5 py-3 text-[13px] open-sans-main hover:bg-[#C4B8A0]  active:bg-[#A07830] "       disabled={pageNumber==1}       onClick={() => setPageNumber(pageNumber - 1)}               >← previous</button>
                <button  className ="bg-[#EBE1D0]  rounded-full px-5 py-3 text-[13px] open-sans-main hover:bg-[#C4B8A0] active:bg-[#A07830] "      disabled={pageNumber==(Math.ceil(total/6))}       onClick={() => setPageNumber(pageNumber + 1)}               >next →</button>
            </div>














        </section>
























    )
}

export default ProductGrid