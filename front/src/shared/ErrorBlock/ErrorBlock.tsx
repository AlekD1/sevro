import "./ErrorBlock.scss";
import Link from "next/link";

function ErrorBlock() {
	return (
		<div className="ErrorBlock">
			<div className="container ErrorBlock-container">
				<div className="ErrorBlock-container_icon">
					<img src="./img/logo-sevro-error.png" className="ErrorBlock-container_photo"></img>
				</div>
				<div className="ErrorBlock-container_text">
					<div className="ErrorBlock-container_text_error-name">
						<img src="./img/logo-sevro-error.png" className="ErrorBlock-container_photo"></img>
						404
					</div>
					<div className="ErrorBlock-container_text_notfound">Страница не найдена</div>
					<div className="ErrorBlock-container_text_description">
						страница, на которую вы пытаетесь попасть, не существует или была удалена. Перейдите на{" "}
						<u>
							<Link href="/" className="ErrorBlock-container_text_description_link">
								Главную страницу{" "}
							</Link>
						</u>
						.
					</div>
				</div>
			</div>
		</div>
	);
}

export default ErrorBlock;
