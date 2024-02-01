'use client'
import "./promo.scss"
import Link from "next/link";
import useSWR from "swr";
import {ContactInfoInterface} from "@/interfases/interfaces";
import {getContacts} from "@/api/clientAPI";


function PromoSlice() {

    const {data, isLoading} = useSWR<ContactInfoInterface | undefined>('contacts/', getContacts)

    return (
        <div className="Promo-slice">
            <div className="container ">
                <div className="Promo-slice__info ">
                    Найди работу в студенческих отрядах
                </div>
                <div className="Promo-slice__button">
                    <Link href={data && data.join ? data?.join.value : 'https://vk.com/sev_rso'} target="_blank">
                        <button className="Promo-slice__button__stylebtn">
                            Вступить
                            <img src="./img/arrow-right.png"/>
                        </button>
                    </Link>
                </div>
            </div>
        </div>
    );
}

export default PromoSlice;
