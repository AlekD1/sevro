import type {Metadata} from 'next'
import "../css/global.scss"
import Header from "@/components/Header/Header";
import Footer from "@/components/Footer/Footer";


export const metadata: Metadata = {
    title: 'SevRSO',
    description: 'Описание',
}

export default function RootLayout({
                                       children,
                                   }: {
    children: React.ReactNode
}) {
    return (
        <html lang="ru">
            <body>
                <Header/>
                <div className="content">
                    {children}
                </div>
                <Footer/>
            </body>
        </html>
    )
}
