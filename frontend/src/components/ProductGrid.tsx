
import { useState, useEffect } from "react"
import { SlArrowRight } from "react-icons/sl";
import { SlArrowLeft } from "react-icons/sl";




type ProductGridProps = {
  search: string;
}

function ProductCard({ product }) {    
    const [img_num, setImg_num] = useState(1)
    const displayImage = product.item_images.find(image => image.display_order == img_num)
    return (
        <div >
            <div className= "relative " >
                <a href={product.product_url}>
                    <img src = {displayImage.image_url}
                    className= "rounded-2xl object-cover object-center w-full h-150"/>
                </a> 

                <div className= "">
                    <button className=" w-10 h-10  flex  items-center justify-center absolute top-1/2 left-2 bg-transparent rounded-full hover:bg-[#C4B8A0]  hover:text-[#000000] text-[#C4B8A0] active:bg-[#A07830] text-[12px] "   disabled={img_num==1} onClick={() => setImg_num(img_num - 1)} ><SlArrowLeft /></button>
                    <button  className =" w-10 h-10 flex  items-center justify-center  absolute top-1/2 right-2 bg-transparent rounded-full text-[12px] text-[#C4B8A0] hover:text-[#000000]  hover:bg-[#C4B8A0] active:bg-[#A07830] " disabled={img_num==product.item_images.length} onClick={() => setImg_num(img_num + 1)}  ><SlArrowRight /></button>
                </div>
                 

            </div>


            <div className= "pt-4  " >
                <p className="uppercase text-[12px]  tracking-[0.2em] text-[#A07830] "   >{product.brand_name}</p>
                <p className="pt-1 text-[15px] "                                         >{product.name}</p>
                <p className="pt-1 text-[14px] "                                         >${product.price.toFixed(2)}</p>
                <p className="pt-3 text-[12px] text-gray-500"                            ><a href={product.product_url}>View Link → </a>  </p>

            </div>
        </div>
    )
}






function ProductGrid({search}: ProductGridProps){
    
    const [products, setProducts] = useState([])
    const [pageNumber, setPageNumber] = useState(1)
    const [total, setTotal] = useState(0)

    async function fetchProducts() {
        const result = await fetch(`${import.meta.env.VITE_API_URL}/items?page=${pageNumber}&limit=6&search=${search}`)
        const data = await result.json()
        setProducts(data.items)
        setTotal(data.total)

    }
    useEffect( ()=> {fetchProducts()}, [pageNumber])
    useEffect(() => {
        if (pageNumber === 1) {
            fetchProducts()
            
        } else {
            setPageNumber(1)
        }
        }, [search])



    return(

        <section className = "max-w-[1440px] mx-auto px-6 md:px-16 pb-25">
            
            <p className="uppercase text-[#A07830] text-[12px] pt-15 tracking-[0.3em] open-sans-main" >Featured Pieces</p>

            <div className="grid pt-5 grid-cols-1 md:grid-cols-3 lg:grid-cols-3  w-full gap-25">
            {products.map(product => <ProductCard  key={product.id} product={product} />)}
            </div>

            <div className= "flex justify-between pt-20">
                <button className="bg-[#EBE1D0] rounded-full  px-5 py-3 text-[13px] open-sans-main hover:bg-[#C4B8A0]  active:bg-[#A07830] "       disabled={pageNumber==1}       onClick={() => setPageNumber(pageNumber - 1)}               >← previous</button>
                <button  className ="bg-[#EBE1D0]  rounded-full px-5 py-3 text-[13px] open-sans-main hover:bg-[#C4B8A0] active:bg-[#A07830] "      disabled={pageNumber==(Math.ceil(total/6))}       onClick={() => setPageNumber(pageNumber + 1)}               >next →</button>
            </div>

        </section>
    )
}

export default ProductGrid