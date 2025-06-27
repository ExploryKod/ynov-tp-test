import { IIDGenerator } from '../ports/id-generator.interface';
import { IEventRepository } from '../ports/event-repository.interface';
export declare class AddNewEvent {
    private readonly repository;
    private readonly idGenerator;
    constructor(repository: IEventRepository, idGenerator: IIDGenerator);
    execute(data: {
        title: string;
        participants: number;
        startDate: Date;
        endDate: Date;
    }): Promise<{
        id: string;
    }>;
}
