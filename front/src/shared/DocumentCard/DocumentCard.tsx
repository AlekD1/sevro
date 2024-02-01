import './documentcard.scss';
import {DocumentInterface} from "@/interfases/interfaces";
import Link from "next/link";
function DocumentCard({title, file, created_at}: DocumentInterface) {
    return (

        <div className="Document-Card">
            <Link href={file} target="_blank" >
                <button className='Document-Card__content'>
                    <p>{title}</p>
                    <svg viewBox="0 0 73 73" fill="none">
                        <g clip-path="url(#clip0_553_884)">
                            <path d="M46.72 51.1C46.72 51.1 58.8555 51.1 60.003 51.1C66.3759 51.1 71.54 45.936 71.54 39.5646C71.54 33.1931 66.3759 28.0276 60.003 28.0276C59.9738 28.0276 59.9476 28.032 59.9184 28.032C60.0074 27.3108 60.0687 26.5808 60.0687 25.8362C60.0687 16.0396 52.1278 8.09717 42.3297 8.09717C34.6954 8.09717 28.2086 12.9283 25.7062 19.691C24.1192 18.1011 21.9233 17.1156 19.4997 17.1156C14.654 17.1156 10.7266 21.043 10.7266 25.8873C10.7266 26.0114 10.7412 26.1311 10.7456 26.2537C5.39466 27.7327 1.45996 32.6222 1.45996 38.4433C1.45996 45.4337 7.12622 51.1 14.1182 51.1C15.3256 51.1 26.28 51.1 26.28 51.1" stroke="#0078B7" stroke-width="2" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round" />
                            <path d="M43.8002 59.86L36.5002 67.16L29.2002 59.86" stroke="#0078B7" stroke-width="2" stroke-miterlimit="10" stroke-linecap="round" />
                            <path d="M36.5 37.96V66.6753" stroke="#0078B7" stroke-width="2" stroke-miterlimit="10" stroke-linecap="round" />
                        </g>
                        <defs>
                            <clipPath id="clip0_553_884">
                                <rect width="73px" height="73px" fill="white" />
                            </clipPath>
                        </defs>
                    </svg>
                </button>
            </Link>

        </div>
    );
}

export default DocumentCard;
