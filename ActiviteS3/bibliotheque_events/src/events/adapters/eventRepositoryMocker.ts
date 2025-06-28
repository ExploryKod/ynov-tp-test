import { Event } from '../entities/event.entity';
import { IEventRepository } from '../ports/event-repository.interface';

export class EventRepositoryMocker implements IEventRepository {
  public database: Event[] = [];
  async create(event: Event): Promise<void> {
    this.database.push(event);
  }
}
