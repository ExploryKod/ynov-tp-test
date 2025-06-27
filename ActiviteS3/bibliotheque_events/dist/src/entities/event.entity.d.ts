type EventProps = {
    id: string;
    title: string;
    participants: number;
    startDate: Date;
    endDate: Date;
};
export declare class Event {
    props: EventProps;
    constructor(props: EventProps);
}
export {};
