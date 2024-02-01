export interface QAInterface {
    title: string
    value: string
}

export interface StatisticInterface {
    title: string
    value: string
    position?: number
}

export interface NewsCardInterface {
    id?: number
    title: string
    image: string
    description: string
}

export interface NewsItem {
    id: number;
    title: string;
    description: string;
    image: string;
    content: string;
    created_at: string;
    tags: number[];
}

interface SocialItem {
    value: string;
}

export interface ContactInfoInterface {
    vk: SocialItem;
    telegram: SocialItem;
    join: SocialItem;
    phone: SocialItem;
    email: SocialItem;
}

export interface DirectionInterface {
    id: number;
    name: string;
    main_image: string;
    icon: string;
    description: string;
}

export interface DirectionCardInterface {
    id: number;
    main_image: string;
    icon: string;
    type?: any
}

interface Figure {
    id: number;
    name: string;
    image: string;
    phone: string;
    email: string;
    position: number;
}

export interface SquadListItemInterface {
    id: number;
    name: string;
    direction?: number;
    main_image: string;
    description: string;
    content?: string;
    links?: any[];
    create?: string;
    figures?: Figure[];
    vk: string
}

export interface PersonInterface {
    id: number;
    position: string;
    name: string;
    image: string;
    on_main?: boolean;
    phone: string;
    email: string;
}

export interface DocumentInterface {
    title: string;
    file: string;
    created_at: string;
}
