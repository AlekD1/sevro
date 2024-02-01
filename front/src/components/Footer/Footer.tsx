'use client'
import "./footer.scss";
import Link from "next/link";
import {ContactInfoInterface} from "@/interfases/interfaces";
import useSWR from "swr";
import {getContacts} from "@/api/clientAPI";


function Footer() {


    const {data, isLoading} = useSWR<ContactInfoInterface | undefined>('contacts/', getContacts)

    return (
        <footer className="Footer-slice">
            <div className="container">
                <div className="Footer-slice__content">
                    <div className="Footer-slice__content_nav">
                        <div className="Footer-slice__content__links">
                            навигация
                            <div className="Footer-slice__content__links__nav">
                                <ul>
                                    <li>
                                        <Link href="/about">о нас</Link>
                                    </li>
                                    <li>
                                        <Link href="/news">новости</Link>
                                    </li>
                                    <li>
                                        <Link href="/gallery">галерея</Link>
                                    </li>
                                    <li>
                                        <Link href="/info">бойцам</Link>
                                    </li>

                                    <li>
                                        <Link href="/cooperation">сотрудничество</Link>
                                    </li>
                                    <li>
                                        <Link href="/question">Q&A</Link>
                                    </li>
                                </ul>
                            </div>
                        </div>
                        <div className="Footer-slice__content__contact">
                            контакты
                            <div className="Footer-slice__content__contact_nav">
                                {data ?
                                    <ul>
                                        {data.vk ?
                                            <li>
                                                <Link href={data.vk.value} target={"_blank"}>вконтакте</Link>
                                            </li>
                                            : null
                                        }
                                        {data.telegram ?
                                            <li>
                                                <Link href={data.telegram.value} target={"_blank"}>телеграм</Link>
                                            </li>
                                            : null
                                        }
										{data.phone ?
											<li>
												<Link href={`tel:${data.phone.value}`}>{data.phone.value}</Link>
											</li>
											: null
										}
										{data.email ?
											<li>
												<Link href={`mailto:${data.email.value}`}>{data.email.value}</Link>
											</li>
											: null
										}
                                    </ul>
                                    : null
                                }

                            </div>
                        </div>
                    </div>
                    <div className="Footer-slice__content__info">
                        <p className="Footer-slice__content__info__name">Найди работу в студенческих отрядах</p>


							<button
								onClick={() => window.open( data && data.join ? data?.join.value : 'https://vk.com/sev_rso', '_ blank')}
								className="Footer-slice__content__info__button">
								<p>Вступить</p>
								<img src="/img/arrow-right-dark.png"></img>
							</button>
                    </div>
                </div>
                <div className="Footer-slice__copyright">
                    <p className="Footer-slice__copyright__text">
                        © 2023. Все права защищены. Создано с <a href="https://vk.com/sds.codezilla">❤️</a> от Севро
                    </p>
                </div>
            </div>
        </footer>
    );
}

export default Footer;
