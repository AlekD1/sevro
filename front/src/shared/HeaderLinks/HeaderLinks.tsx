import Link from "next/link";
import React from "react";

interface HeaderLinksProps {
    setIsOpen?: React.Dispatch<React.SetStateAction<boolean>>;
}

function HeaderLinks({setIsOpen}: HeaderLinksProps) {

    return (
        <>
            <ul onClick={setIsOpen ? () => setIsOpen(false) : undefined}>
                <li>
                    <Link href="/about">о нас</Link>
                </li>
                <li>
                    <Link href="/#news">новости</Link>
                </li>
                {/*<li>*/}
                {/*    <Link href="/gallery">галерея</Link>*/}
                {/*</li>*/}
                <li>
                    <Link href="/info">бойцам</Link>
                </li>
                <li>
                    <Link href="/#form">сотрудничество</Link>
                </li>
                <li>
                    <Link href="/#question">Q&A</Link>
                </li>
            </ul>
        </>
    );
};

export default HeaderLinks;
