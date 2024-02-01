import ky from "ky";
import {ContactInfoInterface} from "@/interfases/interfaces";

export const clientAPI =   ky.extend({prefixUrl: 'http://127.0.0.1:8000/api/'});

export async function getContacts(): Promise<ContactInfoInterface | undefined> {
    try {
        return await clientAPI.get("contacts/").json();
    } catch (error) {
        return undefined
    }
}
