import React from "react";

interface BurgerProps {
    isOpen: boolean
}

function Burger ({isOpen}: BurgerProps) {

    if(!isOpen) return (
        <svg
            width="50"
            height="36"
            viewBox="0 0 50 36"
            fill="none"
            id="menu-button"
            className="Header__burger__button"
        >
            <rect
                id="bar1"
                width="50"
                height="4"
                rx="2"
                fill="#F7F7F7"
            />
            <rect
                id="bar2"
                y="16"
                width="50"
                height="4"
                rx="2"
                fill="#F7F7F7"
            />
            <rect
                id="bar3"
                y="32"
                width="50"
                height="4"
                rx="2"
                fill="#F7F7F7"
            />
        </svg>
    )
    return (
        <svg
            width="50"
            height="36"
            viewBox="0 0 50 36"
            fill="none"
            id="menu-button"
            className="Header__burger__button"
        >
            <rect
                id="bar1"
                width="50"
                height="4"
                rx="2"
                fill="#F7F7F7"
            />
            <rect
                id="bar2"
                y="16"
                width="50"
                height="4"
                rx="2"
                fill="#F7F7F7"
            />
            <rect
                id="bar3"
                y="32"
                width="50"
                height="4"
                rx="2"
                fill="#F7F7F7"
            />
        </svg>
    );
};

export default Burger;
