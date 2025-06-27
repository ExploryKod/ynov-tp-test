import { Event } from '../entities/event.entity';
export interface IEventRepository {
    create(event: Event): Promise<void>;
}
