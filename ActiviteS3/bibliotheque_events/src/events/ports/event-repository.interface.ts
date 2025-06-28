import { Event } from '../entities/event.entity';

export const I_EVENT_REPOSITORY = 'I_EVENT_REPOSITORY';

export interface IEventRepository {
  create(event: Event): Promise<void>;
}
