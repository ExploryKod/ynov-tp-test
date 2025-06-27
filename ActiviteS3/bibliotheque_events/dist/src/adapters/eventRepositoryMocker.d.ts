import { Event } from '../entities/event.entity';
import { IEventRepository } from '../ports/event-repository.interface';
export declare class EventRepositoryMocker implements IEventRepository {
    database: Event[];
    create(event: Event): Promise<void>;
}
