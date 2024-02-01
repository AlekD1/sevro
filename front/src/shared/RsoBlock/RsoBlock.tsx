import "../RsoBlock/rsoblock.scss";
import Image from "next/image";

interface RsoBlockInterface {
	title: string;
	img: any;
}

function RsoBlock({ title, img }: RsoBlockInterface) {
	return (
		<div className="RsoBlock__style">
			<Image src={img} alt=" " />
			<p>{title}</p>
		</div>
	);
}

export default RsoBlock;
