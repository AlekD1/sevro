'use client'
import React, {useEffect, useRef} from "react";
import {register} from 'swiper/element/bundle';
import "swiper/css"
import "./newsslider.scss"
register();

interface SliderInterface {
    title: string
    headerContent: React.ReactNode
    children?: React.ReactNode
}


function Slider({title, headerContent, children}: SliderInterface) {

    const swiperElRef = useRef<any>(null);

    const swiperParams = {
        slidesPerView: 1,
        loop: true,
        rewind: true,
        injectStyles: [
            `
      ::slotted(swiper-slide) {
          display: flex;
          justify-content: center;
        }
      `,
        ],
        breakpoints: {
            420: {
                slidesPerView: 1,
            },
            600: {
                slidesPerView: 2,
            },
            900: {
                slidesPerView: 3,
            },
            1190: {
                slidesPerView: 4,
            },
        },
    };

    useEffect(() => {
        const swiperEl: any = document.querySelector('swiper-container');

        if (swiperEl) {
            Object.assign(swiperEl, swiperParams);
            swiperEl.initialize();
        }
    }, []);


    return (
        <div className="NewsSlider">
            <div className="container NewsSlider-container">
                <div className="NNewsSlider__header-slice">{title}</div>
                <div className="NewsSlider__slider">
                    <div className="NewsSlider__slider__header">
                        {headerContent}
                        <div className="NewsSlider__slider__header-arrows">
                            <button onClick={() => {
                                swiperElRef.current.swiper.slidePrev()
                            }} className="NewsSlider__slider__header-arrows_left">
                                <svg
                                    xmlns="http://www.w3.org/2000/svg"
                                    width="12"
                                    height="22"
                                    viewBox="0 0 12 22"
                                >
                                    <path
                                        d="M11.28 0.800102C10.776 0.344102 10.752 0.368102 5.448 5.6721L0.119995 11.0001L5.448 16.3281C10.752 21.6321 10.776 21.6561 11.28 21.2001L11.784 20.7441L6.912 15.8721L2.04 11.0001L6.912 6.1281L11.784 1.2561L11.28 0.800102Z"
                                        fill="black"
                                    />
                                </svg>
                            </button>
                            <button onClick={() => {
                                swiperElRef.current.swiper.slideNext()
                            }} className="NewsSlider__slider__header-arrows_right">
                                <svg
                                    xmlns="http://www.w3.org/2000/svg"
                                    width="24"
                                    height="24"
                                    viewBox="0 0 24 24"
                                >
                                    <path
                                        d="M6.72 22.1999C7.224 22.6559 7.248 22.6319 12.552 17.3279L17.88 11.9999L12.552 6.6719C7.248 1.3679 7.224 1.3439 6.72 1.7999L6.216 2.2559L11.088 7.1279L15.96 11.9999L11.088 16.8719L6.216 21.7439L6.72 22.1999Z"
                                        fill="black"
                                    />
                                </svg>
                            </button>
                        </div>
                    </div>
                    <swiper-container
                        init={false}
                        ref={swiperElRef}
                    >
                        {children}
                    </swiper-container>
                </div>
            </div>
        </div>
    );
}

export default Slider;
