import { Event } from '../entities/event.entity';
import { IIDGenerator } from '../ports/id-generator.interface';
import { IEventRepository } from '../ports/event-repository.interface';

export class AddNewEvent {
  constructor(
    private readonly repository: IEventRepository,
    private readonly idGenerator: IIDGenerator,
  ) {}

  async execute(data: any) {
    return { id: 'id-1' };
  }
}
